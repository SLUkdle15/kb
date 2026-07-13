# Integration Testing Principles

_(Based on Vladimir Khorikov's "Unit Testing Principles, Practices, and Patterns")_

## Aim

> How to write good integration test?

## What is characteristic of a good integration test ?

1. **Protection against regressions**
2. **Resistance to refactoring**  --> always maxing out
3. **Fast feedback**
4. **Maintainability**

To be worth keeping, an integration test must provide enough protection against regressions to offset its slow execution and high maintenance cost

## What should it verify?

A well-written integration test treats the domain model as a black box, verifying only the final state of managed dependencies (like the database) and the interactions with un-managed dependencies (like a message bus)

## Writing Good Integration Tests

1. Scope: target application services and test for longest happy path and any complex edge cases that unit tests cannot reach. Avoid fail fast errors.
2. Mock only un-managed dependencies. Use mocks or spies ti verify interactions at the very edges of your system. 
3. Establish DB prerequisites: 
	1. Migration Base delivery
	2. Developer isolation
	3. Avoid in-memory DB
4. Optimize the test life cycle:
	1. Clean up at the start:
	2. Independent transactions
	3. Sequential execution
5. Improve maintainability via helper

## Managed Dependencies