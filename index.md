---
type: vault-guide
---

# SecondBrainVault

This Obsidian vault is designed to help you capture, organize, distill, and express knowledge using a BASB-inspired workflow.

The vault is organized by actionability. The most important question is not "What topic is this about?" but "Where will this be useful next?"

## Start Here

- [[inbox/inbox]]
- [[next/next]]
- [[projects/projects]]
- [[areas/areas]]
- [[resources/resources]]
- [[archives/archives]]
- [[raw/raw]]

## Active Areas

- [[areas/badminton-training/badminton-training|Badminton Training]]
- [[areas/chinese-learning/chinese-learning|Chinese Learning]]
- [[areas/chess-training/chess-training|Chess Training]]
- [[areas/photography/photography|Photography]]
- [[areas/golf-training/golf-training|Golf Training]]
- [[areas/personal-finance/personal-finance|Personal Finance]]
- [[areas/romantic-relationship/romantic-relationship|Romantic Relationship]]
- [[areas/career-and-work/career-and-work|Career and Work]]
- [[areas/travel-planning/travel-planning|Travel Planning]]

## Workflows

Codex agent skills under `.agents/skills` handle reusable workflows:

- `create-project`
- `create-next-action`
- `dispose-project`
- `distill-note`
- `inbox-triage`
- `lint`
- `rename-capture`
- `weekly-review`

## Operating Principles

- [[resources/basb/BASB Operating Principles]]
- [[resources/basb/Actionability Checklist]]

## PARA

PARA is a practical structure for organizing knowledge by how active and actionable it is:

- **Projects**: Short-term outcomes with a finish line.
- **Areas**: Ongoing responsibilities you maintain over time.
- **Resources**: Reference material for topics, interests, and future work.
- **Archives**: Inactive, completed, or outdated material kept for reference.

## GTD Action Layer

Use `next` for commitments that are more actionable than inbox captures but not necessarily full projects:

- **Next Actions**: Concrete actions to do soon.
- **Calendar**: Date-specific or time-specific commitments.
- **Maybe**: Someday/maybe ideas and possible future projects.
- **Waiting**: Items blocked by someone or something else.

## Where a Note Belongs

Use this order when deciding where to put something:

1. If it is a concrete standalone action, move it to `next/next-actions`.
2. If it is date-specific or time-specific, move it to `next/calendar`.
3. If it is a someday/maybe idea, move it to `next/maybe`.
4. If it is blocked by someone or something else, move it to `next/waiting`.
5. If it helps an active project, move it to `projects`.
6. If it supports an ongoing responsibility, move it to `areas`.
7. If it is useful reference material, move it to `resources`.
8. If it is inactive, completed, outdated, or no longer actionable, move it to `archives`.
9. If you are unsure, leave it in `inbox` and review it later.

Use [[resources/basb/Actionability Checklist]] when you need a quick decision flow.

## Linking Between Sections

Folders decide where a note lives by actionability. Links show where the note is useful.

- Project notes should link to the area they serve and the resources they use.
- Area notes should link to related resources and active projects.
- Resource notes should link back to the project or area where they are likely to be reused.

## Naming Conventions

- Use lowercase folder names and lowercase folder-note filenames.
- Use `raw` for attachments, screenshots, PDFs, exports, and other non-note source files.
- Prefix new captured note filenames with the current date: `YYYY-MM-DD - Note Title.md`.
- Keep the note's H1 clean and readable without the date prefix.

## Tag Convention

Do not use tags for topics, folders, PARA categories, sources, or note types.

Use folders for actionability and wiki links for meaning. Only use tags for temporary workflow status, such as `#status/waiting`, `#status/review`, or `#status/draft`.

## CODE Workflow

CODE is the knowledge workflow for this vault:

- **Capture**: Save ideas, notes, references, questions, and observations into `inbox`.
- **Organize**: Move each note to the place where it can create value soonest.
- **Distill**: Summarize only enough to make the note easy to reuse.
- **Express**: Turn notes into outputs such as decisions, designs, essays, plans, documents, talks, or shipped work.

## Weekly Review Rhythm

Once per week, run the `weekly-review` agent skill.

During the review:

- [ ] Clear `inbox`.
- [ ] Review active projects.
- [ ] Move stale notes into Areas, Resources, or Archives.
- [ ] Identify the highest-leverage project for the next week.
- [ ] Capture anything important from your desktop, downloads folder, calendar, and open loops.

## Agent Skills

Reusable workflows live in `.agents/skills`.

Use them instead of copying templates:

- `create-project` asks for missing project essentials and creates the project plus first next action.
- `create-next-action` routes small commitments into calendar, next-actions, maybe, or waiting.
- `dispose-project` closes or archives a project and preserves reusable material.
- `distill-note` turns notes into summaries, checklists, questions, or reusable packets.
- `inbox-triage` routes captures to the right folder.
- `lint` health-checks the vault for broken links, orphan notes, stale candidates, missing next actions, and missing concept pages.
- `rename-capture` names raw captures and moves them into inbox.
- `weekly-review` reviews inbox, next actions, active projects, and stale material.

## Moving Completed Projects to Archives

When a project is complete:

1. Run `dispose-project`.
2. Record what was delivered, lessons learned, and reusable Intermediate Packets.
3. Move any reusable knowledge into `areas` or `resources`.
4. Move the whole project folder from `projects` to `archives`.
5. Update links from active notes if needed.
