# Quantile Binning

**File:** `python/data-science/preprocessing_and_eda/quantile_binning.py`
**Sphere:** Data Science — Preprocessing and EDA

---

## What it solves

**Partition a continuous numeric column into equal-frequency bins (quantile-based) vs equal-width bins.** Quantile binning preserves roughly equal bin counts even on skewed data; equal-width creates imbalanced bins on skew.

**When to use:** Discretizing continuous features, handling skewed distributions, creating balanced categorical features.

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `data` | List[float], numeric values | |
| `n_bins` | int > 0, number of bins | |

---

## How inputs shape the output

- **Quantile bins are roughly equal-frequency** (15-35 per bin for 100 points, 4 bins).
- **Equal-width bins on skewed data are imbalanced** — first half > 1.5× second half.
- **All bins are used** — no empty bins.

---

## Worked example (real run)

```
$ python3 python/data-science/preprocessing_and_eda/quantile_binning.py
quantile_binning.py: PASS
```

**Reading the output:** on exponential-like skewed data with 4 bins, quantile binning gives ~25 per bin. Equal-width bins are heavily imbalanced (early bins packed).

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| n_bins > len(data) | some bins may be empty | needs more data |
| all identical values | all in one bin | correct |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-20