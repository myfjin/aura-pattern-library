# post stratification variance

**Language:** Python · **Sphere:** data-science · **Category:** Experiments II

**Signature:** `(t: List[int], y: List[float]) → Tuple[float, float]`

## What it does

Post-stratification variance reduction: stratify AFTER observing data, using prognostic covariate.

On a prognostic covariate (correlated with outcome but NOT treated), stratifying reduces
ATE estimator variance. Core claim: post-stratifying on prognostic covariate cuts variance
by measured fraction vs simple difference-in-means.

## Guarantee

When it runs, post stratification variance guarantees abs(ate_simple - ate_post) < 0.3; var_post < var_simple; reduction > 0.15 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `abs(ate_simple - ate_post) < 0.3`
- `var_post < var_simple`
- `reduction > 0.15`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
