# Workflow

This project uses:

```text
Goal → Graph → Phase → Branch → Verify
```

## Goal

The desired world state. Stored in `PROJECT_KERNEL.md`.

## Graph

The feature and dependency graph. Stored in `FEATURE_GRAPH.yaml`.

## Phase

A demonstrable product increment. Stored in `PHASE_PLAN.md`.

## Branch

One isolated implementation attempt for one job. Stored in Git and listed in `BRANCH_MANIFEST.yaml`.

## Verify

Tests, validation, reviews, demos, and Boss/User feedback. Stored in `reviews/`.

## Normal loop

```text
Boss/User goal
  → CEO Agent spec/phase/jobs
  → PM Agent branches/worktrees
  → Developer sub-agents execute
  → PM review
  → CEO review
  → Boss/User verification
  → merge/replan
```

## Rules of thumb

- Prefer smaller jobs.
- Prefer explicit dependencies.
- Keep discovery separate from implementation.
- Every job needs acceptance criteria.
- Every branch needs a job contract.
- Every phase needs a phase review.
