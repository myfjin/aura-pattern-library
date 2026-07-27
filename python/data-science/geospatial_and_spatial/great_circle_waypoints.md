# great circle waypoints

**Language:** Python · **Sphere:** data-science · **Category:** Geospatial & Spatial

**Signature:** `(lat1: float, lon1: float, lat2: float, lon2: float, n_waypoints: int) → List[Tuple[float, float]]`

## What it does

Great-circle intermediate waypoints via spherical linear interpolation (slerp).

Core idea: interpolate along great circle arc between two points on Earth sphere.
Verify each waypoint's cumulative distance equals proportional share of total distance.

When to use: flight path generation, mapping geodetic routes, animation along globe.

## Guarantee

When it runs, great circle waypoints guarantees 340 < total_dist < 350; len(waypoints) == n_wp; abs(waypoints[0][0] - lat1) < 0.1 and abs(waypoints[0][1] - lon1) < 0.1 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `340 < total_dist < 350`
- `len(waypoints) == n_wp`
- `abs(waypoints[0][0] - lat1) < 0.1 and abs(waypoints[0][1] - lon1) < 0.1`
- `abs(waypoints[-1][0] - lat2) < 0.1 and abs(waypoints[-1][1] - lon2) < 0.1`
- `relative_error < 0.05`
- `error_fine < 0.01`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
