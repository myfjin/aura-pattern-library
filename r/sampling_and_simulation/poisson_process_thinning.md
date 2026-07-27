# poisson process thinning

**Language:** R · **Sphere:** R · **Category:** Sampling & Simulation

**Signature:** `(t: ?) → ?`

## What it does

Poisson Process Thinning: inhomogeneous Poisson via thinning of homogeneous process
Implements Lewis-Shedler thinning: generate homogeneous PP, accept events with intensity ratio
Core: Λ(t) = ∫λ(s)ds (intensity envelope), thin with prob λ(t)/Λ_max at each point
Planted: λ(t) = 2 + sin(πt/T) on [0, T]; verify intensity ratio and inter-arrival times

## Guarantee

When it runs, poisson process thinning guarantees ks_homo$p.value > 0.05 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `ks_homo$p.value > 0.05`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **hard** — reseed_ref (validator v1.9)
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** Top-level script (no function wrapper).
**Valid input:** No params; T=4, λ_max=3.1, intensity `λ(t)=2+sin(πt/T)` fixed.
**Core:** Simulates an inhomogeneous Poisson process by thinning: generate a homogeneous process at rate λ_max (exponential gaps), keep each arrival with prob `λ(t)/λ_max`.
**Assert:** Homogeneous inter-arrivals `ks.test` vs pexp(λ_max) not rejected; reports #original vs #thinned.
**⚠️ Defect:** Only the **homogeneous** inter-arrivals are statistically verified — the **thinned** (inhomogeneous) result is *not* tested for the correct intensity (bin intensities are computed but never asserted against the empirical counts), so a wrong thinning probability would pass. Builds `arrivals`/`keep` via `c()` in a `while` loop → O(n²) reallocation.

---
*△ AURA Pattern Library — © Reality Optimizer*
