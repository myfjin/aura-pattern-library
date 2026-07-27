# polygon area centroid

**Language:** Python · **Sphere:** data-science · **Category:** Geospatial & Spatial

**Signature:** `(vertices: List[Tuple[float, float]]) → Tuple[float, Tuple[float, float]]`

## What it does

Shoelace formula: polygon area and centroid from vertex coordinates.

Core idea: area via sum of cross products; centroid via weighted average.
Works for both convex and concave polygons (signed area can be negative).

When to use: geometry calculations, shape analysis, mass properties.

## Guarantee

When it runs, polygon area centroid guarantees abs(area_sq - 1.0) < 0.001; abs(cx_sq - 0.5) < 0.01 and abs(cy_sq - 0.5) < 0.01; abs(area_tri - 0.5) < 0.001 (proven by run).

**Checkable constraints:**

- `abs(area_sq - 1.0) < 0.001`
- `abs(cx_sq - 0.5) < 0.01 and abs(cy_sq - 0.5) < 0.01`
- `abs(area_tri - 0.5) < 0.001`
- `abs(cx_tri - 1 / 3) < 0.01 and abs(cy_tri - 1 / 3) < 0.01`
- `abs(area_l - 3.0) < 0.01`
- `0.3 < cx_l < 1.3 and 0.3 < cy_l < 1.3`
- `area_line < 0.001`
- `abs(area_sq_rev - area_sq) < 0.001`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
