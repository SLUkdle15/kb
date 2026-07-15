# Git Hooks

Versioned copies of this vault's git hooks. Git does not run hooks from this
folder — after cloning, install them with:

```sh
cp .agents/hooks/pre-commit .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```

- `pre-commit` — regenerates `calendar.ics` (via `.agents/scripts/build_calendar_ics.py`) whenever a commit touches `next/calendar`.
