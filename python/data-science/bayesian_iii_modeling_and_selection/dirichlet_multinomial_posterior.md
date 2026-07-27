# dirichlet multinomial posterior

**Language:** Python · **Sphere:** data-science · **Category:** Bayesian III — Modeling & Selection

**Signature:** `(counts: List[int], prior_alpha: float) → List[float]`

## What it does

Dirichlet-Multinomial: posterior concentrates on true category probabilities as n grows.

Core claim: posterior concentrates on true category probs as n grows.

## Guarantee

When it runs, dirichlet multinomial posterior guarantees error_large < error_small (weak-grade: directional, proven by run).

**Checkable constraints:**

- `error_large < error_small`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
