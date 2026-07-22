# FCM System Overview

System: FCM — FTEL internal contract management for the Legal team (~10 users).

Related area: [[areas/software-architect-growth/software-architect-growth|Software Architect Growth]]

## Scope

- Managing contract submission.
- Managing document storage.
- Managing workflow between users and Legal.
- Tracking contract status.
- Integrating with the AI model for contract checking.
- Integrating with the e-contract system for digital signature.
- Storing the final signed contract.
- Maintaining contract history and audit logs.


## Architecture Characteristics

- Reliability
- Data Integrity / Consistency
- Privacy
- Security
- Auditability
- Supportability / Observability

## Architecture Decisions

- [[resources/software-engineering/system-architecture/adr/0001 - Use a modular monolith as a single WAR|Use a Modular Monolith as a Single WAR]]

## Related

- [[resources/software-engineering/system-architecture/incidents/2026-06-28 - eContract Gateway Misconfiguration Incident|eContract Gateway Misconfiguration Incident]]
