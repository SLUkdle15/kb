---
name: rename-inbox
description: Refine filenames and H1 titles for captured notes found in inbox. Use when the user asks to rename, clean up naming, title, or make an inbox capture easier to find.
---

# Rename Inbox

Use this skill to improve the filename and H1 of a captured note that currently lives in `inbox`.

## Inputs

- Required note path or title fragment, unless there is only one plausible note in `inbox`.

## Workflow

1. Read `AGENTS.md`.
2. Locate the target note only under `inbox`. Do not search `raw`, `projects`, `areas`, `resources`, or `archives` for rename targets.
3. Read the note body before naming.
4. Identify the durable idea, source, model, or use case.
5. Rename the markdown note inside `inbox` using `YYYY-MM-DD - Note Title.md`.
6. Update the H1 to a clean title without the date prefix.
7. Report the old path, new path, and new H1.

## Naming Rules

- Use the note's existing date prefix or `created` frontmatter date when present; otherwise use the current date.
- Prefer specific titles over broad topic labels.
- Keep folder names lowercase.
- Preserve original note content.
