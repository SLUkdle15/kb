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

## Active Projects

- [[projects/give-the-ai-chatbot-excel-tools/give-the-ai-chatbot-excel-tools|Give the AI Chatbot Excel Tools]]

## Next Actions

- [[next/next-actions/2026-10-02 - Deploy the Workflow MCP to Production|Deploy the Workflow MCP to Production]] — the implementation is done, the deploy is not
- [[archives/next-actions/2026-09-29 - Update the Workflow MCP Tools and Descriptions|Update the Workflow MCP Tools and Descriptions]] — implementation completed 2026-10-02
- [[next/waiting/2026-09-18 - Fix the 502 on the AI Chatbot Excel Export|Fix the 502 on the AI Chatbot Excel Export]] — waiting on the production deploy
- [[next/maybe/2026-09-18 - Save a Push Status for Records Sent to DSC|Save a Push Status for Records Sent to DSC]] (someday/maybe)

## Captures Not Yet Filed

Raw debugging captures from these systems, still in `inbox` and not yet worth a resource note.

- [[inbox/2026-09-29 - A 200 in the Audit Log Can Be a Handled Exception|A 200 in the Audit Log Can Be a Handled Exception]] — from `fcm-template-service`: a handled exception is logged as HTTP 200, so filtering audit logs by status misses the failures. Leaves an open item, explicit connect and read timeouts on `ApiClient`.
- [[inbox/2026-09-29 - Server A to Server B Connectivity Checks|Server A to Server B Connectivity Checks]] — the order to check a failing WebClient call from A to B, and why a clean traceroute still says nothing about the port. Breaks off mid-sentence on step 5.

## Related Resources

- [[resources/software-engineering/logging/logging|Logging]] — what to log, at which level, and how it reaches Grafana
