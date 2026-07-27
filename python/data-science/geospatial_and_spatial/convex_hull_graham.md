# convex hull graham

**Language:** Python · **Sphere:** data-science · **Category:** Geospatial & Spatial

**Signature:** `(points: List[Tuple[float, float]]) → List[Tuple[float, float]]`

## What it does

Graham scan: compute convex hull of a point set.

Core idea: sort points by polar angle from lowest point, use stack to
maintain left-turn invariant. Hull vertices are exactly the extremes.

When to use: bounding envelopes, distance metrics, collision bounds.

## Guarantee

When it runs, convex hull graham guarantees hull_set == corners; (0, 0) in hull_cloud or any((abs(p[0]) < 0.01 and abs(p[1]) < 0.01 for p in hull_cloud)) (weak-grade: directional, proven by run).

**Checkable constraints:**

- `len(hull) == 4`
- `hull_set == corners`
- `len(hull_tri) == 3`
- `len(hull_line) >= 2`
- `(0, 0) in hull_cloud or any((abs(p[0]) < 0.01 and abs(p[1]) < 0.01 for p in hull_cloud))`
- `len(hull_cloud) >= 4`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
