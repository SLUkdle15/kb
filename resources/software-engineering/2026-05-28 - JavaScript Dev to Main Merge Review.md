# JavaScript Dev to Main Merge Review

Related area: [[areas/software-architect-growth/software-architect-growth|Software Architect Growth]]

## Merge review steps

1. Compare `dev` against the merge base with `main`.

   ```sh
   git diff --name-status origin/main...origin/dev
   ```

   This shows files changed on `dev` since the merge base with `main`.

2. Check for migration changes.

   - Look for a migration folder or migration files.

   ```sh
   git diff --name-status origin/main...origin/dev -- migrations/
   ```

3. Check environment configuration changes.
