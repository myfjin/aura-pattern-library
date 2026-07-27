# shapley value sampling

**Language:** Python · **Sphere:** data-science · **Category:** Model Understanding & Tuning

**Signature:** `(features: List[float]) → float`

## What it does

Shapley Value Sampling (Monte Carlo Approximation)

Core idea: Estimate each feature's marginal contribution via random coalition sampling.
For a simple additive model, sampled Shapley values should match analytic per-feature contributions.

When to use: You want fair feature attribution that respects coalition marginal values, without
computing all 2^n coalitions exactly.

## Guarantee

When it runs, shapley value sampling guarantees max_error < 0.5; max_error < analytic_shapley(0, feature_values) * 0.3 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `max_error < 0.5`
- `max_error < analytic_shapley(0, feature_values) * 0.3`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
