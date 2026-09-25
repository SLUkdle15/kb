---
type: distilled-note
---

# B-Tree vs LSM-Tree Storage Engines

This is an important trade-off in storage systems: well-chosen indexes speed up read queries, but every index slows down writes. For this reason, databases don't usually index everything by default, but require you—the application developer or database administrator—to choose indexes manually, using your knowledge of the application's typical query patterns.

Most common is B tree: keep key-value pairs sorted by key, breaking the db into fixed-size blocks or pages and read or write one page at a time. — One current truth, updated in place.

LSM table: Append-only history, truth reconstructed on read.

Postgres uses B tree.
