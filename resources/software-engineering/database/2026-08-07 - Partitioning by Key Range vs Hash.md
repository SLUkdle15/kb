---
type: distilled-note
---

# Partitioning by Key Range vs Hash

The main reason for wanting to partition data is scalability. Different partitions can be placed on different nodes in a shared-nothing cluster.

A partition with disproportionately high load is called a **hot spot**.

The two basic strategies trade against each other:

- **Partitioning by key range** keeps keys sorted, which preserves range queries but risks hot spots and skew.
- **Partitioning by hash of key** spreads load more evenly but loses the ability to do range queries.
