# Worker Prompt — Spatial Viewport Core

You are the spatial viewport core worker for `code2hack/rokid-spatious-viewport`.

## Branch

Use or create:

```text
feat/spatial-viewport-core
```

## Required reading

Read before coding:

- `AGENTS.md`
- `docs/PROJECT_PLAN.md`
- `docs/WORK_BREAKDOWN.md`
- `docs/adr/0001-scope-spatial-viewport.md`
- `docs/adr/0002-selected-streaming-strategy.md`

## Mission

Implement the pure geometry and simulator foundation for the head-tracked spatial viewport.

The goal is:

```text
captured/synthetic content size
→ padded virtual canvas
→ pose or fake-pose input
→ reticle point
→ viewport rectangle
→ debug/simulator crop
```

This worker should produce reusable core math before Rokid SDK or MediaProjection details depend on it.

## Scope

Allowed:

- Pure Kotlin/JVM or shared module geometry types.
- Padded canvas calculation.
- Pose-to-reticle mapping.
- Reticle-to-viewport mapping.
- Clamp/padding behavior.
- Dead-zone/smoothing hooks.
- Unit tests for corner behavior.
- Simple simulator using synthetic frame/source if PM approves.
- Debug overlays if a UI module already exists.

Not allowed in this worker unless PM explicitly expands scope:

- MediaProjection foreground service.
- Android capture consent flow.
- Rokid-side renderer.
- Head-pose SDK assumptions.
- Bluetooth ring.
- ASR.
- Termux-specific logic.
- AccessibilityService app control.

## Required geometry behavior

The padded canvas must allow the fixed center reticle to point at the true content corners.

Given:

```text
contentWidth
contentHeight
viewportWidth
viewportHeight
```

The padded coordinate system should support:

```text
paddedLeft   = -viewportWidth / 2
paddedTop    = -viewportHeight / 2
paddedRight  = contentWidth + viewportWidth / 2
paddedBottom = contentHeight + viewportHeight / 2
```

When reticle points at `(0, 0)`, the viewport is allowed to extend outside the content area into padding. Same for the other three content corners.

## Suggested data types

Adapt names to repo style, but preserve the concepts:

```kotlin
data class IntSize(val width: Int, val height: Int)
data class FloatPoint(val x: Float, val y: Float)
data class FloatRect(val left: Float, val top: Float, val right: Float, val bottom: Float)
data class PoseDelta(
    val yawDegrees: Float,
    val pitchDegrees: Float,
    val rollDegrees: Float = 0f,
)
data class ViewportConfig(
    val contentSize: IntSize,
    val viewportSize: IntSize,
    val maxYawDegrees: Float,
    val maxPitchDegrees: Float,
)
data class ViewportState(
    val reticleContentPoint: FloatPoint,
    val viewportCanvasRect: FloatRect,
    val contentCanvasRect: FloatRect,
    val paddedCanvasRect: FloatRect,
)
```

## Before coding

Report to the PM:

1. Existing module structure suitable for pure geometry.
2. Proposed package/module name.
3. Test framework available.
4. Files/modules to touch.

## Acceptance criteria

- Geometry code is independent from MediaProjection.
- Unit tests cover center and all four corners.
- Reticle can point at all four content corners.
- Viewport can extend into padding by half viewport size.
- Dead-zone/smoothing can be added without rewriting mapping.
- Build/test command passes, or failure is documented with next action.

## Suggested commit message

```text
feat(viewport): add spatial viewport geometry core
```
