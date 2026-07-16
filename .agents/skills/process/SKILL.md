---
name: process
description: Process one specified Markdown note from inbox. Use when the user asks to rename, clean up, classify, route, split, move, distill, or organize a specific inbox capture.
---

# Process Inbox

Use this skill to turn one user-specified inbox capture into useful vault material. This includes light cleanup, destination suggestions, splitting mixed captures, moving or creating draft notes, and distilling reusable ideas.

## Inputs

- Required note path or title fragment under `inbox`.
- Optional `mode`: `suggest` or `apply`. Default to `suggest` unless the user clearly asks to move, create, or update files.
- Do not process the whole `inbox` folder. If the user does not specify a note, ask for the note path or title fragment.

## Workflow

1. Read `AGENTS.md`, `index.md`, and the target inbox note.
2. Locate exactly one target note only under `inbox`. Do not search `raw`, `projects`, `areas`, `resources`, or `archives` for targets.
   - If no note path or title fragment is provided, stop and ask the user for one.
   - If the title fragment matches multiple notes, stop and ask the user to choose one.
   - Do not list, scan, summarize, or process unrelated inbox notes.
3. Read the note body before naming, routing, splitting, or distilling.
4. Detect what the capture contains:
   - Concrete action, calendar item, waiting item, or someday/maybe item.
   - Active project outcome with a finish line.
   - Ongoing area material.
   - Reusable resource or reference.
   - Raw source artifact reference.
   - Draft thought or source material that needs distillation.
5. Suggest where each part should go by actionability:
   - `next/next-actions`, `next/calendar`, `next/maybe`, or `next/waiting` for commitments.
   - `projects` for active outcomes with a finish line and at least one next action.
   - `areas` for ongoing responsibilities.
   - `resources` for reusable knowledge.
   - `archives` for inactive material.
   - `raw` only for non-note source artifacts.
6. Decide whether to keep the note whole or split it:
   - Split when one capture contains multiple durable ideas, multiple actions, or mixed project/resource material.
   - Keep whole when the note has one clear use and splitting would create weak fragments.
7. In `suggest` mode, report the classification, recommended destination, split plan, and unresolved questions. Do not edit files.
8. In `apply` mode, create or move draft notes using the rules below.

## Light Refine Only

If the user only asks to rename, clean up naming, improve formatting, add a clean H1, or make an inbox capture easier to find and read:

1. Identify the durable idea, source, model, or use case.
2. Lightly edit the Markdown so it is readable and consistent:
   - Keep or add one clean H1 without the date prefix.
   - Use sentence-style section headings for meaningful groups.
   - Convert label lines such as `Core idea:` into proper headings when useful.
   - Normalize bullet and numbered lists.
   - Do not add frontmatter/properties unless the user explicitly asks for them.
   - Preserve existing frontmatter only when it contains source metadata the user still wants to keep.
3. Rename the markdown note inside `inbox` using `YYYY-MM-DD - Note Title.md`.
4. Report the old path, new path, and new H1.

## Apply Mode

When creating organized notes:

1. Use dated filenames: `YYYY-MM-DD - Note Title.md`.
2. Put notes in the folder where they will be useful next.
3. Add a clean H1 without the date prefix.
4. Link new notes back to the source inbox note unless the source note is moved whole.
5. If creating a next action, follow the `next` skill.
6. If creating an active project, follow the `project` skill and ensure at least one linked next action exists.
7. If material is ambiguous, leave it in `inbox` and report the question instead of forcing a move.

## Distillation

Distilled notes should preserve the reusable idea, not the whole source. Use this shape when it fits:

```md
# Note Title

Source: [[inbox/source-note]]

## Core Idea

## Why It Matters

## Useful Details

## Use Next
```

Keep distillation concise. Preserve uncertainty from the source note when the capture is a draft thought.

## Naming Rules

- Use the note's existing date prefix when present; otherwise use the current date.
- Prefer specific titles over broad topic labels.
- Keep folder names lowercase.
- Preserve original note content when refining in place.
- Do not add topic tags or PARA category tags.
- Do not rewrite the note into a new argument; preserve the captured meaning.
- Avoid creating many tiny notes that have no clear future use.

## Reporting

Report:

- Source note path.
- Classification.
- Destination or split plan.
- Files moved or created.
- Distilled notes created.
- Questions left unresolved.
