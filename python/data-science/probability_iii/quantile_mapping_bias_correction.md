# quantile mapping bias correction

**Language:** Python · **Sphere:** data-science · **Category:** Probability III

**Signature:** `(data_biased: List[float], data_reference: List[float]) → List[float]`

## What it does

Quantile mapping: correct distributional bias by matching quantiles.

Maps biased distribution onto reference via quantile alignment. Core claim:
post-correction quantiles match reference; planted shift corrected.

## Guarantee

When it runs, quantile mapping bias correction guarantees abs(corr_med - ref_med) < 1.0 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `abs(corr_med - ref_med) < 1.0`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
