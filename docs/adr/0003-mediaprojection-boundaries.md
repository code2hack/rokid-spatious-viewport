# ADR 0003 — MediaProjection Boundaries and App Mirroring Rules

## Status

Accepted for initial architecture.

## Context

The project wants to mirror app/display surfaces from Android to Rokid glasses. Android MediaProjection is the official capture mechanism, but it has permission, session, and privacy constraints.

## Decision

Use MediaProjection as the only capture mechanism for arbitrary Android app/display pixels.

Support:

- Android 14+ user-selected app-window capture where available.
- Full-display capture fallback.
- Capture-size change handling.
- Projection stop/release handling.

Do not support:

- Bypassing secure content.
- Persisting frames by default.
- Silent capture without user consent.
- Pretending arbitrary app control is included in MediaProjection.

## Capture boundaries

- App screen sharing is user-selected by system UI.
- Android may restrict capture to default display for display capture.
- Projection tokens are session-scoped and should be treated as one-use for virtual display creation.
- `FLAG_SECURE` windows and sensitive views may be blank/hidden.
- App control requires an input bridge, likely an optional AccessibilityService.

## Consequences

The app must have clear UI for:

- Start capture.
- Stop capture.
- Active capture status.
- Permission/session errors.
- Secure-content blank regions.
- Interaction mode disabled/enabled.
