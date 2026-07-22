# AI Chat Bot System Overview

System: AI chat bot — enterprise AI chatbot platform for FPT (internal corporate use).

Related area: [[areas/software-architect-growth/software-architect-growth|Software Architect Growth]]

## Scope

- Monorepo with one application.
- `aichatbot-service` — the core chatbot runtime. A Node.js/Express backend that runs a LangGraph multi-agent system: a supervisor routes user messages to specialist AI agents, which use tools (HRIS employee/leave/tax data, contracts, inventory, Google Calendar, MCP servers, DB-configured dynamic tools), RAG over Weaviate, skills (SOP-style instructions), and stream answers back over SSE.
- Serves multiple integration "partners" (HRAI Portal, FChat, FoxPro SDK, CMS…).

## Architecture Characteristics

- Drivers: configurability/extensibility, integrability, availability, supportability.
- Implicit: security (authn/authz).
- Explicitly deprioritized for the early phase: performance and scalability.

## Architecture Decisions

- [[resources/software-engineering/system-architecture/adr/0002 - Choose Email to Reference Instead of ID|Choose Email to Reference Instead of ID]]
