# Data Profiling Summary

**File:** `python/data-science/preprocessing_and_eda/data_profiling_summary.py`
**Sphere:** Data Science — Preprocessing and EDA

---

## What it solves

**Per-column profile of a mixed dataset: type inference, missing count, cardinality, min/max/mean for numeric, top values for categorical.** One-pass summary to understand data structure, missingness, range, and uniqueness without external libraries.

**When to use:** Exploratory data analysis, data quality checks, understanding dataset structure before modeling.

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `data` | List[List[Any]], rows of mixed types | |
| `column_names` | List[str], optional column names | |

---

## How inputs shape the output

- **Numeric columns get min, max, mean** — correct range and central tendency.
- **Categorical columns get top values and counts** — correct frequency analysis.
- **Missing counts are accurate** — the defining quality check.

---

## Worked example (real run)

```
$ python3 python/data-science/preprocessing_and_eda/data_profiling_summary.py
data_profiling_summary.py: PASS
```

**Reading the output:** age (numeric, 2 missing, min=25, max=42), city (categorical, 3 values, top=NYC), salary (numeric, 1 missing), employed (categorical, 2 values).

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| empty dataset | empty dict | correct |
| all missing values | cardinality 0, type unknown | correct |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-20