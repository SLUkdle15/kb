---
type: distilled-note
---

# ACID and Why Consistency Belongs to the Application

- **Atomicity** — the queries within a transaction fail together and commit together. All or nothing.
- **Isolation** — concurrently executing transactions are isolated from each other.
- **Durability** — once a transaction has committed successfully, any data it has written will not be forgotten, even if there is a hardware fault or the database crashes.

The distinction that reframes the other three: atomicity, isolation, and durability are properties of the **database**, whereas consistency in the ACID sense is a property of the **application**.
