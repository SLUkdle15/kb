---
type: distilled-note
---

# Read Committed and Hibernate L1 Cache Stale Reads

**Read committed** is the weak isolation baseline: no dirty reads and no dirty writes.

On a Spring + Hibernate + MariaDB stack, read committed contains no dirty read. But Hibernate provides an L1 cache, which gives a stale read — a second lookup of the same entity within the session issues no SQL and hands back the same managed instance.

```java
Purchase p = em.find(Purchase.class, 1L);
p.setStatus("XYZ");

Purchase p2 = em.find(Purchase.class, 1L);  // no SQL issued
p2.getStatus();   // "XYZ"
p == p2;          // true — same instance
```
