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

## Notes

- Use the three-dot range. `git diff A...B` compares `B` against the merge base of the two branches, so it shows only what `B` changed and ignores where `A` moved on. A two-dot diff mixes both sides and produces a misleading review.
- Also run the reverse range, `git diff --name-status origin/dev...origin/main`, to see what `main` has that `dev` does not. Expect `dev` to contribute nothing to that view and `main` to differ only in production env files — `.gitlab-ci.yml` and `application-prod`. Anything else means `main` has really diverged, and the merge is about to overwrite it.
- Migrations and env vars cause most failures here, because both break at deploy time rather than at review time.
