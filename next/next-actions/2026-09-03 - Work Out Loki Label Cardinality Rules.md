# Work Out Loki Label Cardinality Rules

Area: [[areas/work-systems/work-systems|Work Systems]]

## Action

Work out which fields belong in Loki labels and which stay in the log body, and what that means for the MDC identifiers described in [[resources/software-engineering/logging/2026-09-03 - MDC Carries the Identifiers|MDC Carries the Identifiers]].

Loki indexes labels only, and a high-cardinality label creates a stream per value, so this is the decision that sets logging cost for NCTool and FCM.

https://grafana.com/docs/loki/latest/send-data/

## Done When

I can say which fields are safe as labels and which must stay queryable at read time, captured as a note in [[resources/software-engineering/logging/logging|Logging]].
