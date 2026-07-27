# feature scaling toolkit

**Language:** Python · **Sphere:** data-science · **Category:** Optimization & Distances

**Signature:** `(data: List[float]) → Tuple[List[float], float, float]`

## What it does

FEATURE SCALING: Min-Max, Z-Score, Robust Scaling

Core idea: Different scaling methods normalize features to comparable ranges.
Min-max scales to [0, 1]; z-score centers to mean=0, std=1; robust uses median/IQR
to resist outliers. Choose based on data distribution and algorithm requirements.

When to use: KNN, SVM, neural networks, or any algorithm sensitive to feature magnitude.
Verify output properties (bounds, mean, std) match expectations.

## Guarantee

When it runs, feature scaling toolkit guarantees abs(min(scaled_minmax) - 0.0) < 1e-10; abs(max(scaled_minmax) - 1.0) < 1e-10; abs(actual_mean - 0.0) < 1e-10 (proven by run).

**Checkable constraints:**

- `min(scaled_minmax) >= 0.0`
- `max(scaled_minmax) <= 1.0`
- `abs(min(scaled_minmax) - 0.0) < 1e-10`
- `abs(max(scaled_minmax) - 1.0) < 1e-10`
- `abs(actual_mean - 0.0) < 1e-10`
- `abs(actual_std - 1.0) < 1e-10`
- `all((math.isfinite(x) for x in scaled_robust))`
- `abs(zscore_outlier) > 1.0`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:**
- `min_max_scale(data: List[float]) -> Tuple[List[float], float, float]`
- `z_score_scale(data: List[float]) -> Tuple[List[float], float, float]`
- `robust_scale(data: List[float]) -> Tuple[List[float], float, float]`
- `verify_properties(scaled: List[float], ...) -> bool`
**Valid input:** `data` is a list of numbers (empty list allowed, returns empty/zero stats).
**Core:** Three feature scalers: min-max to `[0,1]`, z-score to zero mean/unit std, and robust `(x - median)/IQR`.
**Assert:** On data `[10,12,11,13,14,100]`, checks min-max bounds, z-score mean≈0 and std≈1, robust finite values, outlier ranking, and invertibility of min-max and z-score.
**⚠️ Defect:** `robust_scale` computes quartiles with naive index slicing (`n//4` and `3*n//4`) rather than a proper percentile method. For small or even-length data this can be quite inaccurate; the demo does not verify that the scaled robust values actually have median 0 or that the interquartile range is 1.

---
*△ AURA Pattern Library — © Reality Optimizer*
