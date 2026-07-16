---
name: distill
description: Distill a long or dense note into smaller, focused notes. Use when the user asks to distill, split, break up, summarize, condense, or progressively summarize a note, or when a note has grown too long to reuse.
---

# Distill Note

Use this skill to distill **one** specified note: sharpen its core idea and, when it covers more than one reusable idea, break it into smaller focused notes.

## Inputs

- Required: the path of the note to distill.
- Optional `mode`: `suggest` or `apply`. Default to `suggest` unless the user clearly asks to make the changes.

## Workflow

1. Read `AGENTS.md` and `index.md`.
2. Read the target note fully. Check which notes link to it before proposing changes.
3. Assess whether distillation is needed:
   - The note is long or covers several distinct ideas.
   - The title no longer describes everything inside.
   - Only part of the note is reusable outside its original context.
   - Actionable items are buried inside reference material.
4. Build a distillation plan:
   - A short summary of the core idea to place at the top of the note.
   - Split candidates: sections that stand alone as a smaller, reusable note.
   - A PARA destination for each split note (`projects`, `areas`, `resources`, or `next` for buried actions).
   - A proposed filename for each split note (`YYYY-MM-DD - Note Title.md`), specific enough to be found by title alone.
   - Links: the source note links to each split note, and each split note links back to the source.
5. For splits routed to `resources`, decide the exact placement:
   - Use an existing topic subfolder (`resources/badminton`, `resources/software-engineering/...`) when one clearly fits.
   - Propose a new subfolder only when the split plus existing notes would give it two or more members; a new subfolder needs a folder note (like `badminton/badminton.md`) and an entry in `resources/resources.md`.
   - Otherwise leave the note flat at the `resources` root.
   - Say which of these applies and why in the report.
6. Reject weak splits:
   - Tiny fragments with no clear future use.
   - Context that only makes sense inside the source note.
   - Splits that would turn one readable note into many hollow stubs.
7. In `suggest` mode, report the plan only. Do not edit files.
8. In `apply` mode:
   - Create the smaller notes using the shape below.
   - Create any new subfolder with its folder note before adding notes to it.
   - In the source note, add the summary and replace moved sections with links to the new notes.
   - Route buried actions with the `next` skill instead of leaving them in a reference note.
   - Update the relevant folder index notes.

## Split Note Shape

Use this shape when it fits. Omit sections that add clutter.

```md
# Split Note Title

Source: [[source-note]]

<distilled content>
```

## Naming Rules

- Use dated filenames: `YYYY-MM-DD - Note Title.md` with today's date.
- Use a clean H1 without the date prefix.
- Prefer specific titles over broad topic labels.
- Keep folder names lowercase.
- Do not add topic tags or PARA category tags.

## Guardrails

- Never delete the source note; it becomes the summary hub that links to the split notes.
- Preserve meaning: move content, do not rewrite claims while splitting.
- Ask before splitting a note other notes link into heavily, if the split would change what those links mean.

## Reporting

Report:

- Whether the note needs distillation at all.
- The proposed summary and split candidates, each with its filename and exact destination (existing subfolder, new subfolder, or flat).
- Files created and edits made in `apply` mode.
- Split candidates rejected as too weak.
- Open questions that block a clean split.
