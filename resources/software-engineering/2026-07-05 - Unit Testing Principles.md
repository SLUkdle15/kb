# Unit Testing Principles

_(Based on Vladimir Khorikov's "Unit Testing Principles, Practices, and Patterns")_

## Aim

> How to write good integration test?

## What Makes a Test "Unit"

- Verifies a single unit of **behavior**
- Runs fast
- Runs in **isolation from other tests** — not isolation from collaborators

This is why a test hitting a real local database can still count as a good "unit" test under his definition — even though it wouldn't under the old one.

## Characteristic of a good integration test

1. **Protection against regressions**
2. **Resistance to refactoring**
3. **Fast feedback**
4. **Maintainability**
5. **Avoid rigid naming**: `Delivery_with_a_past_date_is_invalid`
6. **AAA pattern**

There is no such ideal test, always aim for maxing out protection against regressions,

## Writing Good Integration Tests

1. Refactor into **controller + logic** split; the controller is the seam you verify wiring through.
2. Only mock unmanaged dependencies; don't verify stubs
		this is proved to be increase the attribute 1 of the test
3. Use a **local DB** (real engine, not an in-memory substitute like SQLite standing in for Postgres) → fast + full control, no shared state with other devs/CI.
4. Keep tests small, readable, and minimize out-of-process dependencies
		this is proved to be increase the attribute 4 of the test
5. Decide state reset strategy: transaction rollback per test (fast) vs. full recreate/migrate per run (safer for schema/trigger changes).
6. Avoid heavy shared setup/fixtures across a test class — prefer explicit private factory methods per test for readability.
7. Don't test logging unless the log output itself is the business behavior (e.g. an audit trail).
