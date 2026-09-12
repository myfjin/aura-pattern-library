# k-Nearest Neighbors Classifier

**File:** `python/data-science/core_ml/knn_classifier.py`
**Sphere:** Data Science — Core ML

---

## What it solves

**The laziest classifier that still works.** To classify a new point, find the k nearest training samples by Euclidean distance and predict the majority class among them. No training phase — the model IS the data. Prediction is expensive (O(n) per point) but the model is simple, non-linear, and often surprisingly effective.

**When to use:** Non-linear decision boundaries, small to medium datasets, quick prototypes. KNN is the first thing to try when you have no idea what your data looks like — if KNN works, there's signal; if it doesn't, the features probably need work.

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `X_train` | list of `[float]` feature vectors | empty → IndexError |
| `y_train` | list of int labels | length mismatch → IndexError |
| `k` | int ≥ 1, odd recommended to break ties | even → ties broken arbitrarily |

---

## How inputs shape the output

- **k is the smoothness knob:** k=1 → perfect on training, noisy on test (overfit); k=large → smooth boundaries, may underfit. The demo's k=5 with well-separated clusters (centers 5 units apart, σ=1) achieves >80% accuracy.
- **Distance metric matters:** Euclidean distance assumes all features are on the same scale. If one feature has a much larger range, it dominates — normalize first.
- **Class balance matters:** if one class has many more points, it dominates the vote. The demo uses equal class sizes (25 each) to avoid this.

---

## Worked example (real run)

```
$ python3 python/data-science/core_ml/knn_classifier.py
KNN_CLASSIFIER PASS: accuracy = 0.950, k = 5
```

**Reading the output:** 95% accuracy on a two-class problem with clusters centered at (0,0) and (5,5). The high accuracy reflects the clean separation — KNN shines when classes are well-separated in feature space.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| empty X_train | IndexError in `euclidean_distance` | needs guard |
| k > len(X_train) | works but may underperform | — |
| single class in y_train | always predicts that class | correct but useless |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-18 · evidence: `output/manual_audit_2026-07-19.csv`
