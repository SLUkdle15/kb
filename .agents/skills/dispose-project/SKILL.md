---
name: dispose-project
description: Dispose, close, pause, cancel, complete, or archive a PARA project in this Obsidian vault. Use when the user asks to finish, archive, clean up, or retire a project.
---

# Dispose Project

Use this skill when a project is completed, canceled, paused, obsolete, or no longer active.

## Inputs

- Required project folder, project note, or title fragment.
- Optional status: `completed`, `canceled`, `paused`, or `obsolete`.
- Optional `mode`: `suggest` or `apply`. Default to `suggest`.

## Essential Disposal Fields

When a completion note is useful, keep it short:

```md
# Project Completion

## Status

## Outcome

## Reusable Material

## Lessons

## Archive Actions
```

Ask only for missing essentials before applying destructive-looking moves.

## Workflow

1. Read `AGENTS.md` and `projects/projects.md`.
2. Inspect the target project folder and notes.
3. Determine the disposal status.
4. Identify reusable material that belongs in `areas` or `resources`.
5. In `suggest` mode, report the archive plan.
6. In `apply` mode:
   - Create a completion note when useful.
   - Move reusable material into `areas` or `resources`.
   - Move the inactive project folder into `archives`.
   - Update obvious links.

## Guardrails

- Do not delete project material unless explicitly requested.
- Do not archive active projects without a clear status.
- If project status, reusable material, or archive destination is unclear, ask before applying changes.
