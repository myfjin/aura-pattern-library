# stratified split

**Language:** R · **Sphere:** R · **Category:** Multivariate & Applied Modeling

## What it does

Stratified Train-Test Split
Implements stratified split preserving class proportions; proportions asserted within tolerance
Use when: maintaining class balance in train-test split

## Guarantee

When it runs, stratified split guarantees all.equal(as.numeric(prop_train), as.numeric(prop_orig), tolerance = 0.05); all.equal(as.numeric(prop_test), as.numeric(prop_orig), tolerance = 0.05) (proven by run).

**Checkable constraints:**

- `all.equal(as.numeric(prop_train), as.numeric(prop_orig), tolerance = 0.05)`
- `all.equal(as.numeric(prop_test), as.numeric(prop_orig), tolerance = 0.05)`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — reseed (validator v1.9)
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** Top-level script (no function wrapper).
**Valid input:** No params; y = factor(60 pos / 40 neg), split_prop=0.8 fixed.
**Core:** Stratified train/test split: within each class level, sample `floor(n_level·0.8)` for train, remainder to test — preserving class proportions in both splits.
**Assert:** `all.equal` of train & test class proportions to the original, tol=0.05.
**⚠️ Defect:** `floor` rounding can drift proportions for small/odd strata (exact here, not guaranteed generally). Final index vectors are built class-by-class (`c()`-growth) and **not shuffled**, so train/test rows come out grouped by class — order-dependent downstream code could be affected. No handling for a class too small to split.

---
*△ AURA Pattern Library — © Reality Optimizer*
