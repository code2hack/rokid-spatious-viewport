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
- docs/codex/NEXT_IMPLEMENTATION_DECISIONS.md
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
4. which stale root/meta docs still mention old rokid-termux framing,
5. what files/modules you propose to touch for docs cleanup, Android skeleton, viewport core, and MediaProjection later,
6. whether worker sessions are useful now.

Proceed in this exact implementation order:
1. Clean root/meta docs to match the spatial viewport pivot.
2. Create Kotlin Android project skeleton.
3. Add pure viewport geometry module/tests first.
4. Add MediaProjection capture proof after the Android skeleton and viewport-core exist.

Do not work on Rokid SDK, ASR, Bluetooth ring, Termux-specific logic, OCR, semantic app control, or AccessibilityService yet.

Keep the first implementation slice small. Prefer pure geometry code and a phone-side simulator before Rokid-specific work.
```

## 2. Current recommended agent count

Current phase:

```text
Minimum: 1 PM/integrator Codex session
Recommended: 1 PM + 2 worker sessions after skeleton exists
Maximum: 1 PM + 3 worker sessions
```

Do not exceed two product workers until the capture + viewport simulator is working.

## 3. Worker assignment rules

The PM should only start worker sessions after repo inspection and after deciding whether the Android skeleton exists.

The PM should give each worker:

- the branch name,
- the exact worker prompt file to read,
- the allowed scope,
- the expected deliverable,
- the files/modules it should avoid,
- the command(s) to run for verification.

Workers should not share the same files unless the PM explicitly coordinates the merge order.

## 4. Work item 0 — root/meta docs cleanup

Branch:

```text
docs/spatial-viewport-pivot-cleanup
```

Expected deliverable:

```text
Root/meta docs consistently describe Rokid Spatious Viewport as a head-tracked spatial viewport for mirrored Android app/display surfaces.
```

The PM may do this directly before starting workers.

## 5. Work item 1 — Kotlin Android project skeleton

Branch:

```text
chore/android-kotlin-skeleton
```

Expected deliverable:

```text
A minimal Kotlin Android Gradle project with a simple app entry/debug screen and documented build command.
```

Do not implement MediaProjection in this work item.

## 6. Worker 1 — Spatial viewport core

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

## 7. Worker 2 — MediaProjection capture

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

Do not assign this worker until the Kotlin Android skeleton exists. Prefer waiting until viewport-core exists.

## 8. Optional worker 3 — Build/docs/test hygiene

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

## 9. Merge order recommendation

Preferred merge order:

1. Root/meta docs cleanup.
2. Kotlin Android project skeleton.
3. Spatial viewport core geometry/tests.
4. MediaProjection capture proof.
5. Integration of captured frames into viewport simulator.
6. Overscan cache prototype.
7. Rokid renderer skeleton.

Reason:

The Android skeleton and geometry model should become the shared contract before capture integration and Rokid rendering depend on it.

## 10. Review checklist for PM

Before merging worker work, check:

- build/test command passes or failure is documented,
- stale `rokid-termux` scope is removed or demoted to future-use-case language,
- Android implementation uses Kotlin, not Java,
- scope did not expand into ASR/ring/Rokid/Accessibility prematurely,
- captured frames are not persisted by default,
- `FLAG_SECURE` boundaries are respected,
- geometry tests cover corners and padding,
- viewport reticle can point at all four content corners,
- code names match the current product scope, not old `rokid-termux` scope.

## 11. Stop conditions

Stop and ask the user before:

- changing repository name/package identity again,
- adding cloud/network streaming outside local/dev use,
- adding AccessibilityService app-control features,
- adding recording/screenshot persistence,
- starting Rokid SDK integration with unknown API assumptions,
- adding ASR or Bluetooth ring scope.
