# Status Model

## Job statuses

| Status | Meaning |
|---|---|
| draft | Job is being written. |
| ready_for_dispatch | PM can assign it. |
| dispatched | PM created branch/worktree/session. |
| in_progress | Sub-agent is working. |
| self_reported_done | Sub-agent claims done and wrote report. |
| pm_review | PM is reviewing. |
| pm_failed | PM rejected it. |
| ceo_review | CEO is reviewing. |
| ceo_failed | CEO rejected it. |
| user_review | Boss/User review required. |
| approved | Job passed required review. |
| merged | Job branch merged. |
| postponed | Valid job, not now. |
| abandoned | Job should not continue. |
| blocked | Waiting on dependencies. |
| scaffolded | Pre-created as part of initial scaffold. |

## Phase statuses

| Status | Meaning |
|---|---|
| planned | Phase exists but is not active. |
| dispatching | PM is assigning jobs. |
| in_progress | Jobs are active. |
| integration | Job branches are being combined. |
| human_review | Boss/User review needed. |
| complete | Phase exit criteria passed. |
| replanned | Phase changed based on review. |
| cancelled | Phase will not continue. |
| ready_to_commit | Initial scaffold phase only. |
| candidate | Possible future phase. |
