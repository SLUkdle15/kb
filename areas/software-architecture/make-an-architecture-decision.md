---
type: protocol
---

# Make an Architecture Decision

Source: [[resources/software-engineering/software-architecture/2026-07-14 - What a Software Architect Needs to Do|What a Software Architect Needs to Do]]

## Checklist

- [ ] Confirm the decision is **architecturally significant**: it affects structure, nonfunctional characteristics, dependencies, interfaces, or construction techniques.
- [ ] Wait for the **Last Responsible Moment**: decide only when delaying further would cost more than deciding.
- [ ] List candidate options and **analyze trade-offs** for each.
- [ ] **Assess risk** with the architecture risk matrix: impact × likelihood, each rated low (1), medium (2), high (3).
- [ ] **Record** it as an ADR — follow [[areas/software-architecture/write-an-adr|Write an ADR]].
- [ ] Decide how to **govern** the decision: a fitness function where measurable, ADR compliance otherwise.
- [ ] **Communicate** the decision to the dev team and coach them through it.

## Notes

- The *why* matters more than the *how* — capture the justification, not the implementation.