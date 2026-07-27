# cuped variance reduction

**Language:** Python · **Sphere:** data-science · **Category:** Causal Inference & Experimentation

**Signature:** `(values: List[float]) → float`

## What it does

CUPED (Controlled-experiment Using Pre-Experiment Data).

In A/B tests, Y_post = metric post-treatment, Y_pre = metric pre-treatment.
CUPED adjusted metric = Y_post - theta * Y_pre, where theta = Cov(Y_pre, Y_post) / Var(Y_pre).
This removes covariate-driven noise, reducing the variance of the treatment effect estimate.
We measure actual variance reduction from CUPED vs naive difference.

## Guarantee

When it runs, cuped variance reduction guarantees abs(cuped_effect - true_effect) < abs(naive_effect - true_effect); variance_reduction > 0.1 (proven by run).

**Checkable constraints:**

- `variance_reduction > 0.1`
- `abs(cuped_effect - true_effect) < abs(naive_effect - true_effect)`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
