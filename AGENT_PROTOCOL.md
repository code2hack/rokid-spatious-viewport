# Agent Protocol

Status: **active from P00**

## Core law

Every artifact must trace back to a goal, and every goal must have a verification path.

```text
Goal → Feature → Phase → Job → Branch → Worktree → PR → Review → Merge → Demo → Feedback
```

## Roles

### Boss

Owns:

- Project taste.
- Final goal.
- Final acceptance.
- Priority changes.

Does not need to:

- Micromanage every implementation detail.
- Review every low-level diff if PM/CEO review is sufficient.

### CEO Agent

Owns product truth:

- `PROJECT_KERNEL.md`
- `PRODUCT_SPEC.md`
- `FEATURE_GRAPH.yaml`
- `PHASE_PLAN.md`
- Phase/job planning.
- CEO review.
- Human verification packet.

CEO Agent should not perform broad implementation unless acting explicitly as a developer for a scoped job.

### PM Agent

Owns execution truth:

- Branch/worktree/session mapping.
- Local dispatch.
- Running validation.
- PM reviews.
- Updating `PM_STATUS.md`.
- Preparing PRs/issues.

PM Agent should not change product direction without CEO/Boss approval.

### Developer sub-agent

Owns one job:

- Reads one job contract.
- Works in one branch/worktree.
- Produces required output.
- Runs required checks.
- Writes a completion report.

Developer sub-agent should not:

- Change unrelated files.
- Rewrite the plan.
- Create hidden dependencies.
- Modify secrets or credentials.

### Reviewer

Owns verification:

- Checks scope.
- Checks acceptance criteria.
- Checks tests/validation.
- Identifies risk.
- Provides pass/fail with reasons.

## Branch policy

- Initial scaffold may be pushed to `main` because the repository started empty.
- After P00, do not push directly to `main`.
- Use one job branch per job.
- Use one worktree per job branch.
- Use phase branches when multiple jobs need integration before main.
- Keep job branches small.

Naming:

```text
phase/P01-discovery
job/P01-J001-termux-environment-discovery
job/P01-J002-rokid-capability-discovery
```

## Worktree policy

Default local layout:

```text
repo/
../worktrees/
  job-P01-J001-termux-environment-discovery/
  job-P01-J002-rokid-capability-discovery/
```

A worktree maps to exactly one job branch.

## Job lifecycle

```text
draft
ready_for_dispatch
dispatched
in_progress
self_reported_done
pm_review
pm_failed
ceo_review
ceo_failed
user_review
approved
merged
postponed
abandoned
```

## Phase lifecycle

```text
planned
dispatching
in_progress
integration
human_review
complete
replanned
cancelled
```

## Review gates

### Sub-agent self-check

Question: Did I complete the assigned contract?

Required output:

```text
reviews/Pxx/Jxxx-self-report.md
```

### PM review

Question: Is the implementation mechanically correct, scoped, and testable?

Required output:

```text
reviews/Pxx/Jxxx-pm-review.md
```

### CEO review

Question: Does this preserve product coherence and move toward the goal?

Required output:

```text
reviews/Pxx/Jxxx-ceo-review.md
```

### Boss/User verification

Question: Is this actually useful/right?

Required output:

```text
reviews/Pxx/Jxxx-user-verification.md
```

## Conflict handling

When jobs conflict:

1. Do not silently merge.
2. Identify whether the conflict is file-level, semantic, dependency, test, or architecture overlap.
3. Create an integration/fix job.
4. Update `BRANCH_MANIFEST.yaml`.
5. Record a decision if architecture changed.

## Scope deviation rule

A sub-agent may deviate from allowed scope only if:

- The deviation is required to pass acceptance criteria.
- The deviation is documented in the completion report.
- PM Agent approves during review.

## Communication format

Completion reports should include:

```markdown
## Summary
## Files changed
## Acceptance criteria result
## Validation commands run
## Risks
## Follow-up recommendations
```

Review reports should include:

```markdown
## Verdict
pass / fail / needs-human
## Scope check
## Validation check
## Product/architecture check
## Required fixes
## Notes for CEO/Boss
```
