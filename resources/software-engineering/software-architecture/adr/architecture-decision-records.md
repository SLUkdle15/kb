# Architecture Decision Records

Use this collection for ADRs that capture meaningful architecture decisions, trade-offs, alternatives, and consequences.

Parent resource: [[resources/software-engineering/software-architecture/software-architecture|Software Architecture]]

Protocol: [[areas/software-architecture/write-an-adr|Write an ADR]]

## ADRs

### [[resources/software-engineering/software-architecture/2026-07-15 - FCM System Overview|FCM]]

- [[resources/software-engineering/software-architecture/adr/0001 - Use a modular monolith as a single WAR|Use a Modular Monolith as a Single WAR]]
- [[resources/software-engineering/software-architecture/adr/0002 - Choose Email to Reference Instead of ID|Choose Email to Reference Instead of ID]]

## Note Shape

ADR filenames use a monotonic sequence instead of the vault's usual date prefix:

```text
0001 - Decision Title.md
0002 - Decision Title.md
```

Use the next available number and a short decision phrase that reads well in a directory listing.

```md
# Decision Title

## Status: Proposed, Accepted, Superseded

## Context

What is forcing me to make this decision?

## Decision

What is the decision and corresponding justification?

## Consequences

What is the impact of this decision?

## Compliance

How will I ensure compliance with this decision?

## Notes
```
