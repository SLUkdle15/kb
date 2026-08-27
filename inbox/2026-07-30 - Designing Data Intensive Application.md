# Designing Data Intensive Application

> [!summary]
> Reading notes from DDIA. Core ideas so far: every system balances reliability, scalability, and maintainability; the document-vs-relational choice trades schema flexibility and locality against join support; declarative queries state the what and leave the how to the optimizer; storage engines trade read speed against write cost (indexes, B-trees vs LSM-trees); replication trades consistency guarantees against latency, availability, and read throughput (single-leader vs multi-leader vs leaderless); and partitioning trades range-query support against even load distribution, with secondary indexes kept either local to each partition or global by term; and transactions give atomicity, isolation, and durability from the database while consistency stays a property of the application, with weak isolation levels such as read committed ruling out dirty reads and writes but not stale reads from a cache above them; and the isolation ladder trades anomaly prevention against abort rate, with only serializable tracking reads and therefore preventing write skew. Serial execution rules out interactive multi-statement transactions, forcing the whole transaction into a stored procedure, which earns its keep mainly for set-based work, hot-row contention, and writers you do not control. In a distributed system, partial failure means some parts break unpredictably while others work fine, so the requirement is knowing how the system reacts and recovers rather than necessarily tolerating every fault; and a packet-switched network gives no bandwidth reservation, so the available bandwidth cannot be guessed the way a circuit's can.

11

## Distilled notes

- [[resources/software-engineering/system-architecture/2026-07-31 - Reliability Scalability Maintainability|Reliability Scalability Maintainability]]
- [[resources/software-engineering/system-architecture/2026-07-31 - Document vs Relational Data Model|Document vs Relational Data Model]]
- [[resources/software-engineering/system-architecture/2026-08-03 - Declarative vs Imperative Query Languages|Declarative vs Imperative Query Languages]]
- [[resources/software-engineering/system-architecture/2026-08-03 - B-Tree vs LSM-Tree Storage Engines|B-Tree vs LSM-Tree Storage Engines]]
- [[resources/software-engineering/system-architecture/2026-08-04 - Column-Oriented Storage|Column-Oriented Storage]]
- [[resources/software-engineering/system-architecture/2026-08-05 - Single-Leader vs Multi-Leader vs Leaderless Replication|Single-Leader vs Multi-Leader vs Leaderless Replication]]
- [[resources/software-engineering/system-architecture/2026-08-05 - Replication Lag and Consistency Guarantees|Replication Lag and Consistency Guarantees]]
- [[resources/software-engineering/system-architecture/2026-08-07 - Partitioning by Key Range vs Hash|Partitioning by Key Range vs Hash]]
- [[resources/software-engineering/system-architecture/2026-08-07 - Local vs Global Secondary Indexes in Partitioned Data|Local vs Global Secondary Indexes in Partitioned Data]]
- [[resources/software-engineering/system-architecture/2026-08-24 - ACID and Why Consistency Belongs to the Application|ACID and Why Consistency Belongs to the Application]]
- [[resources/software-engineering/system-architecture/2026-08-24 - Read Committed and Hibernate L1 Cache Stale Reads|Read Committed and Hibernate L1 Cache Stale Reads]]
- [[resources/software-engineering/system-architecture/2026-08-26 - Isolation Levels and the Anomalies They Allow|Isolation Levels and the Anomalies They Allow]]
- [[resources/software-engineering/system-architecture/2026-08-26 - Interactive Transactions vs Stored Procedures|Interactive Transactions vs Stored Procedures]]
- [[resources/software-engineering/system-architecture/2026-08-27 - The Three Troubles of Distributed Systems|The Three Troubles of Distributed Systems]]
- [[resources/software-engineering/system-architecture/2026-08-27 - Packet Switching Cannot Reserve Bandwidth|Packet Switching Cannot Reserve Bandwidth]]

