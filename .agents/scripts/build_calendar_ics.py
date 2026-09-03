#!/usr/bin/env python3
"""Build calendar.ics at the vault root from notes in next/calendar.

Each calendar note contributes one event, in one of two shapes:

- One-off: Title from the note's H1 (falls back to the filename without the
  date prefix). Date from the first `Due:` line, e.g. `Due: 2026-07-15` or
  `Due: 2026-07-15 14:30` (falls back to the filename's YYYY-MM-DD prefix).
  Date-only becomes an all-day event; a time makes a 1-hour timed event. An
  optional `Remind:` line adds a VALARM that many days before the date.

- Recurring weekly: Title from the H1. Day/time from an `Every:` line, e.g.
  `Every: Tuesday 17:30`. Produces a weekly-recurring event at that day/time,
  defaulting to a 1-hour duration. List several days for a routine that repeats
  more than once a week, e.g. `Every: Monday and Thursday 21:00`. Give an explicit end time with
  `Every: Saturday 15:00-17:00` for a longer session. An optional `Remind:`
  line, e.g. `Remind: 3`, adds a VALARM that fires that many days before each
  occurrence — change the number to change the lead time; no script edit
  needed.

Subscribe to the generated file from a phone calendar via its raw GitHub URL.
Run after adding/removing calendar notes, then commit and push calendar.ics.
"""

import datetime
import re
import sys
from pathlib import Path

VAULT = Path(__file__).resolve().parents[2]
CALENDAR_DIR = VAULT / "next" / "calendar"
OUTPUT = VAULT / "calendar.ics"

DUE_RE = re.compile(r"^Due:\s*(\d{4}-\d{2}-\d{2})(?:\s+(\d{1,2}:\d{2}))?", re.M)
DAY_NAMES = "Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday"
DAY_NAME_RE = re.compile(DAY_NAMES)
EVERY_RE = re.compile(
    rf"^Every:\s*((?:{DAY_NAMES})(?:\s*(?:,|and)\s*(?:{DAY_NAMES}))*)\s+"
    r"(\d{1,2}:\d{2})(?:-(\d{1,2}:\d{2}))?",
    re.M,
)
REMIND_RE = re.compile(r"^Remind:\s*(\d+)", re.M)
H1_RE = re.compile(r"^#\s+(.+)$", re.M)
FILENAME_DATE_RE = re.compile(r"^(\d{4}-\d{2}-\d{2}) - (.+)$")

WEEKDAYS = {
    "Monday": (0, "MO"),
    "Tuesday": (1, "TU"),
    "Wednesday": (2, "WE"),
    "Thursday": (3, "TH"),
    "Friday": (4, "FR"),
    "Saturday": (5, "SA"),
    "Sunday": (6, "SU"),
}


def escape(text: str) -> str:
    return text.replace("\\", "\\\\").replace(",", "\\,").replace(";", "\\;")


