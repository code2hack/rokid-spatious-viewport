# Phase Plan

Status: **spatial viewport pivot accepted**  
Last updated: **2026-06-30**

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

Status: **completed / superseded by spatial viewport pivot**

### Goal

Initialize durable project memory and the naive CEO/PM/sub-agent workflow.

### Exit criteria

- Scaffold files exist.
- Initial project memory exists.
- PM and worker agent instructions exist.

## P01 — Spatial viewport pivot cleanup and Android foundation

Status: **current**

### Goal

Align durable docs with the spatial viewport pivot and create the minimal Kotlin Android foundation for implementation.

### Entry criteria

- Repository exists as `rokid-spatious-viewport`.
- PM Agent has local clone on u4090.
- Boss accepted the pivot from `rokid-termux` to spatial app/display viewport.

### Included features

- F001 Spatial viewport scope cleanup.
- F002 Kotlin Android skeleton.
- F003 Pure viewport geometry core.
- F004 MediaProjection capture proof.

### Required implementation order

```text
1. Clean root/meta docs to match the spatial viewport pivot.
2. Create Kotlin Android project skeleton.
3. Add pure viewport geometry module/tests first.
4. Add MediaProjection capture proof after the Android skeleton and viewport-core exist.
```

### Jobs

| Job | Title | Branch | Depends on |
|---|---|---|---|
| P01-J001 | Spatial viewport docs cleanup | `docs/spatial-viewport-pivot-cleanup` | P00 |
| P01-J002 | Kotlin Android project skeleton | `chore/android-kotlin-skeleton` | P01-J001 |
| P01-J003 | Pure viewport geometry core/tests | `feat/spatial-viewport-core` | P01-J002 |
| P01-J004 | MediaProjection capture proof | `feat/mediaprojection-capture` | P01-J002, P01-J003 preferred |

### Verification

- Root/meta docs no longer present `rokid-termux` as core scope.
- Kotlin Android skeleton builds.
- Viewport-core tests pass.
- MediaProjection capture proof starts through system consent and shows frames in debug UI.
- No Rokid SDK, ASR, Bluetooth ring, Termux-specific logic, OCR, semantic app control, or AccessibilityService is added in this phase.

### Exit criteria

- Android skeleton exists and build command is documented.
- Pure viewport geometry module exists with corner/padding tests.
- MediaProjection proof exists or its blockers are explicitly documented.
- PM can plan the phone-side simulator/overscan phase without guessing.

## P02 — Phone-side spatial viewport simulator and overscan prototype

Status: **candidate**

### Goal

Use captured or synthetic frames to prove the spatial viewport UX on the Fold 6 before depending on Rokid APIs.

### Candidate features

- F005 Phone-side viewport simulator.
- F006 Fixed center reticle overlay.
- F007 Recenter/freeze/debug controls.
- F008 Overscan cache prototype.

### Exit criteria

- A synthetic or captured frame is placed on a padded virtual canvas.
- A fixed-reticle viewport pans over that canvas.
- Overscan cache behavior is visible in debug UI.
- PM can decide whether to start Rokid renderer work.

## P03 — Rokid renderer proof

Status: **candidate**

### Goal

Render the cached viewport on Rokid glasses and drive local crop with actual or fake head pose.

### Candidate features

- F009 Rokid-side renderer skeleton.
- F010 Head-pose provider abstraction.
- F011 Tile cache client.
- F012 Transport abstraction.

### Exit criteria

- Rokid-side app displays viewport from cached region.
- Head movement or fake pose controls the local crop.
- Same geometry model is shared with phone-side simulator.

## P04+ — Product expansion

Status: **unplanned**

Possible directions after P03:

- Bluetooth ring input provider.
- ASR command provider.
- Termux optimized mirrored-app profile.
- Browser/document optimized profile.
- Accessibility-gated interaction bridge.
- OCR/semantic app understanding.
- Packaging and distribution.
