# Designing Data Intensive Application

> [!summary]
> Reading notes from DDIA. Core ideas so far: every system balances reliability, scalability, and maintainability; the document-vs-relational choice trades schema flexibility and locality against join support; declarative queries state the what and leave the how to the optimizer; storage engines trade read speed against write cost (indexes, B-trees vs LSM-trees); replication trades consistency guarantees against latency, availability, and read throughput (single-leader vs multi-leader vs leaderless); and partitioning trades range-query support against even load distribution, with secondary indexes kept either local to each partition or global by term.

5-6-7-9-11

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
