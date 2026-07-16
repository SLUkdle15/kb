# CLAUDE.md

This repository is a personal **Obsidian knowledge vault** built on BASB (Building a Second Brain) with a **PARA** structure and **GTD**-style action management. It is notes, not code. Treat every change as an edit to someone's thinking system: be conservative, preserve meaning, and prefer linking over moving.

## How this vault is organized

Top-level content folders (all lowercase):

- `inbox` — raw, unprocessed captures.
- `next` — GTD commitments: `next/next-actions`, `next/calendar`, `next/maybe`, `next/waiting`.
- `projects` — active outcomes with a finish line and at least one next action.
- `areas` — ongoing responsibilities with no finish line.
- `resources` — reusable knowledge and references.
- `archives` — inactive but retained material.

Key navigation files:

- `index.md` — human-facing map of the vault and BASB concepts.
- `log.md` — append-only, chronological timeline (e.g. lint runs). Keep entries short.
- `projects/projects.md`, `next/next.md`, `resources/restaurants/restaurants.md` — folder indexes; read the relevant one before working in that folder.

## Agent rules

The enforceable rules (naming, routing, linking, tags, projects) live in `AGENTS.md` and are shared with the Codex CLI. They are authoritative — read them before editing notes:

@AGENTS.md

## Skills

Reusable workflows live in `.agents/skills/` and are exposed to Claude Code via `.claude/skills` (a symlink, so there is a single source of truth shared with Codex). **Prefer the matching skill over editing notes by hand:**

- `create-next-action` — add a GTD action and route it (next-actions / calendar / maybe / waiting).
- `create-project` — start a PARA project with outcome, definition of done, and ≥1 linked next action.
- `dispose-project` — complete / cancel / pause / archive a project.
- `create-restaurant` — capture a new restaurant note in `resources/restaurants`.
- `process-inbox` — classify, route, split, or distill **one** specified inbox note.
- `packetize-notes` — find and draft reusable Intermediate Packets.
- `lint` — health-check the vault (structure + semantics); runs `.agents/skills/lint/scripts/build_index.py`.
- `weekly-review` — review inbox, next actions, projects, and areas.

Most skills default to **suggest** mode (report only) and apply changes only when the user clearly asks.

## Working conventions

- Use lowercase folder names and wiki links (`[[...]]`).
- New capture notes are dated: `YYYY-MM-DD - Note Title.md`, with a clean H1 that omits the date prefix.
- Do not use topic / PARA / source / type tags — only temporary workflow-status tags like `#status/waiting`.
- Do not delete notes or move ambiguous ones without asking; surface a question instead.