def build_event(path: Path) -> list[str] | None:
    text = path.read_text(encoding="utf-8")
    name_match = FILENAME_DATE_RE.match(path.stem)

    h1 = H1_RE.search(text)
    if h1:
        title = h1.group(1).strip()
    elif name_match:
        title = name_match.group(2)
    else:
        title = path.stem

    every = EVERY_RE.search(text)
    if every:
        return build_recurring_event(path, title, every)

    due = DUE_RE.search(text)
    if due:
        date_str, time_str = due.group(1), due.group(2)
    elif name_match:
        date_str, time_str = name_match.group(1), None
    else:
        print(f"skip (no date found): {path.name}", file=sys.stderr)
        return None

    date = datetime.date.fromisoformat(date_str)
    stamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    uid = re.sub(r"[^a-z0-9]+", "-", path.stem.lower()).strip("-") + "@kb-vault"

    lines = [
        "BEGIN:VEVENT",
        f"UID:{uid}",
        f"DTSTAMP:{stamp}",
        f"SUMMARY:{escape(title)}",
    ]
    if time_str:
        hour, minute = (int(p) for p in time_str.split(":"))
        start = datetime.datetime.combine(date, datetime.time(hour, minute))
        end = start + datetime.timedelta(hours=1)
        lines += [
            f"DTSTART:{start.strftime('%Y%m%dT%H%M%S')}",
            f"DTEND:{end.strftime('%Y%m%dT%H%M%S')}",
        ]
    else:
        next_day = date + datetime.timedelta(days=1)
        lines += [
            f"DTSTART;VALUE=DATE:{date.strftime('%Y%m%d')}",
            f"DTEND;VALUE=DATE:{next_day.strftime('%Y%m%d')}",
        ]

    remind = REMIND_RE.search(text)
    if remind:
        lines += [
            "BEGIN:VALARM",
            "ACTION:DISPLAY",
            f"DESCRIPTION:{escape(title)}",
            f"TRIGGER:-P{int(remind.group(1))}D",
            "END:VALARM",
        ]
    lines.append("END:VEVENT")
    return lines


def build_recurring_event(path: Path, title: str, every: re.Match) -> list[str]:
    day_names = DAY_NAME_RE.findall(every.group(1))
    time_str, end_time_str = every.group(2), every.group(3)
    byday = ",".join(WEEKDAYS[name][1] for name in day_names)
    hour, minute = (int(p) for p in time_str.split(":"))

    # DTSTART must land on the soonest upcoming listed day; the RRULE covers the rest.
    now = datetime.datetime.now()
    candidates = []
    for name in day_names:
        days_ahead = (WEEKDAYS[name][0] - now.weekday()) % 7
        date = now.date() + datetime.timedelta(days=days_ahead)
        candidate = datetime.datetime.combine(date, datetime.time(hour, minute))
        if candidate <= now:
            candidate += datetime.timedelta(days=7)
            date += datetime.timedelta(days=7)
        candidates.append((candidate, date))
    start, start_date = min(candidates)
    if end_time_str:
        end_hour, end_minute = (int(p) for p in end_time_str.split(":"))
        end = datetime.datetime.combine(start_date, datetime.time(end_hour, end_minute))
    else:
        end = start + datetime.timedelta(hours=1)

    stamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    uid = re.sub(r"[^a-z0-9]+", "-", path.stem.lower()).strip("-") + "@kb-vault"

    lines = [
        "BEGIN:VEVENT",
        f"UID:{uid}",
        f"DTSTAMP:{stamp}",
        f"SUMMARY:{escape(title)}",
        f"DTSTART:{start.strftime('%Y%m%dT%H%M%S')}",
        f"DTEND:{end.strftime('%Y%m%dT%H%M%S')}",
        f"RRULE:FREQ=WEEKLY;BYDAY={byday}",
    ]

    remind = REMIND_RE.search(path.read_text(encoding="utf-8"))
    if remind:
        lines += [
            "BEGIN:VALARM",
            "ACTION:DISPLAY",
            f"DESCRIPTION:{escape(title)}",
            f"TRIGGER:-P{int(remind.group(1))}D",
            "END:VALARM",
        ]

    lines.append("END:VEVENT")
    return lines


def main() -> None:
    events: list[str] = []
    count = 0
    for path in sorted(CALENDAR_DIR.glob("*.md")):
        if path.stem == "calendar":  # folder note
            continue
        event = build_event(path)
        if event:
            events += event
            count += 1

    ics = [
        "BEGIN:VCALENDAR",
        "VERSION:2.0",
        "PRODID:-//kb-vault//calendar//EN",
        "X-WR-CALNAME:KB Next Calendar",
        *events,
        "END:VCALENDAR",
    ]
    OUTPUT.write_text("\r\n".join(ics) + "\r\n", encoding="utf-8")
    print(f"wrote {OUTPUT.name} with {count} event(s)")


if __name__ == "__main__":
    main()
