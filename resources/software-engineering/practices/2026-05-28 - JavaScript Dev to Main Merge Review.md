---
type: distilled-note
---

# JavaScript Dev to Main Merge Review

Related area: [[areas/technical-growth/technical-growth|Technical Growth]]
Protocol: [[areas/work-systems/merge-dev-to-production|Merge Dev to Production]]

Before merging `dev` into `main`, review what `dev` actually changed, then check the two kinds of change that need a closer look: migrations and environment configuration.

**What `dev` changed:** `git diff --name-status origin/main...origin/dev` compares `dev` against its merge base with `main`, so it lists only the files changed on `dev` since the branches split.

**Migrations:** look for a migration folder or migration files. The same diff narrowed to that folder, `git diff --name-status origin/main...origin/dev -- migrations/`, shows whether any are part of the merge.

**Environment configuration:** check whether the merge changes any environment configuration.

The step-by-step checklist lives in the protocol.
