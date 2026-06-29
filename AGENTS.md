# AGENTS.md — Repository Entry Instructions

This repository is intended to be worked by a PM/integrator Codex session plus, when useful, narrowly scoped worker sessions.

## Required first read

Any agent working in this repository must read these files before coding:

1. `docs/codex/START_PROMPT.md`
2. `docs/codex/PM_ORCHESTRATION.md`
3. `docs/PROJECT_PLAN.md`
4. `docs/WORK_BREAKDOWN.md`
5. `docs/adr/0001-scope-spatial-viewport.md`
6. `docs/adr/0002-selected-streaming-strategy.md`
7. `docs/adr/0003-mediaprojection-boundaries.md`

## Current project scope

Rokid Spatious Viewport is a head-tracked spatial viewport for mirrored Android app/display surfaces.

It is not primarily a Termux terminal project anymore. Termux remains an important future/flagship mirrored app use case, but the core architecture is app-surface mirroring plus spatial viewport navigation.

## Current implementation priority

The first breakthrough is:

```text
MediaProjection capture
→ captured frame on padded virtual canvas
→ viewport pan over that canvas
→ fixed center reticle
→ overscan cache prototype
```

Do not start with Rokid SDK, ASR, Bluetooth ring, Termux internals, semantic OCR, or AccessibilityService unless the PM explicitly assigns that work.

## Agent roles

### PM / integrator agent

The PM agent owns architecture, task slicing, branch sequencing, review, and final integration.

The PM must:

- Read `docs/codex/PM_ORCHESTRATION.md`.
- Inspect the current repo/build state before assigning work.
- Keep worker tasks narrow and non-overlapping.
- Ask workers for plans before code when scope is uncertain.
- Merge geometry/core abstractions before capture integration when possible.
- Keep commits small.
- Preserve privacy/security boundaries from ADR 0003.

### Worker agents

Worker agents should only implement their assigned task. They should not broaden scope.

A worker must:

- Read this file and the assigned worker prompt.
- State the files/modules it expects to touch before making large changes.
- Avoid unrelated refactors.
- Add tests for pure logic when possible.
- Report unknowns instead of guessing silently.

## Recommended current worker split

Use at most two worker agents in the current phase unless the PM explicitly decides otherwise.

1. MediaProjection capture worker
   - Branch: `feat/mediaprojection-capture`
   - Prompt: `docs/codex/workers/MEDIAPROJECTION_CAPTURE.md`

2. Spatial viewport core worker
   - Branch: `feat/spatial-viewport-core`
   - Prompt: `docs/codex/workers/SPATIAL_VIEWPORT_CORE.md`

A third worker is optional only for docs/build tooling. Do not start a Rokid worker yet.

## Hard boundaries

- Do not bypass `FLAG_SECURE` or protected content.
- Do not persist captured frames by default.
- Do not implement arbitrary app control as part of MediaProjection capture.
- Do not enable AccessibilityService interaction without explicit PM/user approval.
- Do not assume Rokid SDK details before verifying them.
- Do not use Spark for this phase. u4090 is the main development machine.
