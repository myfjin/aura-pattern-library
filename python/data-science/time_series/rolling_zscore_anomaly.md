# rolling zscore anomaly

**Language:** Python · **Sphere:** data-science · **Category:** Time Series

**Signature:** `(series: List[float], window: int, threshold: float) → Tuple[List[float], List[int]]`

## What it does

Rolling Z-Score Anomaly Detection

Detect anomalies using rolling-window z-scores. For each point, compute
the z-score within a rolling window: z = (x - window_mean) / window_std.
Flag points where |z| exceeds a threshold (e.g., 3) as anomalies.
Use for detecting sudden spikes or drops in streaming data.

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
