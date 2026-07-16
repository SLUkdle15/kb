---
name: project
description: Create a PARA project in this Obsidian vault from a note or desired outcome. Use when the user asks to start, kickoff, create, or plan a project with a finish line.
---

# Create Project

Use this skill when a note or request implies a short-term outcome with a finish line.

## Inputs

- Required source note path, title fragment, or outcome statement.
- Optional project folder slug. Infer one if omitted.
- Optional deadline.
- Optional next actions. At least one is required for an active project.

## Essential Project Fields

Every project note should contain only the fields needed to move work forward:

```md
# Project Name

## Outcome

## Deadline

## Definition of Done

## Next Actions

## Notes
```

Omit empty optional sections only when they add no value. Keep project notes short.

## Workflow

1. Read `AGENTS.md`.
2. Extract any supplied project details from the user's request.
3. Check for missing essentials:
   - Outcome
   - Definition of done
   - At least one next action
4. If any essentials are missing, ask concise follow-up questions before creating an active project.
5. If the user gave enough information, create a lowercase project folder under `projects`.
6. Create a short project note using the essential fields above.
7. Link source notes when a source note was provided.
8. Create or identify at least one concrete next action in `next/next-actions`.
9. Link the next action from the project note under `## Next Actions`.
10. Link the next action note back to the project.

## Missing-Information Behavior

If the user says something like "create a project with deadline and these next actions," do not force a template. Instead:

1. Use what they provided.
2. Tell them what is missing.
3. Ask only for the missing essentials.
4. Offer a suggested outcome or definition of done when it can be safely inferred.

## Guardrails

- A project must have a finish line. If it is ongoing, recommend creating an area instead.
- Every active project must have at least one linked next action. If no next action is known, clarify it before creating an active project.
- Do not move the source note unless the user asks.
- Keep project names outcome-oriented, not only topic-oriented.
