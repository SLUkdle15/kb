---
name: refine-inbox
description: Refine captured Markdown notes found in inbox. Use when the user asks to rename, clean up naming, improve formatting, add a clean H1, or make an inbox capture easier to find and read.
---

# Refine Inbox

Use this skill to improve the filename, H1, and Markdown readability of a captured note that currently lives in `inbox`.

## Inputs

- Required note path or title fragment, unless there is only one plausible note in `inbox`.

## Workflow

1. Read `AGENTS.md`.
2. Locate the target note only under `inbox`. Do not search `raw`, `projects`, `areas`, `resources`, or `archives` for targets.
3. Read the note body before naming or formatting.
4. Identify the durable idea, source, model, or use case.
5. Lightly edit the Markdown so it is readable and consistent:
   - Keep or add one clean H1 without the date prefix.
   - Use sentence-style section headings for meaningful groups.
   - Convert label lines such as `Core idea:` into proper headings when useful.
   - Normalize bullet and numbered lists.
   - Do not add frontmatter/properties unless the user explicitly asks for them.
   - Preserve existing frontmatter only when it contains source metadata the user still wants to keep.
6. Rename the markdown note inside `inbox` using `YYYY-MM-DD - Note Title.md`.
7. Report the old path, new path, and new H1.

## Naming Rules

- Use the note's existing date prefix when present; otherwise use the current date.
- Prefer specific titles over broad topic labels.
- Keep folder names lowercase.
- Preserve original note content.
- Do not add topic tags or PARA category tags.
- Do not rewrite the note into a new argument; preserve the captured meaning.
