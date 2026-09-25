# Find Out Why Grep on the Logs Fails

Area: [[areas/work-systems/work-systems|Work Systems]]
Due: 2026-09-23

## Action

Greps that used to narrow a log file are coming back wrong — no hits, or not the hits expected. Reproduce it on a real file first and write down which command failed, then work out which assumption broke: the line layout (console positional vs ECS JSON), the level filter written with surrounding spaces, or the file not being the one the job actually writes to.

the json structure fuck it

Reference: [[resources/software-engineering/logging/2026-09-07 - Grep Narrows a Log File, Then Read Around the Hit|Grep Narrows a Log File, Then Read Around the Hit]] — the patterns that are supposed to work.

## Done When

The failing grep is explained, and the note above is corrected if the reason is that its patterns no longer match the logs.
Tài khoản đang bị khóa 

## Status

Completed 2026-09-25 — the greps were never wrong. They matched the right lines; the whole JSON object printed back, so the failure was in the reading. Written up in [[resources/software-engineering/logging/2026-09-25 - Grep Finds the JSON Log Line, jq Makes It Readable|Grep Finds the JSON Log Line, jq Makes It Readable]], with [[areas/work-systems/read-the-json-logs|Read the JSON Logs]] as the lookup protocol.
