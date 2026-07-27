# fixed effects within

**Language:** Python · **Sphere:** data-science · **Category:** Econometrics & Finance

**Signature:** `(y: List[float], x: List[float]) → float`

## What it does

Fixed-effects estimator (within): removes time-invariant entity effects.

Panel data: y_it = α_i + β·x_it + ε_it. Within-estimator demeansdata per
entity, eliminating α_i. Core claim: pooled OLS biased, within unbiased.
Planted panel with entity effects.

## Guarantee

When it runs, fixed effects within guarantees abs(beta_within - beta_true) < 0.3; abs(beta_within - beta_true) < abs(beta_pooled - beta_true); beta_pooled > beta_true + 0.5 (proven by run).

**Checkable constraints:**

- `abs(beta_within - beta_true) < 0.3`
- `beta_pooled > beta_true + 0.5`
- `abs(beta_within - beta_true) < abs(beta_pooled - beta_true)`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
