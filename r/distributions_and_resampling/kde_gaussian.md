# kde gaussian

**Language:** R · **Sphere:** R · **Category:** Distributions & Resampling

## What it does

Kernel Density Estimation (Gaussian KDE)
Implements gaussian KDE with Silverman bandwidth by hand; verifies against density()
Use when: estimating probability density and understanding kernel smoothing

## Guarantee

When it runs, kde gaussian guarantees all.equal(kde_vals, dens_grid, tolerance = 0.05) (proven by run).

**Checkable constraints:**

- `all.equal(kde_vals, dens_grid, tolerance = 0.05)`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **hard** — reseed_ref (validator v1.9)
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** Top-level script (no function wrapper).
**Valid input:** A numeric vector named `x`. The script generates a bimodal demo sample if `x` is absent.
**Core:** Computes Silverman's rule-of-thumb bandwidth and evaluates a Gaussian KDE on a regular grid using `dnorm()`.
**Assert:** Manual KDE values match the `density()` oracle (with the same bandwidth) within tolerance on the grid.
**⚠️ Defect:** Silverman's bandwidth assumes the data are roughly unimodal and Gaussian; it can oversmooth multimodal data. No input validation: `NA` values in `x` silently propagate through `var()` and `dnorm()`. `var(x)` uses the sample variance (denominator `n-1`), but Silverman's rule typically uses sample standard deviation with an adjusted constant — the script conflates the two. No function wrapper.

---
*△ AURA Pattern Library — © Reality Optimizer*
