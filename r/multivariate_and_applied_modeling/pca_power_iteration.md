# pca power iteration

**Language:** R · **Oracle sphere:** data-science (this file is the R twin) · **Category:** Core ML

## What it does

PCA via Power Iteration (with deflation) — oracle-verified against prcomp()

Power iteration finds the dominant eigenvector of the covariance matrix; DEFLATION
(subtract lambda1 * v1 v1^T) removes it so the SAME iteration finds the second.
Two lessons this file carries from its own first draft:
- iid gaussian data has near-EQUAL eigenvalues (no structure): power iteration
converges slowly and any tolerance must be loose. Plant real factor structure
and the method converges fast and tight. Test data must contain the thing
the method claims to find.
- eigenvectors match the oracle up to a GLOBAL sign: align by dot product,
never compare abs() per element (that would accept mixed sign-flips that
are not the eigenvector at all).
Use when: understanding eigenvalue geometry; PCA without an SVD library.

## Guarantee

When it runs, pca power iteration guarantees eigenvalues[0] > eigenvalues[1]; eigenvalues[0] > 2.0 (weak-grade: directional, proven by run on the PY original).

**Checkable constraints:**

- `eigenvalues[0] > eigenvalues[1]`
- `eigenvalues[0] > 2.0`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — established on the PY original and shared by this R twin (twin agreement is the evidence: hard, reseed_ref, xlang); the original oracle was not executed against this file
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
