# one hot encoding

**Language:** Python · **Sphere:** data-science · **Category:** Preprocessing & EDA

## What it does

One-Hot Encoding Pattern.

Converts categorical features into binary indicators (one-hot vectors).
Core idea: represent each unique category value with a binary column per category,
exactly one column = 1, rest = 0. Essential for feeding categorical data to algorithms
that expect numeric input.

When to use: preprocessing categorical columns before model training, feature engineering
for tree-free algorithms, handling multi-class nominal features.

## Guarantee

When it runs, one hot encoding guarantees enc.n_features == 3; enc.vocabulary == {'bird': 0, 'cat': 1, 'dog': 2}; sum(row) == 1 (proven by run).

**Checkable constraints:**

- `enc.vocabulary == {'bird': 0, 'cat': 1, 'dog': 2}`
- `enc.n_features == 3`
- `sum(row) == 1`
- `decoded == animals`
- `unknown_result[0] == [0, 1, 0]`
- `unknown_result[1] == [0, 0, 0]`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
