# Decide Whether NCTool Logs Keep the Seven-Hour Offset

Area: [[areas/work-systems/work-systems|Work Systems]]

## Action

NCTool log timestamps sit seven hours off local time — UTC written by the app, read by people in UTC+7. Decide whether that stays or changes, rather than leaving it as a thing everyone converts in their head.

Keeping UTC is defensible: it is what ECS `@timestamp` expects and what makes logs comparable across systems. The cost is every manual grep and every incident timeline needing the offset applied. Check what Grafana already renders before changing the application — if the dashboard shows local time, the problem is only on the box.

Reference: [[resources/software-engineering/logging/2026-09-03 - Structured JSON Logs in Production|Structured JSON Logs in Production]]

## Done When

The offset is either deliberately kept, with the reason written down, or changed in the logging config.
