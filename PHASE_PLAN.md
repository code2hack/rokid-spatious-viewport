# Phase Plan

Status: **draft**  
Last updated: **2026-06-29**

## Phase philosophy

A phase is not a batch of chores. A phase is a demonstrable state transition.

Each phase must have:

- A phase goal.
- Entry criteria.
- Exit criteria.
- Included features.
- Excluded features.
- Job contracts.
- Verification plan.
- Review packet.

## P00 — MetaProject scaffold

Status: **ready to commit**

### Goal

Initialize durable project memory and the naive CEO/PM/sub-agent workflow.

### Included features

- F000 MetaProject scaffold.

### Jobs

| Job | Title | Branch | Status |
|---|---|---|---|
| P00-J001 | Project kernel and product spec | `job/P00-J001-project-kernel` | scaffolded |
| P00-J002 | Agent protocol and prompts | `job/P00-J002-agent-protocol` | scaffolded |
| P00-J003 | GitHub workflow templates | `job/P00-J003-github-workflow` | scaffolded |
| P00-J004 | Repository validation | `job/P00-J004-repo-validation` | scaffolded |

### Exit criteria

- Scaffold files exist.
- Validation passes.
- Initial commit is pushed to `main`.
- Boss has a ChatGPT Project seed prompt and local Codex PM seed prompt.

## P01 — Discovery and first-demo definition

Status: **planned**

### Goal

Turn the project goal hypothesis into a verified direction.

### Entry criteria

- P00 merged to `main`.
- PM Agent has local clone.
- Boss has created ChatGPT Project or equivalent CEO context.

### Included features

- F001 Termux environment discovery.
- F002 Rokid capability discovery.
- F003 Bootstrap design.
- F004 First demo definition.

### Jobs

| Job | Title | Branch | Depends on |
|---|---|---|---|
| P01-J001 | Termux environment discovery | `job/P01-J001-termux-environment-discovery` | P00 |
| P01-J002 | Rokid capability discovery | `job/P01-J002-rokid-capability-discovery` | P00 |
| P01-J003 | Bootstrap design | `job/P01-J003-bootstrap-design` | P01-J001, P01-J002 |
| P01-J004 | First demo definition | `job/P01-J004-first-demo-definition` | P01-J001, P01-J002 |

### Verification

- Discovery reports are written.
- Unknowns are explicit.
- No large implementation is added.
- CEO Agent updates `PROJECT_KERNEL.md`, `PRODUCT_SPEC.md`, `FEATURE_GRAPH.yaml`, and `PHASE_PLAN.md` if discovery changes the direction.
- Boss approves the first demo definition.

### Exit criteria

- Target environment is described.
- Product direction is clarified.
- First demo is specified.
- P02 jobs can be created without guessing.

## P02 — Bootstrap and probe

Status: **candidate**

### Goal

Implement the safe setup/probe foundation.

### Candidate features

- F005 Termux bootstrap implementation.
- F006 PM agent local runtime.
- F007 Device probe.

### Exit criteria

- User can run a documented setup path.
- User can run a non-destructive device probe.
- PM Agent can dispatch branches/worktrees consistently.

## P03 — First useful demo

Status: **candidate**

### Goal

Deliver the smallest useful behavior on the target environment.

### Candidate features

- F008 First useful demo.

### Exit criteria

- Demo runs in the target environment.
- Demo has manual verification steps.
- Boss verifies the demo.
- P04 direction is replanned from actual feedback.

## P04+ — Product expansion

Status: **unplanned**

Possible directions after P03:

- Better device integration.
- More complete agent runtime.
- Packaging and distribution.
- Documentation site.
- Automation around GitHub issues/PRs.
- Rokid-specific app/API integration, if discovery supports it.
