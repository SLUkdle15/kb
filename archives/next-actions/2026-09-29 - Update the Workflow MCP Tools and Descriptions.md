# Update the Workflow MCP Tools and Descriptions

Area: [[areas/work-systems/work-systems|Work Systems]]
System: [[resources/software-engineering/system-architecture/2026-07-17 - AI Chat Bot System Overview|AI Chat Bot]]

## Action

Asked in chat on 2026-09-29: bring the workflow MCP server back in line with the workflow system as it is now, and write the tool descriptions properly so the team can use it.

Two parts:

- **Drift** — diff the MCP's exposed tools against what the workflow system actually offers today, and update anything that changed, was added, or was removed.
- **Descriptions** — rewrite each tool's description against real system behavior, not the original guess. These are what an agent and a teammate both read to pick a tool, so they have to say what the tool really does, what it needs, and when not to use it.

Shipping it to the team means it reaches production — use [[areas/work-systems/merge-dev-to-production|Merge Dev to Production]] for that step.

## Done When

The workflow MCP exposes the current tool set, every description matches actual behavior, and it is deployed where the team can use it.

## Outcome

Implementation done 2026-10-02: the exposed tool set matches the workflow system and every description is rewritten against real behavior.

The deploy half of the Done When was not met — the work is on `dev` and has not reached production. Carried into [[next/next-actions/2026-10-02 - Deploy the Workflow MCP to Production|Deploy the Workflow MCP to Production]] rather than left implied by an archived note.
