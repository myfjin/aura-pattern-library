# bootstrap portfolio var

**Language:** Python · **Sphere:** data-science · **Category:** Econometrics & Finance

**Signature:** `(returns: List[float], confidence_level: float, num_bootstrap: int) → Tuple[float, float]`

## What it does

Portfolio Value-at-Risk via bootstrap: nonparametric tail-risk estimation.

VaR at confidence c is the (1−c) quantile of the RETURN distribution — the loss level
the portfolio exceeds only (1−c) of the time. It is a quantile of returns themselves,
NOT of the sampling distribution of the mean. The bootstrap here resamples returns,
takes the (1−c) quantile of each resample, and averages — giving a stable VaR estimate
(and, via the spread of resample quantiles, a CI). Core claim: bootstrap VaR matches the
empirical return quantile; VaR is negative (a loss).

## Guarantee

When it runs, bootstrap portfolio var guarantees abs(var_95 - empirical_q05) < 0.005; var_95 < 0; var_95 < -0.015 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `abs(var_95 - empirical_q05) < 0.005`
- `var_95 < 0`
- `var_95 < -0.015`
- `var_95 > -0.1`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
