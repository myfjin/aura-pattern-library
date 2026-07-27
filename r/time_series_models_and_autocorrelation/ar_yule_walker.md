# ar yule walker

**Language:** R · **Sphere:** R · **Category:** Time Series — Models & Autocorrelation

## What it does

AR(p) via Yule-Walker Equations: solve from sample autocovariance
Implements γ_j = Σ φ_k * γ_{|j-k|} as linear system (Rγ = γ_acov); matches ar(method="yw")
Core: compute sample ACF γ, build Toeplitz matrix from lags 0..p-1, solve for φ coefficients
Planted: AR(2) with known φ=(0.7, -0.3), generate 200 samples, recover coefficients

## Guarantee

When it runs, ar yule walker guarantees all.equal(phi_yw, oracle_ar$ar, tolerance = 0.001); all.equal(oracle_ar$order, p) (proven by run).

**Checkable constraints:**

- `all.equal(phi_yw, oracle_ar$ar, tolerance = 0.001)`
- `all.equal(oracle_ar$order, p)`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **hard** — reseed_ref (validator v1.9)
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** Top-level script (no function wrapper).
**Valid input:** No params; AR(2) sim φ=(0.7,−0.3), n=200, order p=2.
**Core:** Estimates AR(2) coefficients via the Yule-Walker equations: builds the Toeplitz autocovariance matrix R and solves `R·φ = γ`. Verifies against `ar(method="yw")`.
**Assert:** `all.equal(φ_yw, ar()$ar, 1e-3)`; recovered order == p.
**⚠️ Defect:** Yule-Walker estimates are **biased toward stationarity** (shrink coefficients) in small samples. Order p=2 is fixed — the script assumes the true order, so it can't detect over/under-fitting. Uses the biased ACF (matching `ar`'s default).

---
*△ AURA Pattern Library — © Reality Optimizer*
