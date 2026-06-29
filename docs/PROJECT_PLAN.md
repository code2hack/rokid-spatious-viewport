# Rokid Spatious Viewport — Project Plan

Status: planning handoff for Codex  
Primary development device: u4090  
Android companion device target: Samsung Fold 6  
Glasses target: Rokid-side app  
Repository: `rokid-spatious-viewport`

## 1. Product thesis

Rokid Spatious Viewport turns Rokid glasses into a head-tracked viewport into Android app surfaces.

The Android companion app captures a user-approved Android display or app window, maps the captured frame into a larger virtual canvas, and sends a tiled overscan region to the Rokid app. The Rokid app crops locally from the cached region according to head pose, displays a fixed center reticle, and sends interaction events back to Android.

Termux remains an important use case, but it is no longer the core scope. The core scope is app-surface mirroring plus spatial viewport navigation.

## 2. Core mental model

```text
Android app/window/display capture
        ↓
Captured frame stream
        ↓
Virtual canvas with padding, overlays, and optional minimap
        ↓
Tile grid + overscan cache around current viewport
        ↓
Transport to Rokid app
        ↓
Rokid-side local crop from cached region
        ↓
Head-tracked visible viewport + fixed center reticle
```

The user should feel that a large Android app surface is floating in front of them. The physical Rokid display is only a window into that large surface.

## 3. Confirmed platform basis

Android MediaProjection is the capture foundation. Android 14 / API 34 supports app screen sharing, allowing users to share a single app window rather than the full device screen. The selected app contents exclude system UI such as status bar, navigation bar, and notifications. Android's API documentation describes MediaProjection as capturing a device display or app window and projecting it to a virtual display rendered onto an app-provided `Surface`.

MediaProjection sessions require explicit user consent. A session is tied to a single `createVirtualDisplay()` call, and on Android 14+ the token cannot be reused for multiple virtual displays. The app must handle projection stop events and release capture resources.

`FLAG_SECURE` and sensitive view protection are hard boundaries: secure app windows or secure regions may be hidden from capture or screen sharing. This is expected and should not be bypassed.

MediaProjection captures pixels only. Input/control of arbitrary mirrored apps is a separate layer, most likely gated behind an optional Android `AccessibilityService` that can dispatch gestures.

## 4. Scope decision

### In scope for v0.x

- Android companion app for MediaProjection capture.
- Android 14+ single-app capture flow where available.
- Full-display capture fallback.
- Spatial viewport renderer.
- Virtual canvas larger than physical Rokid display.
- Head-pose-driven viewport movement.
- Fixed center reticle.
- Tiled overscan streaming strategy.
- Local crop on Rokid side from cached region.
- Basic phone-side simulator before Rokid transport is ready.
- Optional interaction mapping design: reticle to app coordinate, tap/scroll gestures later.

### Out of scope for first implementation

- Bypassing protected content or `FLAG_SECURE`.
- Capturing off-screen contents that an app has not rendered.
- Full semantic understanding of arbitrary apps.
- ASR-heavy command system.
- Bluetooth ring integration.
- Termux-specific terminal emulation.
- Multi-app compositing beyond the selected captured region.
- Production-grade cloud/remote streaming.

These are future extensions after the capture + viewport loop feels good.

## 5. Product modes

### 5.1 Single-app viewport mode

The user starts capture, Android system UI asks what to share, and the user selects one app. The captured app surface becomes the main virtual canvas.

This should be the default target on Android 14+.

### 5.2 Full-display viewport mode

The user shares the full default display. The entire captured display becomes the main virtual canvas.

This is the fallback mode and is useful for Android versions without single-app capture.

### 5.3 Local simulator mode

The Android companion app renders the spatial viewport on the Fold 6 screen using phone sensors or touch drag as a fake head-pose source.

This mode is mandatory for fast development before the Rokid-side app and transport are stable.

### 5.4 Rokid live mode

