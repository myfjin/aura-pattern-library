# acf pacf from scratch

**Language:** R · **Sphere:** R · **Category:** Time Series — Models & Autocorrelation

## What it does

ACF and PACF from Scratch: Durbin-Levinson algorithm for partial autocorrelation
Implements ACF directly and PACF via Durbin-Levinson recursion; verifies against acf()/pacf()
Core: ACF = γ_k / γ_0; PACF φ_{k,k} solved iteratively from Durbin-Levinson equations
Planted: AR(2) process with known structure, compute lags 1-10

## Guarantee

When it runs, acf pacf from scratch guarantees all.equal(acf_est, acf_oracle, tolerance = 1e-06); all.equal(pacf_est, pacf_oracle, tolerance = 1e-05) (proven by run).

**Checkable constraints:**

- `all.equal(acf_est, acf_oracle, tolerance = 1e-06)`
- `all.equal(pacf_est, pacf_oracle, tolerance = 1e-05)`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **hard** — reseed_ref (validator v1.9)
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** Top-level script (no function wrapper).
**Valid input:** No params; y = AR(2) sim (φ=0.6,−0.2), n=150, max_lag=10.
**Core:** Autocovariance γ_k, ACF ρ_k = γ_k/γ_0, and PACF via the Durbin-Levinson recursion (`φ_{k,k}` and the reflected `φ_{k,1:(k-1)}` update). Verifies against base `acf()` / `pacf()`.
**Assert:** `all.equal(acf_est, acf oracle, 1e-6)`; `all.equal(pacf_est, pacf oracle, 1e-5)`.
**⚠️ Defect:** Uses the **biased** autocovariance estimator (divides by `n`, not `n−k`) — this deliberately matches R's `acf()` default, but is biased low at large lags. Durbin-Levinson can be numerically unstable near a unit root. `max_lag` fixed; not a reusable function.

---
*△ AURA Pattern Library — © Reality Optimizer*
