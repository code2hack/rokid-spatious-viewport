---
id: P01-J003
phase: P01
title: Bootstrap design
branch: job/P01-J003-bootstrap-design
status: blocked
feature: F003
depends_on:
  - P01-J001
  - P01-J002
owner: developer-sub-agent
---

## Job ID

P01-J003

## Branch

`job/P01-J003-bootstrap-design`

## Objective

Design the future bootstrap/setup architecture after Termux and Rokid discovery reports exist.

## Background

This job should not start until P01-J001 and P01-J002 are reviewed.

## Scope In

- Read discovery reports.
- Propose bootstrap script responsibilities.
- Define safety boundaries.
- Define package list and optional packages.
- Define config/report output format.
- Identify validation strategy.

## Scope Out

- Do not implement the full bootstrap.
- Do not install packages on target device.
- Do not require root.
- Do not use credentials.

## Allowed Files / Areas

- `docs/design/**`
- `reviews/P01/**`
- `PRODUCT_SPEC.md`
- `FEATURE_GRAPH.yaml`
- `PHASE_PLAN.md`

## Blocked Files / Areas

- `scripts/bootstrap*` unless creating a design-only placeholder with PM approval.

## Dependencies

- P01-J001
- P01-J002

## Acceptance Criteria

- [ ] `docs/design/bootstrap-design.md` exists.
- [ ] Design references discovery reports.
- [ ] Safety model is explicit.
- [ ] Proposed commands are separated from final implementation.
- [ ] P02 implementation jobs are proposed.

## Validation Commands

```bash
python3 scripts/meta_validate.py
```

## Required Output

- `docs/design/bootstrap-design.md`
- `reviews/P01/J003-self-report.md`

## Completion Report

Write:

```text
reviews/P01/J003-self-report.md
```

## Status

blocked
