# Definition of Done

Status: **active from P00**

## Universal rule

A task is not done because an agent says it is done. A task is done only when its verifier can confirm the acceptance criteria.

## Job done

A job is done when all are true:

- Job contract exists in `tasks/Pxx/Jxxx-*.md`.
- Job has exactly one branch.
- Job branch is based on the correct phase or main branch.
- Implementation stays within declared scope or explicitly explains deviations.
- Required outputs exist.
- Acceptance criteria are checked.
- Validation commands are run or explicitly marked not applicable.
- Completion report is written by the developer sub-agent.
- PM review is written.
- No secrets, credentials, or private device data are committed.

## PR done

A PR is done when all are true:

- PR title includes job or phase ID.
- PR body references task contract.
- CI/checks pass or failures are explicitly waived by Boss/CEO.
- PM review passes.
- CEO review passes where required.
- Boss/User review passes for visible product behavior.
- Merge target is correct.

## Phase done

A phase is done when all are true:

- All included jobs are merged, postponed, or abandoned with reasons.
- Integrated state passes validation.
- Phase review is written in `reviews/Pxx/phase-review.md`.
- `FEATURE_GRAPH.yaml` and `PHASE_PLAN.md` are updated.
- `PM_STATUS.md` is updated.
- Boss accepts the phase or redirects the next phase.

## Release done

A release is done when all are true:

- User-facing documentation is current.
- Installation/setup path is verified.
- Demo or core workflow is verified from a clean environment where practical.
- Known limitations are documented.
