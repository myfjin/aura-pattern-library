# shapley value sampling

**Language:** C++ · **Sphere:** data-science · **Category:** Model Understanding & Tuning

**Signature:** `(features: List[float]) → float`

## What it does

Shapley Value Sampling (Monte Carlo Approximation)
C++17 self-contained implementation.

## Guarantee

When it runs, shapley value sampling guarantees max_error < 0.5; max_error < analytic_shapley(0, feature_values) * 0.3 (weak-grade: directional, proven by run on the PY original).

**Checkable constraints:**

- `max_error < 0.5`
- `max_error < analytic_shapley(0, feature_values) * 0.3`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — established on the PY original and shared by this C++ twin (twin agreement is the evidence: consensus, xlang); the original oracle was not executed against this file
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
