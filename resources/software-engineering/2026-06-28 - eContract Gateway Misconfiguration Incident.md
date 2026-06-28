# eContract Gateway Misconfiguration Incident

Date: 2026-06-28

## Background

The eContract feature is being expanded from FCM (a legal-team-only project at FTEL) into a shared gateway that multiple departments can reuse. During this migration, the gateway URL in production needs to stay pointed at FCM until the expansion is ready.

## What Happened

A team member performing the upgrade accidentally set the production eContract system to point at the **dev environment** of the new gateway instead of FCM's production gateway.

## Impact

- Documents were being created successfully but callbacks never fired.
- FIM clients under FCM could not receive document results.

## Fix

- Contacted the responsible party to revert the gateway URL back to FCM production.
- Re-initiated the pending callbacks using a built-in mechanism — system restored to correct state.
- No data loss; recovery was possible because the callback re-initiation path existed.

## Lessons Learned

- 
