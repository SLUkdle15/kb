---
name: inbox-triage
description: Triage Obsidian BASB/PARA inbox notes. Use when the user asks to process, sort, review, clear, or organize notes in inbox; supports suggest-only and apply modes.
---

# Inbox Triage

Use this skill to process captured notes in `inbox`.

## Inputs

- Optional `mode`: `suggest` or `apply`. Default to `suggest` unless the user clearly asks to make changes.
- Optional note path or title fragment. If omitted, process all markdown notes in `inbox`.

## Workflow

1. Read `AGENTS.md`, `resources/agent-skills.md`, and `resources/basb/Actionability Checklist.md`.
2. Inspect the target inbox note or all markdown notes in `inbox`.
3. Classify each note by nearest useful destination:
   - `projects` for active outcomes with a finish line.
   - `areas` for ongoing responsibilities.
   - `resources` for reusable reference material.
   - `archives` for inactive, completed, or outdated material.
4. In `suggest` mode, report destination, reason, possible rename, and next action.
5. In `apply` mode, move only obvious notes. Leave ambiguous notes in `inbox` with a concise processing note if useful.

## Guardrails

- Capture stays human-owned; do not invent missing source material.
- Do not delete notes.
- Preserve date-prefixed filenames unless a rename clearly improves retrieval.
- Use lowercase folder names.
