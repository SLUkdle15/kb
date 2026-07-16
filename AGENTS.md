# Agent Rules

## Naming and Folders

Use lowercase folder names for vault structure and links. Top-level content folders are `inbox`, `next`, `projects`, `areas`, `resources`, and `archives`.

When creating a new note from a user capture, prefix the filename with the current date:

```text
YYYY-MM-DD - Note Title.md
```

Keep the note's H1 clean and readable without the date prefix.

Use `next` for GTD-style commitments that are more actionable than inbox captures but not necessarily full projects:

- `next/next-actions` for concrete standalone actions to do soon.
- `next/calendar` for date-specific or time-specific commitments.
- `next/maybe` for someday/maybe ideas and possible future projects.
- `next/waiting` for things blocked by someone or something else.

## Projects

Every active project must have a `Next Actions` section with at least one linked note from `next/next-actions`. Project next-action notes must link back to the project.

If no next action is known, do not create an active project; leave it in `next/maybe` or clarify the next action first.

A next action may be standalone. If it is not tied to a project, link it to the relevant area, resource, or source note when useful.

## Linking

Folders decide where a note lives by actionability. Links show where the note is useful.

- Projects link to relevant areas, resources, and next actions.
- Areas link to related resources and active projects.
- Resources link back to likely projects or areas when reuse is clear.

## Agent Skills

Reusable workflows live in `.agents/skills`.

Use a matching skill before editing notes. Do not copy templates manually when a skill exists.

Keep this file focused on enforceable agent rules. For human-facing navigation and BASB concepts, use `index.md`.

## Tags

Do not use tags for topics, folders, PARA categories, sources, or note types.

Only use temporary workflow-status tags, such as `#status/waiting`, `#status/review`, or `#status/draft`.

If a tag would duplicate a folder name or a linked concept, do not add it.
