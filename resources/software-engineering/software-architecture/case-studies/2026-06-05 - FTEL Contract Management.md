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

## Architecture characteristics

- **Reliability**: split into integration fault-tolerance + data integrity/consistency across the async wf
- **Privacy**: financial & personal contract data
- **Security**: authentication and authorization
- **Auditability**:  history tables, signing trail, MDC tracing
- **Supportability / Observability** — logging, request IDs for tracing

## Constraints

- Technical:
- Business:
	- Initial users are mainly the Legal team, around 10 users.
- Team:
- Operational:

## Architecture Overview

- Style: Layered + modular monolith (one deployable backend WAR assembled from shared
  library modules) with a decoupled React SPA frontend.
- Components: 
	- **fcm-web** — React 18 / Vite SPA frontend
	- **fcm-service** — the single deployable backend (Spring Boot WAR), context path /fcm.
	- **fcm-template-service** — shared library modules linked into the WAR:
	- **fcm-api-clients** — OkHttp client JARs for external systems (over common-api-client).
- Data stores:
	- **MySQL** — primary relational store (schema fcm / CommonService): contracts, templates, histories, categories, users, sequence tables for reference codes.
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
|   3 | Lost side effects on integration failure — mail, OCR, and eContract fire `AFTER_COMMIT` with no retry or circuit breaker. Failure can be silent and there is no rollback.                                                 |   3 |   2 | 🟠 6  | Add Resilience4j with timeout, retry, and circuit breaker to the API clients. Use a transactional outbox or Kafka for side effects so they survive failures and are retried. Alert on dead side effects.                                                            |
|   4 | Stuck async OCR/AI pipeline — `PollingService` or timers have no clear timeout or dead-letter handling. If DSCAI is slow or down, contracts may stay `in progress`.                                                       |   2 |   2 | 🟠 4  | Add max-attempt and timeout on polling, then move the contract/job to a `FAILED` state with a retry action. Dead-letter unrecoverable jobs. Surface stuck-job metrics and alerts.                                                                                   |
|   5 | Document-link privacy — MinIO or presigned link lifetime and shareability are unknown. Path-belongs-to-contract checks are useful but do not protect leaked links.                                                        |   2 |   2 | 🟠 4  | Use short-lived presigned URLs, or always proxy downloads through the permission-checked download endpoint. Never return long-lived or public links. Log link issuance.                                                                                             |

## Follow-Up Questions

- 
