#!/usr/bin/env python3
"""Build a "what's happening this month" view from next/calendar and dated
next-actions/waiting notes.

Scans:
- next/calendar/*.md — one-off `Due:` items and weekly `Every: Weekday HH:MM`
  recurring items (same parsing as .agents/scripts/build_calendar_ics.py).
- next/next-actions/*.md and next/waiting/*.md — any note with a `Due:` line.

Buckets items into:
- Overdue: Due date before today, still sitting in the vault.
- Today.
- This Week: due within the next 7 days (excluding today).
- Later This Month: due later in the target month.
- Weekly Recurring: every occurrence of a weekly `Every:` item within the
  target month.

Items due in a different month than the target (and not overdue) are
skipped. Prints Markdown to stdout; pass --out to also write a note file.
"""

import argparse
import datetime
import re
import sys
from pathlib import Path

VAULT = Path(__file__).resolve().parents[4]

DUE_RE = re.compile(r"^Due:\s*(\d{4}-\d{2}-\d{2})", re.M)
EVERY_RE = re.compile(
    r"^Every:\s*(Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday)\s+(\d{1,2}:\d{2})",
    re.M,
)
H1_RE = re.compile(r"^#\s+(.+)$", re.M)
FILENAME_DATE_RE = re.compile(r"^(\d{4}-\d{2}-\d{2}) - (.+)$")

WEEKDAYS = [
    "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday",
]


def title_of(path: Path, text: str) -> str:
    h1 = H1_RE.search(text)
    if h1:
        return h1.group(1).strip()
    m = FILENAME_DATE_RE.match(path.stem)
    return m.group(2) if m else path.stem


def rel_link(path: Path) -> str:
    return path.relative_to(VAULT).with_suffix("").as_posix()


def month_bounds(target: datetime.date) -> tuple[datetime.date, datetime.date]:
    start = target.replace(day=1)
    if start.month == 12:
        end = start.replace(year=start.year + 1, month=1)
    else:
        end = start.replace(month=start.month + 1)
    return start, end


def collect_dated(dirs: list[Path]) -> list[tuple[Path, str, datetime.date]]:
    items = []
    for d in dirs:
        for path in sorted(d.glob("*.md")):
            if path.stem == d.name:  # folder note, e.g. calendar.md
                continue
            text = path.read_text(encoding="utf-8")
            due = DUE_RE.search(text)
            if not due:
                continue
            date = datetime.date.fromisoformat(due.group(1))
            items.append((path, title_of(path, text), date))
    return items


def collect_weekly(calendar_dir: Path) -> list[tuple[Path, str, str, str]]:
    items = []
    for path in sorted(calendar_dir.glob("*.md")):
        if path.stem == "calendar":
            continue
        text = path.read_text(encoding="utf-8")
        every = EVERY_RE.search(text)
        if every:
            items.append((path, title_of(path, text), every.group(1), every.group(2)))
    return items


def occurrences_in_month(weekday_name: str, start: datetime.date, end: datetime.date) -> list[datetime.date]:
    target_weekday = WEEKDAYS.index(weekday_name)
    d = start
    out = []
    while d < end:
        if d.weekday() == target_weekday:
            out.append(d)
        d += datetime.timedelta(days=1)
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--month", help="Target month as YYYY-MM (default: current month)")
    ap.add_argument("--out", help="Optional path to also write the view as a note")
    args = ap.parse_args()

    today = datetime.date.today()
    if args.month:
        year, month = (int(p) for p in args.month.split("-"))
        target = datetime.date(year, month, 1)
    else:
        target = today.replace(day=1)
    start, end = month_bounds(target)

    calendar_dir = VAULT / "next" / "calendar"
    dated = collect_dated([calendar_dir, VAULT / "next" / "next-actions", VAULT / "next" / "waiting"])
    weekly = collect_weekly(calendar_dir)

    overdue, due_today, this_week, later = [], [], [], []
    week_cutoff = today + datetime.timedelta(days=7)

    for path, title, date in dated:
        if date < today:
            overdue.append((path, title, date))
        elif not (start <= date < end):
            continue
        elif date == today:
            due_today.append((path, title, date))
        elif date < week_cutoff:
            this_week.append((path, title, date))
        else:
            later.append((path, title, date))

    overdue.sort(key=lambda x: x[2])
    this_week.sort(key=lambda x: x[2])
    later.sort(key=lambda x: x[2])

    lines = [f"# {target.strftime('%B %Y')} View", ""]
    lines.append(f"_Generated {today.isoformat()}._")
    lines.append("")

    def section(name: str, rows: list[tuple[Path, str, datetime.date]], show_date: bool = True) -> None:
        lines.append(f"## {name}")
        lines.append("")
        if not rows:
            lines.append("- (none)")
        for path, title, date in rows:
            date_str = f" — {date.strftime('%a %-m/%-d')}" if show_date else ""
            lines.append(f"- [[{rel_link(path)}|{title}]]{date_str}")
        lines.append("")

    if overdue:
        section("Overdue", overdue)
    section("Today", due_today)
    section("This Week", this_week)
    section("Later This Month", later)

    lines.append("## Recurs Every Week This Month")
    lines.append("")
    if not weekly:
        lines.append("- (none)")
    for path, title, weekday_name, time_str in weekly:
        dates = occurrences_in_month(weekday_name, start, end)
        date_list = ", ".join(d.strftime("%-d") for d in dates)
        lines.append(f"- [[{rel_link(path)}|{title}]] — {weekday_name}s {time_str} ({date_list})")
    lines.append("")

    output = "\n".join(lines).rstrip() + "\n"
    print(output)

    if args.out:
        out_path = Path(args.out)
        out_path.write_text(output, encoding="utf-8")
        print(f"wrote {out_path}", file=sys.stderr)


if __name__ == "__main__":
    main()
