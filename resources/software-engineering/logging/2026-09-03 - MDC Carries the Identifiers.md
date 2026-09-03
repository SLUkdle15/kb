---
type: distilled-note
---

# MDC Carries the Identifiers

The MDC (mapped diagnostic context) is a thread-local map that SLF4J merges into every log event the thread emits. Put an identifier in it once and every subsequent line in that unit of work carries it, without threading the id through each message.

```java
try (MDC.MDCCloseable ignored = MDC.putCloseable("draftId", draftId)) {
    ...
}
```

Always scope it — try-with-resources, or `MDC.remove` in a `finally`. Thread pools reuse threads, so a key left behind attaches itself to somebody else's request, which is worse than not having it.

Where to set it follows what the id identifies. A request or correlation id belongs in a servlet filter or interceptor, so the whole request is tagged from the edge. A business id like `draftId` belongs at the top of the unit of work that owns it.

With a JSON encoder each MDC entry becomes its own field, which is the point: Grafana filters on `draftId` instead of matching substrings, and the message text stays constant enough to group on — see [[resources/software-engineering/logging/2026-09-03 - Structured JSON Logs in Production|Structured JSON Logs in Production]]. With a plain pattern layout the entries are invisible until the pattern names them explicitly with `%X{draftId}`.

The one trap is that thread-local means thread-local. Work handed to `@Async`, a `CompletableFuture`, or a reactive scheduler starts on a different thread with an empty MDC unless the context is explicitly propagated, so a unit of work that hops threads loses its identifiers halfway through.
