# Move FIM onto the eContract Gateway

Area: [[areas/work-systems/work-systems|Work Systems]]
System: [[resources/software-engineering/system-architecture/2026-07-15 - FCM System Overview|FCM]]

## Action

FIM still goes through FCM's own eContract path; it should go through the shared gateway. The move is already executed in dev and not merged in prod, so the work next week is to establish what is actually left: which change has to be merged, who merges it, and how the prod path gets verified once it is.

Get the gateway URL right this time — pointing prod at the dev gateway is exactly what broke the callbacks in June.

Reference: [[resources/software-engineering/system-architecture/incidents/2026-06-28 - eContract Gateway Misconfiguration Incident|eContract Gateway Misconfiguration Incident]]

## Done When

The remaining steps are written down with an owner for each, or FIM is running through the gateway in prod with callbacks verified. If the list turns out to be long, promote this to a project.
