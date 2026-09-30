# Circuit Breaker and Retry in NC Tool Job

Date: 2026-09-30

Reference notes for the resilience4j setup in `nc-tool-job`, written after investigating
the AI outage of 30 Sep 2026. Everything below was verified against the code and the
resilience4j 2.2.0 jars rather than recalled.

Parent resource: [[resources/software-engineering/system-architecture/system-architecture|System Architecture]]

Related note: [[resources/software-engineering/system-architecture/2026-06-28 - eContract Gateway Misconfiguration Incident|eContract Gateway Misconfiguration Incident]] — another production misconfiguration write-up.


---

## 1. Your exact configuration

All of it lives in **one file**: `src/main/java/org/ftel/nctool/config/WebClientConfig.java`.
Nothing is in any `.properties` file, on `dev` or on `main`.

| Setting | Value | Where it comes from |
|---|---|---|
| `failureRateThreshold` | 50% | set, line 51 / 62 |
| `waitDurationInOpenState` | 10s | set, line 52 / 63 |
| `slidingWindowSize` | 5 | set, line 53 / 64 |
| `slidingWindowType` | `COUNT_BASED` | library default |
| `minimumNumberOfCalls` | **5** | **derived** — default is 100, clamped to the window size |
| `permittedNumberOfCallsInHalfOpenState` | **10** | library default, never set |
| `automaticTransitionFromOpenToHalfOpenEnabled` | `false` | library default |
| `aiRetry.maxAttempts` | **3 total** (1 initial + 2 retries) | set, line 78 |
| `aiRetry` backoff | 2s, multiplier 2.0 → waits of 2s then 4s | set, line 79 |

Two breakers exist, configured identically: `aiServiceCircuitBreaker` and
`iqcServiceCircuitBreaker`.

`CircuitBreakerRegistry.ofDefaults()` (line 45) and `RetryRegistry.ofDefaults()`
(line 72) do **not** apply to these — an explicit config is passed to
`registry.circuitBreaker(name, config)`, so the registry is only a holder.

---

## 2. How calls are wired

`WebclientUtils` offers **two** variants, and the choice decides how a failure surfaces.

| Wrapper | Protection | Behaviour on failure |
|---|---|---|
| `callWithRetryAndCircuitBreaker` | retry + breaker | **propagates** the exception |
| `callWithCircuitBreaker` | breaker only | **swallows** it, returns a fallback |

Which call uses which:

| Call | Wrapper |
|---|---|
| `AiApiClient.predict` | retry + breaker, propagating |
| `AiApiClient.predictGsafe` | retry + breaker, propagating |
| `IqcClient.getContractDetail` | breaker only, swallowing |
| **`IqcClient.downloadImageAsInputStream`** | **neither** — a bare `webClient.get()...block()` |

That last row matters. The image download has **no breaker, no retry, no fallback**.
It is why the 220 `Tunnel failed, got: 503` errors on 30 Sep were raw, one-shot, and
never retried even once.

---

## 3. The four interactions that caused the outage

### 3.1 Retry multiplies failures into the breaker's window

```java
Decorators.ofSupplier(supplier)
        .withCircuitBreaker(circuitBreaker)   // inner
        .withRetry(retry)                     // OUTER
```

Each `with*` wraps the previous, so **retry ends up outermost** — which is also
resilience4j's own documented default aspect order, not a mistake.

Consequence: every one of the 3 retry attempts passes through the breaker separately
and is recorded separately. **One logical call writes 3 failure records.** A window of
5 is therefore only about 1.7 real calls wide, and a single timed-out call is enough
to trip the breaker (3 of 5 = 60% > the 50% threshold).

### 3.2 `slidingWindowSize(n)` silently changes the trip threshold

In `CircuitBreakerConfig.Builder#build()`, for a COUNT_BASED window:

```java
minimumNumberOfCalls = Math.min(minimumNumberOfCalls, slidingWindowSize)
```

Writing `.slidingWindowSize(5)` looks like it only narrows the window. It also drops
"how many calls before I will judge anything" from **100 to 5**. Nothing in the code
says so, and the comment next to it (`// 50% failure rate trips the breaker`) does not
hint at it.

**Set `minimumNumberOfCalls` explicitly** so the real threshold is visible.

### 3.3 The breaker only leaves OPEN when something probes it

`CircuitBreakerStateMachine$OpenState.getState()` decompiles to two instructions:

```
getstatic  State.OPEN
areturn
```

It returns `OPEN` unconditionally, with **no clock check**. The OPEN → HALF_OPEN
transition lives *only* inside `tryAcquirePermission()`:

```
clock.instant().isAfter(retryAfterWaitDuration)  →  toHalfOpenState()
```

Two traps follow:

