# Search a Log File from the Linux Terminal

Area: [[areas/work-systems/work-systems|Work Systems]]

## Action

Learn to work a log file from the terminal, for when Grafana is not available or the log only exists on the box: locating the file, searching it, following it live, and reading rotated or compressed logs.

Left over from [[archives/next-actions/2026-08-17 - Review the Efficient Spring Logging Guide in Grafana|the Grafana logging review]], which closed without covering it.

## Done When

I can find and search a log file on a server without looking up the commands.



Format: <timestamp> <traceId> [<thread>] <LEVEL> <logger>: <message> — wrapped in ANSI color codes

f=
tail -50 $f
less -50

grep -c ' ERROR ' $f              # how many?           → 47
grep ' ERROR ' $f | tail -5       # the 5 most **recent**

poke around with
grep -m1 -A20 ' ' $f        after for see log

grep -n 'Thread starvation' "$f" | tail -1    # → 1227 (with line)
sed -n '1217,1237p' "$f"                      # 10 before, 10 after

less +1227g $f
or less +/'Thread starvation' $f

Exlcude
grep ' WARN ' $f | grep -v 'No configuration'

there is the way to do time via regrex skip for now

write to file: > z.txt


## Disposition

Completed 2026-09-07. Distilled into [[resources/software-engineering/logging/2026-09-07 - Grep Narrows a Log File, Sed Widens It|Grep Narrows a Log File, Sed Widens It]]. Following a log live and reading rotated or compressed logs were in the original scope and were not covered; neither was time-range filtering, which the capture deferred explicitly.
