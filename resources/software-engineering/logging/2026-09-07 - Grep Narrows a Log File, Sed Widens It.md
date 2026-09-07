---
type: distilled-note
---

# Grep Narrows a Log File, Sed Widens It

For when Grafana is not available or the log only exists on the box. `grep` answers *where* and *how many*; it is bad at showing what surrounded the hit. So the move is two steps: narrow to a line number, then widen around it.

Hold the path in a variable once, because every command below needs it:

```bash
f=logs-from-nc-tool-job-in-nc-tool-job-84676fc49c-hzj9m.log
tail -50 "$f"
```

Knowing the field order is what makes the searches work:

```text
<timestamp> <traceId> [<thread>] <LEVEL> <logger>: <message>
```

wrapped in ANSI color codes. The level sits between spaces, so search `' ERROR '` with the spaces — otherwise the word matches loggers and message text too.

## Count First, Then Read the Recent Ones

```bash
grep -c ' ERROR ' "$f"        # how many?  -> 47
grep ' ERROR ' "$f" | tail -5 # the 5 most recent
```

The count decides how to read the rest. 47 is worth filtering; 4 is worth reading in full.

To see the shape of the file before knowing what to search for, take the first match and the lines after it:

```bash
grep -m1 -A20 ' ' "$f"
```

## Narrow to a Line Number, Then Widen

`-A`/`-B` work when the pattern is known and rare. When the surrounding block matters more, get the line number and slice:

```bash
grep -n 'Thread starvation' "$f" | tail -1   # -> 1227
sed -n '1217,1237p' "$f"                     # 10 before, 10 after
```

Or jump there in the pager instead, which keeps scrolling available:

```bash
less +1227g "$f"
less +/'Thread starvation' "$f"
```

## Exclude the Known Noise

A level filter is only useful once the recurring benign lines are gone. Chain a `grep -v` rather than writing one clever pattern:

```bash
grep ' WARN ' "$f" | grep -v 'No configuration'
```

Each `-v` is a decision that a line is known and uninteresting, and they stack readably.

## Keep the Result

```bash
grep ' ERROR ' "$f" > z.txt
```

Worth doing before narrowing further — the filtered file is smaller to work with, and it survives the terminal scrollback.

Time-range filtering needs a regex over the timestamp field and is not covered here.
