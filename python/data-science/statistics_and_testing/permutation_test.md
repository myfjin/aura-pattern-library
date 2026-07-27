# permutation test

**Language:** Python · **Sphere:** data-science · **Category:** Statistics & Testing

**Signature:** `(group_a: List[float], group_b: List[float], n_perms: int) → Tuple[float, float]`

## What it does

Permutation Test for Two-Sample Difference of Means

Core idea: Under the null hypothesis (no group difference), group labels are exchangeable.
Randomly permute group assignments many times, compute the test statistic for each
permutation, and count how many are as extreme as the observed. The proportion is the p-value.

When to use: Test whether two groups differ without parametric assumptions. Works well for
small samples and non-normal data.

## Guarantee

When it runs, permutation test guarantees p_null > 0.05; p_alt < 0.05 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `p_null > 0.05`
- `p_alt < 0.05`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `def permutation_test(group_a: List[float], group_b: List[float], n_perms: int = 10000) -> Tuple[float, float]:`
**Valid input:** Both groups are non-empty lists of numbers.
**Core:** Two-sample permutation test for the difference of means. Shuffles the pooled data, splits at the original group-A size, recomputes the mean difference, and estimates a two-tailed p-value by the fraction of permutations with absolute difference at least as large as observed.
**Assert:** Two samples from the same normal distribution produce a high p-value; a sample shifted by +5 produces a low p-value.
**⚠️ Defect:** The exact permutation distribution is only approximated by random shuffling; the p-value can vary noticeably across runs for borderline cases. The function recomputes `len(group_b)` inside the loop unnecessarily but this is minor.

---
*△ AURA Pattern Library — © Reality Optimizer*
