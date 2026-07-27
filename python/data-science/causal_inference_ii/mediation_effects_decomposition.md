# mediation effects decomposition

**Language:** Python · **Sphere:** data-science · **Category:** Causal Inference II

**Signature:** `(x_vals: ?, y_vals: ?) → float`

## What it does

Mediation analysis: decompose a total effect into direct + indirect via a mediator.

Linear model X→M→Y. Total = direct (X→Y holding M) + indirect (X→M→Y). Product method:
indirect = β(X→M) × β(M→Y | X). The M→Y coefficient MUST be the partial (multiple-
regression) coefficient adjusting for X — using the X-coefficient here instead silently
SWAPS direct and indirect.
Core claim: planted linear system recovered — total≈7, direct≈1, indirect≈6.

## Guarantee

When it runs, mediation effects decomposition guarantees abs(total - 7.0) < 0.5; abs(direct - 1.0) < 0.5; abs(indirect - 6.0) < 0.7 (proven by run).

**Checkable constraints:**

- `abs(total - 7.0) < 0.5`
- `abs(direct - 1.0) < 0.5`
- `abs(indirect - 6.0) < 0.7`
- `abs(direct + indirect - total) < 1e-06`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
