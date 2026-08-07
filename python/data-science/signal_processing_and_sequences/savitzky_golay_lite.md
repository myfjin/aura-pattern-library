# savitzky golay lite

**Language:** Python · **Sphere:** data-science · **Category:** Signal Processing & Sequences

**Signature:** `(window: List[float], poly_order: int) → Tuple[float, float, float]`

## What it does

Savitzky-Golay Filter (Local Polynomial Smoothing).

Fit a low-order polynomial (e.g., quadratic) to a rolling window.
Smoother than moving-average and preserves peak heights better than moving-average.
We verify that SG filter preserves peak heights while moving-average attenuates them.

## Guarantee

When it runs, savitzky golay lite guarantees sg_peak_error < 0.9; ma_peak_error > 1.1; sg_peak_error < 0.7 * ma_peak_error (weak-grade: directional, proven by run).

**Checkable constraints:**

- `sg_peak_error < 0.9`
- `ma_peak_error > 1.1`
- `sg_peak_error < 0.7 * ma_peak_error`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
