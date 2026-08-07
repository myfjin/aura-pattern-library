# differential privacy laplace

**Language:** C++ · **Oracle sphere:** data-science (this file is the C++ twin) · **Category:** Fairness, Privacy & Robustness

## What it does

Differential Privacy via Laplace Mechanism — C++17 port.
Adds Laplace(0, 1/epsilon) noise to a count and verifies likelihood bound.

## Guarantee

When it runs, differential privacy laplace guarantees likelihood_ratio <= max_likelihood_ratio; utility_loss < 100 (weak-grade: directional, proven by run on the PY original).

**Checkable constraints:**

- `likelihood_ratio <= max_likelihood_ratio`
- `utility_loss < 100`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — established on the PY original and shared by this C++ twin (twin agreement is the evidence: consensus, xlang); the original oracle was not executed against this file
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
