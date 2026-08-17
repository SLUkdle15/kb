---
type: protocol
---

# Merge Dev to Production

Source: [[resources/software-engineering/2026-05-28 - JavaScript Dev to Main Merge Review|JavaScript Dev to Main Merge Review]]

Use when merging `dev` into `main` for a production deploy.

## Checklist

- [ ] Review the full diff against the merge base: `git diff --name-status origin/main...origin/dev`.
- [ ] Check migrations — backward-compatible with the deployed code, and note whether each runs before or after the deploy.
- [ ] Check environment config — every new or renamed env var and secret exists in production before the merge.
- [ ] Merge and deploy.
- [ ] Verify in production: the changed paths work and Grafana looks normal.

## Notes

- Use the three-dot range. A two-dot diff hides what `main` moved on and produces a misleading review.
- Migrations and env vars cause most failures here, because both break at deploy time rather than at review time.
