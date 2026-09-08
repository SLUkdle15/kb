# Fix the AI Rule Warnings in NCTool

Area: [[areas/work-systems/work-systems|Work Systems]]

## Action

`AiRuleService` floods WARN on the scheduling thread in the `nc-tool-job` pod. Three distinct things in one sample:

```text
2026-09-06 22:01:45.521 [scheduling-1] WARN o.ftel.nctool.service.AiRuleService - No configuration found for AI ID: 61.1 in contract: QNAAP8387
2026-09-06 22:01:47.391 [scheduling-1] WARN o.ftel.nctool.service.AiRuleService - No AI predictions provided for contract: 1229648826
2026-09-06 22:01:51.111 [scheduling-1] WARN o.ftel.nctool.service.AiRuleService - No configuration found for AI ID: 0.1 in contract: BDABG1480
```

- Missing config for AI IDs that jobs still ask for (`61.1`, `0.1`).
- Contracts reaching the service with no AI predictions at all.
- The `0.1` / `BDABG1480` line repeated four times inside the same millisecond — the same contract looks processed more than once.

Decide per case whether the fix is data (add the missing configuration), code (stop asking, or stop warning when absent is normal), or the duplicate processing.

Reproduce from the pod log:

```bash
grep 'WARN' logs-from-nc-tool-job-in-nc-tool-job-84676fc49c-hzj9m.log | tail -10
```

Read around a hit to see what the job did before the warning — see [[resources/software-engineering/logging/2026-09-07 - Grep Narrows a Log File, Then Read Around the Hit|Grep Narrows a Log File, Then Read Around the Hit]].

## Done When

Each of the three is either fixed or knowingly accepted, and a WARN grep on a fresh log no longer shows this noise.

## Disposition

Completed 2026-09-08.
