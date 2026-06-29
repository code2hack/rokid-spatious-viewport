# ADR 0001 — Pivot from Termux Terminal to Spatial App Viewport

## Status

Accepted for initial planning.

## Context

The project began as `rokid-termux`: a Termux companion app plus Rokid-side display/input app. During brainstorming, the main product primitive shifted from terminal rendering to app-surface mirroring.

Android MediaProjection can capture a user-approved device display or app window into an app-provided rendering surface. This makes the more general product possible: mirror any capturable Android app/display into a head-tracked virtual canvas.

## Decision

The project scope is now:

```text
Rokid Spatious Viewport = head-tracked spatial viewport for mirrored Android app/display surfaces.
```

Termux is one important mirrored app/use case, but not the architectural root.

## Consequences

- Core architecture should be app-agnostic pixel capture first.
- MediaProjection is the capture foundation.
- The first UI target is a spatial viewport, not a terminal emulator.
- Terminal-specific features move to later profiles/plugins.
- Arbitrary app interaction is separate from mirroring.
- Protected content remains protected.

## Non-goals

- Reimplement Android window manager.
- Capture off-screen app content not rendered by the target app.
- Bypass secure-window restrictions.
- Build ASR/ring/semantic automation before viewport proof.
