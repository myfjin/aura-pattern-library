# mvn cholesky

**Language:** R · **Sphere:** R · **Category:** Sampling & Simulation

## What it does

Multivariate Normal via Cholesky: Σ = LL', X = μ + L*Z with Z~N(0,I)
Implements Cholesky factorization and verifies against chol() built-in; sample cov matches Σ
Core: decompose covariance Σ, transform independent normals, verify sample covariance
Planted: 2x2 covariance [1, 0.6; 0.6, 1], μ=0; sample n=500, measure cov recovery

## Guarantee

When it runs, mvn cholesky guarantees all.equal(L, L_oracle, tolerance = 1e-06); all.equal(Sigma_sample, Sigma, tolerance = 0.15) (proven by run).

**Checkable constraints:**

- `all.equal(L, L_oracle, tolerance = 1e-06)`
- `all.equal(Sigma_sample, Sigma, tolerance = 0.15)`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — reseed (validator v1.9)
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** Top-level script (no function wrapper).
**Valid input:** No params; 2×2 Σ=[1,0.6;0.6,1], μ=0, n=500 fixed.
**Core:** Multivariate normal via Cholesky: hand-computes lower-triangular L (`L11=sqrt(Σ11)`, `L21=Σ21/L11`, `L22=sqrt(Σ22-L21²)`), checks against `t(chol(Σ))`, samples `X=Z·Lᵀ+μ`, compares sample covariance to Σ.
**Assert:** `all.equal(L, chol-oracle, tol=1e-6)`; sample cov `all.equal(Σ, tol=0.15)`.
**⚠️ Defect:** Hard-coded to the **2×2 case** — the Cholesky formula is not generalized to n×n, so it only works for this one covariance. No positive-definiteness check: if `Σ22-L21²<0`, `sqrt` yields NaN silently. Cov tolerance 0.15 is loose for n=500.

---
*△ AURA Pattern Library — © Reality Optimizer*
