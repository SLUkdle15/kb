---
type: distilled-note
---

# Local vs Global Secondary Indexes in Partitioned Data

There are two ways to handle secondary indexes in a partitioned database:

- **Partitioning the index by document** — each partition keeps its index local, covering only the documents in that partition. Writes stay local, but reads have to scatter across all partitions.
- **Partitioning the index by term** — a global index, with each partition holding a piece of it. Reads hit fewer partitions, but a single write may have to touch several.
