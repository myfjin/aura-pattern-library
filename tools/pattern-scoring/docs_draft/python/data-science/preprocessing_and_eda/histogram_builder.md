# Histogram Builder

**File:** `python/data-science/preprocessing_and_eda/histogram_builder.py`
**Sphere:** Data Science — Preprocessing and EDA

---

## What it solves

**Build a histogram with equal-width bins and automatic bin-count selection (Sturges' rule).** k = ceil(log₂(n)) + 1 works well for normal data. Easy rule without parameter tuning.

**When to use:** Exploratory data analysis, visualizing distributions, detecting multimodality.

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `data` | List[float], numeric values | |
| `n_bins` | int, number of bins (None = auto) | |

---

## How inputs shape the output

- **Counts sum to n** — conservation of data.
- **Edges are ordered** — monotonic bin boundaries.
- **Bin count follows Sturges' rule** — k = ceil(log₂(n)) + 1.

---

## Worked example (real run)

```
$ python3 python/data-science/preprocessing_and_eda/histogram_builder.py
histogram_builder.py: PASS
```

**Reading the output:** bimodal data (two Gaussians at 20 and 60) produces a histogram with two substantial peaks and sparse center.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| empty data | empty result | correct |
| all identical values | single bin | correct |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-20