The Android companion sends tile regions to Rokid. Rokid uses its own head pose to crop locally from the cached region.

This is the real product mode.

## 6. Architecture overview

```text
android-companion/
  CaptureSessionController
  MediaProjectionService
  CaptureSurface / ImageReader / SurfaceTexture path
  FrameSource
  VirtualCanvasMapper
  TileScheduler
  TileEncoder
  TransportServer
  InputBridge
  DebugViewportActivity

rokid-client/
  TransportClient
  TileCache
  HeadPoseProvider
  ViewportMapper
  ViewportRenderer
  ReticleOverlay
  InputEventEmitter
  DiagnosticsOverlay

shared/
  Protocol messages
  Geometry types
  Tile coordinates
  Frame metadata
  Input event schema
  Capability negotiation
```

The exact repository/module structure can be decided by Codex after inspecting the current repo. The important part is to keep the capture/viewport/tile math independent from Android UI as much as possible.

## 7. Capture pipeline

### 7.1 MediaProjection session

Responsibilities:

- Start capture consent flow.
- Prefer `MediaProjectionConfig.createConfigForUserChoice()` on API 34+ so the user can choose app window or display.
- Fall back to normal screen-capture intent on older APIs.
- Start foreground service with `mediaProjection` type where required.
- Create virtual display targeting a capture `Surface`.
- Register `MediaProjection.Callback` and release resources on stop.
- Handle captured-content size changes.

### 7.2 Capture surface options

Candidate paths:

1. `ImageReader`
   - Good for correctness and CPU-visible frames.
   - Easier to debug.
   - Higher latency/copy cost.

2. `SurfaceTexture` / OpenGL texture
   - Better for GPU crop/composite/encode.
   - More complex.
   - Better long-term target.

3. Direct encoder surface
   - Good for one video stream.
   - Less flexible for tiled/cached strategy.

Recommendation:

- P1: Use `ImageReader` or a simple texture path to prove capture and viewport math.
- P2: Move crop/composite to GPU path.
- P3: Add tile encoder/cached overscan.

## 8. Virtual canvas model

Definitions:

```text
captureFrame:     pixels produced by MediaProjection
contentCanvas:    captureFrame mapped into a virtual 2D coordinate system
paddedCanvas:     contentCanvas plus padding on all sides
viewport:         physical Rokid visible area in canvas coordinates
reticle:          fixed point at the center of the viewport
overscanRegion:   region larger than viewport sent to Rokid for local crop
cacheRegion:      Rokid-side currently available tile set
```

The padded canvas should allow the center reticle to point at the true corners of the captured app frame. This means the canvas bounds used for head mapping should include half-viewport padding around the content frame.

```text
paddedLeft   = -viewportWidth  / 2
paddedTop    = -viewportHeight / 2
paddedRight  = contentWidth  + viewportWidth  / 2
paddedBottom = contentHeight + viewportHeight / 2
```

When the reticle points to a content corner, part of the visible viewport can show padding/background outside the captured content. That is expected.

## 9. Head-pose to viewport mapping

The head-pose provider should output a stabilized orientation or orientation delta, not raw gyroscope integration.

Basic mapping:

```text
recenterPose = pose when user calibrates
poseDelta    = currentPose - recenterPose
normalizedX  = clamp(poseDelta.yaw   / maxYaw,   -1, 1)
normalizedY  = clamp(poseDelta.pitch / maxPitch, -1, 1)
reticleX     = map(normalizedX, -1..1, contentLeft..contentRight)
reticleY     = map(normalizedY, -1..1, contentTop..contentBottom)
viewportX    = reticleX - viewportWidth  / 2
viewportY    = reticleY - viewportHeight / 2
```

Required controls:

- Recenter.
- Freeze/lock viewport.
- Adjust sensitivity.
- Adjust dead zone.
- Toggle follow mode.
- Show minimap.

Stabilization requirements:

- Dead zone around center.
- Low-pass smoothing.
- Velocity-aware damping.
- Optional snap-to-edge or snap-to-line later.

