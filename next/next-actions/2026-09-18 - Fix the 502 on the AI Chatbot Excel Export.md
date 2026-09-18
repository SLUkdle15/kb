# Fix the 502 on the AI Chatbot Excel Export

Area: [[areas/work-systems/work-systems|Work Systems]]
System: [[resources/software-engineering/system-architecture/2026-07-17 - AI Chat Bot System Overview|AI Chat Bot]]

## Action

Exporting to Excel returns 502. Two questions come before any fix, and they split the problem in half:

1. Does a request from today reach the service at all? If nothing hits, the 502 comes from in front of the service — proxy, gateway, or timeout — not from the export code.
2. Does the exported file exist? If the file is written and the response still fails, the export ran and the failure is in returning it.

Answer both from the logs before changing anything.

## Done When

The 502 is traced to one side of that split, and either fixed or handed to whoever owns that side.
