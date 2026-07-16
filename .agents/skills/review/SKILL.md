---
name: review
description: Run a weekly review for this Obsidian BASB/PARA and GTD-style vault. Use when the user asks to review the week, clear inbox, review active projects, inspect next actions, or choose focus for next week.
---

# Weekly Review

Use this skill to review and maintain the vault without relying on a copy-paste template.

## Inputs

- Optional `mode`: `suggest` or `apply`. Default to `suggest`.
- Optional focus area, such as `projects`, `inbox`, `next`, or `areas`.

## Essential Review Checks

Run only the checks needed for the user's request:

```md
# Weekly Review - YYYY-MM-DD

## Inbox

## Next Actions

## Active Projects

## Areas Under Pressure

## Stale or Completed Items

## Focus for Next Week
```

Do not force a review note unless the user asks to create one or uses `mode=apply`.

## Workflow

1. Read `AGENTS.md`, `index.md`, and `projects/projects.md`.
2. Inspect `inbox`, `next`, and `projects`.
3. Check that every active project has at least one linked next action.
4. Identify notes that should move to `projects`, `areas`, `resources`, `archives`, or `next`.
5. In `suggest` mode, report recommended changes and missing next actions.
6. In `apply` mode:
   - Create a dated review note only if useful.
   - Apply obvious moves.
   - Leave ambiguous items in place with clear questions.

## Guardrails

- Do not inspect files outside the vault unless the user explicitly asks.
- Do not delete notes.
- Ask before moving ambiguous items.
