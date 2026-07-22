---
type: distilled-note
---

# What a Software Architect Needs to Do

> [!summary]
> An architect's job is less about writing code and more about defining, prioritizing, measuring, and governing architecture characteristics, making architecturally significant decisions (recorded as ADRs where the *why* matters more than the *how*), assessing risk, and continuously coaching the dev team. Breadth beats depth: move from "I don't know what I don't know" to "I know I don't know."

Source: *Fundamentals of Software Architecture*

Related: [[resources/software-engineering/system-architecture/system-architecture|System Architecture]] · [[areas/software-architect-growth/2026-06-03 - Software Architect Roadmap|Software Architect Roadmap]]

Protocol: [[areas/software-architect-growth/make-an-architecture-decision|Make an Architecture Decision]]

## Role and mindset questions

1. What does a software architect need to think about? (mindset — technical, business, and stakeholder concerns compared to a developer's)
	1. Architecture vs Design: define AC and AP, make ADs vs write code.
	2. Sacrifice expertise to broaden knowledge (technical breadth): I don't know I don't know -> I know I don't know.
	3. Analyze trade-offs.
	4. Understand the business domain.
	5. Should write code (write best quality code), write tests, and do code review.
2. How does an SA do?
	1. **Extract/define** AC (from domain, requirements, implicit knowledge)
	2. **Prioritize** AC (least-worst architecture — pick the vital few)
	3. **Measure** AC
	4. **Govern** them (fitness functions + ADR) at component level
	5. **Understand/know app architecture style** 
	6. **Make architecture decisions (AD)**
		1.  According to Michael, **architecturally significant** decisions are those decisions that affect the structure, nonfunctional characteristics, dependencies, interfaces, or construction techniques.
	7. **Assessing risks**
3. What is the real value of an Architecture Decision Record (ADR)?
	1. Why is more important than how - second law
	2. Storing in GIT and a wiki page
4. Where does a software architect's responsibility end and a DBA's begin?
	1. No end or beginning — this is bidirectional, and the SA's job is to constantly coach and mentor the development team.
5. What is the risk of a quality (attribute) assessment?
	1. The architecture risk matrix (illustrated in Figure 20-1) uses two dimensions to qualify risk: the overall impact of the risk and the likelihood of that risk occurring. Each dimensions has a low (1), medium (2), and high (3) rating.
	2. Presenting the risk assessment with feature x risk criteria.

## Follow-up questions after reading

1. Modularity: standardize parts that group together to construct a more complex structure.
	1. Ex: `com.example.app`.
	2. Good means high cohesion — doing one thing — and loose coupling.
2. Component level: library/ module level
3. Package by layer vs package by feature? *(open)*
4. Not all characteristics can be governed by a fitness function.
5. What's the difference between an AD and a design principle? *(open)*

