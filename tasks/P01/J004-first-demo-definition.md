---
id: P01-J004
phase: P01
title: First demo definition
branch: job/P01-J004-first-demo-definition
status: blocked
feature: F004
depends_on:
  - P01-J001
  - P01-J002
owner: developer-sub-agent
---

## Job ID

P01-J004

## Branch

`job/P01-J004-first-demo-definition`

## Objective

Define the smallest useful demo for the project.

## Background

The first demo must be small enough to build in P02/P03 and meaningful enough for Boss/User verification.

## Scope In

- Read discovery reports.
- Propose 2–3 demo candidates.
- Compare usefulness, risk, and verification cost.
- Recommend one first demo.
- Write manual verification steps.
- Propose P02/P03 jobs.

## Scope Out

- Do not implement the demo.
- Do not require unverified hardware capabilities.
- Do not require credentials unless Boss explicitly approves.
- Do not over-optimize for polish.

## Allowed Files / Areas

- `docs/design/**`
- `reviews/P01/**`
- `PRODUCT_SPEC.md`
- `FEATURE_GRAPH.yaml`
- `PHASE_PLAN.md`

## Blocked Files / Areas

- Demo implementation directories unless creating documentation only.

## Dependencies

- P01-J001
- P01-J002

## Acceptance Criteria

- [ ] `docs/design/first-demo.md` exists.
- [ ] At least two alternatives are compared.
- [ ] One demo is recommended.
- [ ] Manual verification steps are written.
- [ ] P02/P03 job candidates are listed.
- [ ] Boss/User acceptance criteria are explicit.

## Validation Commands

```bash
python3 scripts/meta_validate.py
```

## Required Output

- `docs/design/first-demo.md`
- `reviews/P01/J004-self-report.md`

## Completion Report

Write:

```text
reviews/P01/J004-self-report.md
```

## Status

blocked
