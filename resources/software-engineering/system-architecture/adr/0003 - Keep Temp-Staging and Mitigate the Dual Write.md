# Keep temp-staging for uploads; mitigate the dual write

System: [[resources/software-engineering/system-architecture/2026-07-15 - FCM System Overview|FCM]]

## Status

Accepted, 2026-09-04. Retroactive: temp-staging predates this ADR. What is being decided here is to keep it and mitigate it, not to adopt it.

## Context

- solving the abandonned file upload
- easy clean 
- but introduce dual write problem: the temp path prefix denormalizes a fact the database owns into the storage key space. "Is this file referenced by a saved record?" belongs to the DB; staging copies it into the object's prefix, so the same fact has two representations that can disagree, with nothing to reconcile them. Dual write is the symptom; denormalization without reconciliation is the disease.
- Trigger: the contract 154 incident, 2026-09-03.

## Options Considered

- **Keep temp-staging and mitigate it** (chosen). Local change, no reshaping of existing flows.
- **Upload straight to the final path and collect orphans with a reconciliation job** (rejected). This is the structurally cleaner option: one write, and the DB stays the only owner of "is this referenced." Rejected because `moveFileFromTemp` has seven call sites across `ContractEventListener` and `TemplateEventListener`, so it is a refactor of the contract and template flows rather than a contained fix.

## Decision

- Increase the timeout on the move.
- On timeout, verify the destination instead of treating the timeout as a failure. This is the half that matters: no timeout value can distinguish "still working" from "dead."
- On read, fall back to looking the file up in temp.

## Consequences

- A genuine move failure still tells the user "saved." The move runs `AFTER_COMMIT` and cannot roll the row back, so this ADR does not fix that — it only narrows how often it happens and makes it visible afterwards.
- A timeout is now distinguishable from a genuine failure. Previously they were indistinguishable, which is why the incident took as long as it did to diagnose.
- `MOVE_FILE_HAS_EXCEPTION` becomes a real signal rather than noise, and `DOWNLOAD_FILE_SERVED_FROM_TEMP` is alertable: if that line appears, a move did not complete.

## Compliance

- New document types upload straight to their final path. Do not extend temp-staging.
- Nothing may purge `temp/`. The read fallback depends on those orphaned bytes still being there; a lifecycle rule on the temp prefix would convert a recoverable inconsistency into real data loss.

## Notes

- Names for the pattern, for future reference: denormalization without reconciliation (the disease), dual write (the symptom), single source of truth (the principle violated). It also inverts "make the common case fast" — except the cost here is correctness surface, not latency, which makes it worse than the usual version of that mistake.
- Prefer leaks over dangling references. A failed save that leaves an unreferenced file is a leak: garbage, collectable, harmless. A failed save that leaves a row pointing at nothing is corruption. The current ordering produces the second; committing the DB row last would produce the first. This is the cheapest structural improvement still available and is not taken here.
- Standard remedies for this shape: transactional outbox, saga / compensating transaction, reconciliation job. The rejected option above is the last one.
