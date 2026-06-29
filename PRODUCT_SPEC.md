# Product Specification

Status: **draft / spatial viewport pivot accepted**  
Product name: **Rokid Spatious Viewport**  
Workflow owner: **CEO Agent**  
Execution owner: **PM Agent**

## Product thesis

Rokid Spatious Viewport turns Rokid glasses into a head-tracked viewport into mirrored Android app/display surfaces.

The Android companion app captures a user-approved Android app window or display using MediaProjection, maps the captured frame into a padded virtual canvas, and eventually sends a tiled overscan region to the Rokid-side app. The Rokid app crops locally from the cached region according to head pose and displays a fixed center reticle.

Termux is a future/flagship mirrored-app use case, not the core architecture.

## Problem

Small glasses displays are not large enough to show a full Android app surface comfortably. Mirroring an entire app into the physical viewport forces the user to choose between unreadably small text and constant manual zooming/panning.

Common failure modes:

- Full app mirror is too small to read.
- Pixel mirroring lacks spatial navigation.
- Head movement is underused as a viewport control.
- App-specific terminal or workflow assumptions limit product scope too early.
- Capture and input/control concerns are mixed together.

## Target users

### Boss / maintainer

Needs a clear path from concept to prototype without stale `rokid-termux` assumptions.

### PM Agent

Needs unambiguous implementation order, branch sequencing, review checklists, and state transitions.

### Developer sub-agent

Needs a small task with clear scope, allowed files, tests, and required report.

### Future technical user

Wants to view Android app surfaces through Rokid glasses using a stable, readable, head-tracked viewport.

## Core product objects

| Object | Meaning |
|---|---|
| Captured surface | Android app/display pixels approved through MediaProjection. |
| Content canvas | Captured frame mapped into a virtual coordinate system. |
| Padded canvas | Content canvas plus half-viewport padding so the reticle can point at true corners. |
| Viewport | Physical Rokid visible region in canvas coordinates. |
| Reticle | Fixed center pointer used for aiming/selection. |
| Head pose | Orientation input used to move the viewport. |
| Overscan region | Region larger than the visible viewport cached on the Rokid side. |
| Tile | Encoded piece of the virtual canvas/overscan region. |
| PM job | Scoped, reviewable state transition. |

## MVP definition

The first MVP is not a polished Rokid product. It is a verified phone-side spatial viewport foundation:

1. Kotlin Android project skeleton builds.
2. Pure viewport geometry module exists and is unit tested.
3. MediaProjection capture proof can show user-approved captured frames in a debug view.
4. Captured/synthetic frame can be placed on a padded virtual canvas.
5. A fixed-reticle viewport can pan over that canvas.

## Current implementation order

```text
1. Clean root/meta docs to match the spatial viewport pivot.
2. Create Kotlin Android project skeleton.
3. Add pure viewport geometry module/tests first.
4. Add MediaProjection capture proof after the Android skeleton and viewport-core exist.
```

## Candidate capabilities

### C001 — Kotlin Android skeleton

A minimal Kotlin Android Gradle app that builds and provides a debug entry screen.

Acceptance:

- Kotlin Android skeleton exists.
- Build command is documented.
- Main/debug screen exists.
- No MediaProjection implementation yet.

### C002 — Spatial viewport core

Pure Kotlin viewport geometry independent from Android UI.

Acceptance:

- Padded canvas calculation exists.
- Pose/normalized input can map to reticle point.
- Reticle maps to viewport rectangle.
- Unit tests cover center and all four corners.
- Reticle can point at true content corners with half-viewport padding.

### C003 — MediaProjection capture proof

A minimal Android capture proof.

Acceptance:

- Starts through Android system consent.
- Creates virtual display/capture surface.
- Shows captured frames in debug UI.
- Stops and releases resources cleanly.
- Handles resize/rotation or documents limitation.

### C004 — Phone-side viewport simulator

A debug UI that pans a viewport over synthetic/captured content.

Acceptance:

- Shows fixed center reticle.
- Pans across padded canvas.
- Recenter/freeze controls exist or are stubbed.
- Debug coordinates are visible.

### C005 — Overscan cache prototype

Local prototype of Strategy C before Rokid transport.

Acceptance:

- Computes overscan region larger than viewport.
- Can crop visible viewport from cached region.
- Shows cache/viewport debug overlay.

### C006 — Rokid renderer skeleton

Future step after phone-side simulator and capture proof are stable.

Acceptance:

- Uses same viewport geometry model.
- Displays cached region on Rokid.
- Uses actual or fake head-pose provider.

## Out of scope before C001–C003 complete

- Rokid SDK integration.
- ASR input.
- Bluetooth ring input.
- Termux-specific terminal emulation.
- OCR/semantic app understanding.
- AccessibilityService app control.
- Recording/screenshot persistence.
- Cloud/network streaming outside local/dev experiments.

## Verification strategy

A change is accepted only when it passes the appropriate level:

1. Local build/test validation.
2. PM Agent diff and scope review.
3. Product-coherence review against this spec and ADRs.
4. Boss/User verification for visible behavior.

## Open questions

| ID | Question | Owner | Target phase |
|---|---|---|---|
| Q001 | Exact Rokid display/head-pose SDK path? | PM + future Rokid worker | After phone simulator |
| Q002 | Should the skeleton use Compose or Android Views? | PM | Skeleton step |
| Q003 | Which capture surface path should be used first: ImageReader or SurfaceTexture? | MediaProjection worker | Capture proof |
| Q004 | What Fold 6 Android version is used for testing? | PM/Boss | Capture proof |
| Q005 | Which mirrored app is the first manual demo target? | Boss + PM | After capture proof |
