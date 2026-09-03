---
type: distilled-note
---

# Log Levels Are a Threshold, Not a Category

The levels are ordered: ERROR, WARN, INFO, DEBUG, TRACE. Setting a logger to a level emits that level and everything above it, so a level is a threshold rather than a selection — INFO means "INFO and worse", not "INFO only".

Two thresholds are worth setting separately: `root`, which governs the frameworks and libraries, and the application's own package.

- **Dev** — root at INFO, own package at DEBUG.
- **Prod** — root at WARN, own package at INFO.

```yaml
logging:
  level:
    root: warn
    com.example.nctool: info
```

In dev this gives the entry and boundary DEBUG lines from the application's own code while Spring, Hibernate, and the HTTP clients stay at INFO. In prod, root at WARN drops library chatter entirely, and the package at INFO leaves exactly the one-line-per-completed-unit stream described in [[resources/software-engineering/logging/2026-09-03 - One Unit of Work, One INFO Log|One Unit of Work, One INFO Log]].

Because the level is a threshold, dropping root to WARN in prod costs nothing in failure visibility: library warnings and errors still come through. Only the routine INFO narration goes away — which is what makes the remaining INFO lines mean something.

The two environments are separate profile files, `application-dev.yml` and `application-prod.yml`, so promoting a package to DEBUG to chase a problem in prod is a config change, not a code change.
