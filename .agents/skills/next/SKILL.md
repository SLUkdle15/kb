---
name: next
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
Protocol: [[areas/area/protocol-name]]
Due: YYYY-MM-DD
Waiting on:

## Action

## Done When
```

## Workflow

1. Read `AGENTS.md` and `next/next.md`.
2. Extract the action, route, date/time, and related project or area from the user request.
3. Ask only for missing essentials when routing is ambiguous.
4. Check the owning area's index note for a `## Protocols` section. If a protocol covers the activity behind the action:
   - Add a `Protocol:` link to the protocol note in the action note.
   - Read the protocol's checklist and surface unmet items as extra suggested actions (for example, a dinner action matching the weekday-dinner protocol also suggests logging the restaurant in `resources/restaurants`).
5. Create a dated note using `YYYY-MM-DD - Action Title.md`.
6. Put the note in the routed folder.
7. Link back to the project or area when provided.
8. If linked to an active project, make sure the project note links to this next action.

## Guardrails

- Do not create a project for a small single action unless the user asks.
- Do not use tags.
- Keep action notes short and executable.
- Use lowercase folder names.
