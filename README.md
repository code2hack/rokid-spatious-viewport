# Rokid Spatious Viewport

Status: **spatial viewport pivot accepted**  
Primary development device: **u4090**  
Android companion target: **Samsung Fold 6**  
Implementation language preference: **Kotlin**

Rokid Spatious Viewport turns Rokid glasses into a head-tracked viewport into mirrored Android app/display surfaces.

The Android companion app captures a user-approved Android display or app window, maps the captured frame into a padded virtual canvas, and eventually streams a tiled overscan region to the Rokid-side app. The Rokid app crops locally from the cached region according to head pose and shows a fixed center reticle.

Termux is now only a future/flagship mirrored-app use case. The project is no longer primarily a Termux bootstrap or terminal project.

## Current implementation order

The PM should follow this order:

1. **Clean root/meta docs** so all durable docs match the spatial viewport pivot.
2. **Create a Kotlin Android project skeleton**.
3. **Add a pure viewport geometry module with tests**.
4. **Add a MediaProjection capture proof** after the Android skeleton and geometry module exist.

Do not start with Rokid SDK, ASR, Bluetooth ring, Termux-specific logic, OCR, semantic app control, or AccessibilityService.

## Project control files

| File | Purpose |
|---|---|
| `AGENTS.md` | Repository entry instructions for PM and worker agents. |
| `docs/codex/START_PROMPT.md` | Starting prompt for the PM Codex session. |
| `docs/codex/PM_ORCHESTRATION.md` | Explicit PM orchestration and worker assignment guide. |
| `docs/codex/NEXT_IMPLEMENTATION_DECISIONS.md` | Current implementation-order decisions. |
| `docs/PROJECT_PLAN.md` | Spatial viewport product and architecture plan. |
| `docs/WORK_BREAKDOWN.md` | Phase-by-phase work breakdown. |
| `docs/adr/` | Accepted architecture decisions. |
| `PROJECT_KERNEL.md` | Durable project kernel and constraints. |
| `PRODUCT_SPEC.md` | Current product specification. |
| `FEATURE_GRAPH.yaml` | Current feature graph. |
| `PHASE_PLAN.md` | Current phase plan. |

## PM bootstrap

A PM Codex session should start with:

```text
Read AGENTS.md and follow the PM/integrator instructions.
```

The PM should then read `docs/codex/NEXT_IMPLEMENTATION_DECISIONS.md` before coding or assigning workers.

## First technical breakthrough

```text
Kotlin Android skeleton
→ pure viewport geometry model/tests
→ MediaProjection capture proof
→ captured frame on padded virtual canvas
→ viewport pan over that canvas
→ fixed center reticle
→ overscan cache prototype
```

## Hard boundaries

- Do not bypass `FLAG_SECURE` or protected content.
- Do not persist captured frames by default.
- MediaProjection is display-only; app control is a separate optional future layer.
- AccessibilityService interaction requires explicit approval.
- Spark is out of scope for this phase.
