# Worker Prompt — MediaProjection Capture

You are the MediaProjection capture worker for `code2hack/rokid-spatious-viewport`.

## Branch

Use or create:

```text
feat/mediaprojection-capture
```

## Required reading

Read before coding:

- `AGENTS.md`
- `docs/PROJECT_PLAN.md`
- `docs/WORK_BREAKDOWN.md`
- `docs/adr/0003-mediaprojection-boundaries.md`

## Mission

Implement the smallest Android companion-side MediaProjection capture proof.

The goal is not the full product. The goal is:

```text
start user-approved capture
→ create virtual display / capture surface
→ show captured frames in a debug view
→ stop/release cleanly
```

## Scope

Allowed:

- Android project/module setup if absent and approved by PM.
- MediaProjection permission/consent flow.
- Foreground service for capture.
- VirtualDisplay creation.
- Capture surface via `ImageReader`, `SurfaceTexture`, or simplest viable path.
- Debug preview of captured frames.
- Projection stop callback.
- Rotation/resize handling.
- Minimal logging/diagnostics.

Not allowed in this worker unless PM explicitly expands scope:

- Rokid-side renderer.
- Head-pose APIs.
- Bluetooth ring.
- ASR.
- Termux-specific logic.
- OCR/semantic app understanding.
- AccessibilityService app control.
- Frame persistence/recording.
- Bypassing protected content.

## Platform rules

- Treat Android system consent as required.
- On Android 14/API 34+, prefer user-choice app/display sharing when available.
- Full-display capture is acceptable as fallback.
- Register and handle projection stop callbacks.
- Do not persist captured frames by default.
- Do not attempt to bypass `FLAG_SECURE`; blank/protected content is expected.

## Before coding

Report to the PM:

1. Existing Android project/module structure.
2. Proposed files/modules to touch.
3. Capture implementation path selected first: `ImageReader`, `SurfaceTexture`, or another simple path.
4. Build/test command to verify.

## Acceptance criteria

- User can start capture through Android system consent.
- Captured content appears in a debug view.
- User can stop capture.
- Projection stop releases resources.
- Rotation/resize does not crash, or limitation is documented.
- Build/test command passes, or failure is documented with next action.

## Suggested commit message

```text
feat(android): add mediaprojection capture proof
```
