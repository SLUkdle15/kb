---
type: protocol
---

# Merge Dev to Production

Source: [[resources/software-engineering/practices/2026-05-28 - JavaScript Dev to Main Merge Review|JavaScript Dev to Main Merge Review]]

Use when merging `dev` into `main` for a production deploy.

## Checklist

- [ ] `git log main..dev --oneline`
- [ ] Review the full diff against the merge base: `git diff --name-status origin/main...origin/dev`.
- [ ] Check migrations — backward-compatible with the deployed code, and note whether each runs before or after the deploy.
- [ ] Check environment config — every new or renamed env var and secret exists in production before the merge.
- [ ] Merge and deploy.

## Notes

- Use the three-dot range. `git diff main...dev` # Only changes made on dev since it branched off main (ignores new commits on main)
