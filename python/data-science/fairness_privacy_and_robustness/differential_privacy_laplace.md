# differential privacy laplace

**Language:** Python · **Sphere:** data-science · **Category:** Fairness, Privacy & Robustness

**Signature:** `() → None`

## What it does

Differential Privacy via Laplace Mechanism.

Implements ε-differential privacy using Laplace noise on a count query.
Verifies that the likelihood ratio of neighboring datasets is bounded by e^ε,
and measures utility loss against the true count.

## Guarantee

When it runs, differential privacy laplace guarantees likelihood_ratio <= max_likelihood_ratio; utility_loss < 100 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `likelihood_ratio <= max_likelihood_ratio`
- `utility_loss < 100`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
