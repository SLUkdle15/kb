---
type: distilled-note
---

# The Three Troubles of Distributed Systems

In a distributed system, there may well be some parts of the system that are broken in some unpredictable way, even though other parts of the system are working fine. This is known as a **partial failure**.

Three things go wrong in a distributed system, and everything else follows from them:

1. **Partial failure** — parts break unpredictably while the rest keeps working.
2. **Unreliable networks** — packets can be lost, delayed, duplicated, or reordered, and [[resources/software-engineering/system-architecture/2026-08-27 - Packet Switching Cannot Reserve Bandwidth|bandwidth cannot be reserved]], so delay is unbounded.
3. **Unreliable clocks** — clocks on different machines disagree, so you cannot trust a timestamp to order events across nodes.

## Handling a fault is not the same as tolerating it

Handling network faults doesn't necessarily mean tolerating them. If your network is normally fairly reliable, a valid approach may be to simply show an error message to users while your network is experiencing problems.

What is not optional is the response itself: you need to know how your software reacts to network problems, and ensure that the system can recover from them. It may make sense to deliberately trigger network problems and test the system's response.
