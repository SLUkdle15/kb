# Add an Excel Online MCP Server to the AI Chatbot

Area: [[areas/work-systems/work-systems|Work Systems]]
System: [[resources/software-engineering/system-architecture/2026-07-17 - AI Chat Bot System Overview|AI Chat Bot]]

## Action

Add an Excel Online MCP server as a tool for `aichatbot-service`, so agents can read and write spreadsheets. MCP servers are already one of the tool sources the supervisor routes to.

First question to settle: whether an existing Excel Online / Microsoft Graph MCP server can be pointed at, or one has to be written. If it is the second, this is a project rather than a single action.

## Done When

The chatbot can act on an Excel Online file through MCP, or the scope is re-cut into a project.
