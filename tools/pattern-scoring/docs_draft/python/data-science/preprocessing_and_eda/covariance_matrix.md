# Covariance Matrix

**File:** `python/data-science/preprocessing_and_eda/covariance_matrix.py`
**Sphere:** Data Science — Preprocessing and EDA

---

## What it solves

**Compute the sample covariance matrix between all numeric columns.** Covariance measures how two variables jointly vary (sign = direction, magnitude = strength). Diagonal contains variance of each variable.

**When to use:** Understanding variance structure, multivariate analysis, PCA setup, detecting correlations with magnitude awareness.

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `data` | List[List[float]], columns as lists | all same length |

---

## How inputs shape the output

- **Matrix is symmetric** — cov(i,j) = cov(j,i).
- **Diagonal is positive** (variances) — matches direct variance computation.
- **Positively correlated variables have positive covariance** — the defining property.

---

## Worked example (real run)

```
$ python3 python/data-science/preprocessing_and_eda/covariance_matrix.py
covariance_matrix.py: PASS
```

**Reading the output:** x and y (positively correlated) have positive covariance. z (independent) has lower covariance with x and y. Diagonal matches direct variance.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| < 2 rows | ValueError | needs at least 2 rows |
| column length mismatch | ValueError | all columns same length |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-20