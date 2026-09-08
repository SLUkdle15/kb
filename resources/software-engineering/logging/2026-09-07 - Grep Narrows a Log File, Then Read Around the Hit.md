---
type: distilled-note
---

# Grep Narrows a Log File, Then Read Around the Hit

For when Grafana is not available or the log only exists on the box. `grep` answers *where* and *how many*, and the harder half is always the same question afterwards: what surrounded the hit? Count first, then read around it — with the cheapest tool that can.

Hold the path in a variable once, because every command below needs it:

```bash
f=logs-from-nc-tool-job-in-nc-tool-job-84676fc49c-hzj9m.log
tail -50 "$f"
```

Knowing how the line is laid out is what makes the searches work, and there are two layouts. The console one is positional:

```text
<timestamp> <traceId> [<thread>] <LEVEL> <logger>: <message>
```

wrapped in ANSI color codes. The level sits between spaces, so search `' ERROR '` with the spaces — otherwise the word matches loggers and message text too.

The same events also come as ECS JSON, one object per line, with the fields nested rather than ordered:

```json
{"@timestamp":"2026-09-08T01:00:00.001943514Z","log":{"level":"INFO","logger":"org.ftel.nctool.service.ScheduledJobService"},"process":{"pid":1,"thread":{"name":"scheduling-1"}},"service":{"name":"nc-tool","version":"0.0.1-SNAPSHOT","node":{}},"message":"Starting scheduled job: Retry failed CMS sends","ecs":{"version":"8.11"}}
```

One object per line is the part that matters: every line-based tool below still works. Position is gone, so the surrounding-spaces trick does not apply, but the bare word is enough in practice:

```bash
grep 'WARN' "$f"
```

Only when something else on the line carries the word is it worth spelling out the field — `grep -F '"level":"WARN"'`, where `-F` keeps the quotes and colon from being read as a regex. The nesting can be ignored either way: `level` sits inside `log` and the thread name inside `process.thread`, but a substring match never sees the structure.

## Count First, Then Read the Recent Ones

```bash
grep -c ' ERROR ' "$f"        # how many?  -> 47
grep ' ERROR ' "$f" | tail -5 # the 5 most recent
```

The count decides how to read the rest. 47 is worth filtering; 4 is worth reading in full.

## Read Around a Hit

Everything below is one question — what surrounded this line? Three tools answer it, and they are worth reaching for in this order.

`grep` context flags first. Nothing to look up, nothing to compute:

```bash
grep -m1 -A20 ' ERROR' "$f"                  # first hit, 20 lines after
grep -B10 -A10 'Thread starvation' "$f"      # 10 either side of every hit
```

`-m1` stops at the first match, which is what makes this safe on a file with hundreds of hits. It is also the way to see the shape of the file before knowing what to search for.

Then the pager, when one screen is not enough and the reading continues from there:

```bash
less +/'Thread starvation' "$f"   # jump to the first match, keep scrolling
less +1227g "$f"                  # jump to a known line number
```

`sed` last. It cannot find the line itself, so it costs a `grep -n` first, and then the range has to be worked out by hand:

```bash
grep -n 'Thread starvation' "$f" | tail -1   # -> 1227
sed -n '1217,1237p' "$f"                     # 10 before, 10 after
```

Two commands and mental arithmetic for what `-B10 -A10` does in one. It earns that only when the window is lopsided — starting well before the hit, or running far past it — which the context flags cannot express.

## Exclude the Known Noise

A level filter is only useful once the recurring benign lines are gone. Chain a `grep -v` rather than writing one clever pattern:

```bash
grep ' WARN ' "$f" | grep -v 'No configuration'
```

Each `-v` is a decision that a line is known and uninteresting, and they stack readably.

## Pull Out the Values, Not the Lines

`grep -o` prints only the matched part instead of the whole line, and `\K` in a PCRE pattern (`-P`) throws away everything matched before it. With `sort -u`, a flood of repeated warnings collapses into the distinct set behind it:

```bash
grep -F '"level":"WARN"' "$f" | grep -oP 'AI ID: \K[^ ]+' | sort -u
```

Counting WARN lines answers *how bad*; this answers *which ones* — usually three or four values, and that short list is the thing to go fix.

## Keep the Result

```bash
grep ' ERROR ' "$f" > z.txt
```

Worth doing before narrowing further — the filtered file is smaller to work with, and it survives the terminal scrollback.

Time-range filtering needs a regex over the timestamp field and is not covered here.
