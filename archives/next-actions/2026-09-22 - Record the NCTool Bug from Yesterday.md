# Record the NCTool Bug from Yesterday

Area: [[areas/work-systems/work-systems|Work Systems]]

## Action

Write down the NCTool bug hit on 2026-09-21 while it is still fresh — what was run, what happened, what was expected, and which log or record shows it.

## Done When

The bug is recorded with enough detail to reproduce it, and either filed as a fix action or ruled out as not worth one.

## Outcome

An untested change went to production assuming T-1 data that CSOC does not provide on the current day, so the job lost the T-1 day's data. The change was reverted and a manual HTTP trigger was opened on production. No further fix action: the manual trigger covers a missed run.
