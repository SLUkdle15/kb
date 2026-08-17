# Software Architect Roadmap

Related area: [[areas/technical-growth/technical-growth|Technical Growth]]

One candidate path for [[areas/personal-development/favorite-problems|Favorite Problems]] #1, not a committed career track. Based on the [roadmap.sh Software Architect roadmap](https://roadmap.sh/software-architect).

Goal: become someone who can understand business goals, translate them into system requirements, design trade-off-based architecture, communicate the design clearly, guide teams through implementation, and evolve systems over time. That capability is worth building whether or not the title ever follows.

---

## Target Profile

Since you are already a senior developer, do not start from beginner coding material.

If this path is the one being followed:

- Depth: architecture — design, trade-offs, quality attributes
- Adjacent: solution and cloud architecture
- Main output: architecture portfolio

Use these as high-level maps:

- roadmap.sh Software Architect roadmap
- Solution Architect Roadmap GitHub repo
- Azure Architecture Center or AWS/GCP architecture centers
- C4 model resources
- Architecture Decision Records resources

Do not try to finish everything. Use them as checklists.

---

## Phase 1: Core Architecture Thinking

Main question:

> What makes a design good or bad?

Study:

- Fundamentals of Software Architecture
- Software Architecture in Practice
- A Philosophy of Software Design
- Just Enough Software Architecture
- 97 Things Every Software Architect Should Know

Focus on:

- Scalability
- Availability
- Maintainability
- Deployability
- Security
- Cost
- Observability
- Reliability
- Modifiability
- Performance

Practice saying:

> We choose X because of Y, but the downside is Z.

Deliverables:

- Architecture characteristics checklist
- Sample ADRs
- One-page architecture review template
- Trade-off matrix template

Exercise:

```text
Goal:
Current architecture:
Main bottlenecks:
Top 5 quality attributes:
3 possible designs:
Chosen design:
Trade-offs:
Risks:
Migration plan:
```

---

## Phase 2: System Design and Distributed Systems

Main question:

> How do large systems behave under load, failure, and change?

Study:

- Designing Data-Intensive Applications
- Understanding Distributed Systems
- Foundations of Scalable Systems
- Building Microservices
- Monolith to Microservices
- Microservices Up & Running

Focus topics:

- Caching
- Queues
- Event-driven architecture
- Consistency
- Replication
- Partitioning
- Service boundaries
- API gateways
- Rate limiting
- Idempotency
- Failure handling
- Observability
- Data ownership

Design these systems seriously:

1. URL shortener
2. Food delivery platform
3. Chat or messaging system
4. Payment and order system
5. Multi-tenant SaaS platform

For each design, produce:

- Context diagram
- Container diagram
- Main data model
- API design
- Scaling strategy
- Failure scenarios
- Monitoring plan
- Security concerns
- Cost concerns
- ADRs

---

## Phase 3: Domain-Driven Design and Service Boundaries

Main question:

> Where should the boundaries be?

Study:

- Domain-Driven Design by Eric Evans
- Learning Domain-Driven Design
- Patterns, Principles, and Practices of Domain-Driven Design
- Mastering Strategic Domain-Driven Design

Focus on:

- Bounded contexts
- Aggregates
- Domain events
- Ubiquitous language
- Context maps
- Core domain vs supporting domain
- Anti-corruption layer

Practice domain modeling for one real domain:

- E-commerce
- Banking wallet
- Learning platform
- Booking system
- Logistics
- HR/payroll

For the chosen domain, model:

- Subdomains
- Bounded contexts
- Context map
- Integration patterns
- Domain events
- Service ownership

Key idea:

> Architects are paid well because they can draw boundaries well.

---

## Phase 4: API, Integration, and Event Architecture

Main question:

> How do systems talk to each other without becoming a mess?

Study:

- Mastering API Architecture
- Continuous API Management
- Enterprise Integration Patterns
- Building Event-Driven Microservices
- Flow Architectures
- Communication Patterns

Learn:

