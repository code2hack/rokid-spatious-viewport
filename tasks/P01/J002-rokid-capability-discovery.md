---
id: P01-J002
phase: P01
title: Rokid capability discovery
branch: job/P01-J002-rokid-capability-discovery
status: ready_for_dispatch
feature: F002
depends_on: []
owner: developer-sub-agent
---

## Job ID

P01-J002

## Branch

`job/P01-J002-rokid-capability-discovery`

## Objective

Discover and document the Rokid-side target, constraints, and plausible integration paths.

## Background

The repo name implies Rokid-specific intent, but the exact target device/model/app environment is unknown. This job should identify what must be clarified before implementation.

## Scope In

- List information needed from Boss about target device and usage.
- Research high-level Rokid developer resources.
- Document possible integration paths.
- Document blockers and unknowns.
- Recommend next questions and a conservative first-demo path.

## Scope Out

- Do not implement an Android app.
- Do not use private SDK credentials.
- Do not claim device compatibility without verification.
- Do not reverse engineer proprietary components.
- Do not require root.

## Allowed Files / Areas

- `docs/discovery/**`
- `tasks/P01/J002-rokid-capability-discovery.md`
- `reviews/P01/**`
- `PRODUCT_SPEC.md` only if adding clearly marked discovery notes.
- `FEATURE_GRAPH.yaml` only if updating status with PM approval.

## Blocked Files / Areas

- `.github/**`
- `scripts/bootstrap*`
- App source directories, if later added.

## Dependencies

- P00 scaffold.

## Acceptance Criteria

- [ ] `docs/discovery/rokid-capabilities.md` exists.
- [ ] Report separates facts, assumptions, and questions.
- [ ] Target device/model/app unknowns are explicit.
- [ ] At least two possible project directions are compared.
- [ ] Recommended first-demo path is conservative and testable.
- [ ] No proprietary or credential-dependent implementation is added.

## Validation Commands

```bash
python3 scripts/meta_validate.py
```

## Required Output

- `docs/discovery/rokid-capabilities.md`
- `reviews/P01/J002-self-report.md`

## Completion Report

Write:

```text
reviews/P01/J002-self-report.md
```

## Status

ready_for_dispatch
