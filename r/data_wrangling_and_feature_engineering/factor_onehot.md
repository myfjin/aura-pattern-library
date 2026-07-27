# factor onehot

**Language:** R · **Sphere:** R · **Category:** Data Wrangling & Feature Engineering

## What it does

One-Hot Encoding from Factors
Implements one-hot from factor levels; column sums equal level counts; unseen-level policy
Use when: converting categorical to numeric features

## Guarantee

When it runs, factor onehot guarantees all.equal(as.numeric(col_sums), as.numeric(level_counts), tolerance = 1e-08); all(row_sums == 1); sum(unseen_vec) == 0 (proven by run).

**Checkable constraints:**

- `all.equal(as.numeric(col_sums), as.numeric(level_counts), tolerance = 1e-08)`
- `all(row_sums == 1)`
- `sum(unseen_vec) == 0`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — reseed (validator v1.9)
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** Top-level script (no function wrapper).
**Valid input:** A `factor` named `f` with explicit `levels`. The script constructs its own demo factor if `f` is absent.
**Core:** Builds a one-hot matrix by looping over factor levels and setting the matching column to 1 for each observation.
**Assert:** Column sums equal the level counts from `table(f)`; every row sums to exactly 1; an unseen level is represented by an all-zero row.
**⚠️ Defect:** No input validation: if `f` is not a factor, `levels(f)` may return `NULL` or character levels and the loop will silently produce an empty or wrong matrix. `NA` factor values cause `which(levels(f) == f[i])` to return `integer(0)`, so the corresponding row becomes all zeros without warning. The unseen-level "policy" is only demonstrated with a manually zeroed vector, not actually enforced by a reusable function.

---
*△ AURA Pattern Library — © Reality Optimizer*
