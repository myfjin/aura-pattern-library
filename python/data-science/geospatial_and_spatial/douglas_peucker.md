# douglas peucker

**Language:** Python · **Sphere:** data-science · **Category:** Geospatial & Spatial

**Signature:** `(points: List[Tuple[float, float]], epsilon: float) → List[Tuple[float, float]]`

## What it does

Douglas-Peucker polyline simplification: reduce point count while bounding deviation.

Core idea: find point with max distance to chord; if > epsilon, recurse on
both halves; otherwise remove all intermediate points. Output ⊂ input,
max deviation ≤ epsilon.

When to use: map rendering, trajectory compression, lossy path storage.

## Guarantee

When it runs, douglas peucker guarantees len(simp_gentle) < len(gentle); 2 <= len(simp_gentle) <= len(gentle); simp_line[0] == line[0] and simp_line[-1] == line[-1] (weak-grade: directional, proven by run).

**Checkable constraints:**

- `len(simp_gentle) < len(gentle)`
- `2 <= len(simp_gentle) <= len(gentle)`
- `len(simp_line) == 2`
- `simp_line[0] == line[0] and simp_line[-1] == line[-1]`
- `len(simp_corner_tight) >= 3`
- `2 <= len(simp_corner_loose) <= 4`
- `simp_tight[0] == tight[0] and simp_tight[-1] == tight[-1]`
- `simp_tight[i] in tight`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
