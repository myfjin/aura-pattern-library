# Cross-Validation Data Leakage

**File:** `python/data-science/applied_ds_practice/cross_validation_leakage.py`
**Sphere:** Data Science — Applied DS Practice

---

## What it solves

**The silent score inflator.** You split data into train/test, but you did feature selection on the FULL dataset before splitting. That means the test set secretly helped choose the features — so your cross-validation score looks better than it should. This pattern demonstrates the leak: feature selection on all data inflates CV accuracy by ~0.05–0.10 compared to the honest approach (fit feature selection inside each fold on training data only).

**When to use:** Any time you do preprocessing (feature selection, scaling, imputation) before cross-validation. The rule is simple: anything that looks at the data must be inside the CV loop, not outside.

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `X` | list of `[float]` feature vectors | empty → ZeroDivision |
| `y` | list of int labels {0, 1} | — |
| `k` (top features) | int ≥ 1 | — |

---

## How inputs shape the output

- **Noise-to-signal ratio drives the leak size:** with 100 noise features and only 5 true features, the leaky selector picks features that happen to correlate with the test set by chance — inflating scores. More noise = bigger leak.
- **The leak is detectable:** the demo asserts `mean_leaky > mean_correct` and the gap exceeds 0.05. If your real pipeline shows a suspiciously high CV score, this pattern is the diagnosis.
- **k (number of features selected) matters:** selecting more features dilutes the leak (more noise features slip in), selecting fewer concentrates it.

---

## Worked example (real run)

```
$ python3 python/data-science/applied_ds_practice/cross_validation_leakage.py
Leaky CV (select on full data):   0.5625
Correct CV (select on train):     0.5000
Leakage inflation:                +0.0625
cross_validation_leakage.py PASS
```

**Reading the output:** the leaky pipeline scores 0.56 vs the honest 0.50 — a 12.5% relative inflation. The assert proves the leak is real and detectable.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| empty X | ZeroDivision in `univariate_correlation` | needs guard |
| single feature | works but degenerate | — |
| k > n_features | IndexError in list comprehension | needs guard |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-18 · evidence: `output/manual_audit_2026-07-19.csv`
