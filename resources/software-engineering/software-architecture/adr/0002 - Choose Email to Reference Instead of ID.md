# Choose Email to Reference Instead of ID

System: [[resources/software-engineering/software-architecture/2026-07-15 - FCM System Overview|FCM]]

## Status

Accepted

## Context

- The FCM notification feature needs a way to reference the users it notifies.
- Referencing users by FPT employee ID is unreliable because the employee table is not kept in sync with the actual employee records, so ID lookups can return stale or missing users.
- The primary concern for notifications is correctness: they must reach the right person.

## Decision

- The notification feature will reference users by email instead of by employee ID.
- Email is the identifier employees actually use, so it stays correct even when the employee table lags behind reality.
- Rejected alternative: employee ID. An integer ID is compact and index-friendly, but its correctness depends on the unsynced employee table, which fails the primary concern.

## Consequences

- Notifications stay correct without depending on the employee table being synced.
- This trades performance and scalability for correctness. Email is stored as `varchar(256)`, which is larger than an integer ID, so indexing, lookups, joins, and storage are less efficient at scale.
- A reference is only as stable as the address itself: if an employee's email changes, existing references to the old address break.

## Compliance

- Notification tables and DTOs reference users by email only; do not add employee ID columns or foreign keys to the employee table.
- Normalize emails (trimmed, lowercased) before storing or comparing them.
- Index email columns used for lookups and joins to limit the performance cost.
- In code review, reject changes that reintroduce employee ID references into the notification feature.

## Notes
