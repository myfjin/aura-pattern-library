# Empirical Bayes Shrinkage (James-Stein)

**File:** `python/data-science/probabilistic_modeling/empirical_bayes_shrinkage.py`
**Sphere:** Data Science — Probabilistic Modeling

---

## What it solves

**Shrink group means toward the grand mean — total squared error beats raw group means (Stein's paradox measured).** Estimates the hyperparameter from data, then shrinks via Bayesian posterior. The positive-part James-Stein estimator (K−3 rule) provably dominates raw means in expectation for K ≥ 4.

**When to use:** Meta-analysis, small-group inference, estimation of many parameters.

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `groups` | List[List[float]], observations per group | |

---

## How inputs shape the output

- **Shrunken means are closer to grand mean than raw means** — the defining property.
- **Shrinkage beats raw means in aggregate SE** over 400 replications (Stein's paradox measured).
- **Homogeneous data shrinks harder** than heterogeneous data — the comparative property.

---

## Worked example (real run)

```
$ python3 python/data-science/probabilistic_modeling/empirical_bayes_shrinkage.py
replications: 400 · mean SE raw 1.234 vs shrunken 1.012 · shrinkage wins 62%
own-weight: heterogeneous 0.45 vs homogeneous 0.12
PASS
```

**Reading the output:** over 400 replications, shrinkage beats raw means in total squared error and wins >55% of individual datasets. Homogeneous data shrinks harder.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| K < 4 | (K−3) rule gives negative factor | needs at least 4 groups |
| all groups identical | shrinkage factor near 0 | correct — no heterogeneity |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-20