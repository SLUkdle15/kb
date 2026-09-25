---
type: distilled-note
---

# Grep Finds the JSON Log Line, jq Makes It Readable

Protocol: [[areas/work-systems/read-the-json-logs|Read the JSON Logs]]

Grep does not fail on ECS JSON logs. It matches exactly what it was asked to match, and then prints a 400-character object where the interesting part is four fields buried between `process.thread` and `ecs.version`. The failure is in the reading, not the searching, and it takes a second tool. `jq` turns the matched line back into something a person can look at.

The division of labour is the point: grep narrows, `jq` renders.

## One Event, One Readable Line

```bash
f=logs-from-nc-tool-job-in-nc-tool-job-84676fc49c-hzj9m.log
jq -r '"\(.["@timestamp"][11:23]) \(.log.level) \(.log.logger|split(".")|last): \(.message)"' "$f"
```

```text
01:00:00.001 INFO ScheduledJobService: Starting scheduled job: Retry failed CMS sends
01:00:01.902 ERROR CmsClient: CMS send failed
```

That is the console layout rebuilt by hand, which is the honest way to think about it — the positional line was never lost, it just has to be asked for. `-r` prints the string raw instead of quoted. `.["@timestamp"]` needs the bracket form because `@` is not a bare key. `[11:23]` slices the clock time out of the ISO timestamp, and `split(".")|last` drops the package prefix off the logger.

When it is not yet clear which fields matter, leave out `-r` and the format string entirely — `jq 'select(.log.level=="ERROR")' "$f"` pretty-prints whole events, indented, one screen each.

## The Line That Is Not JSON

`jq` aborts at the first line it cannot parse. A startup banner, a stack trace printed straight to stdout, a half-written last line in a file still being appended to — any one of them ends the run with `jq: parse error: Invalid numeric literal at line 5`, after printing only what came before it. On a long file the output looks plausible and is silently truncated.

```bash
jq -rR 'fromjson? // empty | "\(.log.level) \(.message)"' "$f"
```

`-R` hands each line to the filter as a raw string instead of parsing it, `fromjson?` parses it with the `?` swallowing the failure, and `// empty` drops the line that failed. This belongs in the reflex, not in the fix applied after the first parse error.

## Grep First, jq Second

`jq` parses every line; grep does not, and on a large file that gap is the whole wait. Narrowing with grep and formatting the survivors is both faster and shorter to type:

```bash
grep -F '"level":"ERROR"' "$f" | jq -r '.message, .error.type'
```

The context flags survive the pipe as well, which is what keeps [[resources/software-engineering/logging/2026-09-07 - Grep Narrows a Log File, Then Read Around the Hit|reading around the hit]] available on JSON. The `--` separators grep inserts between hit groups are not JSON, so the armor from the previous section is what makes this work:

```bash
grep -B5 -A5 -F '"level":"ERROR"' "$f" | jq -rR 'fromjson? // empty | "\(.["@timestamp"][11:23]) \(.log.level) \(.message)"'
```

## The Stack Trace

This is the part grep can never show. A trace arrives as one field with its newlines and tabs escaped — `"java.net.SocketTimeoutException: Read timed out\n\tat java.base/..."` — so every grep hit on it is a single unreadable line. `-r` prints those escapes as the real characters:

```bash
jq -rR 'fromjson? // empty | select(.log.level=="ERROR") | .error.stack_trace' "$f"
```

```text
java.net.SocketTimeoutException: Read timed out
	at java.base/sun.nio.ch.NioSocketImpl.timedRead(NioSocketImpl.java:283)
	at org.ftel.nctool.cms.CmsClient.send(CmsClient.java:88)
```

One event that stayed one event is the reason for [[resources/software-engineering/logging/2026-09-03 - Structured JSON Logs in Production|logging JSON in production]] in the first place, and this is where the local reading finally gets the benefit too.

## Fields Instead of Patterns

Once the line is an object, `select` replaces the pattern guessing. Following one identifier through the run is the common case, and it works because [[resources/software-engineering/logging/2026-09-03 - MDC Carries the Identifiers|the MDC put it in a field]]:

```bash
jq -rR 'fromjson? // empty | select(.aiId=="AI-4711") | "\(.["@timestamp"][11:23]) \(.log.level) \(.message)"' "$f"
```

Counting by level answers how bad before anything is read:

```bash
jq -rR 'fromjson? // empty | .log.level' "$f" | sort | uniq -c
```

## Search the Message, Not the Line

`grep` searches the whole rendered object, so a word that appears in a logger name, a field value, or a stack trace counts as a hit. Searching the message text specifically means naming the field and testing it:

```bash
jq -rR 'fromjson? // empty | select(.message|test("failed";"i")) | "\(.["@timestamp"][11:23]) \(.log.level) \(.message)"' "$f"
```

`test` takes a regex, and the `"i"` makes it case-insensitive — `contains("failed")` is the plain-substring version when the pattern has regex characters in it. Because the test names `.message`, searching `CmsClient` this way returns nothing even though the string is on every line of the file, sitting in `log.logger`. That is the point: the noise is excluded by construction rather than by a chain of `grep -v`.

On a large file, narrow with `grep` first and let `jq` apply the precision, which keeps the speed without keeping the false hits:

```bash
grep -F 'failed' "$f" | jq -rR 'fromjson? // empty | select(.message|test("failed";"i")) | "\(.["@timestamp"][11:23]) \(.log.level) \(.message)"'
```

Since [[resources/software-engineering/logging/2026-09-03 - Structured JSON Logs in Production|the message is written as a constant sentence]], the whole set is short enough to read instead of searched blind:

```bash
jq -rR 'fromjson? // empty | .message' "$f" | sort | uniq -c | sort -rn
```

## Without jq on the Box

`grep -oP '"message":"\K[^"]*' "$f"` looks like it does the same job and is worth knowing for a machine with no `jq` installed, but it is wrong in two ways that do not announce themselves. It matches `error.message` as readily as the top-level one, so nested exception text appears in the output as if it were a log message. And the `[^"]*` stops at the first escaped quote, so a message quoting a value truncates mid-sentence — `Rejected payload \` instead of the rest of the line. Fine for a glance, not for deciding something.

## Time Range

ISO-8601 timestamps are fixed-width and ordered, so a string comparison is a time comparison, and the prefix can be cut anywhere — hour, minute, second:

```bash
jq -rR 'fromjson? // empty | select(.["@timestamp"] >= "2026-09-08T01:00" and .["@timestamp"] < "2026-09-08T01:05") | "\(.["@timestamp"][11:23]) \(.log.level) \(.message)"' "$f"
```

This is the one search the positional console layout cannot express without a regex over the timestamp, and the reason to reach for the JSON file even when both are on the box.
