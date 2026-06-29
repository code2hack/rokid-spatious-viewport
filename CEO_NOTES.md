# CEO Notes

Status: **active**

## 2026-06-29 — Scaffold initialization

Repository target: `code2hack/rokid-termux`

Initial condition: empty repository.

Decision: initialize a lightweight MetaProject scaffold before any product implementation.

## Product truth

Current goal is a hypothesis:

> Build a useful, reproducible, agent-friendly Termux workflow for Rokid / Android-device experimentation.

This must be validated in P01.

## Immediate CEO responsibilities

1. Review `PROJECT_KERNEL.md`.
2. Confirm or rewrite the goal hypothesis.
3. Review P01 discovery jobs.
4. After P01, update:
   - `PROJECT_KERNEL.md`
   - `PRODUCT_SPEC.md`
   - `FEATURE_GRAPH.yaml`
   - `PHASE_PLAN.md`
   - `BRANCH_MANIFEST.yaml`

## Initial product risks

- The exact target Rokid environment is unknown.
- It is unclear whether Termux runs directly on the target device or on a companion Android phone.
- It is unclear whether the project should produce scripts, docs, a local agent runtime, or an app.
- Building before discovery may waste work.

## CEO review focus for P01

- Does each discovery report separate facts from assumptions?
- Are device-specific claims verified?
- Are implementation recommendations practical?
- Is the first demo small enough?
- Can P02 jobs be dispatched without ambiguity?
