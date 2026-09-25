---
type: distilled-note
---

# Make the Chain Dependency-Driven, Not Clock-Driven

A multi-step job chain has two ways to decide when a step starts.

**Clock-driven** gives each step its own hard-coded schedule. The gap between two steps is a guess about how long the earlier one takes, and that guess *is* the design — nothing measures it and nothing enforces it. The chain is correct only while every step keeps finishing inside a window someone assumed once and never revisited.

**Dependency-driven** starts a step because the step it depends on reported done. Run time can drift without breaking the chain, because no step is holding a stopwatch on another.

The failure is specific: a step fires on schedule while its predecessor is still running, and reads input that is half-written or still belongs to the previous run. It does not surface as a scheduling bug — it surfaces as wrong data, an empty result, or a run that silently did nothing, which is why it survives so long.

Widening the interval does not convert one kind into the other. It buys a larger guess, and it expires the next time run time grows. The real options are a completion signal between the steps, or an overlap guard that refuses to start a run while the previous one is in flight.

The local instance is the NCTool scheduler's two-hour assumption — see [[archives/next-actions/2026-09-28 - Reschedule the NCTool Job Past the Two-Hour Assumption|Reschedule the NCTool Job Past the Two-Hour Assumption]].
