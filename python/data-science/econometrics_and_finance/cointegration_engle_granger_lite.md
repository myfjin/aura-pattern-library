# cointegration engle granger lite

**Language:** Python · **Sphere:** data-science · **Category:** Econometrics & Finance

**Signature:** `(y: List[float], x: List[float]) → Tuple[float, bool]`

## What it does

Engle-Granger cointegration test: detect a long-run equilibrium relationship.

Two I(1) series are cointegrated if their linear combination is I(0) (stationary).
The test is TWO-STEP: (1) regress y on x by OLS; (2) test the RESIDUALS for a unit
root (Dickey-Fuller). Stationary residuals ⇒ cointegrated. Correlation alone is NOT
a cointegration test — two independent random walks are routinely highly correlated
(spurious regression), which is exactly what the residual unit-root step rules out.
Core claim: a genuinely cointegrated I(1) pair is detected; independent walks are rejected.

## Guarantee

When it runs, cointegration engle granger lite guarantees not indep_detected; t_coint < t_indep - 2.0 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `coint_detected`
- `not indep_detected`
- `t_coint < t_indep - 2.0`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
