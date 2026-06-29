# PM Status

Status owner: **PM Agent**  
Last updated: **2026-06-29**

## Repository

| Field | Value |
|---|---|
| Repo | `code2hack/rokid-termux` |
| Default branch | `main` |
| Current phase | P00 |
| Current state | scaffold package prepared |
| Next action | apply scaffold, validate, commit, push |

## Phase status

| Phase | Name | Status | Notes |
|---|---|---|---|
| P00 | MetaProject scaffold | ready_to_commit | Apply scaffold and push initial commit. |
| P01 | Discovery and first-demo definition | planned | Dispatch after P00 is on `main`. |
| P02 | Bootstrap and probe | candidate | Depends on P01. |
| P03 | First useful demo | candidate | Depends on P02 and Boss acceptance. |

## Job status

| Job | Title | Branch | Status | Owner | Review |
|---|---|---|---|---|---|
| P00-J001 | Project kernel and product spec | `job/P00-J001-project-kernel` | scaffolded | CEO | n/a |
| P00-J002 | Agent protocol and prompts | `job/P00-J002-agent-protocol` | scaffolded | CEO | n/a |
| P00-J003 | GitHub workflow templates | `job/P00-J003-github-workflow` | scaffolded | CEO | n/a |
| P00-J004 | Repository validation | `job/P00-J004-repo-validation` | scaffolded | CEO | n/a |
| P01-J001 | Termux environment discovery | `job/P01-J001-termux-environment-discovery` | ready_for_dispatch | PM | pending |
| P01-J002 | Rokid capability discovery | `job/P01-J002-rokid-capability-discovery` | ready_for_dispatch | PM | pending |
| P01-J003 | Bootstrap design | `job/P01-J003-bootstrap-design` | blocked | PM | pending |
| P01-J004 | First demo definition | `job/P01-J004-first-demo-definition` | blocked | PM | pending |

## PM next commands

```bash
python3 scripts/meta_validate.py

# After scaffold is pushed to main:
git switch -c phase/P01-discovery
git push -u origin phase/P01-discovery

# Create job worktrees from P01 contracts:
scripts/pm_dispatch_phase.sh P01 origin/phase/P01-discovery
```
