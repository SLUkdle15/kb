---
name: lint
description: Health-check this Obsidian BASB/PARA and GTD-style vault. Use when the user asks to lint, audit, health-check, inspect contradictions, find stale claims, detect orphan notes, suggest missing links, identify missing concept pages, or check projects and actions.
---

# Lint

Use this skill to health-check the vault with a layered scan: deterministic structure first, semantic review second.

## Inputs

- Optional `mode`: `quick`, `focused`, or `deep`. Default to `focused`.
- Optional focus folder or note path.
- Optional `apply`: only make edits when the user clearly asks. Default is report-only.

## Workflow

1. Read `AGENTS.md`.
2. Run the index builder:

   ```sh
   python3 .agents/skills/lint/scripts/build_index.py --vault . --out /tmp/vault-lint
   ```

   This appends a compact event to `log.md` by default. Use `--no-log` for validation runs that should not touch the timeline.

3. Read `/tmp/vault-lint/report.md` first. Use `/tmp/vault-lint/index.json` when exact paths, links, or counts matter.
4. For `quick`, report deterministic findings only.
5. For `focused`, inspect the most relevant flagged notes:
   - projects missing next actions
   - orphan notes
   - broken wiki links
   - notes with stale-looking terms
   - repeated missing concepts
   - recently modified notes if relevant
6. For `deep`, sample related clusters and compare claims across notes. Use web search only for claims that are time-sensitive, decision-relevant, or explicitly require current facts.

## Checks

- Contradictions between notes: compare definitions, dates, rules, decisions, and factual claims in related notes.
- Stale claims: flag old or time-sensitive claims using dates, external links, and terms like current/latest/best/pricing/version.
- Orphans: notes with no inbound wiki links.
- Missing concept pages: repeated broken wiki links or repeated named concepts without a note.
- Missing cross-references: notes with shared concepts, aliases, sources, or project context but no links.
- Projects without next actions: active project notes must have a `Next Actions` section and link to `next/next-actions`.
- Inbox triage: identify captures that look like actions, projects, references, or archives.
- Data gaps: unsupported claims, old sources, weak assumptions, or questions that would benefit from primary/current sources.

## Output

Use this structure unless the user asks for something narrower:

```md
# Lint - YYYY-MM-DD

## High Priority

## Structural Findings

## Semantic Findings

## Link Suggestions

## Missing Concept Pages

## Stale or Source-Weak Claims

## Questions to Investigate

## Suggested Next Actions
```

Keep findings actionable. Include file links and exact evidence. Do not rewrite or move notes unless the user requested apply mode.

## Log

`log.md` is append-only and chronological. Each entry starts with:

```md
## [YYYY-MM-DD] lint | Vault health check
```

Keep log entries short: record the run, key counts, and report path. Do not paste the full lint report into `log.md`.

## Guardrails

- Do not delete notes.
- Do not invent sources.
- Treat contradiction and stale-claim results as candidates unless verified.
- Preserve lowercase vault folder names.
- Respect the project rule: every active project must have at least one linked next action.
