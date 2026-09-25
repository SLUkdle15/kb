---
type: distilled-note
---

# Replication Lag and Consistency Guarantees

If an application reads from an asynchronous follower, it may see outdated information if the follower has fallen behind. This leads to apparent inconsistencies in the database: if you run the same query on the leader and a follower at the same time, you may get different results, because not all writes have been reflected in the follower. This inconsistency is just a temporary state—if you stop writing to the database and wait a while, the followers will eventually catch up and become consistent with the leader. For that reason, this effect is known as **eventual consistency**.

Anomalies that replication lag causes, and the guarantees that prevent them:

1. **Reading your own writes** — if the user views the data shortly after making a write, the new data may not yet have reached the replica.
2. **Monotonic reads** — moving backward in time when making several reads from different replicas.
3. **Consistent prefix reads** — this guarantee says that if a sequence of writes happens in a certain order, then anyone reading those writes will see them appear in the same order.
