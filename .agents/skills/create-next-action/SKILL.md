---
name: create-next-action
description: Create and route a GTD-style action note in this Obsidian vault. Use when the user asks to add a task, next action, reminder, someday/maybe item, waiting item, or calendar action.
---

# Create Next Action

Use this skill for small commitments that are actionable but not necessarily projects.

## Inputs

- Required action statement.
- Optional date or time.
- Optional project, area, or source note to link.
- Optional route: `next-action`, `calendar`, `maybe`, or `waiting`.

## Routing Rules

Route the item by the strongest signal:

1. If it has a specific date or time, create it in `next/calendar`.
2. If it is someday/maybe, optional, or low-commitment, create it in `next/maybe`.
3. If it is blocked by someone or something else, create it in `next/waiting`.
4. Otherwise create it in `next/next-actions`.

If the action looks like it should take about 30 minutes or less but cannot be done now, it is usually a `next/next-actions` item.

If it requires multiple steps and a finish line, suggest creating a project instead.

## Note Shape

Use only the fields that fit the item:

```md
# Action Title

Project: [[projects/project-folder/project-note]]
Area: [[areas/area/area]]
Due: YYYY-MM-DD
Waiting on:

## Action

## Done When
```

## Workflow

1. Read `AGENTS.md` and `next/next.md`.
2. Extract the action, route, date/time, and related project or area from the user request.
3. Ask only for missing essentials when routing is ambiguous.
4. Create a dated note using `YYYY-MM-DD - Action Title.md`.
5. Put the note in the routed folder.
6. Link back to the project or area when provided.
7. If linked to an active project, make sure the project note links to this next action.

## Guardrails

- Do not create a project for a small single action unless the user asks.
- Do not use tags.
- Keep action notes short and executable.
- Use lowercase folder names.
