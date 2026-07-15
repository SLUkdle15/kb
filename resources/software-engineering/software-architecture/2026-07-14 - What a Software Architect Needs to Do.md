# What a Software Architect Needs to Do

Source: *Fundamentals of Software Architecture*

Related: [[resources/software-engineering/software-architecture/software-architecture|Software Architecture]] · [[areas/software-architecture/2026-06-03 - Software Architect Roadmap|Software Architect Roadmap]]

## Role and mindset questions

1. What does a software architect need to think about? (mindset — technical, business, and stakeholder concerns compared to a developer's)
	1. Architecture vs Design: define AC and AP, make ADs vs write code.
	2. Sacrifice expertise to broaden knowledge (technical breadth): I don't know I don't know -> I know I don't know.
	3. Analyze trade-offs.
	4. Understand the business domain.
	5. Should write code (write best quality code), write tests, and do code review.
2. How does an SA make AD?
	1. **Extract/define** AC (from domain, requirements, implicit knowledge)
	2. **Prioritize** AC (least-worst architecture — pick the vital few)
	3. **Measure** AC
	4. **Govern** them (fitness functions + ADR) at component level
	5. **Understand/know app architecture style** 
	6. **Make architecture decisions (AD)** 
3. What is the real value of an Architecture Decision Record (ADR)? *(open)*
4. Where does a software architect's responsibility end and a DBA's begin?
	1. No end or beginning — this is bidirectional, and the SA's job is to constantly coach and mentor the development team.
5. What is the risk of a quality (attribute) assessment? *(open)*

## Follow-up questions after reading

1. Modularity: standardize parts that group together to construct a more complex structure.
	1. Ex: `com.example.app`.
	2. Good means high cohesion — doing one thing — and loose coupling.
2. Component level: library/ module level
3. Package by layer vs package by feature? *(open)*
4. Not all characteristics can be governed by a fitness function.
5. What's the difference between an AD and a design principle? *(open)*

