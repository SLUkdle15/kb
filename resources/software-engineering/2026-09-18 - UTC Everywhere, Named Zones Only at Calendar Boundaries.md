---
type: distilled-note
---

# UTC Everywhere, Named Zones Only at Calendar Boundaries

The rule that prevents this class of bug:

UTC everywhere for storage, logs, and wire formats. A named zone appears only where a human-facing calendar day is defined — and there it is always written out explicitly, never inherited from the JVM default.

Came up while deciding [[archives/next-actions/2026-09-18 - Decide Whether NCTool Logs Keep the Seven-Hour Offset|whether NCTool logs keep the seven-hour offset]].
