# JavaScript Dev to Main Merge Review Checklist

Related area: [[areas/software-engineering/software-engineering|Software Engineering]]

## Merge review steps

1. Check for migration changes.
   - Look for a migration folder or migration files.

2. Compare `dev` against the merge base with `main`.

   ```sh
   git diff --name-status origin/main...origin/dev
   ```

   This shows files changed on `dev` since the merge base with `main`.

3. Check environment configuration changes.
