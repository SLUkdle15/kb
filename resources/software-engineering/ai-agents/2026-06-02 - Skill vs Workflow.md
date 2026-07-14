# Skill vs Workflow

## Core Idea

Agent = runtime or worker that performs tasks.

Tool = callable function, API, script, or external capability.

Skill = reusable playbook, module, or runbook for a bounded capability, including instructions, rules, examples, and tool-usage guidance.

Workflow = end-to-end orchestration from user intent to completed outcome.

Plugin = installable package that can add tools, skills, integrations, or runtime capabilities.

## Skill vs workflow

A skill can contain workflow-like steps and often should. However, those steps should describe how to perform the skill's bounded capability, not necessarily the whole business workflow.

Example:

- A `read-id-card` skill contains the mini-workflow: check image -> OCR -> extract fields -> validate -> confirm -> return structured data.
- An insurance-claim workflow uses `read-id-card`, receipt-extraction, claim-validation, and submission skills.

Breaking a workflow into multiple skills improves reuse, testing, ownership, and debugging. You can still evaluate the whole workflow end-to-end while also evaluating each skill separately.

## When orchestration becomes a workflow

Use a workflow when orchestration needs:

- Branching
- Retries
- Approvals
- State tracking
- Step-level logging
- Permissions
- Human review
- Timeout handling
- Evaluation per step
- Conditional routing
- Integration with backend APIs
