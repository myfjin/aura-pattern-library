# Bayesian Two-Segment Changepoint

**File:** `python/data-science/probabilistic_modeling/bayesian_two_segment_changepoint.py`
**Sphere:** Data Science — Probabilistic Modeling

---

## What it solves

**Compare model evidence for no-change vs change-at-t via marginal likelihood.** Finds the planted change location by comparing the log-likelihood of a single-segment model vs a two-segment model split at each possible point. The Bayes factor favors the 2-segment model when a real change exists.

**When to use:** Quality control, structural break detection, time-series anomalies.

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `data` | List[float], time series | |
| `var` | float > 0, assumed noise variance | |

---

## How inputs shape the output

- **Detected split near the planted change** (within 5 indices of true split at 25).
- **Bayes factor favors 2-segment model** (log BF > 0) for data with a change.
- **No-change data has small |BF|** (< 3) — the defining guard against overfitting.

---

## Worked example (real run)

```
$ python3 python/data-science/probabilistic_modeling/bayesian_two_segment_changepoint.py
PASS
```

**Reading the output:** data with a mean shift at index 25 has the changepoint detected near 25 with strong Bayes factor. No-change data has small BF.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| split at edge | log-likelihood = -inf | too few points per segment |
| very small change | BF may not favor 2-segment | not enough signal |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-20