## 10. Strategy C: tiled canvas with overscan margin

This is the selected streaming strategy.

### 10.1 Goal

The Rokid side should not wait for Android round trips on every small head movement. Rokid must be able to locally crop inside a cached overscan area.

### 10.2 Tile grid

The Android side divides the virtual canvas into fixed-size tiles.

Candidate tile sizes:

- 256 × 256 for simple cache granularity.
- 512 × 512 for lower metadata overhead.
- Adaptive tile size later.

Initial recommendation: start with 512 × 512 unless device constraints suggest otherwise.

### 10.3 Overscan region

For each frame/viewport pose, Android sends:

- Current visible viewport region.
- Overscan margin around it.
- Directionally biased extra tiles based on recent head velocity.
- Optional low-resolution full-frame/minimap.

Example:

```text
overscanLeft   = viewportLeft - marginX
overscanTop    = viewportTop  - marginY
overscanRight  = viewportRight + marginX
overscanBottom = viewportBottom + marginY
```

Default margin target:

```text
marginX = viewportWidth  * 0.75
marginY = viewportHeight * 0.75
```

Prediction target:

```text
if headVelocityX > threshold: add extra margin to right
if headVelocityX < threshold: add extra margin to left
if headVelocityY > threshold: add extra margin downward
if headVelocityY < threshold: add extra margin upward
```

### 10.4 Rokid-side tile cache

Rokid maintains tile cache keyed by:

```text
sessionId
frameId or contentEpoch
tileX
tileY
tileLevel
```

Rokid renders the current viewport by sampling cached tiles. If tiles are missing, it should:

- Use last-known tile if still close in time.
- Use lower-resolution fallback if available.
- Show subtle loading/edge indicator only if necessary.

### 10.5 Update policy

MVP may send full overscan image first, then split into tiles later. The architecture should still expose tile concepts early.

Evolution path:

1. Full-frame local crop prototype.
2. Full overscan region per frame.
3. Tile cache with dirty-tile updates.
4. Predicted directional prefetch.
5. Multi-resolution tiles.
6. Codec optimization.

## 11. Transport

Transport must be abstracted because Rokid connection details may change.

Interface:

```kotlin
interface ViewportTransport {
    fun sendControl(message: ControlMessage)
    fun sendTile(tile: EncodedTile)
    fun sendFrameMetadata(metadata: FrameMetadata)
    fun receivePoseUpdates(): Flow<PoseUpdate>
    fun receiveInputEvents(): Flow<InputEvent>
}
```

Possible transports:

- Local loopback for simulator.
- WebSocket over Wi-Fi/Bluetooth PAN/ADB for development.
- Rokid SDK channel if available.
- USB or vendor channel if exposed.

Recommendation:

- P1: in-process simulator.
- P2: WebSocket transport between Fold 6 and a client app/device.
- P3: adapt to Rokid-specific transport once verified.

## 12. Input and interaction plan

MediaProjection only mirrors pixels. Input needs a separate bridge.

### 12.1 MVP input

- Recenter.
- Freeze/unfreeze viewport.
- Return to center.
- Phone-side touch drag to simulate head movement.
- Phone-side tap to simulate reticle click.

### 12.2 App control input

Optional later layer:

```text
reticle in Rokid viewport
  ↓
canvas coordinate
  ↓
captured app-frame coordinate
  ↓
phone display coordinate
  ↓
AccessibilityService dispatchGesture tap/scroll
```

A tap should only be injected when the user explicitly confirms via ring, phone, or voice. This avoids accidental interactions from head movement.

### 12.3 Future input devices

- Bluetooth ring for confirm/cancel/scroll/recenter.
- ASR for command phrases.
- Phone touchpad mode.
- Hardware keyboard mode.

The input layer should be provider-based from the beginning but only the simplest provider needs implementation first.

## 13. UX rules

