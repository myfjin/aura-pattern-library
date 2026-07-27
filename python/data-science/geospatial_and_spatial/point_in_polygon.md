# point in polygon

**Language:** Python · **Sphere:** data-science · **Category:** Geospatial & Spatial

**Signature:** `(point: Tuple[float, float], polygon: List[Tuple[float, float]]) → bool`

## What it does

Ray casting algorithm: test if a point is inside a polygon.

Core idea: cast a ray from point to infinity; count edge crossings.
Odd count = inside, even = outside. Handles concave and convex polygons.

When to use: geofencing, collision detection, geographic containment.

## Guarantee

When it runs, point in polygon guarantees point_in_polygon((0.5, 0.5), square); point_in_polygon((0.1, 0.1), square); point_in_polygon((0.9, 0.9), square) (weak-grade: directional, proven by run).

**Checkable constraints:**

- `point_in_polygon((0.5, 0.5), square)`
- `point_in_polygon((0.1, 0.1), square)`
- `point_in_polygon((0.9, 0.9), square)`
- `not point_in_polygon((2, 2), square)`
- `not point_in_polygon((-1, -1), square)`
- `not point_in_polygon((0.5, -1), square)`
- `point_in_polygon((0.5, 0.5), concave)`
- `point_in_polygon((0.5, 1.5), concave)`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
