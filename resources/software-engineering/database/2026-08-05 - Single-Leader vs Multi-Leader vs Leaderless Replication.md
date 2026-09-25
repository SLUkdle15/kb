---
type: distilled-note
---

# Single-Leader vs Multi-Leader vs Leaderless Replication

Reasons to replicate data:

- To keep data geographically close to your users (and thus reduce latency)
- To allow the system to continue working even if some of its parts have failed (and thus increase availability)
- To scale out the number of machines that can serve read queries (and thus increase read throughput)

In leader-based replication, it is impractical for all followers to be synchronous: any one node outage would cause the whole system to grind to a halt.

## Multi-leader replication

Clients send each write to one of several leader nodes, any of which can accept writes. The leaders send streams of data change events to each other and to any follower nodes.

Use cases: multi-datacenter operation, clients with offline operation, or collaborative editing.

## Leaderless replication

Clients send each write to several nodes, and read from several nodes in parallel in order to detect and correct nodes with stale data.