- REST
- GraphQL
- gRPC
- Async messaging
- Kafka-style event streams
- Transactional outbox
- Saga pattern
- API versioning
- Backward compatibility
- Schema evolution
- Consumer-driven contracts

Reference design exercise:

Design this system:

- Order service
- Payment service
- Inventory service
- Notification service
- Shipping service

Then create two versions:

1. Synchronous REST version
2. Event-driven version

Compare the trade-offs.

---

## Phase 5: Cloud and Infrastructure Architecture

Main question:

> Can this run reliably in production?

Use:

- Azure Architecture Center
- AWS Well-Architected Framework
- Google Cloud Architecture Center
- Kubernetes documentation
- Real reference architectures

Focus on:

- Compute choices
- Containers
- Databases
- Messaging
- Networking
- Identity
- Secrets management
- CI/CD
- Observability
- Disaster recovery
- Cost optimization
- Security baseline
- Multi-region design

For each system design, add:

- Deployment diagram
- Cloud service choices
- Cost estimate
- SLOs and SLAs
- Backup strategy
- Disaster recovery strategy
- Security model
- CI/CD pipeline
- Runtime monitoring

Important rule:

> Learn vendor-neutral principles first, then map them to AWS, Azure, or GCP services.

---

## Phase 6: Architecture Documentation

Main question:

> Can other people understand and execute your design?

Study:

- Documenting Software Architectures: Views and Beyond
- Software Architecture Metrics
- C4 model
- ADRs
- The Good Docs Project

Master these artifacts:

- C4 diagrams
- ADRs
- Architecture overview
- Sequence diagrams
- Context maps
- Threat model
- Non-functional requirements document
- Migration plan
- Decision log
- Risk register

Minimum architecture document template:

```text
1. Problem statement
2. Business goals
3. Constraints
4. Architecture characteristics
5. Current state
6. Proposed architecture
7. Key decisions
8. Trade-offs
9. Risks
10. Rollout plan
11. Observability
12. Security
13. Cost
```

---

## Phase 7: Legacy Modernization

Main question:

> Can you improve a messy system without rewriting everything?

Study:

- Working Effectively with Legacy Code
- Refactoring
- Your Code as a Crime Scene
- Building Evolutionary Architectures
- Architecture Modernization
- Monolith to Microservices

Practice on an existing project:

- Map current architecture
- Find hotspots
- Identify coupling
- Define target architecture
- Create migration slices
- Add observability
- Extract one capability
- Document ADRs

Key idea:

> Real architecture is often modernization under constraints, not perfect greenfield design.

---

## Phase 8: Leadership and Communication

Main question:

> Can you influence without just being the boss?

Study:

- The Software Architect Elevator
- Peopleware
- The Art of Agile Development
- Architecture decision-making resources

Practice:

- Present architecture in 10 minutes
- Explain trade-offs to non-technical people
- Run architecture review meetings
- Negotiate with product and business
- Mentor developers
- Write clear technical proposals
- Handle disagreement calmly

Mindset shift:

Senior developers often ask:

> What is the best design?

Architects ask:

> Best for which business goal, constraint, team, timeline, and risk?

---

## Weekly Grind Structure

Do this every week:

```text
Read: 3-5 chapters or equivalent articles
Design: 1 architecture problem
Write: 1 ADR or design doc
Review: 1 real system or company architecture
Discuss: explain your design to another engineer
Improve: revise based on feedback
```

---

## Monthly Themes

Use this as a loose 8-month path:

```text
Month 1: Architecture fundamentals
Month 2: Distributed systems
Month 3: DDD and boundaries
Month 4: APIs and integration
Month 5: Cloud architecture
Month 6: Legacy modernization
Month 7: Security, reliability, observability
Month 8: Architecture leadership
```

After 6-8 months, you should have a strong architecture portfolio.

---

## Recommended Reading Order

Do not read randomly. Use this order.

### Starter Stack

1. Fundamentals of Software Architecture
2. A Philosophy of Software Design
3. Designing Data-Intensive Applications
4. Learning Domain-Driven Design
5. Software Architecture: The Hard Parts

### Practical Architecture Stack

