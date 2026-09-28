# Give the AI Chatbot Excel Tools

## Outcome

The chatbot can act on an Excel Online file end to end — read a sheet, write back to it — for a normal signed-in user, through tools an agent can be routed to.

Area: [[areas/work-systems/work-systems|Work Systems]]
System: [[resources/software-engineering/system-architecture/2026-07-17 - AI Chat Bot System Overview|AI Chat Bot]]
Gotchas: [[projects/give-the-ai-chatbot-excel-tools/gotchas|Gotchas]]

## Definition of Done

- A real request ("read this sheet", "add this row") is answered correctly by an agent using the Excel tools.
- It works as the signed-in user, not as a shared account and not as a test account.
- Each remaining piece is either built or explicitly cut.

## Next Actions

- [[next/next-actions/2026-09-28 - Implement the Refresh Token Flow for Excel|Implement the Refresh Token Flow for Excel]]
- [[next/next-actions/2026-09-28 - Roll Out Excel Token Handling|Roll Out Excel Token Handling]]
- [[next/waiting/2026-09-25 - Excel Query Rollout|Excel Query Rollout]]

## Notes

This started as a single action — point the chatbot at an existing Excel Online MCP server. That action's own condition was that if more than a server is needed, it becomes a project. It is more: the server is the small half.

The shape of the auth is already decided in [[resources/software-engineering/auth/2026-09-17 - Microsoft Graph Auth Architecture for MCP Excel and OneDrive|Microsoft Graph Auth Architecture for MCP Excel and OneDrive]] — delegated per-user Graph tokens carried as `x-credential-token`, the workflow service owning the connection and the MCP server only consuming the header. What that decision leaves to do:

- **Admin consent** — one tenant-wide grant on the new app registration for `Files.ReadWrite.All`, `Sites.Read.All`, `offline_access`. Someone else has to do this, so it is the piece most likely to set the pace.
- **The workflow service's side** — the per-user OAuth connection, the encrypted refresh token, minting, and injecting the header on each call, with [[resources/software-engineering/auth/2026-09-17 - Proactive and Reactive OAuth Token Refresh|both halves of the refresh]]. The refresh token flow is mine: a hardcoded token stops working after 90 days, so it has to be built rather than left to someone else.
- **The MCP server's side** — token never cached, never logged, `GRAPH_ACCESS_TOKEN` unset in production, and an auth failure that tells the user in Vietnamese to reconnect their Microsoft account.

That list came from the architecture note, not from a survey of the code. It was checked against what is actually built on 2026-09-20, and the Excel clone and query are now implemented. On 2026-09-28 the token handling rollout and the refresh token flow moved to my side; admin consent and the rest of the list still belong to other people.

## Progress

- 2026-09-18 — project created from the Excel MCP server action, which is now complete.
- 2026-09-20 — list checked against what is actually built; next piece to build is the Excel clone, query, and token handling.
- 2026-09-22 — Excel clone implemented; query and token handling moved to 2026-09-23.
- 2026-09-25 — Excel query and token handling implemented; the project is now parked on a wait for other people to implement and support their side.
- 2026-09-28 — the hardcoded token will not last past 90 days, so the refresh token flow for Excel is now a next action.
- 2026-09-28 — token handling rollout split out of the wait: it is mine to implement, so it is now a next action; the wait covers only the Excel query rollout on other people's side.
