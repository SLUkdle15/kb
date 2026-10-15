# Refactor the Breaker Incident Note and Finish ADR 0005

Area: [[areas/work-systems/work-systems|Work Systems]]
Incident: [[resources/software-engineering/system-architecture/incidents/2026-09-30 - Retry Around the Breaker Turned One Slow AI Call Into 334 Rejected Jobs|Retry Around the Breaker Turned One Slow AI Call Into 334 Rejected Jobs]]
ADR: [[resources/software-engineering/system-architecture/adr/0005 - Count Each AI Call Once in the Circuit Breaker|Count Each AI Call Once in the Circuit Breaker]]

## Action

1. **Refactor the incident note.** Cut it down to what happened and why. The reusable lesson already lives in [[resources/software-engineering/practices/2026-10-12 - Retry Around a Circuit Breaker Counts Every Attempt as a Failure|the practices note]], and the fix belongs in the ADR.
2. **Fill in the rest of ADR 0005**: Decision, Consequences, Compliance and Notes. Questions to settle:
   - Order: breaker outside retry, or keep retry outside with a window sized in attempts.
   - Window: `slidingWindowSize` and `minimumNumberOfCalls`, both set explicitly, or `TIME_BASED`.
   - `JobRunner`: pause and requeue on `CallNotPermittedException` without using up a retry.

## Done When

The incident note is refactored, and ADR 0005 has every section filled in, with Status set to Accepted. Implementing the fix becomes its own next action.
