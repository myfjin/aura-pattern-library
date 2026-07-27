# pca power iteration

**Language:** C++ · **Sphere:** data-science · **Category:** Core ML

**Signature:** `(X: List[List[float]]) → TupleType[List[List[float]], List[float]]`

## What it does

pca_power_iteration.cpp
Principal Component Analysis via power iteration (from scratch).

## Guarantee

When it runs, pca power iteration guarantees eigenvalues[0] > eigenvalues[1]; eigenvalues[0] > 2.0 (weak-grade: directional, proven by run on the PY original).

**Checkable constraints:**

- `eigenvalues[0] > eigenvalues[1]`
- `eigenvalues[0] > 2.0`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — established on the PY original and shared by this C++ twin (twin agreement is the evidence: hard, reseed_ref, xlang); the original oracle was not executed against this file
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `power_iterate(C, iters = 1000, tol = 1e-12)` → `list(vector, value)`; helper `align(v, oracle)`.
**Valid input:** `C` a symmetric (covariance) matrix; `iters` positive; `tol` small positive. In-script: n=300, 5 correlated features.
**Core:** Top eigenvector/eigenvalue via power iteration (normalize `w = Cv/‖Cv‖` to convergence), then Hotelling deflation `C − λ₁v₁v₁ᵀ` to get PC2. Compares vectors/eigenvalues to `prcomp` (sign-aligned).
**Assert:** `max|v − oracle| < 1e-3` for PC1 & PC2; relative eigenvalue error `< 1e-3`.
**⚠️ Defect:** Only the top-2 components are extracted; deflation accumulates numerical error for later PCs (fine at 2, degrades if extended). Power iteration converges slowly when the top two eigenvalues are close (near-degenerate spectra) — the fixed `iters=1000` cap could return an unconverged vector without erroring. Random init means run-to-run iteration count varies.

---
*△ AURA Pattern Library — © Reality Optimizer*
