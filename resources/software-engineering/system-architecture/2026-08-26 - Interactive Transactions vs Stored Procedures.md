---
type: distilled-note
---

# Interactive Transactions vs Stored Procedures

In the early days of databases, the intention was that a database transaction could encompass an entire flow of user activity.

The **interactive style** is what replaced it: an application makes a query, reads the result, perhaps makes another query depending on the result of the first, and so on. The queries and results are sent back and forth between the application code (running on one machine) and the database server (on another).

For this reason, systems with single-threaded serial transaction processing don't allow interactive multi-statement transactions. Instead, the application must submit the entire transaction code to the database ahead of time, as a **stored procedure**.

## When it's the right call

**1. Set-based work over lots of rows.** Month-end reconciliation across a million rows. Pulling them into the JVM to loop is madness — one round-trip per row, GC pressure, minutes of runtime. SQL does it in one pass. This is the strongest case and it's really "do it in SQL," proc or not.

**2. Extreme contention on a hot row.** Ticket sales, flash-sale inventory. Shaving a transaction from 4ms to 0.1ms genuinely multiplies throughput because everyone is queued behind the same lock. Usually you can get this with a single conditional `UPDATE` instead of a proc.

**3. Multiple writers you don't control.** A Java service, a Python job, and a BI tool all update the same table. Business rules in Java are enforced only for Java. A proc (or better, a constraint/trigger) is enforced for everyone.

**4. Legacy or DBA-owned systems.** Banking, insurance, telco — the rules already live in PL/SQL and have for 20 years. Rewriting them into Java isn't a technical decision.

**5. Something SQL does natively and Java doesn't.** Recursive CTEs, window functions, `MERGE`, PostGIS. Not really "stored procedure," just "don't drag data into the app to do what the DB is better at."
