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
| `AGENT_PROTOCOL.md` | Rules for CEO Agent, PM Agent, developer sub-agents, and reviewers. |
| `DEFINITION_OF_DONE.md` | Verification gates for jobs, PRs, phases, and releases. |
| `PM_STATUS.md` | Execution-state dashboard. |
| `CEO_NOTES.md` | Product-state and planning notes. |

## First execution path

1. Finish Phase P00 by committing this scaffold.
2. Start Phase P01 discovery.
3. Use one branch per job.
4. Let the PM Agent create one worktree per job.
5. Let each sub-agent work inside exactly one worktree.
6. PM Agent reviews each job.
7. CEO Agent reviews product coherence.
8. Boss verifies usefulness.
9. Merge only verified work.

## Phase P01 preview

Phase P01 should discover what this project actually needs before building too much:

- Termux installation and runtime constraints.
- Rokid device / platform constraints.
- Whether the product should be a bootstrap script, an agent runtime, a device app, a workflow guide, or a hybrid.
- The smallest useful demo.

## Local validation

```bash
python3 scripts/meta_validate.py
```

## PM bootstrap

```bash
scripts/pm_dispatch_phase.sh P01 origin/main
```

This reads `tasks/P01/J*.md`, extracts job branches, and creates Git worktrees under `../worktrees` by default.
