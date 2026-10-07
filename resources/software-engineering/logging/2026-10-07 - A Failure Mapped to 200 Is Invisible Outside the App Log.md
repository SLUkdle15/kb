---
type: distilled-note
---

# A Failure Mapped to 200 Is Invisible Outside the App Log

A global exception handler that maps a failure to HTTP 200 masks it behind a lying status code. The error is in the app log, but every dashboard, alert and retrying caller sees success.

In `fcm-template-service`, `GlobalExceptionHandler.handleCallApiException` is annotated `@ResponseStatus(value = HttpStatus.OK)` (`GlobalExceptionHandler.java:139`), so a `CallApiException` comes back as HTTP 200 with an error body carrying `errorCode 500`.

**The log is not what is wrong.** `AuditLoggerFilter` records the status of the response it was handed, so `-> 200` is faithful. The handler decided the status before the filter saw it; chasing the filter finds nothing.

What it costs:

- **The log** — filtering by status will not find these failures. The signal is in the body's `errorCode`; see [[areas/work-systems/read-the-json-logs|Read the JSON Logs]].
- **The dashboard and the alert** — both count statuses, so a service failing every request reports a flawless success rate.
- **The caller** — a client that retries on 5xx sees 200 and does not retry.

The status code is the only part of a response most observability reads. Deciding it in an exception handler decides what all three of those will believe.
