# ADR-0001: Use Goal → Graph → Phase → Branch → Verify

Status: **accepted**  
Date: **2026-06-29**

## Context

The project is being used to test a naive but practical AI-agent workflow.

The core idea is that a project starts from a goal and proceeds through structured state transitions.

## Decision

Use the workflow:

```text
Goal → Graph → Phase → Branch → Verify
```

Definitions:

- Goal: desired world state.
- Graph: feature/task/dependency representation.
- Phase: demonstrable increment.
- Branch: isolated implementation attempt for one job.
- Verify: acceptance criteria, tests, reviews, and Boss/User judgment.

## Consequences

Positive:

- Reduces ambiguity for agents.
- Makes state transitions traceable.
- Separates product truth from execution truth.
- Encourages small reviewable branches.

Negative:

- Adds documentation overhead.
- Requires PM discipline.
- May be too heavy for tiny changes.

## Mitigation

Keep the process lightweight and automate only repeated actions after the manual workflow is proven.
