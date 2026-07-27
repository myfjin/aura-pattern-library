# robust streaming mad

**Language:** Python · **Sphere:** data-science · **Category:** Streaming III

**Signature:** `(stream: List[float], outlier_idx: set, k: float) → Tuple[int, int, int]`

## What it does

Robust anomaly detection via the median / MAD rule.
Core idea: center on the median and scale by MAD (median absolute deviation, x1.4826 for
a normal consistency constant); flag points with a robust z-score |x-med|/(1.4826*MAD) > k.
Median and MAD have a 50% breakdown point, so a few gross outliers do not corrupt the
threshold the way mean/std would. The demo plants outliers at KNOWN indices and measures
detection against those exact indices (no separate re-planting).
When: online outlier flagging with a low false-positive rate under heavy contamination.

## Guarantee

When it runs, robust streaming mad guarantees tp == n_out; fp <= 3 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `tp == n_out`
- `fp <= 3`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
