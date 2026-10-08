---
name: review
description: Run a weekly review for this Obsidian BASB/PARA and GTD-style vault. Use when the user asks to review the week, clear inbox, review active projects, inspect next actions, or choose focus for next week.
---

# Weekly Review

The review is what keeps the rest of the system trustworthy. A list the user has stopped believing is a list they have stopped using, so the job is not to tidy notes — it is to end the session with the vault matching reality.

> The Weekly Review is the time to
> - Gather and process all your "stuff."
> - Review your system.
> - Update your lists.
> - Get clean, clear, current, and complete.
>
> — David Allen, *Getting Things Done*

Work through the four steps below. Run only the parts the user's request calls for.

## Inputs

- Optional `mode`: `suggest` or `apply`. Default to `suggest`.
- Optional focus area, such as `projects`, `inbox`, `next`, or `areas`.

Start by reading `AGENTS.md`, `index.md`, and `projects/projects.md`.

## 1. Gather and Process

Everything loose goes to `inbox`, and `inbox` gets emptied: each capture is classified and routed to `projects`, `areas`, `resources`, `archives`, or `next`.

- A book being read keeps a living capture note in `inbox` that grows until the book is finished. It is not a stale capture and is not routed early — skip it.
- A capture that resists classification stays where it is, with the question surfaced. Do not force a move.

## 2. Review the System

**`next/calendar`** — the past week first, then the weeks ahead.

- A dated item whose date has passed and is still in the folder needs a decision: did it happen (complete it), or does it need a new date (reschedule)? Never leave a past date sitting.
- For recurring items, confirm the rhythm is still real. Retire the note when the commitment stops.
- After any change here, rebuild the feed with `python3 .agents/scripts/build_calendar_ics.py` and remind the user to push, or the phone keeps showing the old date.

**`next/next-actions`** — tick off what is done, then sweep what is left.

- Anything that takes under about five minutes is a do-it-now candidate for this session, not a re-filing job. An action that keeps surviving reviews is usually smaller than its note makes it look.
- Judge age by the date in the filename. Past about 30 days it is not a next action any more. Say how many days it has been sitting and force one of four outcomes: do it now, promote it to a project because it is really multi-step, demote it to `next/maybe`, or drop it.

**`projects`** — every active project needs at least one linked next action, and that action must link back.

- A `next/calendar` note counts; committing to a date is a stronger commitment, not a weaker one.
- A `next/waiting` note counts once the action that produced it has been done. A project parked on a wait is still active.
- A project with no next action and no wait is the review's main finding. Clarify the action or move the outcome to `next/maybe`.

**`next/waiting`** — chase anything overdue.

- A stalled wait is handled inside its own note: update it, re-trigger it, or close it. Do not spin off a new next action to chase it.
- A wait the user has deliberately left untriggered is a decision, not an oversight. Leave it.

**`next/maybe`** — activate what is ready now, drop what is no longer wanted.

- Items parked here for effort rather than interest are correctly filed. Age alone is not a finding; what deserves the question is whether the trigger that would reactivate the item still exists.

**`areas`** — note which ongoing responsibilities are under pressure, and whether any needs a project to relieve it.

## 3. Update the Lists

Add what is new, remove what is done or dead, and sharpen anything vague enough to be skipped next week. Keep the folder indexes (`projects/projects.md`, `next/next.md`, and the relevant folder notes) matching what is actually in the folders.

## 4. Get Clean, Clear, Current, Complete

The standard the first three steps are aiming at, and the right order to report against:

- **Clean** — inboxes empty, loose ends gathered.
- **Clear** — every item has an outcome and a next action.
- **Current** — the lists match this week's real situation.
- **Complete** — nothing is still living only in the user's head.

## Output

In `suggest` mode, report findings and missing next actions. Do not edit files.

In `apply` mode, make the obvious changes, leave ambiguous items in place with clear questions, and create a dated review note only if it is useful:

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

Do not force a review note unless the user asks for one.

## Guardrails

- Do not inspect files outside the vault unless the user explicitly asks.
- Do not delete notes.
- Ask before moving ambiguous items.
