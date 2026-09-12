# Class Weights for Imbalanced Classification

**File:** `python/data-science/model_understanding_and_tuning/class_weight_imbalance.py`
**Sphere:** Data Science — Model Understanding and Tuning

---

## What it solves

**When classes are imbalanced, training loss can favor predicting the majority class.** Assigning higher weight to the minority class penalizes misclassification more, recovering minority recall.

**When to use:** Binary or multiclass classification with severe class imbalance, where you care about minority class performance.

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `X` | List[List[float]], feature vectors | |
| `y` | List[float], binary labels | |
| `class_weights` | Tuple[float, float], (weight_0, weight_1) | |

---

## How inputs shape the output

- **Weighted training recovers minority recall** — matches or beats unweighted.
- **Weighted recall > 0.1** — at least some minority recovery.
- **Inverse frequency weighting** — pos_weight = neg_count / pos_count.

---

## Worked example (real run)

```
$ python3 python/data-science/model_understanding_and_tuning/class_weight_imbalance.py
Unweighted: Precision 0.00%, Recall 0.00%
Weighted: Precision 25.00%, Recall 33.33%
✓ Class Weight Imbalance: PASS
```

**Reading the output:** unweighted logistic regression misses all minority samples. Weighted training recovers 33% recall.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| already balanced | weights have little effect | correct |
| extreme imbalance | weights may cause instability | needs careful tuning |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-20