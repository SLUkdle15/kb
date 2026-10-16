# DSCAI OAuth Timeout

Area: [[areas/work-systems/work-systems|Work Systems]]
Captured: 2026-10-16

Raw capture, not yet investigated. One transaction, seen 2026-10-16 07:27:23.

## What the Log Shows

```text
2026-10-16 07:27:23.245 [http-nio-9005-exec-1] ERROR v.c.f.f.s.app.client.DscaiApiClient MDC_TRANSACTION_ID=09ca2a69f3f041e1b43b0a052fb707cb: OAUTH_HAS_EXCEPTION: java.net.SocketTimeoutException: timeout - 0
2026-10-16 07:27:23.248 [http-nio-9005-exec-1] ERROR v.c.f.f.s.c.e.h.GlobalExceptionHandler MDC_TRANSACTION_ID=09ca2a69f3f041e1b43b0a052fb707cb: handleCallApiException(): BaseException{code='500', message='INTERNAL_SERVER_ERROR', messageDescription='null'}
2026-10-16 07:27:23.249 [http-nio-9005-exec-1] WARN  o.s.w.s.m.m.a.ExceptionHandlerExceptionResolver MDC_TRANSACTION_ID=09ca2a69f3f041e1b43b0a052fb707cb: Resolved [BaseException{code='500', message='INTERNAL_SERVER_ERROR', messageDescription='null'}]
```

## There Is No Stack Trace Here

These are three single-line events, not a call stack. The exception reached the log as its `toString()` — class name plus message — so every frame was discarded at the point of logging.

That is the shape SLF4J produces when the throwable is passed as a *format argument* instead of the trailing argument:

```java
log.error("OAUTH_HAS_EXCEPTION: {} - {}", e, retryCount);   // message only
log.error("OAUTH_HAS_EXCEPTION, attempt {}", retryCount, e); // trace included
```

A throwable is only printed with its trace when it is the last argument and has no `{}` of its own. So the first thing to fix is the logging, not the timeout: without frames there is no way to tell which call site inside `DscaiApiClient` timed out, or what the business call above it was.

## What the Three Lines Do Say

Read as logger names, they give the handling path rather than the call path:

1. `[http-nio-9005-exec-1]` — a Tomcat worker on port 9005. The call is synchronous and inside a user-facing request, so the timeout is holding a request thread, not a background job.
2. `DscaiApiClient` catches the `SocketTimeoutException`, logs it, and rethrows something the handler recognises as a call-API failure.
3. `GlobalExceptionHandler.handleCallApiException()` maps it to `BaseException{code='500', message='INTERNAL_SERVER_ERROR', messageDescription='null'}` — the upstream cause is dropped, so the caller gets a 500 that names nothing. At least it is a 500 and not the invisible case in [[resources/software-engineering/logging/2026-10-07 - A Failure Mapped to 200 Is Invisible Outside the App Log|A Failure Mapped to 200 Is Invisible Outside the App Log]].
4. `ExceptionHandlerExceptionResolver` logs `Resolved [...]` at WARN — Spring confirming the `@ExceptionHandler` consumed it. Not a second fault.

Two readings worth confirming rather than believing:

- **`timeout - 0` is probably two fields, not one message.** It parses as `{} - {}` where the first is the exception and the second is some counter that was `0`. A bare message of `timeout` (rather than `Read timed out` or `connect timed out`) is what OkHttp/Okio throws, which would point at the HTTP client in use and at a *read* timeout rather than a connect failure.
- **The failure is in acquiring the token, not in the business call.** `OAUTH_HAS_EXCEPTION` fires on the OAuth step, so while the token endpoint is unreachable every call through this client fails the same way. If the token is cached, failures arrive in bursts at refresh time instead of steadily — which would explain a single isolated line like this one.

**The 4 ms between the lines is not how long the timeout took.** The first line is written when the exception is *caught*; the wait happened before it. Nothing in this excerpt shows the configured timeout or the real elapsed time.

## To Check

- Find the log statement and settle `timeout - 0` and what the `0` counts: `grep -rn "OAUTH_HAS_EXCEPTION" --include=*.java`
- Pull the whole request by its id to get the entry line and the true elapsed time — [[resources/software-engineering/logging/2026-09-07 - Grep Narrows a Log File, Then Read Around the Hit|grep, then read around the hit]], or filter `MDC_TRANSACTION_ID` as a field if these are JSON logs ([[resources/software-engineering/logging/2026-09-03 - MDC Carries the Identifiers|MDC Carries the Identifiers]]).
- One-off or recurring? Three lines from one transaction say nothing about frequency; check Grafana around 07:27.
- What are the connect and read timeouts on the OAuth call, is the token cached, and does a failed fetch poison the cache?
- Is there retry or a breaker around `DscaiApiClient`? Compare [[resources/software-engineering/system-architecture/incidents/2026-09-30 - Retry Around the Breaker Turned One Slow AI Call Into 334 Rejected Jobs|the 30 Sep breaker outage]], where `downloadImageAsInputStream` had no protection at all — and where a long read timeout against a small thread pool did the real damage.
