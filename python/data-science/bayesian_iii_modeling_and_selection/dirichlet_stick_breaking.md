# dirichlet stick breaking

**Language:** Python · **Sphere:** data-science · **Category:** Bayesian III — Modeling & Selection

**Signature:** `(alpha: float, num_breaks: int) → List[float]`

## What it does

Dirichlet stick-breaking process: samples probabilities that sum to 1.

Weights sum→1; E[#active clusters] increases monotonically with α (concentration).
Core claim: weights sum→1; E[#active clusters] increases with α.

## Guarantee

When it runs, dirichlet stick breaking guarantees weight_sum > 0.9; mean_active_high > mean_active_low (weak-grade: directional, proven by run).

**Checkable constraints:**

- `weight_sum > 0.9`
- `mean_active_high > mean_active_low`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **hard** — positive, xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
