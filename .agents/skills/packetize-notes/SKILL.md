---
name: packetize-notes
description: Detect, suggest, and create Intermediate Packet drafts across projects, areas, resources, or selected notes. Use when the user asks to scan for reusable packets, packetize notes, create packet drafts, or find reusable outlines, checklists, decisions, examples, templates, quote sets, drafts, or research summaries.
---

# Packetize Notes

Use this skill to find and create small reusable pieces of output that can move future work forward.

## Inputs

- Optional scope: `projects`, `areas`, `resources`, `inbox`, a folder, or a specific note path. Default to `projects`, `areas`, and `resources`.
- Optional `mode`: `suggest` or `apply`. Default to `suggest` unless the user clearly asks to create packet drafts.
- Optional packet type: outline, checklist, decision, quote set, example, draft, research summary, or template.

## Workflow

1. Read `AGENTS.md`, `index.md`, and `resources/personal-knowledge-management/2026-05-27 - Intermediate Packets.md` if present.
2. Inspect only the requested scope. If no scope is provided, scan `projects`, `areas`, and `resources`.
3. Detect packet candidates:
   - Reusable outline, plan, checklist, decision, example, template, quote set, draft, research summary, or comparison.
   - A section that is concrete enough to reuse outside the current note.
   - A partial output that would move an active project forward.
   - Repeated structure across notes that could become a reusable template.
4. Reject weak candidates:
   - Vague ideas with no reusable shape.
   - Raw captures that need basic processing first.
   - Tiny fragments that have no clear future use.
   - Private context that only makes sense inside the source note.
5. Suggest where each packet should live based on where it will be used next:
   - `projects` for active project output.
   - `areas` for recurring responsibility material.
   - `resources` for reusable knowledge or references.
   - `archives` only for inactive but reusable material.
6. In `suggest` mode, report packet candidates, source notes, proposed destinations, and why each candidate is reusable. Do not edit files.
7. In `apply` mode, create packet draft notes using the packet shape below.

## Packet Shape

Use this shape when it fits. Omit sections that add clutter.

```md
# Packet Title

Source: [[source-note]]

## Packet

## Reuse For

## Open Questions
```

## Naming Rules

- Use dated filenames: `YYYY-MM-DD - Packet Title.md`.
- Use a clean H1 without the date prefix.
- Prefer specific packet titles over broad topic labels.
- Keep folder names lowercase.
- Do not add topic tags or PARA category tags.
- Link packet drafts back to the source note.
- Avoid creating many tiny packets when one stronger packet is more useful.

## Reporting

Report:

- Scope scanned.
- Packet candidates found.
- Files created in `apply` mode.
- Candidates rejected as too weak or ambiguous.
- Open questions that block useful packet creation.
