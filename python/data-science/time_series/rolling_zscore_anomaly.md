# rolling zscore anomaly

**Language:** Python · **Sphere:** data-science · **Category:** Time Series

**Signature:** `(series: List[float], window: int, threshold: float) → Tuple[List[float], List[int]]`

## Guarantee

When it runs, rolling zscore anomaly guarantees avg_normal_z < 1.5; avg_anomaly_z > 2.0 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `len(anomalies) > 0`
- `len(nearby_anomalies) > 0`
- `avg_normal_z < 1.5`
- `avg_anomaly_z > 2.0`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
