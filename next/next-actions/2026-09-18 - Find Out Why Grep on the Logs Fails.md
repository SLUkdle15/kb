# Find Out Why Grep on the Logs Fails

Area: [[areas/work-systems/work-systems|Work Systems]]

## Action

Greps that used to narrow a log file are coming back wrong — no hits, or not the hits expected. Reproduce it on a real file first and write down which command failed, then work out which assumption broke: the line layout (console positional vs ECS JSON), the level filter written with surrounding spaces, or the file not being the one the job actually writes to.

Reference: [[resources/software-engineering/logging/2026-09-07 - Grep Narrows a Log File, Then Read Around the Hit|Grep Narrows a Log File, Then Read Around the Hit]] — the patterns that are supposed to work.

## Done When

The failing grep is explained, and the note above is corrected if the reason is that its patterns no longer match the logs.
