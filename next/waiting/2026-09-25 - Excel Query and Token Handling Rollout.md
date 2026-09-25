# Excel Query and Token Handling Rollout

Project: [[projects/give-the-ai-chatbot-excel-tools/give-the-ai-chatbot-excel-tools|Give the AI Chatbot Excel Tools]]
Area: [[areas/work-systems/work-systems|Work Systems]]

## Blocked

Nothing on my side. Excel query and token handling are implemented, so the piece I owned is done — what is left is other people doing theirs.

## Waiting On

Other people to implement their side and to support it once it runs. The named piece is the tenant-wide admin consent grant on the new app registration (`Files.ReadWrite.All`, `Sites.Read.All`, `offline_access`), which only someone else can give — see [[resources/software-engineering/auth/2026-09-17 - Microsoft Graph Auth Architecture for MCP Excel and OneDrive|Microsoft Graph Auth Architecture for MCP Excel and OneDrive]].

## Follow Up

No date yet — chase at the next work sync if nothing has moved.

## Done When

Their side is implemented and supported, so a real request can be answered end to end as the signed-in user.
