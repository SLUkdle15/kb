---
name: protocol
description: Build a reusable protocol (checklist intermediate packet) inside the owning area's folder from an existing note in this Obsidian vault. Use when the user asks to create a protocol, checklist, SOP, playbook, or repeatable procedure from a note.
---

# Build Protocol

Use this skill to distill one existing note into a reusable protocol inside the area that owns the practice.

A protocol is an intermediate packet: a simple checklist plus a few notes, with a link back to the original note. The protocol is the thing you follow; the source note is the thing you study.

## Inputs

- The source note, usually in `resources` (ask if ambiguous).
- The owning area (infer from the source note's topic; ask if no area fits).
- Optional protocol name; otherwise derive a short verb phrase, such as `Write an ADR`.

## Storage

- Protocol notes live in the owning area's folder, such as `areas/software-architecture/write-an-adr.md`. There is no shared protocols folder.
- Filenames are undated, lowercase, hyphenated verb phrases: `write-an-adr.md`. Protocols are evergreen, not captures, so no date prefix.
- Frontmatter: `type: protocol`.

## Protocol Note Shape

```md
---
type: protocol
---

# Verb Phrase Title

Source: [[path/to/original-note|Original Note]]

## Checklist

- [ ] Concrete, ordered steps.

## Notes

- A few pitfalls, judgment calls, or reminders that do not fit a checkbox.
```

## Workflow

1. Read `AGENTS.md` and the owning area's index note.
2. Read the source note fully; check the area folder for an existing protocol covering the same procedure. If one exists, report it instead of duplicating.
3. Distill the procedure into a checklist of roughly 5-10 concrete steps and at most a handful of notes. Depth stays in the source note; the protocol only carries what is needed to execute.
4. Create the note in the owning area's folder with a `Source:` link back to the original note.
5. List the protocol under a `## Protocols` section in the area's index note; create the section if missing.
6. Add a `Protocol:` link in the source note pointing to the new protocol.

## Guardrails

- Do not copy the source note's content wholesale; a protocol that restates the source is a failed distillation.
- Do not modify the source note beyond adding the `Protocol:` link.
- Do not create a new area just to house a protocol; if no area owns the practice, ask where it belongs.
- Do not add topic, PARA, source, or type tags; the `type: protocol` frontmatter is enough.
- Keep the checklist executable without opening the source note; link the source for the why.
- One procedure per protocol; if the source note contains several procedures, propose splitting rather than writing one bloated checklist.
