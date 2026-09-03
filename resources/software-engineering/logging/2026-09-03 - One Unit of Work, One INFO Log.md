---
type: distilled-note
---

# One Unit of Work, One INFO Log

A method that is one unit of work — a draft going to submitted — emits exactly one INFO line, at the end, when it succeeded. Everything else in that method sits below or above that line.

- **DEBUG on entry** — what the method was called with. Free in prod, and the first thing wanted when the unit has to be traced.
- **DEBUG or WARN at the external boundaries** — every call out to a database, HTTP service, or queue. DEBUG on the way out and back on the happy path; WARN when the boundary misbehaves in a way the unit still recovers from, such as a retried call that eventually succeeds.
- **INFO once, on success** — the unit finished and the state changed.
- **WARN for expected failures** — validation rejected the draft, it was already submitted, the caller sent something the code is written to handle. The unit did not complete, but nothing is broken.
- **ERROR only for genuine breakage** — something no one anticipated and someone has to look at.

The reason for the single INFO is that INFO is the level left on in production. If every completed unit of work is one INFO line, the INFO stream reads as a business event log: count the lines and that is the number of submissions. A second INFO inside the same method breaks that count, and the detail it wanted to carry belongs at DEBUG.

The same rule sets the WARN/ERROR split. ERROR should mean a human is needed. A rejected draft is the system working, so alerting on ERROR stays meaningful only if expected failures stay at WARN.

## In SLF4J and Logback

Use parameterized placeholders rather than concatenation — the message is only formatted if the level is enabled, so no `isDebugEnabled()` guard is needed:

```java
log.debug("Submitting draft {}", draftId);
```

Pass the exception as the last argument instead of putting it in the message; Logback then prints the stack trace. `log.error("Submit failed for draft {}", draftId, ex)` keeps the trace, while `log.error(ex.getMessage())` throws it away.

Levels are configured per logger (`logging.level.com.example.submit=DEBUG` in `application.yml`), so the DEBUG lines cost nothing in production and are one config change away when a unit needs tracing — see [[resources/software-engineering/logging/2026-09-03 - Log Levels Are a Threshold, Not a Category|Log Levels Are a Threshold, Not a Category]]. That is what makes it safe to be generous at DEBUG and strict at INFO.

Identifiers do not belong in the message text at all; they go in [[resources/software-engineering/logging/2026-09-03 - MDC Carries the Identifiers|the MDC]], so every line in the unit carries them as a field.
