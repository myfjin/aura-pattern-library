# spatial radius join

**Language:** Python · **Sphere:** data-science · **Category:** Geospatial & Spatial

**Signature:** `(points: List[Tuple[float, float]], centers: List[Tuple[float, float]], radius: float, grid_size: float) → Tuple[List[Tuple[int, int]], int]`

## What it does

Radius join via grid bucketing: find all points-within-radius-of-centers pairs.

Core idea: grid bucket points and centers; for each center, check points in
nearby cells only. Equals brute force result but with far fewer distance checks
on dense point sets.

When to use: spatial clustering, nearest-neighbor search, network analysis.

## Guarantee

When it runs, spatial radius join guarantees len(grid_result) == len(bf_result); set(grid_result) == set(bf_result); grid_checks < bf_checks (weak-grade: directional, proven by run).

**Checkable constraints:**

- `len(grid_result) == len(bf_result)`
- `set(grid_result) == set(bf_result)`
- `grid_checks < bf_checks`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
