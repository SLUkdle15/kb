---
type: distilled-note
---

# Loki Only Receives, Something Else Pushes

Loki has no scrape loop. Unlike Prometheus, which pulls from targets, Loki only ever accepts writes on its push API — so the question for a Spring service is never how Loki reaches the app, but which component does the pushing.

There are two answers.

**An agent on the host.** The app writes [[resources/software-engineering/logging/2026-09-03 - Structured JSON Logs in Production|JSON]] to stdout or a file and knows nothing about Loki. The agent discovers the file, tails it, attaches labels, and batches it to Loki over HTTP. Promtail is the one the older guides use; it went into LTS in early 2025 and out of support around March 2026, with **Grafana Alloy** as its replacement. Same mechanism, so anything written about Promtail's behaviour still describes what Alloy does here.

**A Logback appender in the JVM.** `loki4j` or `tjahzi` push to the same endpoint from inside the application, with no agent and no file on disk.

The trade is what happens when Loki is unreachable. With an agent, the log is already on disk before anything ships it: Loki being down delays delivery but loses nothing, and the file is still there to read on the box when Grafana is not available. With an appender, the application owns batching, retry, and the decision about what to do with a full buffer — a logging path that can now apply backpressure to, or silently discard from, the service itself.

For NCTool and FCM the agent side is the cheaper default: both already emit JSON, so nothing in the application changes, and the platform keeps ownership of shipping. The appender earns its place mainly where there is no host to run an agent on.

Labels are attached at push time by whichever component does the pushing, and label cardinality is where Loki's cost and performance are decided — that part is still an open question here, not a settled practice, and is being worked out in [[next/next-actions/2026-09-03 - Work Out Loki Label Cardinality Rules|Work Out Loki Label Cardinality Rules]].
