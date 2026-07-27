# sharpe sortino ratios

**Language:** C++ · **Sphere:** data-science · **Category:** Econometrics & Finance

**Signature:** `(returns: List[float], risk_free_rate: float) → float`

## What it does

Sharpe and Sortino ratios: risk-adjusted return metrics.
C++17 self-contained implementation.

## Guarantee

When it runs, sharpe sortino ratios guarantees sharpe > 0; sortino > 0; sortino >= sharpe - 0.01 (weak-grade: directional, proven by run on the PY original).

**Checkable constraints:**

- `sharpe > 0`
- `sortino > 0`
- `sortino >= sharpe - 0.01`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — established on the PY original and shared by this C++ twin (twin agreement is the evidence: consensus, xlang); the original oracle was not executed against this file
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
