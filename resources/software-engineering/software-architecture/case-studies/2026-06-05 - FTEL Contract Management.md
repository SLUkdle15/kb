# FTEL Contract Management

Project: [[projects/complete-phase-1-software-architecture-fundamentals/complete-phase-1-software-architecture-fundamentals|Complete Phase 1 Software Architecture Fundamentals]]
Status: draft

## Context

- **Business goal**: Build an internal FTEL document management system to manage contracts submitted by users. The system will support a back-and-forth review workflow and integrate with external systems, including an AI model for contract checking and an e-contract platform for digital signature.
- **Users**: the Legal team around 10 users
- **System boundary**:
	- Managing contract submission.
	- Managing document storage.
	- Managing workflow between users and Legal.
	- Tracking contract status.
	- Integrating with the AI model for contract checking.
	- Integrating with the e-contract system for digital signature.
	- Storing the final signed contract.
	- Maintaining contract history and audit logs.

## Architecture Characteristics

| Characteristic | Why it matters | Measurement | Trade-off |
|---|---|---|---|
| Reliability | Contract workflow depends on external systems such as AI/OCR, eContract, mail, and Kafka. Failures should not lose contract state or side effects. | Failed external calls are retried or moved to a failed/retryable state; no contract remains stuck in processing for more than a defined timeout period. | Adding retries, circuit breakers, and outbox patterns increases implementation and operational complexity. |
| Data Integrity / Consistency | Contract status, files, histories, and signing results must stay consistent across the workflow. | Every contract status change must have a matching history/audit record; reconciliation job reports zero missing history records. | Stronger consistency may reduce async flexibility and requires more transaction handling or reconciliation logic. |
| Privacy | Contracts may contain financial, business, and personal data. | Contract files can only be accessed by authorized users; file links are short-lived or served through permission-checked endpoints. | Strong privacy controls increase access-check complexity and may make file sharing less convenient. |
| Security | The system uses company SSO and must protect contract operations by user role and ownership. | All APIs require authentication; cross-user contract/file access returns 403 in security tests. | Strong authorization adds development effort and requires consistent enforcement across controllers and services. |
| Auditability | Legal workflows need traceability of submissions, reviews, approvals, signing, and downloads. | Every major business event creates an audit/history record with actor, timestamp, action, and contract reference. | Detailed audit logging increases storage usage and requires careful design to avoid missing or incorrect audit entries. |
| Supportability / Observability | Production issues must be diagnosable because the system depends on async jobs and external services. | Logs include request ID/correlation ID; failed integrations, stuck jobs, and retry failures produce metrics or alerts. | More observability adds logging, monitoring, and alerting overhead. |

## Constraints

- Technical:
	- Authentication must use the company’s existing SSO system.
	- The current PostgreSQL database must be reused.
	- The system must integrate with the existing e-contract provider.
- Business:
	- The budget does not allow a full system rewrite
	- Initial users are mainly the Legal team, around 10 users.
- Team:
	- The team is small and has limited DevOps experience.
	- Frontend and backend are handled by separate teams.
- Operational:
	- Production issues must be detectable through logs and monitoring.
	- Critical data must be backed up and recoverable.

## Architecture Overview

- Style: Layered + modular monolith (one deployable backend WAR assembled from shared
  library modules) with a decoupled React SPA frontend.
- Components: 
	- **fcm-web** — React 18 / Vite SPA frontend
	- **fcm-service** — the single deployable backend (Spring Boot WAR), context path /fcm.
	- **fcm-template-service** — shared library modules linked into the WAR:
	- **fcm-api-clients** — OkHttp client JARs for external systems (over common-api-client).
- Data stores:
	- **MariaDB** — primary relational store (schema fcm / CommonService): contracts, templates, histories, categories, users, sequence tables for reference codes.
	- **MinIO** — object/file storage (uploaded documents) via Upload service.
	- **Kafka** — async messaging / notifications (not a store, but the backbone for events).
	- **(Local/in-memory cache)** — CacheFileService + CacheTask for cached files.
- Integrations:
	- **DSCAI — OCR** / AI document extraction (dscai-gateway-service…svc.cluster.local)
	- **eContract** — electronic signing (econtract.fpt.com)
	- **FIM** — financial info (fim-api.fpt.net)
	- **OAuth / Azure AD** — auth (login.microsoftonline.com, MS Graph)
	- Tax service, File Tool (file-tool…svc.cluster.local), AI-FIA, Chang/FoxSkill CMS (foxskill-cms-service…svc.cluster.local)
	- **Mail** — SMTP (mail-fsoft.fpt.net)
- Deployment:
	- **CICD**: Gitlab CI with two stages — build then deploy — per environment
	- **Packaging**: Docker images (tagged ${ref}-${sha} for dev, ${tag} for prod), built from the Maven WAR (Java 17, ./mvnw -Pprod clean verify).
	- **Runtime**: k8s
	- **Profiles**: dev, prod, staging, local

## Architecture Decisions

- 

## Risk assessment

|   # | Risk                                                                                                                                                                                                                      |   L |   I | Score | Mitigation                                                                                                                                                                                                                                                          |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --: | --: | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Audit gaps — history written in `AFTER_COMMIT` listener can throw or skip with no new transaction. Business state commits but audit record is lost; this can also break downloads that rely on `getAuditHistory()` links. |   2 |   3 | 🔴 6  | Write `*HistoryDAO` rows inside the main `@Transactional` service method, not in the listener. If it must stay event-driven, use `REQUIRES_NEW` + failure log/alert + retry/outbox. Add a reconciliation job that flags state changes with no matching history row. |
|   2 | Broken object-level authorization, IDOR — enforcement is per repository method. One endpoint using plain `findById` instead of the permission-checked method could leak another user's contract or file.                  |   2 |   3 | 🔴 6  | Centralize access checks through one guarded `loadContractForUser(id, user)` path. Forbid raw `findById` in services. Add a security test per controller asserting cross-user access returns `403`. Audit all 19 controllers for the gap.                           |
|   3 | Lost side effects on integration failure — mail, OCR, and eContract fire `AFTER_COMMIT` with no retry or circuit breaker. Failure can be silent and there is no rollback.                                                 |   3 |   2 | 🔴 6  | Add Resilience4j with timeout, retry, and circuit breaker to the API clients. Use a transactional outbox or Kafka for side effects so they survive failures and are retried. Alert on dead side effects.                                                            |
|   4 | Stuck async OCR/AI pipeline — `PollingService` or timers have no clear timeout or dead-letter handling. If DSCAI is slow or down, contracts may stay `in progress`.                                                       |   2 |   2 | 🟠 4  | Add max-attempt and timeout on polling, then move the contract/job to a `FAILED` state with a retry action. Dead-letter unrecoverable jobs. Surface stuck-job metrics and alerts.                                                                                   |
|   5 | Document-link privacy — MinIO or presigned link lifetime and shareability are unknown. Path-belongs-to-contract checks are useful but do not protect leaked links.                                                        |   2 |   2 | 🟠 4  | Use short-lived presigned URLs, or always proxy downloads through the permission-checked download endpoint. Never return long-lived or public links. Log link issuance.                                                                                             |

## Follow-Up Questions

- 