6. Building Microservices
7. Monolith to Microservices
8. Mastering API Architecture
9. Building Event-Driven Microservices
10. Building Evolutionary Architectures

### Professional Architect Stack

11. Software Architecture in Practice
12. Documenting Software Architectures
13. The Software Architect Elevator
14. Peopleware
15. Architecture Modernization

Important rule:

> Do not get trapped collecting books. Read, design, write, and review.

---

## Portfolio Projects

Create 4-6 public case studies. They can be GitHub repos, Notion pages, Markdown docs, or blog posts.

Good topics:

1. E-commerce platform architecture
2. Payment system architecture
3. Event-driven order processing
4. Monolith to microservices migration
5. Multi-tenant SaaS architecture
6. Real-time notification or chat system
7. Cloud deployment architecture
8. Legacy system modernization plan

Each case study should include:

- README
- Diagrams
- ADRs
- Trade-off matrix
- Failure scenarios
- Security considerations
- Cost considerations
- Migration plan

---

## Architecture Case Study Template

Use this for every project.

```md
# Project Name Architecture

## 1. Problem Statement

What problem are we solving?

## 2. Business Goals

- Goal 1
- Goal 2
- Goal 3

## 3. Requirements

### Functional Requirements

- Requirement 1
- Requirement 2

### Non-Functional Requirements

- Availability
- Scalability
- Security
- Maintainability
- Cost
- Observability

## 4. Constraints

- Timeline
- Team size
- Existing systems
- Budget
- Compliance

## 5. Current Architecture

Describe the current state.

## 6. Proposed Architecture

Describe the target state.

## 7. Diagrams

- Context diagram
- Container diagram
- Component diagram
- Sequence diagram
- Deployment diagram

## 8. Key Decisions

| Decision | Reason | Trade-off |
|---|---|---|
| Example decision | Why we chose it | What we give up |

## 9. Architecture Decision Records

Link ADRs here.

## 10. Data Design

- Main entities
- Ownership
- Consistency model
- Backup strategy

## 11. API and Integration Design

- APIs
- Events
- Contracts
- Versioning

## 12. Failure Scenarios

| Scenario | Impact | Mitigation |
|---|---|---|
| Database down | Service unavailable | Retry, fallback, alerting |

## 13. Security

- Authentication
- Authorization
- Secrets
- Threats
- Audit logs

## 14. Observability

- Logs
- Metrics
- Traces
- Alerts
- Dashboards

## 15. Cost Considerations

- Main cost drivers
- Optimization options

## 16. Migration Plan

1. Step one
2. Step two
3. Step three

## 17. Risks

| Risk | Probability | Impact | Mitigation |
|---|---|---|---|
| Example risk | Medium | High | Mitigation plan |

## 18. Open Questions

- Question 1
- Question 2
```

---

## ADR Template

```md
# ADR: Title

## Status

Proposed / Accepted / Deprecated / Superseded

## Context

What is the situation?

## Decision

What did we decide?

## Consequences

Positive:

- Benefit 1
- Benefit 2

Negative:

- Trade-off 1
- Trade-off 2

## Alternatives Considered

| Option | Pros | Cons |
|---|---|---|
| Option A | Pros | Cons |
| Option B | Pros | Cons |
```

---

## Signs You Are Becoming a Software Architect

You are ready when you can:

- Take vague requirements and ask good business questions
- Identify key architecture characteristics
- Choose between monolith, modular monolith, microservices, serverless, and event-driven designs
- Define service boundaries
- Choose data storage and integration patterns
- Explain trade-offs clearly
- Create useful diagrams
- Write ADRs
- Design for failure
- Estimate operational complexity
- Lead technical discussions
- Challenge requirements respectfully

---

## Main Path

```text
Fundamentals
-> Distributed Systems
-> DDD
-> Integration
-> Cloud
-> Documentation
-> Modernization
-> Leadership
```

---

## Main Rule

```text
For every 1 hour reading, spend 2 hours designing and writing.
```

That is how you become an architect, not just someone who has read architecture books.
