# Fix the Duplicate Bug in NCTool and Excel

Area: [[areas/work-systems/work-systems|Work Systems]]
Protocol: [[areas/work-systems/read-the-json-logs|Read the JSON Logs]]
Due: 2026-10-05

## Action

Records are coming out duplicated in NCTool and in the Excel output. Fix it.

Establish first whether this is one bug or two, because the answer changes the fix. If NCTool processes a record twice, the Excel export is only reporting faithfully what it was given and there is nothing to fix on the export side. If NCTool's data is clean and the duplication appears only in the sheet, it is the export — a row written per iteration, or a sheet appended to rather than replaced.

NCTool already has a known duplicate-processing symptom: [[archives/next-actions/2026-09-07 - Fix the AI Rule Warnings in NCTool|Fix the AI Rule Warnings in NCTool]] caught the same contract logged four times inside one millisecond, and that case was left undecided — data, code, or duplicate processing. Check whether this is that, resurfacing with a visible consequence.

Count before fixing: how many duplicates, on how many records, and whether they are exact copies or differ in a field. Exact copies point at a repeated run or a missing idempotency key; near-copies point at the record being rebuilt differently each pass.

## Done When

The duplication is traced to one side — NCTool or the export — the cause is named, and a run produces one row per record.
