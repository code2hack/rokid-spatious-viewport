# Work Breakdown — Rokid Spatious Viewport

This file is written for Codex to convert the planning discussion into implementation tasks.

## Phase 0 — Repository orientation

Goal: understand current repo without making assumptions.

Tasks:

- Inspect repository layout.
- Identify whether an Android Gradle project already exists.
- Identify package name, min/target SDK, Compose/View stack, and Kotlin/Java choice.
- Identify any existing Rokid SDK samples or bindings.
- Add missing docs directory if needed.
- Do not rename project/package until asked.

Deliverables:

- Short repo-structure note in `docs/` or PR summary.
- Build command documented.
- Known missing dependencies documented.

Acceptance:

- `git status` clean before work.
- Existing build/test state recorded.

## Phase 1 — Android MediaProjection capture proof

Goal: capture one user-approved app/display and show frames inside the companion app.

Tasks:

- Add `MediaProjectionService` as a foreground service.
- Declare required permissions:
  - `FOREGROUND_SERVICE`
  - `FOREGROUND_SERVICE_MEDIA_PROJECTION` where target SDK requires it.
- Implement capture consent launcher.
- On API 34+, prefer user-choice config if available.
- Create virtual display targeting a simple capture surface.
- Register projection callback.
- Handle stop/release.
- Handle captured-content resize.
- Render captured frames in a debug view.

Acceptance:

- User can start capture.
- User can choose app/display where Android supports it.
- Captured content appears in debug view.
- Stop capture releases resources.
- Rotation/resize does not crash.

Notes:

- Start simple. `ImageReader` is acceptable even if not final.
- Do not persist captured frames.

## Phase 2 — Spatial viewport core

Goal: make viewport math pure and testable.

Core data types:

```kotlin
data class IntSize(val width: Int, val height: Int)
data class FloatPoint(val x: Float, val y: Float)
data class FloatRect(val left: Float, val top: Float, val right: Float, val bottom: Float)
data class ViewportConfig(
    val viewportSize: IntSize,
    val contentSize: IntSize,
    val maxYawDegrees: Float,
    val maxPitchDegrees: Float,
    val paddingMode: PaddingMode,
)
data class PoseDelta(
    val yawDegrees: Float,
    val pitchDegrees: Float,
    val rollDegrees: Float = 0f,
)
data class ViewportState(
    val reticleCanvasPoint: FloatPoint,
    val viewportCanvasRect: FloatRect,
    val contentCanvasRect: FloatRect,
    val paddedCanvasRect: FloatRect,
)
```

Tasks:

- Implement padded canvas calculation.
- Implement pose-to-reticle mapping.
- Implement reticle-to-viewport mapping.
- Implement clamp behavior.
- Implement dead-zone and smoothing hooks.
- Unit-test corner behavior.

Acceptance:

- Reticle can point at each content corner.
- Viewport rect can extend into padding by half viewport size.
- Mapping is deterministic and unit tested.

## Phase 3 — Phone-side viewport simulator

Goal: prove the UX before Rokid integration.

Tasks:

- Render captured frame onto a virtual canvas.
- Display a cropped viewport in the phone debug UI.
- Keep reticle fixed in the center.
- Use touch drag as fake head pose.
- Optionally use phone sensors as fake head pose.
- Add overlays:
  - viewport bounds
  - reticle coordinate
  - content bounds
  - padded canvas bounds
  - FPS

Acceptance:

- Captured app can be inspected by panning across it.
- Text remains readable at chosen crop scale.
- Recenter/freeze controls work.

## Phase 4 — Overscan cache prototype

Goal: implement Strategy C locally before network/device transport.

Tasks:

- Define tile grid.
- Define tile IDs.
- Compute overscan region around viewport.
- Cache overscan region.
- Render visible viewport from cache.
- Detect cache edge approach.
- Refresh cache when needed.
- Add debug overlay for cache misses.

Acceptance:

- Small movements are served from local cache.
- Cache refresh occurs before viewport hits edge in normal motion.
- Missing-cache behavior is visible but not catastrophic.

## Phase 5 — Transport abstraction

Goal: separate viewport engine from communication path.

Tasks:

- Define protocol messages.
- Define transport interface.
- Implement local in-process transport for simulator.
- Implement WebSocket transport only if useful for development.
- Keep transport replaceable for Rokid SDK channel later.

Acceptance:

- Phone-side producer and client-side renderer can run through the same protocol even in local mode.
- Protocol can carry frame metadata, tile updates, pose updates, and input events.

## Phase 6 — Rokid-side renderer skeleton

Goal: show cached viewport on Rokid and use actual head pose when available.

Tasks:

- Create Rokid app/client module if repo structure supports it.
- Implement tile cache.
- Implement viewport renderer.
- Implement reticle overlay.
- Add head-pose provider interface.
- Add fake pose provider fallback.
- Add recenter/freeze controls.

Acceptance:

- Rokid app displays the viewport using same core geometry model.
- Head movement controls local crop if pose API is available.
- Fake pose mode works when pose API is unavailable.

## Phase 7 — Interaction bridge prototype

Goal: map reticle to captured app coordinates and optionally trigger gestures.

Tasks:

- Implement reticle-to-capture coordinate mapping.
- Implement capture-to-display coordinate mapping.
- Add explicit user-triggered tap action in debug UI.
- Design optional AccessibilityService gate.
- Implement gesture dispatch only after user enables service.

Acceptance:

- Debug overlay shows reticle app coordinate.
- Tap action can be simulated safely.
- Accessibility path is opt-in and can be disabled.

## Phase 8 — Performance pass

Goal: measure before optimizing.

Tasks:

- Add metrics logger.
- Capture FPS.
- Render FPS.
- Encode/decode time.
- Cache hit/miss rate.
- Pose update rate.
- Latency estimate.

Acceptance:

- Debug overlay or logs show metrics.
- Performance bottlenecks are visible.

## Backlog

- Bluetooth ring input provider.
- ASR provider.
- Semantic OCR/action layer.
- Minimap.
- Multi-resolution tiles.
- Directional prediction using head velocity.
- Termux profile.
- Browser/document profile.
- Recording/screenshot mode, disabled by default.
- Automatic privacy blanking for sensitive contexts.
