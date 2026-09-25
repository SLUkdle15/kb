# Fix the 502 on the AI Chatbot Excel Export

Area: [[areas/work-systems/work-systems|Work Systems]]
System: [[resources/software-engineering/system-architecture/2026-07-17 - AI Chat Bot System Overview|AI Chat Bot]]

## Blocked

Nothing on my side. The 502 is fixed on dev; what is left is the production deploy.

## Waiting On

The release to production. Until it ships, the export still 502s for real users.

## Follow Up

At the next deploy to production — verify an export there rather than assuming the dev fix carried.

## Original Diagnosis

Exporting to Excel returned 502. Two questions split the problem in half, and both were answerable from the logs before changing anything:

1. Does a request from today reach the service at all? If nothing hits, the 502 comes from in front of the service — proxy, gateway, or timeout — not from the export code.
2. Does the exported file exist? If the file is written and the response still fails, the export ran and the failure is in returning it.

## Done When

The fix is in production and an export there returns a file.
