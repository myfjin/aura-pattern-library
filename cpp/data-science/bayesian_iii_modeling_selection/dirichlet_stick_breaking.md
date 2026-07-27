# dirichlet stick breaking

**Language:** C++ · **Sphere:** data-science · **Category:** Bayesian III — Modeling & Selection

**Signature:** `(alpha: float, num_breaks: int) → List[float]`

## What it does

Dirichlet stick-breaking process — C++17 port.
Weights sum toward 1; higher concentration α yields more active clusters.

## Guarantee

When it runs, dirichlet stick breaking guarantees weight_sum > 0.9; mean_active_high > mean_active_low (weak-grade: directional, proven by run on the PY original).

**Checkable constraints:**

- `weight_sum > 0.9`
- `mean_active_high > mean_active_low`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — established on the PY original and shared by this C++ twin (twin agreement is the evidence: hard, positive, xlang); the original oracle was not executed against this file
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
