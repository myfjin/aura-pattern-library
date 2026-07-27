# long wide reshape

**Language:** R · **Sphere:** R · **Category:** Data Wrangling & Feature Engineering

## What it does

Long-Wide Reshape (Both Directions)
Implements reshape manually both directions; round-trip identity + spot-check vs reshape()
Use when: transforming data layout

## Guarantee

When it runs, long wide reshape guarantees all.equal(long_manual$value, long_test$value, tolerance = 1e-08) (proven by run).

**Checkable constraints:**

- `all.equal(long_manual$value, long_test$value, tolerance = 1e-08)`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — reseed (validator v1.9)
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** Top-level script (no function wrapper).
**Valid input:** A `data.frame` named `long_df` with columns `id`, `time`, and `value`, where `time` takes exactly two distinct values.
**Core:** Manually reshapes long→wide by filling a matrix with `long_df$value` indexed by `id` and `time`, then reshapes wide→long by iterating rows and columns.
**Assert:** Round-trip long→wide→long reproduces the original `value` column within tolerance.
**⚠️ Defect:** `names(wide_manual) <- c("time_1")` is shorter than the number of columns (2), so R recycles the name with a warning, leaving the second column also named `time_1`. Hardcoded to exactly two time points; any other cardinality will fail or silently produce `NA`s. No input validation. The round-trip test does not verify the wide format itself is semantically correct, only that values can be recovered.

---
*△ AURA Pattern Library — © Reality Optimizer*
