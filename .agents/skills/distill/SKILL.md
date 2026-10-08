---
name: distill
description: File a note the user has already distilled by hand — rename it to the dated convention, mark it `type: distilled-note`, and suggest where in `resources` it belongs. Use when the user says they have distilled, written up, or finished a note and wants it named, marked, or filed. It does not write, split, summarize, or rewrite the content; the user does that.
---

# File a Distilled Note

The user does the distilling. This skill does the mechanical part afterwards: name, mark, place.

## Inputs

- Required: the path or title fragment of **one** note. If none is given, or a fragment matches several notes, ask which one.
- The content is finished work. Do not improve it.

## Workflow

1. Read the note.
2. If it is still raw capture or source material rather than a distilled idea, say so and stop. Marking it `distilled-note` would be a false claim.
3. **Name it.** Derive a title from what the note actually argues:
   - State the claim or the specific question — `Log Levels Are a Threshold, Not a Category`, not `Logging`. A bare topic label is the failure mode.
   - Rename to `YYYY-MM-DD - Note Title.md`. Keep the note's existing date prefix if it has one; otherwise use today's date.
   - Set the H1 to the same title, without the date prefix.
4. **Mark it.** Add `type: distilled-note` frontmatter if absent. Leave any other frontmatter alone.
5. **Suggest a home.** Say where it belongs and why:
   - An existing `resources` subfolder when one clearly fits.
   - Flat at the `resources` root when none does.
   - A new subfolder only when it plus existing notes would have two or more members — and say that it needs a folder note and an entry in `resources/resources.md`.
   - Suggest only. Move it when the user asks.

## Do Not

- Rewrite, condense, split, or reorder the content. Preserve the wording.
- Add a `Source:` line, a `Related:` header, or any other boilerplate block. Attach a link inline at the line it is relevant to.
- Add topic, PARA, or source tags.

## Reporting

- Old path → new path, and the new H1.
- Whether `type: distilled-note` was added or already present.
- Suggested destination, with the reason.
- Anything about the note that was unclear, as a question.
