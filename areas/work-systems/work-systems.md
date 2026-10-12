---
type: area
---

# Work Systems

## Purpose

Maintain the systems I am responsible for at work — currently NCTool and FCM — so they stay healthy, observable, and supportable.

## Standard to Maintain

- Keep logging and monitoring usable in Grafana.
- Track infra migrations through to completion.
- Turn recurring maintenance pain into a project or a next action instead of ad-hoc fixes.

## Systems

- **NCTool** — [[resources/software-engineering/system-architecture/2026-09-30 - Retry Around the Breaker Turned One Slow AI Call Into 334 Rejected Jobs|the 30 Sep 2026 breaker outage]], fix proposed in [[resources/software-engineering/system-architecture/adr/0005 - Count Each AI Call Once in the Circuit Breaker|ADR 0005]]
- **FCM**

## Review Rhythm

Review monthly, or weekly when a migration or incident is active.

## Protocols

- [[areas/work-systems/merge-dev-to-production|Merge Dev to Production]]
- [[areas/work-systems/read-the-json-logs|Read the JSON Logs]]
- [[areas/work-systems/add-an-haproxy-route|Add an HAProxy Route]]
- [[areas/work-systems/check-server-to-server-connectivity|Check Server-to-Server Connectivity]]

## Active Projects

- [[projects/give-the-ai-chatbot-excel-tools/give-the-ai-chatbot-excel-tools|Give the AI Chatbot Excel Tools]]

## Next Actions

- [[next/next-actions/2026-10-12 - Refactor the Breaker Incident Note and Finish ADR 0005|Refactor the Breaker Incident Note and Finish ADR 0005]] — then implement the breaker fix
- [[archives/next-actions/2026-10-12 - Deploy FCM to Production and Repoint the 230 Callback to Signgate|Deploy FCM to Production and Repoint the 230 Callback to Signgate]] — completed 2026-10-12
- [[archives/next-actions/2026-10-06 - Deploy the NCTool AI Code to Production|Deploy the NCTool AI Code to Production]] — completed 2026-10-06
- [[archives/next-actions/2026-10-02 - Fix the FCM Mail Authentication Failure|Fix the FCM Mail Authentication Failure]] — SMTP 535 on `MailService.sendEmail`, completed 2026-10-06
- [[archives/next-actions/2026-10-05 - Add Column Lock and Filter to Clone Sheet|Add Column Lock and Filter to Clone Sheet]] — AI Excel tools, completed 2026-10-05
- [[archives/next-actions/2026-10-02 - Deploy the Workflow MCP to Production|Deploy the Workflow MCP to Production]] — completed 2026-10-02
- [[archives/next-actions/2026-09-29 - Update the Workflow MCP Tools and Descriptions|Update the Workflow MCP Tools and Descriptions]] — implementation completed 2026-10-02
- [[archives/next-actions/2026-09-18 - Verify the AI Chatbot Excel Export Fix in Production|Verify the AI Chatbot Excel Export Fix in Production]] — completed 2026-10-06
- [[next/maybe/2026-09-18 - Save a Push Status and Run the DSC Push in Parallel|Save a Push Status and Run the DSC Push in Parallel]] (someday/maybe)

## Captures Not Yet Filed

Raw debugging captures from these systems, still in `inbox` and not yet worth a resource note.

- None.

## Related Resources

- [[resources/software-engineering/logging/logging|Logging]] — what to log, at which level, and how it reaches Grafana
