---
name: create-project
description: Create a PARA project in this Obsidian vault from a note or desired outcome. Use when the user asks to start, kickoff, create, or plan a project with a finish line.
---

# Create Project

Use this skill when a note or request implies a short-term outcome with a finish line.

## Inputs

- Required source note path, title fragment, or outcome statement.
- Optional project folder slug. Infer one if omitted.
- Optional deadline.

## Workflow

1. Read `AGENTS.md`, `resources/agent-skills.md`, and `resources/templates/Project Kickoff.md`.
2. Determine the project outcome and definition of done.
3. Create a lowercase project folder under `projects`.
4. Create a project kickoff note in that folder.
5. Link source notes and collect existing ammunition from the vault.
6. Add a concrete next action.

## Guardrails

- A project must have a finish line. If it is ongoing, recommend creating an area instead.
- Do not move the source note unless the user asks.
- Keep project names outcome-oriented, not only topic-oriented.
