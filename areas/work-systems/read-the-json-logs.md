---
type: protocol
---

# Read the JSON Logs

Source: [[resources/software-engineering/logging/2026-09-25 - Grep Finds the JSON Log Line, jq Makes It Readable|Grep Finds the JSON Log Line, jq Makes It Readable]]

Use when reading an ECS JSON log file on the box, with no Grafana. Every command below is one shape with three slots — the prefix never changes:

```bash
jq -rR 'fromjson? // empty | <select> | <format>'
```

## Checklist

- [ ] Hold the path once and confirm it is the file the job writes and that the lines are JSON: `f=<path>` then `tail -2 "$f"`.
- [ ] Count by level to decide how much to read: `jq -rR 'fromjson? // empty | .log.level' "$f" | sort | uniq -c`.
- [ ] Read the distinct messages before searching for one: `jq -rR 'fromjson? // empty | .message' "$f" | sort | uniq -c | sort -rn`.
- [ ] Search the message field, not the line: `jq -rR 'fromjson? // empty | select(.message|test("<pattern>";"i")) | "\(.["@timestamp"][11:23]) \(.log.level) \(.message)"' "$f"`.
- [ ] Narrow by time instead, when the window is known: swap the select for `select(.["@timestamp"] >= "<from>" and .["@timestamp"] < "<to>")`, with ISO prefixes cut at any precision.
- [ ] Read the full event behind a hit — drop `-r` and the format slot: `jq -R 'fromjson? // empty | select(<same select>)' "$f"`.
- [ ] Print any stack trace as real lines: `jq -rR 'fromjson? // empty | select(.log.level=="ERROR") | .error.stack_trace' "$f"`.
- [ ] Read what surrounded a hit, if the event alone is not enough: `grep -B10 -A10 -F '<pattern>' "$f" | jq -rR 'fromjson? // empty | "\(.["@timestamp"][11:23]) \(.log.level) \(.message)"'`.
- [ ] Keep anything worth returning to: append `> z.txt` before narrowing further.

## Notes

- `fromjson? // empty` is armor, not decoration. Without it one non-JSON line — a banner, a trace on stdout, a half-written last line — aborts the run with a parse error after printing a plausible-looking partial result.
- On a large file put `grep -F '<pattern>'` in front of the pipe for speed, and keep the `select` as well. `grep` narrows fast but matches the whole object; the `select` is what removes the hits that landed in a logger name or a field value.
- `grep -oP '"message":"\K[^"]*'` is the fallback for a box with no `jq`, and it lies twice: it matches `error.message` as readily as the real one, and it truncates at the first escaped quote inside a message. Use it for a glance, never to decide something.
- `.["@timestamp"]` needs the bracket form because `@` is not a bare key. `[11:23]` is the clock time out of the ISO string.
