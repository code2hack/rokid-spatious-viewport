# Project Kernel

Status: **draft**  
Owner: **Boss + CEO Agent**  
Last updated: **2026-06-29**

## Goal

Build a useful, reproducible, agent-friendly Termux workflow for Rokid / Android-device experimentation.

The first validated outcome should be small: a developer can clone this repo, run a documented setup path, and verify one meaningful demo on the target environment.

## User / consumer

Primary users:

- Boss / maintainer who wants AI agents to develop and verify the project with minimal ambiguity.
- Local PM Agent / Codex session coordinating branches, worktrees, tests, and reviews.
- Future developers or users who want a reproducible Termux-based setup on Android/Rokid-related hardware.

## Value proposition

This project should reduce the friction between an idea and a verified device-side experiment.

Instead of scattered notes and manual commands, the repo should provide:

- A clear goal/spec/phase/job graph.
- Reproducible setup commands.
- Agent-readable job contracts.
- Verification scripts and review checklists.
- A path from discovery to a working demo.

## Goal hypothesis

`rokid-termux` may become one or more of:

1. A Termux bootstrap kit for Android / Rokid-related workflows.
2. A PM-agent runtime using `git worktree`, `tmux`, and local coding agents.
3. A documented research repo for Rokid + Termux constraints.
4. A device-side demo that proves the workflow is useful.

The first phase should decide which interpretation is correct.

## Non-goals

Until Phase P01 discovery finishes, this project should not:

- Require rooting a device.
- Assume a specific Rokid model without evidence.
- Assume a specific Android version without evidence.
- Build a large app before verifying the target environment.
- Introduce cloud services, credentials, or paid APIs as mandatory dependencies.
- Allow agents to perform broad, unscoped refactors.

## Constraints

- Prefer shell/Python scripts that work in constrained environments.
- Prefer no-root Android/Termux workflows unless Boss explicitly changes this.
- Keep each job branch narrow and reviewable.
- Every job must include acceptance criteria.
- Every product decision should be recorded in `decisions/`.
- PM Agent owns local execution state; CEO Agent owns product truth.

## Success criteria

Phase P00 succeeds when:

- This scaffold is committed to the repository.
- `python3 scripts/meta_validate.py` passes.
- The Boss can paste `.agents/prompts/CHATGPT_PROJECT_SEED.md` into a ChatGPT Project.
- The local Codex/PM session can consume `.agents/prompts/LOCAL_CODEX_PM_SEED.md`.

Phase P01 succeeds when:

- Target device and Termux environment constraints are documented.
- The project direction is clarified.
- The first useful demo is specified.
- Phase P02 jobs can be dispatched without guessing.

## First demo

Draft demo, pending P01:

> On the target Android/Termux environment, run a single command from this repo that prints a structured environment report and confirms the minimum package/runtime assumptions.

Possible command:

```bash
./scripts/device_probe.sh
```

`device_probe.sh` is not part of P00. It should be designed after discovery.

## Risks

| Risk | Mitigation |
|---|---|
| We build before understanding device constraints | P01 is discovery-only. |
| Agents edit unrelated files | One job contract, one branch, one worktree. |
| Termux/Rokid assumptions are wrong | Mark all product claims as hypotheses until verified. |
| Workflow overhead becomes heavier than project | Keep Phase P00 minimal and automate only repeated actions. |
| Reviews become vague | Use explicit acceptance criteria and review templates. |

## Current state

Repository initialized with MetaProject scaffold.

## Target state

A verified, documented, reproducible workflow for Rokid/Android/Termux experimentation, developed through phase-based agent coordination.
