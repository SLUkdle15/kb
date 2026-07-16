---
name: complete
description: Complete or dispose of a PARA project or a GTD action in this Obsidian vault — mark it done, canceled, paused, or obsolete and move it to archives. Use when the user asks to finish, complete, close, archive, clean up, or retire a project or a next/calendar/maybe/waiting action.
---

# Complete

Use this skill when a project or an action is completed, canceled, paused, obsolete, or no longer active.

## Inputs

- Required target: a project folder, project note, action note, or title fragment.
- Optional status: `completed`, `canceled`, `paused`, or `obsolete`.
- Optional `mode`: `suggest` or `apply`. Default to `suggest`.

## Completing an Action

For notes under `next/next-actions`, `next/calendar`, `next/maybe`, or `next/waiting`:

1. Read `AGENTS.md` and the action note.
2. Confirm the status. If unclear whether it is done or just stale, ask.
3. In `suggest` mode, report the plan.
4. In `apply` mode:
   - Move the note to `archives/next-actions`.
   - Remove its entry from the folder index note (`next-actions.md`, `calendar.md`, `maybe.md`, or `waiting.md`).
   - If a project links to it, update the project's `Next Actions` section; an active project must keep at least one linked next action, so surface it if this was the last one.
   - Remove any workflow-status tags such as `#status/waiting`.

## Completing a Project

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

### Workflow

1. Read `AGENTS.md` and `projects/projects.md`.
2. Inspect the target project folder and notes.
3. Determine the disposal status.
4. Identify reusable material that belongs in `areas` or `resources`.
5. Handle the project's open actions: complete them alongside the project or surface the ones that should survive it.
6. In `suggest` mode, report the archive plan.
7. In `apply` mode:
   - Create a completion note when useful.
   - Move reusable material into `areas` or `resources`.
   - Move the inactive project folder into `archives`.
   - Remove the project from `projects/projects.md`.
   - Update obvious links.

## Guardrails

- Do not delete material unless explicitly requested; archive it.
- Do not archive active projects without a clear status.
- If status, reusable material, or archive destination is unclear, ask before applying changes.
