---
name: month
description: Generate a view of what's happening this month in this Obsidian vault, grouped by overdue, today, this week, later this month, and weekly recurring. Use when the user asks what they're doing this month, wants a monthly view/dashboard of the calendar, or asks to see this month at a glance.
---

# Month View

Use this skill to build a read of the current (or a given) month from `next/calendar`, `next/next-actions`, and `next/waiting` — without hand-checking dates.

## Inputs

- Optional target month as `YYYY-MM`. Default to the current month.
- Optional `mode`: `suggest` or `apply`. Default to `suggest`.

## Workflow

1. Run the builder:

   ```sh
   python3 .agents/skills/month/scripts/build_month_view.py
   ```

   Pass `--month YYYY-MM` for a month other than the current one.

2. The script buckets every dated item (`Due:` in `next/calendar`, `next/next-actions`, `next/waiting`) into:
   - **Overdue** — due date before today, still open.
   - **Today**
   - **This Week** — due within the next 7 days.
   - **Later This Month** — due later in the target month.
   - **Recurs Every Week This Month** — every `Every: Weekday HH:MM` item in `next/calendar`, expanded to each occurrence in the target month.

   Items due in a different month than the target, and not overdue, are skipped.

3. In `suggest` mode (default), print the view to the user. Do not write a file.
4. In `apply` mode, also write it as a note:

   ```sh
   python3 .agents/skills/month/scripts/build_month_view.py --out "next/calendar/YYYY-MM - <Month> <Year> View.md"
   ```

   Use the target month for the filename (e.g. `2026-09 - September 2026 View.md`). This note is a generated dashboard, not a GTD action — it does not need a `Next Actions` link and is safe to overwrite/regenerate on request rather than accumulating monthly copies; ask the user whether to keep past months' view notes or overwrite the latest one.

## Guardrails

- This is a read-only view over existing notes. Do not edit or move the underlying `next/calendar`, `next/next-actions`, or `next/waiting` notes from this skill — use `complete` or `next` for that.
- Overdue items are a signal to run the `complete` skill (mark done) or reschedule via `next`, not to silently drop.
