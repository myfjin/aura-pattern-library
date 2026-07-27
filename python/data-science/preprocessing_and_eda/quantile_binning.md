# quantile binning

**Language:** Python · **Sphere:** data-science · **Category:** Preprocessing & EDA

**Signature:** `(data: List[float], n_bins: int) → List[int]`

## What it does

Quantile Binning Pattern.

Partitions a continuous numeric column into equal-frequency bins (quantile-based)
vs equal-width bins. Core idea: quantile binning preserves bin counts (roughly equal)
even on skewed data; equal-width creates imbalanced bins on skew.

When to use: discretizing continuous features, handling skewed distributions,
creating balanced categorical features, non-uniform binning.

## Guarantee

When it runs, quantile binning guarantees 15 <= count <= 35; first_half > second_half * 1.5; len(set(quantile_bins)) == n_bins (weak-grade: directional, proven by run).

**Checkable constraints:**

- `15 <= count <= 35`
- `first_half > second_half * 1.5`
- `len(set(quantile_bins)) == n_bins`
- `len(set(equal_bins)) == n_bins`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
