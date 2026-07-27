# table margins

**Language:** R · **Sphere:** R · **Category:** Nonparametric & Categorical

## What it does

Contingency Table with Margins
Implements table + margins by hand; verifies against table() + addmargins()
Use when: cross-tabulating categorical variables

## Guarantee

When it runs, table margins guarantees all(manual_table == oracle_table); all.equal(row_margins, c(table(x)), tolerance = 1e-08); all.equal(col_margins, c(table(y)), tolerance = 1e-08) (proven by run).

**Checkable constraints:**

- `all(manual_table == oracle_table)`
- `all.equal(row_margins, c(table(x)), tolerance = 1e-08)`
- `all.equal(col_margins, c(table(y)), tolerance = 1e-08)`
- `total == sum(manual_table)`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — reseed (validator v1.9)
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** Top-level script (no function wrapper).
**Valid input:** Two factor vectors `x` and `y` of equal length with explicit levels.
**Core:** Builds a contingency table by incrementing counts for each level combination, then computes row margins, column margins, and total by hand. Verifies against `table(x, y)` and `addmargins()`.
**Assert:** Manual table equals `table(x, y)` exactly; row and column margins equal the marginal tables; total equals sum of all counts.
**⚠️ Defect:** `which(levels_x == x[i])` fails silently when `x[i]` is `NA` or an unseen level, causing that observation to be dropped or mis-assigned. No validation that `x` and `y` are factors/characters of equal length. No function wrapper.

---
*△ AURA Pattern Library — © Reality Optimizer*
