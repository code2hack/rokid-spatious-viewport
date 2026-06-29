# Product Specification

Status: **draft / pre-discovery**  
Product name: **rokid-termux**  
Workflow owner: **CEO Agent**  
Execution owner: **PM Agent**

## Product thesis

`rokid-termux` should make device-side experimentation easier by combining:

- Termux as the local command-line environment.
- GitHub as the transition ledger.
- Git worktrees as isolated job execution spaces.
- Tmux as the local multi-agent console.
- MetaProject documents as durable project memory.

## Problem

Developing experimental workflows across Android, Termux, Rokid hardware/software, and AI coding agents can easily become fragmented.

Common failure modes:

- Setup steps are not reproducible.
- Device assumptions are hidden in chat history.
- Agents modify unrelated files.
- Reviews focus on whether code exists, not whether the user goal improved.
- There is no stable place to store product truth and execution truth.

## Target users

### Boss / maintainer

Needs a lightweight control plane for turning goals into verified branches.

### PM Agent

Needs unambiguous job contracts, branch names, worktree paths, review checklists, and state transitions.

### Developer sub-agent

Needs a small task with clear scope, allowed files, tests, and required report.

### Future technical user

Needs setup docs, scripts, troubleshooting notes, and a demo.

## Core objects

| Object | Meaning |
|---|---|
| Goal | Desired world state. |
| Feature | User-visible or project-visible capability. |
| Phase | Demonstrable increment. |
| Job | Scoped, reviewable state transition. |
| Branch | Isolated implementation attempt. |
| Worktree | Local filesystem workspace for one branch. |
| PR | Proposed state transition. |
| Review | Verification gate. |
| Demo | Human-verifiable proof. |

## MVP definition

The first MVP is not a polished app. It is a verified workflow:

1. Clear project goal.
2. Verified target environment report.
3. Reproducible setup script.
4. Minimal demo.
5. Agent workflow that can produce and review changes safely.

## Candidate capabilities

### C001 — Environment discovery

Collect and document:

- Android version.
- Termux source and version.
- CPU architecture.
- Available package manager state.
- Storage permissions.
- Shell and Python availability.
- Git/tmux availability.
- Rokid-specific device/app constraints, if applicable.

### C002 — Termux bootstrap

A single setup path for required packages and shell environment.

### C003 — Agent PM runtime

Scripts and docs for:

- Creating one branch per job.
- Creating one worktree per branch.
- Launching one tmux window/session per job.
- Capturing completion reports.
- Running validation.

### C004 — Device probe

A non-destructive script that reports whether the environment is ready.

### C005 — First demo

A tiny, useful capability that runs on the target environment and proves the workflow.

## Out of scope before P01 completion

- Heavy Android app development.
- Hardware-specific assumptions not verified on the target device.
- Credential-dependent cloud integrations.
- Root-only workflows.
- Complex CI/CD beyond metadata validation.
- Broad automated merging.

## Verification strategy

A change is accepted only when it passes the appropriate level:

1. Local script/test validation.
2. PM Agent diff and scope review.
3. CEO Agent product-coherence review.
4. Boss/User verification for visible behavior.

## Open questions

| ID | Question | Owner | Target phase |
|---|---|---|---|
| Q001 | What exact Rokid device/model/app environment is targeted? | Boss + P01 discovery agent | P01 |
| Q002 | Is Termux running directly on a phone, on a Rokid computing unit, or as part of a companion-device workflow? | Boss + P01 discovery agent | P01 |
| Q003 | Should the project output be scripts, docs, an Android app, or an agent runtime? | CEO Agent | P01 |
| Q004 | What is the smallest demo that feels useful to Boss? | Boss + CEO Agent | P01 |
| Q005 | What local model/agent tooling will the PM session actually use? | PM Agent | P01 |
