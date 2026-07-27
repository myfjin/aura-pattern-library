# monte carlo var es

**Language:** Python · **Sphere:** data-science · **Category:** Simulation & Decision Science

**Signature:** `() → None`

## What it does

Monte Carlo VaR & ES: Value-at-Risk and Expected Shortfall on returns.

Computes Value-at-Risk (VaR) and Expected Shortfall (ES) on heavy-tailed synthetic returns.
Verifies ES >= VaR always, and empirical exceedance rate ≈ alpha (confidence level).

## Guarantee

When it runs, monte carlo var es guarantees var_95 < 0; es_95 < var_95; abs(es_95) >= abs(var_95) (weak-grade: directional, proven by run).

**Checkable constraints:**

- `var_95 < 0`
- `es_95 < var_95`
- `abs(es_95) >= abs(var_95)`
- `0.03 < exceedance_rate < 0.07`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `def monte_carlo_var_es() -> None:`
**Valid input:** None (self-contained with hardcoded 10,000 simulations and 5% confidence level).
**Core:** Monte Carlo estimation of Value-at-Risk (VaR) and Expected Shortfall (ES) on a heavy-tailed synthetic return distribution. VaR is the α-quantile of losses; ES is the average of losses worse than VaR.
**Assert:** VaR is negative (a loss); ES is more negative than VaR; absolute ES ≥ absolute VaR; empirical exceedance rate of VaR is near the 5% confidence level.
**⚠️ Defect:** ES is computed as the mean of returns *below* VaR, which for a discrete sample of size 10,000 includes exactly 500 points. This is the standard empirical ES but uses the full left tail rather than the conditional tail mean, which can be noisy. No parameterization of α, sample size, or return distribution.

---
*△ AURA Pattern Library — © Reality Optimizer*