- Head movement should move the viewport, not the content's logical state.
- Reticle stays fixed in the center of the visible Rokid display.
- User must always have a fast recenter action.
- User must always have a fast freeze/lock action.
- The system should avoid motion jitter while reading text.
- Missing tiles should degrade gracefully.
- Capture permission status must be obvious on phone side.
- Do not record or persist captured frames by default.
- Do not attempt to defeat protected content.

## 14. Privacy and security requirements

- No frame persistence by default.
- No network transport outside local trusted links by default.
- Obvious active-capture indicator in companion UI.
- Stop capture quickly from phone UI.
- Treat secure/blank frames as platform constraints.
- Accessibility-based input bridge must be opt-in and clearly separated from display-only mode.

## 15. MVP acceptance criteria

### Milestone A: Android capture proof

- App starts MediaProjection consent flow.
- User selects app/window or full display depending on Android support.
- Captured frames appear in a debug view.
- App handles projection stop without crash.
- App handles rotation/size change.

### Milestone B: Spatial viewport simulator

- Captured frame is placed on a padded virtual canvas.
- Debug view shows a crop representing the Rokid viewport.
- Drag/touch or phone sensor moves viewport across canvas.
- Center reticle stays fixed.
- Reticle can point at all four content corners.
- Recenter and freeze controls work.

### Milestone C: Overscan cache prototype

- App computes overscan region larger than visible viewport.
- Local renderer crops visible viewport from overscan cache.
- When viewport nears edge, app refreshes overscan region.
- Debug overlay shows viewport bounds, overscan bounds, and cache misses.

### Milestone D: Rokid display proof

- Rokid-side app shows the viewport.
- Rokid head pose drives local crop inside cached region.
- Latency is low enough that small head movements feel local.
- Fallback simulator remains usable when Rokid APIs are unavailable.

### Milestone E: First interaction proof

- Reticle coordinate maps back to captured app/display coordinate.
- User can trigger a tap through a gated input mechanism.
- Scroll gesture is possible in full-display mode or app-share mode.
- Interaction can be disabled completely.

## 16. Metrics to log from day one

- Capture frame size.
- Capture frame rate.
- End-to-end visible frame latency estimate.
- Tile encode time.
- Tile decode time.
- Tile cache hit/miss count.
- Pose update rate.
- Render frame rate.
- Recenter count.
- Projection stop reason if available.

## 17. Unknowns Codex should document, not guess silently

- Exact current repo structure.
- Android project/module status.
- Rokid app SDK availability.
- Rokid display resolution and refresh rate.
- Rokid head-pose API availability and coordinate conventions.
- Actual transport options between Fold 6 and Rokid glasses.
- Fold 6 Android version during testing.
- Whether Samsung-specific behavior affects MediaProjection single-app sharing.
- Whether target apps are commonly protected by `FLAG_SECURE`.

## 18. Recommended first engineering path

1. Inspect existing repository structure.
2. Add this plan under docs if not already present.
3. Create or identify Android companion module.
4. Implement local-only capture proof.
5. Implement viewport math as pure Kotlin unit-testable code.
6. Implement debug simulator UI on phone.
7. Add overscan cache abstraction.
8. Only then connect to Rokid-side rendering.

## 19. Preferred commit sequence

Codex should use small commits:

1. `docs: define spatial viewport plan`
2. `feat(android): add mediaprojection capture skeleton`
3. `feat(viewport): add virtual canvas geometry model`
4. `feat(android): render captured frame in debug viewport`
5. `feat(viewport): add overscan cache prototype`
6. `feat(transport): add local transport abstraction`
7. `feat(rokid): add viewport renderer skeleton`
8. `feat(input): map reticle to app coordinates`

## 20. Final product statement

Rokid Spatious Viewport mirrors a user-selected Android app or display into a large virtual canvas and lets the user inspect it through a head-tracked Rokid viewport. The first breakthrough is not app control; it is making the spatial viewport feel stable, readable, and low-latency.
