---
name: distill-note
description: Distill an Obsidian vault note into reusable knowledge. Use when the user asks to summarize, refine, extract key ideas, create a checklist, make an intermediate packet, or apply progressive summarization.
---

# Distill Note

Use this skill when a note is likely to be reused.

## Inputs

- Required note path or title fragment, unless the conversation clearly identifies one.
- Optional output type: `summary`, `checklist`, `packet`, `questions`, or `all`. Default to `all`.
- Optional `mode`: `suggest` or `apply`. Default to `suggest`.

## Workflow

1. Read `resources/agent-skills.md` and `resources/templates/Progressive Summarization.md`.
2. Locate and read the target note.
3. Preserve the original substance.
4. Extract useful sections:
   - Core claim
   - Key models
   - Practical checklist
   - Open questions
   - Possible projects, areas, or resources
5. In `suggest` mode, show the distilled output without editing.
6. In `apply` mode, append or update concise sections that make the note easier to reuse.

## Stop Rule

Stop when the note is useful for the next likely use case. Do not over-process every note.
