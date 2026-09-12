# Pearson Correlation Matrix

**File:** `python/data-science/preprocessing_and_eda/pearson_correlation_matrix.py`
**Sphere:** Data Science — Preprocessing and EDA

---

## What it solves

**Compute pairwise Pearson correlation coefficients between all numeric columns.** Correlation is covariance normalized by standard deviations. Symmetric matrix with 1s on diagonal. Measures linear association.

**When to use:** EDA to identify relationships, feature selection (drop highly correlated features), multicollinearity detection.

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `data` | List[List[float]], columns as lists | all same length |

---

## How inputs shape the output

- **Diagonal is all 1s** — correlation with self.
- **Matrix is symmetric** — corr(i,j) = corr(j,i).
- **Perfectly correlated variables have r = 1.0** — the defining property.
- **Independent variables have near-zero correlation** — < 0.4.

---

## Worked example (real run)

```
$ python3 python/data-science/preprocessing_and_eda/pearson_correlation_matrix.py
pearson_correlation_matrix.py: PASS
```

**Reading the output:** x and y (y=2x) have r=1.0. z (random) has near-zero correlation with x and y.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| < 2 points | ValueError | needs at least 2 points |
| zero variance in a column | correlation = 0 | correct |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-20