# copula gaussian lite

**Language:** Python · **Sphere:** data-science · **Category:** Probability III

**Signature:** `(rho: float, n: int) → Tuple[List[float], List[float]]`

## What it does

Gaussian copula: model dependence structure separately from marginals.

Copula C(u, v) = P(U ≤ u, V ≤ v) where U, V ~ uniform; independence is C = uv.
Core claim: rank correlation preserved under copula transform; planted copula recovered.

## Guarantee

When it runs, copula gaussian lite guarantees abs(rho_est - rho_true) < 0.2 (proven by run).

**Checkable constraints:**

- `abs(rho_est - rho_true) < 0.2`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
