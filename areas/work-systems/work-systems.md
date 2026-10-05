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

- **NCTool**
- **FCM**

## Review Rhythm

Review monthly, or weekly when a migration or incident is active.

## Protocols

- [[areas/work-systems/merge-dev-to-production|Merge Dev to Production]]
- [[areas/work-systems/read-the-json-logs|Read the JSON Logs]]
- [[areas/work-systems/check-server-to-server-connectivity|Check Server-to-Server Connectivity]]

## Active Projects

- [[projects/give-the-ai-chatbot-excel-tools/give-the-ai-chatbot-excel-tools|Give the AI Chatbot Excel Tools]]

## Next Actions

- [[next/calendar/2026-10-06 - Deploy the NCTool AI Code to Production|Deploy the NCTool AI Code to Production]] — dated Tue 2026-10-06
- [[next/next-actions/2026-10-02 - Fix the FCM Mail Authentication Failure|Fix the FCM Mail Authentication Failure]] — SMTP 535 on `MailService.sendEmail`, undated since 2026-10-05
- [[archives/next-actions/2026-10-05 - Add Column Lock and Filter to Clone Sheet|Add Column Lock and Filter to Clone Sheet]] — AI Excel tools, completed 2026-10-05
- [[archives/next-actions/2026-10-02 - Deploy the Workflow MCP to Production|Deploy the Workflow MCP to Production]] — completed 2026-10-02
- [[archives/next-actions/2026-09-29 - Update the Workflow MCP Tools and Descriptions|Update the Workflow MCP Tools and Descriptions]] — implementation completed 2026-10-02
- [[next/next-actions/2026-09-18 - Verify the AI Chatbot Excel Export Fix in Production|Verify the AI Chatbot Excel Export Fix in Production]] — deployed 2026-10-02; verify an export in production
- [[next/maybe/2026-09-18 - Save a Push Status and Run the DSC Push in Parallel|Save a Push Status and Run the DSC Push in Parallel]] (someday/maybe)

## Captures Not Yet Filed

Raw debugging captures from these systems, still in `inbox` and not yet worth a resource note.

- [[inbox/2026-09-29 - A 200 in the Audit Log Can Be a Handled Exception|A 200 in the Audit Log Can Be a Handled Exception]] — from `fcm-template-service`: a handled exception is logged as HTTP 200, so filtering audit logs by status misses the failures. Leaves an open item, explicit connect and read timeouts on `ApiClient`.

## Related Resources

- [[resources/software-engineering/logging/logging|Logging]] — what to log, at which level, and how it reaches Grafana
