# Codex Start Prompt

Use this prompt when starting the PM/Codex session.

```text
You are working on https://github.com/code2hack/rokid-spatious-viewport.

Current product direction:
Rokid Spatious Viewport is no longer primarily a Termux terminal project. It is a head-tracked spatial viewport for mirrored Android app/display surfaces. The Android companion app captures a user-approved app window or display with MediaProjection, maps it into a padded virtual canvas, and sends a tiled overscan region to the Rokid app. The Rokid app locally crops from the cached region according to head pose and shows a fixed center reticle.

Important constraints:
- Do not bypass FLAG_SECURE or protected content.
- Do not persist captured frames by default.
- MediaProjection is display-only; arbitrary app control is a separate optional interaction layer.
- Strategy C is selected: tiled canvas with overscan margin. Start simple if needed, but preserve this architecture.
- Android 14+ single-app screen sharing should be supported where available; full-display capture is fallback.
- Termux is a future/flagship mirrored-app use case, not the core architecture.
- u4090 is the main development device.
- Spark is out of scope for now.

First tasks:
1. Inspect the repo structure and current build state.
2. Add/confirm planning docs from docs/PROJECT_PLAN.md and docs/WORK_BREAKDOWN.md.
3. Create the smallest Android MediaProjection capture proof if an Android module exists, or propose/create the Android project skeleton if absent.
4. Implement spatial viewport geometry as pure, unit-testable code.
5. Build a phone-side simulator before depending on Rokid-specific APIs.
6. Keep commits small and explain any unknowns.

Do not over-focus on ASR, Bluetooth ring, Termux internals, or app semantics yet. The first breakthrough is: capture an app/display, put it on a padded virtual canvas, and move a viewport over it smoothly.
```
