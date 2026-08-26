---
type: distilled-note
---

# Isolation Levels and the Anomalies They Allow

The ladder runs read uncommitted → read committed → repeatable read → serializable. **Dirty writes are blocked at every level** — the write lock is free and always taken.

**Read committed** (the default in PostgreSQL, Oracle, and SQL Server) rules out dirty reads, but still allows:

- **non-repeatable read** — the same row, read twice, differs
- **read skew** — different rows, read into an inconsistent combination
- **lost update** — the same row, overwritten, so a value is lost
- **write skew** — different rows, both writes survive, so an invariant breaks

**Repeatable read** (snapshot isolation in PostgreSQL) fixes non-repeatable read, read skew, and phantoms, and detects lost updates by aborting with `40001` — but MySQL does not do that detection, which is the trap. It still allows write skew.

**Serializable** is the only level that prevents write skew, because it is the only level that tracks reads. The cost is aborts under contention, so callers must retry.
