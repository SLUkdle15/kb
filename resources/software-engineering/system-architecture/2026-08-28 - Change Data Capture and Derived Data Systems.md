---
type: distilled-note
---

# Change Data Capture and Derived Data Systems

You can capture the changes in a database and continually apply the same changes to a search index. If the log of changes is applied in the same order, you can expect the data in the search index to match the data in the database.

That ordering guarantee is the whole mechanism: same log, same order, same result.

Seen this way, the search index and any other derived data systems are just **consumers of the change stream** — not separate sources of truth to be kept in sync by hand, but downstream readers of one authoritative log. This is change data capture (CDC).
