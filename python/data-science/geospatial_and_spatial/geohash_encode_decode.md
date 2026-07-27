# geohash encode decode

**Language:** Python · **Sphere:** data-science · **Category:** Geospatial & Spatial

**Signature:** `(lat: float, lon: float, precision: int) → str`

## Guarantee

When it runs, geohash encode decode guarantees len(gh) == prec; abs(dec_lat - lat) < lat_err + 0.001; abs(dec_lon - lon) < lon_err + 0.001 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `len(gh) == prec`
- `abs(dec_lat - lat) < lat_err + 0.001`
- `abs(dec_lon - lon) < lon_err + 0.001`
- `gh1 and gh2`
- `abs(dec_lat_fine - lat) < 0.0001`
- `abs(dec_lon_fine - lon) < 0.0001`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **hard** — positive, roundtrip, xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
