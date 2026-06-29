# rokid-termux

Status: **MetaProject scaffold initialized**  
Date: **2026-06-29**  
Workflow: **Goal → Graph → Phase → Branch → Verify**

This repository is managed as a MetaProject experiment: each meaningful change should trace from a goal, to a feature, to a phase, to a job contract, to a Git branch, to verification.

## Current goal hypothesis

Build a reproducible Termux-based development and agent workflow for Rokid / Android-device experimentation.

This is intentionally a hypothesis, not final product truth. The Boss should refine it after the first discovery phase.

## Project control files

| File | Purpose |
|---|---|
| `PROJECT_KERNEL.md` | Smallest durable statement of goal, users, constraints, non-goals, and success criteria. |
| `PRODUCT_SPEC.md` | Draft product specification and feature boundaries. |
| `FEATURE_GRAPH.yaml` | Canonical feature graph. |
| `PHASE_PLAN.md` | Phase-by-phase execution plan. |
| `BRANCH_MANIFEST.yaml` | Branch/job manifest consumed by PM Agent. |
| `AGENT_PROTOCOL.md` | Role boundaries and handoff protocol. |
| `DEFINITION_OF_DONE.md` | Verification gates for jobs, phases, and releases. |

## First phase

P01 is a discovery phase:

1. Verify Termux fork/build/runtime constraints.
2. Verify Rokid AI Glasses development/display/input constraints.
3. Decide whether the first demo should be native Android, Termux-based, browser-based, or hybrid.
4. Produce a first demo definition before heavy implementation.

## Local PM start

After cloning:

```bash
python3 scripts/meta_validate.py
scripts/pm_dispatch_phase.sh P01 origin/phase/P01-discovery
```

See `.agents/prompts/LOCAL_CODEX_PM_SEED.md` for the PM session seed.
