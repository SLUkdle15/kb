---
type: distilled-note
---

# NCTool and FCM on the New Infra

Where the infra migration for the two systems I own actually stands, as of 2026-08-19. My own part of the move is done; what remains is other people's merges and verification.

## What Runs Where

Neither NCTool nor FCM runs completely in prod on the new infra yet. Dev runs on it.

- **FCM** — email and econtract are not yet checked on the new infra. The econtract move to the new gateway is executed in dev, but not merged in prod, so there is nothing in prod to verify against yet. This is what makes FCM hard to verify: dev behaviour does not prove prod behaviour when the prod path is still the old one.
- **NCTool** — has a job that runs constantly, so it cannot be confirmed migrated until the old infra is completely switched off. While both stand, there is no way to tell which one the job is actually running against.

## Settled Decisions

- The forward proxy will not be changed (per lead). It stays as it is through the migration.

## Open Questions

- Is cms-staging moved to the new infra?

## Questions This Answers

- Which parts of NCTool and FCM are actually on the new infra?
- Why can't the FCM econtract path be verified yet?
- What has to happen before the NCTool job counts as migrated?
