# hash join

**Language:** R · **Sphere:** R · **Category:** Data Wrangling & Feature Engineering

## What it does

Hash Join (Environment as Hashmap)
Implements join via environment hashmap; verifies against merge()
Use when: joining tables on keys and want explicit control

## Guarantee

When it runs, hash join guarantees all(result_manual$value1 == result_oracle$value1); all(result_manual$value2 == result_oracle$value2); nrow(result_manual) == nrow(result_oracle) (proven by run).

**Checkable constraints:**

- `nrow(result_manual) == nrow(result_oracle)`
- `all(result_manual$value1 == result_oracle$value1)`
- `all(result_manual$value2 == result_oracle$value2)`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — reseed (validator v1.9)
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** Top-level script (no function wrapper).
**Valid input:** Two `data.frame`s named `df1` (left) and `df2` (right), each with a column `key`.
**Core:** Builds an R `environment` hashmap from `df2$key` → `df2$value2`, then loops over `df1` rows and appends matches to a result data frame. Verifies against `merge(df1, df2, by="key")`.
**Assert:** Result row count and matched values equal the `merge()` oracle.
**⚠️ Defect:** Performs an inner join only: keys present only in `df1` are silently dropped with no indication. Duplicate keys in `df2` are silently overwritten in the environment hashmap, so the join is not duplicate-key-safe. No input validation on column existence or type. No function wrapper, so it cannot be parameterized.

---
*△ AURA Pattern Library — © Reality Optimizer*
