---
type: distilled-note
---

# Retry Around a Circuit Breaker Counts Every Attempt as a Failure

When the retry wraps the circuit breaker, every attempt passes through the breaker on its own. So one logical call that fails writes **one failure record per attempt**, not one.

```text
Retry( CircuitBreaker( call ) )     ← retry outermost

one call, 3 attempts, all fail  →  3 failures in the breaker's window
```

## Why it is bad

- **One bad call trips it.** `slidingWindowSize(5)` holds 5 records, but 3 attempts per call means they cover fewer than 2 real calls. One failed call writes 3 of the 5, which is 60%, over the 50% threshold. The breaker ends up judging a single request, not the service.
- **Retry trips the breaker, then stops helping.** It doesn't retry `CallNotPermittedException`, so it does nothing once the breaker is open.

## It is the default, and it is not always wrong

Retry on the outside is resilience4j's default. It only hurts with a small window. Size both settings in attempts: calls to judge × max attempts.

| Order                                              | `slidingWindowSize` | `minimumNumberOfCalls`                 |
| -------------------------------------------------- | ------------------- | -------------------------------------- |
| Retry outside (default)                            | 30                  | 30: at least 10 calls even if all fail |
| Breaker outside, `CircuitBreaker( Retry( call ) )` | 10                  | 10: one record per call                |

Breaker outside counts real calls but reacts more slowly, because one record can take the whole retry budget to arrive.

## Where it bit

[[resources/software-engineering/system-architecture/incidents/2026-09-30 - Retry Around the Breaker Turned One Slow AI Call Into 334 Rejected Jobs|The 30 Sep 2026 NCTool outage]]: one timed-out AI call wrote 3 failures into a window of 5, the breaker opened, and the job runner rejected 334 queued jobs in 2.8 seconds. The fix is proposed in [[resources/software-engineering/system-architecture/adr/0005 - Count Each AI Call Once in the Circuit Breaker|ADR 0005]].
