# One-Hot Encoding

**File:** `python/data-science/preprocessing_and_eda/one_hot_encoding.py`
**Sphere:** Data Science — Preprocessing and EDA

---

## What it solves

**Convert categorical features into binary indicators (one-hot vectors).** Represent each unique category value with a binary column per category, exactly one column = 1, rest = 0. Essential for feeding categorical data to algorithms that expect numeric input.

**When to use:** Preprocessing categorical columns before model training, feature engineering for tree-free algorithms.

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `data` | List[str], categorical values | |
| `handle_unknown` | str, 'error' or 'ignore' | |

---

## How inputs shape the output

- **Exactly one 1 per row** — the one-hot property.
- **Round-trip: decode matches original** — vocabulary is correct.
- **Unknown categories: 'error' raises, 'ignore' gives all zeros** — the defining behavior.

---

## Worked example (real run)

```
$ python3 python/data-science/preprocessing_and_eda/one_hot_encoding.py
one_hot_encoding.py: PASS
```

**Reading the output:** animals ["cat", "dog", "cat", "bird", "dog", "cat", "bird"] encode to 3-column vectors. Round-trip matches original. Unknown "elephant" with ignore mode gives all zeros.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| unknown category with handle_unknown='error' | ValueError | needs guard |
| empty data | empty vocabulary | correct |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-20