# Deploy the Workflow MCP to Production

Area: [[areas/work-systems/work-systems|Work Systems]]
Protocol: [[areas/work-systems/merge-dev-to-production|Merge Dev to Production]]
System: [[resources/software-engineering/system-architecture/2026-07-17 - AI Chat Bot System Overview|AI Chat Bot]]

## Action

Ship the workflow MCP work to production. The implementation finished on 2026-10-02 — the tool set is back in line with the workflow system and every description is rewritten against real behavior, see [[archives/next-actions/2026-09-29 - Update the Workflow MCP Tools and Descriptions|Update the Workflow MCP Tools and Descriptions]]. It is on `dev` and the team cannot use it from there.

Follow the protocol's checklist rather than merging straight across. The env-var step is the one that matters here: the MCP's tool definitions are what an agent reads to pick a tool, so a stale description in production is worse than a missing one.

## Done When

`dev` is merged to `main`, the deploy is out, and the team is calling the current tool set in production.
