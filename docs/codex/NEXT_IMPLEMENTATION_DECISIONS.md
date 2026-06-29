# Next Implementation Decisions

Status: accepted PM handoff decisions  
Purpose: make the next coding order explicit so the PM does not need chat context.

## Decision summary

The PM should proceed in this order:

```text
1. Clean root/meta docs to match the spatial viewport pivot.
2. Create Kotlin Android project skeleton.
3. Add pure viewport geometry module/tests first.
4. Add MediaProjection capture proof only after the Android skeleton exists.
```

## 1. Clean root/meta docs first

The old `rokid-termux` framing should be cleaned from durable root/meta docs.

Replace old product framing such as:

```text
rokid-termux
Termux companion app
Termux bootstrap project
terminal-first project
```

with:

```text
Rokid Spatious Viewport
head-tracked spatial viewport
mirrored Android app/display surfaces
MediaProjection capture
padded virtual canvas
tiled overscan cache
Rokid-side local crop
```

Termux may remain only as:

```text
A future/flagship mirrored-app use case, not the core architecture.
```

Files to check:

```text
README.md
AGENTS.md
PROJECT_KERNEL.md
PRODUCT_SPEC.md
FEATURE_GRAPH.yaml
PHASE_PLAN.md
docs/PROJECT_PLAN.md
docs/WORK_BREAKDOWN.md
docs/codex/START_PROMPT.md
docs/codex/PM_ORCHESTRATION.md
docs/codex/workers/*.md
```

## 2. Create Kotlin Android project skeleton

After docs are aligned, create a minimal Android project skeleton.

Requirements:

- Prefer Kotlin, not Java.
- Use a minimal Android Gradle project.
- Keep package/module names aligned with spatial viewport, not `rokid-termux`.
- Add a simple app entry/debug screen.
- Do not implement MediaProjection yet.
- Confirm and document the build command.

Suggested shape:

```text
settings.gradle.kts
build.gradle.kts
gradle.properties
app/
  build.gradle.kts
  src/main/
    AndroidManifest.xml
    java/com/code2hack/rokid/spatiousviewport/
      MainActivity.kt
```

Compose is acceptable if kept minimal. Plain Android Views are also acceptable. The PM should pick the least risky skeleton that builds on u4090.

## 3. Add pure viewport geometry module/tests

Add geometry before capture.

The viewport model should be pure Kotlin and unit-testable without Android UI dependencies.

Preferred module shape if practical:

```text
viewport-core/
  build.gradle.kts
  src/main/kotlin/com/code2hack/rokid/spatiousviewport/core/
    Geometry.kt
    ViewportMapper.kt
  src/test/kotlin/com/code2hack/rokid/spatiousviewport/core/
    ViewportMapperTest.kt
```

Required behavior:

Given:

```text
content: 1920 × 1080
viewport: 640 × 480
```

Padded canvas should be:

```text
left   = -320
top    = -240
right  = 2240
bottom = 1320
```

Top-left content corner:

```text
reticle = 0,0
viewport = -320,-240 to 320,240
```

Bottom-right content corner:

```text
reticle = 1920,1080
viewport = 1600,840 to 2240,1320
```

This preserves the product requirement that the fixed center reticle can point at the true corners of the rendered app surface.

## 4. Add MediaProjection capture proof after skeleton + geometry

MediaProjection should start only after:

```text
Android app skeleton builds
viewport-core tests pass
basic app/debug screen exists
```

The first capture proof should only prove:

```text
system consent
virtual display
captured frames visible in debug UI
stop/release
resize/rotation does not crash, or limitation is documented
```

Do not add tiling, Rokid transport, ASR, Bluetooth ring, Termux profile, OCR, or AccessibilityService in this step.

## Suggested commit sequence

```text
docs: align root docs with spatial viewport scope
chore(android): add kotlin android project skeleton
feat(viewport): add pure spatial viewport geometry
test(viewport): cover padded canvas and corner mapping
feat(android): add mediaprojection capture proof
```

Keep commits small. Pause after skeleton + viewport-core if there are major Android build or Gradle decisions.