1. A loop that stops calling and polls `getState()` waiting for recovery **hangs
   forever** — nothing probes, so the state never moves.
2. The first transition is to **HALF_OPEN, not CLOSED**. Reaching CLOSED needs
   `permittedNumberOfCallsInHalfOpenState` (10) successes. Waiting for `CLOSED` means
   waiting on calls you are refusing to make.

If you need an explicit gate, use `tryAcquirePermission()` (which *does* drive the
transition) and call `releasePermission()` if you were only probing — otherwise you
leak half-open permits.

### 3.4 Retry correctly stands aside once the breaker is open

```java
.retryOnException(t -> {
    if (t instanceof WebClientResponseException ex) {
        return ex.getStatusCode().is5xxServerError();
    }
    return t instanceof WebClientRequestException;
})
```

`CallNotPermittedException` is neither type, so the predicate returns false and the
rejection propagates on the first attempt with no backoff. That is the *right*
behaviour — retrying against a breaker you know is open just burns attempts.

But it means the retry has two personalities:

| Breaker state | What retry does |
|---|---|
| CLOSED | Fully active — 3 attempts, each recorded as a separate breaker failure |
| OPEN | Inert — passes the rejection through in microseconds |

So retry *causes* the trip, then sits out the aftermath. And because nothing anywhere
in the path slows down while the breaker is open, a queued backlog drains through it
at full speed.

---

## 4. What that produced on 30 Sep 2026

```
00:45:06.590  Calling AI GSAFE API with 6 requests
00:46:42.598  GSAFE AI check failed: request timed out      (96s = 3 x 30s + 2s + 4s)
00:46:42.612  CircuitBreaker 'aiServiceCircuitBreaker' is OPEN
   ...        334 jobs rejected between 00:46:42.612 and 00:46:45.401
```

One slow AI call → 3 recorded failures → breaker opens → 334 jobs rejected in
**2.8 seconds**, long before the 10-second recovery window could matter.

The breaker did its job perfectly. The caller spent a 10-second outage as if it were
a total failure, because nothing treats "come back shortly" differently from "this
job failed".

---

## 5. What to research

### resilience4j documentation

- **circuitbreaker** → "Sliding window", "State transitions", `minimumNumberOfCalls`
- **retry** → `IntervalFunction`, `retryOnException`
- **decorators / aspect order** → why retry wraps circuit breaker by default

### Source worth reading directly

The jars are already in `~/.m2/repository/io/github/resilience4j/`.

- `CircuitBreakerStateMachine$OpenState` — the lazy transition, about 40 lines
- `CircuitBreakerConfig.Builder#build` — the `minimumNumberOfCalls` clamp
- `jdk.internal.net.http.PlainTunnelingConnection` — source of `Tunnel failed, got: NNN`

Decompile without sources:

```bash
J=$(find ~/.m2 -name 'resilience4j-circuitbreaker-2.2.0.jar' | head -1)
javap -p -c -cp "$J" 'io.github.resilience4j.circuitbreaker.internal.CircuitBreakerStateMachine$OpenState'
```

### Search terms

```
resilience4j retry circuitbreaker order
circuit breaker half-open probe
CallNotPermittedException backpressure
count-based vs time-based sliding window
retry storm / thundering herd
```

### Adjacent concepts worth knowing exist

- **`Bulkhead`** — caps concurrency. Would have prevented the 828-calls-in-one-minute burst.
- **`TimeLimiter`** — bounds a call's duration. Would have cut the 96-second stuck call.
- **Backpressure** — the general name for what the job runner is missing.

### API note for 2.x

`getWaitDurationInOpenState()` **does not exist**. Use:

```java
long waitMs = breaker.getCircuitBreakerConfig()
        .getWaitIntervalFunctionInOpenState()
        .apply(1);            // IntervalFunction extends Function<Integer, Long>
```

---

## 6. Open items, not yet done

Nothing in this section is implemented. The only fix committed so far is the
step-status bug (`84e5710`), which is unrelated to the breaker.

1. **`JobRunner` treats `CallNotPermittedException` as a job failure.** A tripped
   breaker should cost a pause, not the queue. This is the actual defect.
2. **A breaker rejection burns a job retry life.** `retryJob` increments `retryCount`
   before running; 259 jobs reached attempt 3/3 without ever reaching the AI.
3. **Window sizing.** Raise `slidingWindowSize` and set `minimumNumberOfCalls`
   explicitly, or switch to `TIME_BASED`.
4. **30s read timeout × 3 attempts against a 4-thread scheduler pool**
   (`spring.task.scheduling.pool.size=4`) — one stuck call holds a quarter of it for
   96 seconds.
5. **No concurrency cap toward the AI.** A `Bulkhead` would smooth the bursts.
6. **`downloadImageAsInputStream` has no protection at all** — no breaker, no retry.
