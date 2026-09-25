# Database

Use this collection for reusable notes on how data systems work underneath the API: data models, query languages, storage engines, replication, partitioning, transactions, isolation, and what changes once the data is spread across machines.

Parent resource: [[resources/software-engineering/software-engineering|Software Engineering]]

Related resource: [[resources/software-engineering/system-architecture/system-architecture|System Architecture]]

Related area: [[areas/technical-growth/technical-growth|Technical Growth]]

## Notes

Distilled from *Designing Data-Intensive Applications* — Martin Kleppmann.

### Foundations

- [[resources/software-engineering/database/2026-07-31 - Reliability Scalability Maintainability|Reliability Scalability Maintainability]]

### Data models and query languages

- [[resources/software-engineering/database/2026-07-31 - Document vs Relational Data Model|Document vs Relational Data Model]]
- [[resources/software-engineering/database/2026-08-03 - Declarative vs Imperative Query Languages|Declarative vs Imperative Query Languages]]

### Storage engines

- [[resources/software-engineering/database/2026-08-03 - B-Tree vs LSM-Tree Storage Engines|B-Tree vs LSM-Tree Storage Engines]]
- [[resources/software-engineering/database/2026-08-04 - Column-Oriented Storage|Column-Oriented Storage]]

### Replication and partitioning

- [[resources/software-engineering/database/2026-08-05 - Single-Leader vs Multi-Leader vs Leaderless Replication|Single-Leader vs Multi-Leader vs Leaderless Replication]]
- [[resources/software-engineering/database/2026-08-05 - Replication Lag and Consistency Guarantees|Replication Lag and Consistency Guarantees]]
- [[resources/software-engineering/database/2026-08-07 - Partitioning by Key Range vs Hash|Partitioning by Key Range vs Hash]]
- [[resources/software-engineering/database/2026-08-07 - Local vs Global Secondary Indexes in Partitioned Data|Local vs Global Secondary Indexes in Partitioned Data]]

### Transactions and isolation

- [[resources/software-engineering/database/2026-08-24 - ACID and Why Consistency Belongs to the Application|ACID and Why Consistency Belongs to the Application]]
- [[resources/software-engineering/database/2026-08-26 - Isolation Levels and the Anomalies They Allow|Isolation Levels and the Anomalies They Allow]]
- [[resources/software-engineering/database/2026-08-24 - Read Committed and Hibernate L1 Cache Stale Reads|Read Committed and Hibernate L1 Cache Stale Reads]]
- [[resources/software-engineering/database/2026-08-26 - Interactive Transactions vs Stored Procedures|Interactive Transactions vs Stored Procedures]]

### Distributed systems

- [[resources/software-engineering/database/2026-08-27 - The Three Troubles of Distributed Systems|The Three Troubles of Distributed Systems]]
- [[resources/software-engineering/database/2026-08-27 - Packet Switching Cannot Reserve Bandwidth|Packet Switching Cannot Reserve Bandwidth]]

### Batch, streams, and derived data

- [[resources/software-engineering/database/2026-08-28 - Log-Based Message Brokers|Log-Based Message Brokers]]
- [[resources/software-engineering/database/2026-08-28 - From Batch to Stream Processing|From Batch to Stream Processing]]
- [[resources/software-engineering/database/2026-08-28 - Change Data Capture and Derived Data Systems|Change Data Capture and Derived Data Systems]]
