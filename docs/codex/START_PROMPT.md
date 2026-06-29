# Codex Start Prompt

Use this prompt when starting the PM/Codex session.

```text
You are working on https://github.com/code2hack/rokid-spatious-viewport.

Current product direction:
Rokid Spatious Viewport is a head-tracked spatial viewport for mirrored Android app/display surfaces. The Android companion app captures a user-approved app window or display with MediaProjection, maps it into a padded virtual canvas, and eventually sends a tiled overscan region to the Rokid app. The Rokid app locally crops from the cached region according to head pose and shows a fixed center reticle.

Termux is only a future/flagship mirrored-app use case. It is not the core architecture.

Important constraints:
- Do not bypass FLAG_SECURE or protected content.
- Do not persist captured frames by default.
- MediaProjection is display-only; arbitrary app control is a separate optional interaction layer.
- Strategy C is selected: tiled canvas with overscan margin. Start simple if needed, but preserve this architecture.
- Android 14+ single-app screen sharing should be supported where available; full-display capture is fallback.
- Prefer Kotlin, not Java.
- u4090 is the main development device.
- Spark is out of scope for now.

First read:
- AGENTS.md
- docs/codex/PM_ORCHESTRATION.md
- docs/codex/NEXT_IMPLEMENTATION_DECISIONS.md
- docs/PROJECT_PLAN.md
- docs/WORK_BREAKDOWN.md
- docs/adr/0001-scope-spatial-viewport.md
- docs/adr/0002-selected-streaming-strategy.md
- docs/adr/0003-mediaprojection-boundaries.md

Your first job is not to build the full product.

Proceed in this exact order:
1. Inspect the repo structure and current build state.
2. Clean root/meta docs so stale rokid-termux framing is removed or demoted to future use-case language.
3. Create the smallest Kotlin Android project skeleton if one does not already exist.
4. Add pure viewport geometry code and tests.
5. Add MediaProjection capture proof only after the Android skeleton and viewport-core exist.

Do not work on Rokid SDK, ASR, Bluetooth ring, Termux-specific logic, OCR, semantic app control, or AccessibilityService yet.

Before coding, give a short implementation plan and expected file/module changes.
```
