# Three-Way Stratified Split

**File:** `python/data-science/preprocessing_and_eda/three_way_stratified_split.py`
**Sphere:** Data Science — Preprocessing and EDA

---

## What it solves

**Partition a dataset into train/validation/test sets while preserving class proportions in all three splits.** Stratification ensures each split is representative of the full distribution — important for imbalanced data.

**When to use:** Classification datasets, ensuring all class proportions preserved, train-val-test evaluation protocols.

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `data` | List[tuple], samples | |
| `labels` | List[int], class labels | |
| `splits` | Tuple[float, float, float], fractions | must sum to ~1.0 |

---

## How inputs shape the output

- **Class proportions preserved within 5%** in all three splits.
- **All classes present in all splits** — no missing class in any split.
- **No overlap between splits** — train, val, test are disjoint.

---

## Worked example (real run)

```
$ python3 python/data-science/preprocessing_and_eda/three_way_stratified_split.py
three_way_stratified_split.py: PASS
```

**Reading the output:** from 70 class 0 and 30 class 1, the 60/20/20 split preserves the 70/30 proportion in train, val, and test. All splits contain both classes. No overlap.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| splits don't sum to 1 | ValueError | needs valid fractions |
| very small class | may not appear in all splits | needs minimum samples |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-20