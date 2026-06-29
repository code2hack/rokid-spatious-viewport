# ADR-0002: Use one branch and one worktree per job

Status: **accepted**  
Date: **2026-06-29**

## Context

Multiple AI sub-agents may work in parallel. Without isolation, they can overwrite work, change unrelated files, or produce hard-to-review diffs.

## Decision

Each job gets:

- One job contract.
- One Git branch.
- One local worktree.
- One sub-agent session.
- One completion report.
- One PM review.

## Branch naming

```text
job/Pxx-Jxxx-short-name
```

Example:

```text
job/P01-J001-termux-environment-discovery
```

## Worktree naming

Default:

```text
../worktrees/job-P01-J001-termux-environment-discovery
```

## Consequences

Positive:

- Clear ownership.
- Easier review.
- Easier reset/abandon.
- Parallelism without shared working tree conflicts.

Negative:

- More branches.
- More local directories.
- PM Agent must coordinate dependencies.

## Mitigation

Use phase branches for integration and keep jobs small.
