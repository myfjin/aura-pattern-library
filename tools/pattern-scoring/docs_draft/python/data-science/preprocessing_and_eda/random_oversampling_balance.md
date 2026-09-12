# Random Oversampling and SMOTE-Lite

**File:** `python/data-science/preprocessing_and_eda/random_oversampling_balance.py`
**Sphere:** Data Science — Preprocessing and EDA

---

## What it solves

**Rebalance imbalanced datasets by random oversampling (duplicate minority) and SMOTE-lite (interpolate between minority neighbors).** Majority class stays fixed; minority class is augmented to match majority size.

**When to use:** Imbalanced classification, oversampling minority before training, class balance restoration.

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `X` | List[List[float]], feature vectors | |
| `y` | List[int], binary labels | |
| `k` | int, neighbors for SMOTE | |
| `alpha_range` | Tuple[float, float], interpolation range | |

---

## How inputs shape the output

- **Classes are balanced after oversampling** — equal counts.
- **Majority class size unchanged** — only minority is augmented.
- **SMOTE generates synthetic samples** — more samples than original.

---

## Worked example (real run)

```
$ python3 python/data-science/preprocessing_and_eda/random_oversampling_balance.py
random_oversampling_balance.py: PASS
```

**Reading the output:** from 100 class 0 and 20 class 1, random oversampling produces 100 of each. SMOTE-lite also balances while generating synthetic interpolated samples.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| already balanced | returns original | correct |
| only one class | no minority to oversample | correct |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-20