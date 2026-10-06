# Deploy FCM to Production and Repoint the 230 Callback to Signgate

Area: [[areas/work-systems/work-systems|Work Systems]]
Protocol: [[areas/work-systems/merge-dev-to-production|Merge Dev to Production]]
Due: 2026-10-12

## Action

Merge FCM `dev` into `main` and deploy to production. In the same pass, reconfigure `230` so its callback points back to signgate.

A wrong callback target is the failure that already happened once here — see [[resources/software-engineering/system-architecture/2026-06-28 - eContract Gateway Misconfiguration Incident|eContract Gateway Misconfiguration Incident]]: documents kept being created while callbacks silently went nowhere. It surfaces as nothing happening rather than as an error, so confirm a callback actually arrives instead of trusting that the config took.

## Done When

Production is running the deployed FCM code, `230` calls back to signgate, and one document round-trips with its callback received.
