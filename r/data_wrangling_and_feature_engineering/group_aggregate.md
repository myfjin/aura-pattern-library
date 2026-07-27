# group aggregate

**Language:** R · **Sphere:** R · **Category:** Data Wrangling & Feature Engineering

## What it does

Group-by Aggregation (Multi-key)
Implements multi-key grouping via loops/split; verifies against aggregate()
Use when: summarizing data by multiple grouping variables

## Guarantee

When it runs, group aggregate guarantees all.equal(agg_manual$mean, agg_oracle$value, tolerance = 1e-08) (proven by run).

**Checkable constraints:**

- `all.equal(agg_manual$mean, agg_oracle$value, tolerance = 1e-08)`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — reseed (validator v1.9)
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** Top-level script (no function wrapper).
**Valid input:** A `data.frame` named `df` with columns `group1` (character), `group2` (numeric/coercible), and `value` (numeric).
**Core:** Creates a composite key `group1-group2`, loops over unique keys, and computes the mean of `value` per key using `rbind` accumulation. Verifies against `aggregate(value ~ group1 + group2, data=df, mean)`.
**Assert:** Manual aggregation values match the `aggregate()` oracle within tolerance.
**⚠️ Defect:** `rbind` inside a loop is quadratic and slow for many groups. No input validation: missing columns or wrong types raise uncontrolled errors. `as.numeric(parts[2])` silently coerces `group2` to numeric, which can introduce `NA` if the original values were not coercible without warning. It computes only the mean; no extensibility for other aggregations.

---
*△ AURA Pattern Library — © Reality Optimizer*
