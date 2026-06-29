# Project Kernel

Status: **spatial viewport pivot accepted**  
Owner: **Boss + PM/CEO Agents**  
Last updated: **2026-06-30**

## Goal

Build a head-tracked spatial viewport for mirrored Android app/display surfaces on Rokid glasses.

The Android companion app captures a user-approved Android app window or display, maps the captured frame into a padded virtual canvas, and eventually sends a tiled overscan region to the Rokid-side app. The Rokid app crops locally from the cached region according to head pose and displays a fixed center reticle.

The first validated outcome should be small: a Kotlin Android app skeleton, a pure viewport geometry module with tests, and a MediaProjection capture proof that can show captured frames in a debug view.

## User / consumer

Primary users:

- Boss / maintainer who wants a working spatial viewport prototype and clear agent execution plan.
- Local PM Agent / Codex session coordinating branches, worktrees, tests, and reviews.
- Developer sub-agents implementing narrow pieces such as viewport geometry or MediaProjection capture.
- Future users who want to view Android app surfaces through Rokid glasses with a head-tracked viewport.

## Value proposition

Rokid Spatious Viewport should make Android app surfaces usable in glasses without shrinking the whole app into the physical display.

Instead of fitting an entire app into a small visible area, the system provides:

- A larger virtual canvas.
- A fixed center reticle.
- Head-tracked viewport movement.
- Local crop from cached overscan tiles.
- Later optional input via ring, ASR, phone touch, or accessibility-gated gestures.

## Current product truth

The project is not primarily a Termux terminal/bootstrap project anymore.

Termux remains a future/flagship mirrored-app use case, but the core architecture is:

```text
MediaProjection capture
→ padded virtual canvas
→ spatial viewport geometry
→ tiled overscan cache
→ Rokid-side local crop
```

## Current implementation order

```text
1. Clean root/meta docs to match the spatial viewport pivot.
2. Create Kotlin Android project skeleton.
3. Add pure viewport geometry module/tests first.
4. Add MediaProjection capture proof after the Android skeleton and viewport-core exist.
```

## Non-goals for current phase

- Rokid SDK integration before the phone-side simulator and capture proof exist.
- ASR or Bluetooth ring integration.
- Termux-specific logic beyond acknowledging it as a future use case.
- OCR or semantic understanding of arbitrary apps.
- AccessibilityService app control.
- Bypassing `FLAG_SECURE` or protected content.
- Persisting captured frames by default.
- Spark-based development; u4090 is the main development device for now.

## Constraints

- Prefer Kotlin, not Java, for Android implementation.
- Keep pure viewport geometry independent of Android UI dependencies.
- Keep each job branch narrow and reviewable.
- Every job must include acceptance criteria.
- Capture must require Android system consent.
- MediaProjection is display-only; app control is a separate optional future layer.
- Every product decision should be recorded in docs or ADRs.

## Success criteria for the next implementation slice

The next slice succeeds when:

- Root/meta docs no longer present stale `rokid-termux` as the core scope.
- A minimal Kotlin Android project skeleton builds.
- A pure viewport geometry module exists and has tests for center/corner/padding behavior.
- MediaProjection proof starts capture through Android consent and shows captured frames in a debug view.
- The repo documents the build/test commands.

## First demo

Draft demo:

> On the Fold 6, start the Android companion app, approve MediaProjection capture, display the captured app/display frame in a debug viewport, and pan a fixed-reticle viewport over a padded virtual canvas.

## Risks

| Risk | Mitigation |
|---|---|
| Android skeleton choices block progress | Keep skeleton minimal and Kotlin-first. |
| MediaProjection complexity hides viewport logic | Build pure viewport-core before capture proof. |
| Agents revive old Termux scope | Root docs and AGENTS.md explicitly state the pivot. |
| Protected content appears blank | Treat `FLAG_SECURE` as a platform boundary, not a bug. |
| Rokid SDK unknowns slow MVP | Build phone-side simulator first. |

## Target state

A verified, documented, reproducible prototype where a user-approved Android app/display surface can be inspected through a head-tracked spatial viewport, developed through small PM-reviewed branches.
