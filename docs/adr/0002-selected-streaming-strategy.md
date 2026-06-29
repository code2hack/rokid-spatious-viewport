# ADR 0002 — Use Tiled Canvas with Overscan Margin

## Status

Accepted for initial architecture.

## Context

A head-tracked viewport must feel responsive. If every head movement requires a round trip to the Android companion app, panning will feel delayed. Sending the full captured frame at full rate may be wasteful or infeasible depending on connection and resolution.

## Decision

Use Strategy C: tiled canvas with overscan margin.

The Android companion app sends a cached region larger than the visible Rokid viewport. The Rokid app crops locally within this cached region as the user's head moves. Android refreshes tiles when the viewport approaches cache edges and can bias tile prefetch toward predicted head direction.

## Initial implementation path

1. Full-frame local crop in simulator.
2. Full overscan-region update.
3. Tile grid abstraction.
4. Dirty tile updates.
5. Directionally predicted overscan.
6. Multi-resolution tiles.

## Consequences

- Rokid renderer needs a tile cache.
- Protocol must carry tile coordinates and frame metadata.
- Viewport geometry must be deterministic and shared.
- Debug overlays must show viewport, overscan, and cache regions.

## Open parameters

- Tile size: start with 512 × 512 unless testing suggests 256 × 256.
- Overscan margin: start with 0.75 × viewport size in both axes.
- Cache eviction: simple latest-frame cache first.
- Encoding: simple bitmap/JPEG/WebP/H.264 path can be tested; optimize later.
