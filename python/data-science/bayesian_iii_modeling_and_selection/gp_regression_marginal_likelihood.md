# gp regression marginal likelihood

**Language:** Python · **Sphere:** data-science · **Category:** Bayesian III — Modeling & Selection

**Signature:** `(x: List[float], y: List[float], ls: float, noise: float) → float`

## What it does

Gaussian-process regression: the marginal likelihood peaks at the true lengthscale.

The log marginal likelihood  log p(y|ℓ) = −½ yᵀK⁻¹y − ½ log|K| − n/2 log2π  (K the RBF
kernel + noise) trades data-fit against complexity; scanned over ℓ it peaks near the
lengthscale that GENERATED the data. Solved honestly with a Cholesky factorization (the
yᵀK⁻¹y and log|K| both come from L), not a diagonal shortcut. Core claim: on data drawn
from a GP with lengthscale ℓ_true, the marginal likelihood is maximized near ℓ_true.

## Guarantee

When it runs, gp regression marginal likelihood guarantees abs(best_ls - ls_true) <= 0.5 (proven by run).

**Checkable constraints:**

- `abs(best_ls - ls_true) <= 0.5`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
