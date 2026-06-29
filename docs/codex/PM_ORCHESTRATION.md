# PM Orchestration Guide

This file tells the PM/integrator Codex session how to start and how to assign worker sessions.

## 1. Entry prompt for the PM Codex session

Paste this into the PM Codex session after cloning/opening the repo:

```text
You are the PM/integrator agent for code2hack/rokid-spatious-viewport.

First read:
- AGENTS.md
- docs/codex/START_PROMPT.md
- docs/codex/PM_ORCHESTRATION.md
- docs/PROJECT_PLAN.md
- docs/WORK_BREAKDOWN.md
- docs/adr/0001-scope-spatial-viewport.md
- docs/adr/0002-selected-streaming-strategy.md
- docs/adr/0003-mediaprojection-boundaries.md

Your first job is not to build the full product.

First inspect the repository structure and current Android build state. Then report:
1. whether an Android Gradle project already exists,
2. current modules/packages/build commands,
3. whether the repo can build/test now,
4. what files/modules you propose to touch for Milestone A and Milestone B,
5. whether two worker sessions are useful now.

Then propose a small implementation plan for only:
- Milestone A: Android MediaProjection capture proof,
- minimum Milestone B: spatial viewport geometry + phone-side simulator.

Do not work on Rokid SDK, ASR, Bluetooth ring, Termux-specific logic, OCR, semantic app control, or AccessibilityService yet.

Keep the first implementation slice small. Prefer pure geometry code and a phone-side simulator before Rokid-specific work.
```

## 2. Current recommended agent count

Current phase:

```text
Minimum: 1 PM/integrator Codex session
Recommended: 1 PM + 2 worker sessions
Maximum: 1 PM + 3 worker sessions
```

Do not exceed two product workers until the capture + viewport simulator is working.

## 3. Worker assignment rules

The PM should only start worker sessions after repo inspection.

The PM should give each worker:

- the branch name,
- the exact worker prompt file to read,
- the allowed scope,
- the expected deliverable,
- the files/modules it should avoid,
- the command(s) to run for verification.

Workers should not share the same files unless the PM explicitly coordinates the merge order.

## 4. Worker 1 — MediaProjection capture

Branch:

```text
feat/mediaprojection-capture
```

Prompt file:

```text
docs/codex/workers/MEDIAPROJECTION_CAPTURE.md
```

Expected deliverable:

```text
A minimal Android companion-side MediaProjection capture proof that can start/stop user-approved capture and show captured frames in a debug view.
```

Do not assign viewport math or Rokid-side renderer to this worker unless the PM changes the plan.

## 5. Worker 2 — Spatial viewport core

Branch:

```text
feat/spatial-viewport-core
```

Prompt file:

```text
docs/codex/workers/SPATIAL_VIEWPORT_CORE.md
```

Expected deliverable:

```text
Pure spatial viewport geometry code with tests, plus a simple simulator path that can pan a fixed viewport over a synthetic/captured frame source.
```

Do not assign MediaProjection service work to this worker unless the PM changes the plan.

## 6. Optional worker 3 — Build/docs/test hygiene

Only use this worker if the repo needs setup cleanup before product work.

Possible branch:

```text
chore/build-and-docs-hygiene
```

Allowed tasks:

- document build commands,
- add basic CI skeleton,
- fix README entrypoints,
- add package/module notes,
- no product feature implementation.

## 7. Merge order recommendation

Preferred merge order:

1. Build/docs hygiene if needed.
2. Spatial viewport core geometry.
3. MediaProjection capture proof.
4. Integration of captured frames into viewport simulator.
5. Overscan cache prototype.
6. Rokid renderer skeleton.

Reason:

The geometry model should become the shared contract before capture integration and Rokid rendering depend on it.

## 8. Review checklist for PM

Before merging worker work, check:

- build/test command passes or failure is documented,
- scope did not expand into ASR/ring/Rokid/Accessibility prematurely,
- captured frames are not persisted by default,
- `FLAG_SECURE` boundaries are respected,
- geometry tests cover corners and padding,
- viewport reticle can point at all four content corners,
- code names match the current product scope, not old `rokid-termux` scope.

## 9. Stop conditions

Stop and ask the user before:

- changing repository name/package identity again,
- adding cloud/network streaming outside local/dev use,
- adding AccessibilityService app-control features,
- adding recording/screenshot persistence,
- starting Rokid SDK integration with unknown API assumptions,
- adding ASR or Bluetooth ring scope.
