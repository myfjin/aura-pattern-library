# train test split kfold

**Language:** Python · **Sphere:** data-science · **Category:** Statistics & Testing

**Signature:** `(data: List, labels: List, test_size: float) → Tuple[List, List, List, List]`

## What it does

Train/Test Split and K-Fold Cross-Validation

Core idea: Split data into train/test subsets for model evaluation. Extend to k-fold CV
where data is divided into k folds; iterate k times, using each fold as test and the rest
for training, then average results.

When to use: Evaluate model performance with limited data, avoid overfitting estimates,
and get stable generalization metrics.

## Guarantee

When it runs, train test split kfold guarantees len(X_train) + len(X_test) == len(X); len(X_test) == int(len(X) * 0.2); all((len(X_tr) + len(X_te) == len(X) for X_tr, X_te, _, _ in folds)) (weak-grade: directional, proven by run).

**Checkable constraints:**

- `len(X_train) + len(X_test) == len(X)`
- `len(X_test) == int(len(X) * 0.2)`
- `len(folds) == 5`
- `all((len(X_tr) + len(X_te) == len(X) for X_tr, X_te, _, _ in folds))`
- `0 < avg_mse < 100`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `def train_test_split(data: List, labels: List, test_size: float = 0.2) -> Tuple[List, List, List, List]:`, `def kfold_split(data: List, labels: List, k: int = 5) -> List[Tuple[List, List, List, List]]:`, `def simple_mean_predictor(X_train: List, y_train: List) -> float:`, `def mean_squared_error(y_true: List, y_pred: List) -> float:`
**Valid input:** `data` and `labels` are equal-length lists; `0 < test_size < 1`; `k` is a positive integer dividing the dataset reasonably.
**Core:** Random train/test split and k-fold cross-validation split, plus a trivial mean predictor and MSE helper used for the demo assertions.
**Assert:** Train and test sizes match requested fractions; each fold partitions the full dataset; 5-fold CV runs without error and yields a positive, reasonable MSE.
**✔ Retrofitted:** a defect noted in the 2026-07-20 audit was corrected by the AURA-E retrofit pass; the current signed code reflects the fix.

---
*△ AURA Pattern Library — © Reality Optimizer*
