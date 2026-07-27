# quantile type7

**Language:** R · **Sphere:** R · **Category:** Distributions & Resampling

**Signature:** `(x: ?, p: ?) → ?`

## What it does

Quantile Type 7: R's default interpolation method (linear between order statistics)
Implements h=(n-1)*p, quantile = x_{floor(h)+1} + (h-floor(h))*(x_{floor(h)+2} - x_{floor(h)+1})
Core: for order statistics x_{(1)},...,x_{(n)}, interpolate at fractional indices
Planted: random sample n=20, compute quantiles [0.25, 0.5, 0.75, 0.95], match quantile(type=7)

## Guarantee

When it runs, quantile type7 guarantees all.equal(q_est, unname(q_oracle), tolerance = 1e-06) (proven by run).

**Checkable constraints:**

- `all.equal(q_est, unname(q_oracle), tolerance = 1e-06)`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **hard** — reseed_ref (validator v1.9)
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `quantile_type7 <- function(x, p)`
**Valid input:** `x` is a numeric vector of length at least 2; `p` is a probability in `[0, 1]` (the function is demonstrated with `p_vals = c(0.25, 0.5, 0.75, 0.95)`).
**Core:** Sorts `x` and computes R's type-7 quantile by linear interpolation between order statistics using `h = (n - 1) * p`.
**Assert:** Manual quantiles match `quantile(x, p, type=7)` within `1e-6`.
**⚠️ Defect:** No input validation: `p` outside `[0, 1]` causes out-of-bounds indexing silently or with a confusing subscript error; empty `x` or `length(x) == 1` can return `NA` or crash. `NA` values in `x` are sorted to the end and can produce `NA` quantiles without warning. The source sorts `x` both at top level and inside the function, doing redundant work. The function returns a single scalar even when called via `sapply`, so vectorized `p` is only supported by the caller, not the function itself.

---

**R-sphere batch 1: 13/13 patterns documented.** Verifier should check source at `/home/au/aura-pattern-library/r/` (canonical) or `/tmp/aura-review/aura-pattern-library/r/` (review copy). No Rscript on `.8`, so verification is doc-accuracy only: signatures, top-level script vs function, and defect claims vs source.

---
*△ AURA Pattern Library — © Reality Optimizer*
