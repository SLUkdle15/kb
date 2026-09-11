# Reschedule the NCTool Job Past the Two-Hour Assumption

Area: [[areas/work-systems/work-systems|Work Systems]]

## Action

The NCTool scheduler assumes a job run finishes inside two hours, but real runs take longer. Measure how long a run actually takes, then change the schedule so the next trigger cannot fire while the previous run is still going.

Decide which fix this is before changing the cron: a wider interval, or an overlap guard that skips a trigger when a run is still in flight. A wider interval only hides the problem if run time keeps growing.

## Done When

The schedule matches observed run time and no run overlaps its predecessor.
