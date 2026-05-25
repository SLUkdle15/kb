---
name: rename-capture
description: Refine filenames and H1 titles for captured notes found in raw. Use when the user asks to rename, clean up naming, title, or make a raw capture easier to find.
---

# Rename Capture

Use this skill to improve the filename and H1 of a captured note that currently lives in `raw`.

## Inputs

- Required note path or title fragment, unless there is only one plausible note in `raw`.
- Optional `mode`: `suggest` or `apply`. Default to `suggest`.

## Workflow

1. Read `AGENTS.md` and `resources/agent-skills.md`.
2. Locate the target note only under `raw`. Do not search `inbox`, `projects`, `areas`, `resources`, or `archives` for rename targets.
3. Read the note body before naming.
4. Identify the durable idea, source, model, or use case.
5. Propose a filename using `YYYY-MM-DD - Note Title.md` for the renamed capture.
6. Propose a clean H1 without the date prefix.
7. In `apply` mode, move the renamed markdown note from `raw` to `inbox` and update the H1.

## Naming Rules

- Use the note's existing date prefix or `created` frontmatter date when present; otherwise use the current date.
- Prefer specific titles over broad topic labels.
- Keep folder names lowercase.
- Preserve original note content.
