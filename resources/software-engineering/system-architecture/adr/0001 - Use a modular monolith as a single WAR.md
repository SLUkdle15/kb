# Use a Modular Monolith as a Single WAR

System: [[resources/software-engineering/system-architecture/2026-07-15 - FCM System Overview|FCM]]

## Context

- The team needs a deployable structure for FCM that fits the existing Maven and WAR-based service setup.
- Shared concerns such as `fcm-common`, `fcm-common-domain`, and `fcm-common-kafka` are already factored into library modules used by `fcm-service`.

## Decision

- Keep FCM as a modular monolith: one deployable `fcm-service` WAR with shared concerns in library modules.
- Keep API clients separate from domain libraries.

## Consequences

- Familiar structure for the team and works well with Maven.
- Shared libraries can be reused by related CMS, job, and service projects.
- Shared library changes require rebuilds and can break dependents if not pushed or installed consistently.

## Compliance

- Keep common behavior in common modules, not duplicated in `fcm-service`.
- Rebuild or publish changed common modules before dependent services.
- Review common-module changes together with dependent service changes.

## Notes

- Library updates may require `mvn install` or an equivalent publish step.
