---
type: distilled-note
---

# From Batch to Stream Processing

The problem with daily batch processes is that changes in the input are only reflected in the output a day later, which is too slow for many impatient users.

To reduce the delay, run the processing more frequently — say, processing a second's worth of data at the end of every second — or even continuously, abandoning the fixed time slices entirely and simply processing every event as it happens.

That is the idea behind stream processing. It is the same computation as batch, with the window shrunk until it disappears.
