# haversine bearing

**Language:** Python · **Sphere:** data-science · **Category:** Geospatial & Spatial

**Signature:** `(lat1: float, lon1: float, lat2: float, lon2: float, radius_km: float) → float`

## What it does

Haversine great-circle distance and initial bearing.

Core idea: compute geodetic distance between lat/lon points on Earth sphere,
and the initial compass bearing from first to second point.

When to use: routing, distance matrices on geographic coordinates.

## Guarantee

When it runs, haversine bearing guarantees 340 < d_london_paris < 346; 3935 < d_ny_la < 3950; 100 < b < 160 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `340 < d_london_paris < 346`
- `3935 < d_ny_la < 3950`
- `100 < b < 160`
- `b_north < 30`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
