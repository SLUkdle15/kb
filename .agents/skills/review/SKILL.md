---
name: review
description: Run a weekly review for this Obsidian BASB/PARA and GTD-style vault. Use when the user asks to review the week, clear inbox, review active projects, inspect next actions, or choose focus for next week.
---

# Weekly Review

Use this skill to review and maintain the vault without relying on a copy-paste template.

## Inputs

- Optional `mode`: `suggest` or `apply`. Default to `suggest`.
- Optional focus area, such as `projects`, `inbox`, `next`, or `areas`.

## Essential Review Checks

Run only the checks needed for the user's request:

```md
# Weekly Review - YYYY-MM-DD

## Inbox

## Next Actions

## Calendar

## Active Projects

## Areas Under Pressure

## Stale or Completed Items

## Focus for Next Week
```

Do not force a review note unless the user asks to create one or uses `mode=apply`.

## Workflow

1. Read `AGENTS.md`, `index.md`, and `projects/projects.md`.
2. Inspect `inbox`, `next`, and `projects`.
3. Check that every active project has at least one linked next action.
4. Sweep `next/next-actions` for items that take under about five minutes. Surface them as do-it-now candidates to clear in this session rather than re-filing them. An action that keeps surviving reviews is usually smaller than the note makes it look.
5. Sweep `next/calendar` against today's date:
   - A dated item whose date has passed and is still in the folder needs a decision: did it happen (complete it), or does it need a new date (reschedule)? Never leave a past date sitting.
   - For recurring items, confirm the rhythm is still real. Retire the note when the commitment stops.
   - After any change to `next/calendar`, rebuild the feed with `python3 .agents/scripts/build_calendar_ics.py` and remind the user to push, or the phone keeps showing the old date.
6. Flag stuck next actions by age, using the date in the filename. Anything older than about 30 days is not a next action any more — surface it and force one of four outcomes: do it now, promote it to a project because it is really multi-step, demote it to `next/maybe`, or drop it. Say how many days it has been sitting.
7. Identify notes that should move to `projects`, `areas`, `resources`, `archives`, or `next`.
8. In `suggest` mode, report recommended changes and missing next actions.
9. In `apply` mode:
   - Create a dated review note only if useful.
   - Apply obvious moves.
   - Leave ambiguous items in place with clear questions.

## Guardrails

- Do not inspect files outside the vault unless the user explicitly asks.
- Do not delete notes.
- Ask before moving ambiguous items.
