# ols robust se white

**Language:** Python · **Sphere:** data-science · **Category:** Econometrics & Finance

**Signature:** `(y: List[float], X: List[List[float]]) → Tuple[List[float], List[float], List[float]]`

## What it does

OLS robust standard errors (White): correct inference under heteroskedasticity.

Naive SE assumes constant variance; White SE allows it to vary. Demonstrates:
heteroskedastic data, naive SE underestimates, White SE covers. Planted
heteroskedasticity; true parameter in White CI but not naive CI.

## Guarantee

When it runs, ols robust se white guarantees se_white[1] > 1.3 * se_naive[1]; all((s > 0 for s in se_naive + se_white)); 0.0 < beta[1] < 2.5 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `se_white[1] > 1.3 * se_naive[1]`
- `all((s > 0 for s in se_naive + se_white))`
- `0.0 < beta[1] < 2.5`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
