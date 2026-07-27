# bootstrap confidence interval

**Language:** Python · **Sphere:** data-science · **Category:** Statistics & Testing

**Signature:** `(data: List[float], n_boots: int, ci: float) → Tuple[float, float]`

## What it does

Bootstrap Confidence Interval for Sample Mean

Core idea: Resample the observed data WITH replacement many times to build an empirical
distribution of sample statistics. Extract quantiles to form a 95% confidence interval
without assuming normality.

When to use: You have a sample and want a CI for the mean without parametric assumptions,
especially when the sample size is small or the data is non-normal.

## Guarantee

When it runs, bootstrap confidence interval guarantees lower < true_mean < upper; upper - lower > 0; upper - lower < 30 (proven by run).

**Checkable constraints:**

- `lower < true_mean < upper`
- `upper - lower > 0`
- `upper - lower < 30`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `def bootstrap_ci(data: List[float], n_boots: int = 10000, ci: float = 0.95) -> Tuple[float, float]:`
**Valid input:** `data` is a non-empty list of numbers; `n_boots` > 0; `ci` ∈ (0, 1).
**Core:** Non-parametric percentile bootstrap for the sample mean. Resamples the observed data with replacement many times, computes the mean of each resample, sorts the bootstrap means, and returns the quantile-based confidence interval.
**Assert:** For a seeded normal sample with true mean 100, the 95% CI contains 100, has positive width, and the width is reasonably small.
**⚠️ Defect:** Uses a fixed percentile method rather than bias-corrected or accelerated intervals, so skewed data can produce poor coverage. The quantile indices are computed with `int()` truncation, which can underestimate coverage for small `n_boots` and extreme `ci`.

---
*△ AURA Pattern Library — © Reality Optimizer*
