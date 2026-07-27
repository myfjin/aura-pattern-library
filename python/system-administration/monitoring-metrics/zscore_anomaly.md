# zscore anomaly

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 14 · Monitoring & metrics

**Signature:** `(value: int) → ?`

## What it does

zscore_anomaly: detect anomalies using z-score.

## Guarantee

When it runs, zscore anomaly guarantees anomalies[0][1] == 200; not is_anomaly; len(detector.get_anomalies()) == 0 (proven by run).

**Checkable constraints:**

- `not is_anomaly`
- `len(detector.get_anomalies()) == 0`
- `is_anomaly`
- `len(anomalies) == 1`
- `anomalies[0][1] == 200`
- `len(detector2.get_anomalies()) == 1`
- `len(detector2.get_anomalies()) == 2`
- `detector_low.add(50)`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
