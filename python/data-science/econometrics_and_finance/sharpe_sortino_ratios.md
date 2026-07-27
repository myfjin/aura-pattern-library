# sharpe sortino ratios

**Language:** Python · **Sphere:** data-science · **Category:** Econometrics & Finance

**Signature:** `(returns: List[float], risk_free_rate: float) → float`

## What it does

Sharpe and Sortino ratios: risk-adjusted return metrics.

Sharpe = (ret - rf) / σ. Sortino = (ret - rf) / σ_downside where σ_downside
only counts downside (returns < target). Core claim: both computed; Sortino ≥
Sharpe (narrower denominator). Hand-verified on planted data.

## Guarantee

When it runs, sharpe sortino ratios guarantees sharpe > 0; sortino > 0; sortino >= sharpe - 0.01 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `sharpe > 0`
- `sortino > 0`
- `sortino >= sharpe - 0.01`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
