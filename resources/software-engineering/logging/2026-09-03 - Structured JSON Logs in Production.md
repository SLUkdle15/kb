---
type: distilled-note
---

# Structured JSON Logs in Production

Dev logs are read by a person, so a pattern layout on the console is right there. Production logs are read by Grafana, so they should be JSON — one object per event, with `level`, `logger`, timestamp, the message, the MDC entries, and the stack trace arriving as separate fields.

The gain is that message text stops being the query surface. Filtering becomes a field match instead of a regex over a formatted string, and a stack trace stays one event rather than becoming forty unrelated lines that Loki has to be told how to stitch back together.

Logback produces this through an encoder — `logstash-logback-encoder`, or Spring Boot's own structured logging (`logging.structured.format.console`) from 3.4 onward. It is a config choice per profile, not a change to any call site: the same `log.info(...)` renders as a readable line in dev and as JSON in prod. [[resources/software-engineering/infrastructure/2026-08-19 - NCTool and FCM on the New Infra|NCTool]] already emits JSON this way.

What it does change is how messages should be written. The message becomes a value to group by, so it works best as a constant sentence with the variable parts pushed out into fields — identifiers into [[resources/software-engineering/logging/2026-09-03 - MDC Carries the Identifiers|the MDC]] rather than interpolated into the text. `"Draft submitted"` with a `draftId` field groups; `"Draft 4711 submitted"` is a distinct message every time and groups into nothing.
