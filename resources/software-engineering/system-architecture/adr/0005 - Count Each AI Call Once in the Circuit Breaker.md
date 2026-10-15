# Count Each AI Call Once in the Circuit Breaker

System: NCTool (`nc-tool-job`) — [[areas/work-systems/work-systems|Work Systems]]

## Status

Proposed, 2026-10-12. Not implemented yet. To be decided in [[next/next-actions/2026-10-12 - Refactor the Breaker Incident Note and Finish ADR 0005|Refactor the Breaker Incident Note and Finish ADR 0005]].

## Context

- On 30 Sep 2026, one slow AI call opened the breaker, and 334 jobs were rejected in 2.8 seconds. See [[resources/software-engineering/system-architecture/incidents/2026-09-30 - Retry Around the Breaker Turned One Slow AI Call Into 334 Rejected Jobs|the incident]].
- Retry wraps the breaker, so one call writes 3 failures into a window of 5. See [[resources/software-engineering/practices/2026-10-12 - Retry Around a Circuit Breaker Counts Every Attempt as a Failure|why that's bad]].
- `JobRunner` counts a breaker rejection as a job failure.


## Decision



## Consequences


## Compliance


## Notes

-