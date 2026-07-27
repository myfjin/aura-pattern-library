# instrumental 2sls

**Language:** Python · **Sphere:** data-science · **Category:** Econometrics & Finance

**Signature:** `(y: List[float], x: List[float]) → float`

## What it does

Two-stage least squares (2SLS): correct inference with endogenous regressor.

Stage 1: x ~ z. Stage 2: y ~ x̂. Core claim: 2SLS recovers true coeff even
with endogeneity; OLS is biased. Planted endogenous x correlated with ε.

## Guarantee

When it runs, instrumental 2sls guarantees abs(beta_2sls_est - beta_true) < 0.5; beta_ols > beta_2sls_est + 0.2; beta_ols > beta_true + 0.3 (proven by run).

**Checkable constraints:**

- `abs(beta_2sls_est - beta_true) < 0.5`
- `beta_ols > beta_2sls_est + 0.2`
- `beta_ols > beta_true + 0.3`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
