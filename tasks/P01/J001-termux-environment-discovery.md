---
id: P01-J001
phase: P01
title: Termux environment discovery
branch: job/P01-J001-termux-environment-discovery
status: ready_for_dispatch
feature: F001
depends_on: []
owner: developer-sub-agent
---

## Job ID

P01-J001

## Branch

`job/P01-J001-termux-environment-discovery`

## Objective

Discover and document the target Termux environment and constraints.

## Background

The project goal depends on what Termux can actually provide on the target Android/Rokid-related setup. This job should gather facts and avoid implementation.

## Scope In

- Research Termux installation/source/version assumptions.
- Document expected commands to gather local environment data.
- Create a discovery report template.
- Propose the future `device_probe.sh` fields.

## Scope Out

- Do not implement full bootstrap script.
- Do not install packages on Boss device unless explicitly asked by Boss/PM.
- Do not assume root.
- Do not change product direction.

## Allowed Files / Areas

- `docs/discovery/**`
- `tasks/P01/J001-termux-environment-discovery.md`
- `reviews/P01/**`
- `PRODUCT_SPEC.md` only if adding clearly marked discovery notes.
- `FEATURE_GRAPH.yaml` only if updating status with PM approval.

## Blocked Files / Areas

- `.github/**`
- `scripts/bootstrap*`
- Android app source directories, if later added.

## Dependencies

- P00 scaffold.

## Acceptance Criteria

- [ ] `docs/discovery/termux-environment.md` exists.
- [ ] Report separates facts, assumptions, and questions.
- [ ] Report includes commands the Boss/PM can run locally.
- [ ] Report identifies minimum packages likely needed.
- [ ] Report proposes fields for a future non-destructive device probe.
- [ ] No implementation-heavy bootstrap is added.

## Validation Commands

```bash
python3 scripts/meta_validate.py
```

## Required Output

- `docs/discovery/termux-environment.md`
- `reviews/P01/J001-self-report.md`

## Completion Report

Write:

```text
reviews/P01/J001-self-report.md
```

## Status

ready_for_dispatch
