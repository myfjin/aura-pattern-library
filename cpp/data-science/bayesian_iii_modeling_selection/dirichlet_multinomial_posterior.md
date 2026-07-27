# dirichlet multinomial posterior

**Language:** C++ · **Sphere:** data-science · **Category:** Bayesian III — Modeling & Selection

**Signature:** `(counts: List[int], prior_alpha: float) → List[float]`

## What it does

Dirichlet-Multinomial posterior concentration — C++17 port.
Shows posterior mean error shrinks as sample size grows.

## Guarantee

When it runs, dirichlet multinomial posterior guarantees error_large < error_small (weak-grade: directional, proven by run on the PY original).

**Checkable constraints:**

- `error_large < error_small`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — established on the PY original and shared by this C++ twin (twin agreement is the evidence: consensus, xlang); the original oracle was not executed against this file
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
