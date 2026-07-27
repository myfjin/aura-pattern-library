# cross validation leakage

**Language:** Python · **Sphere:** data-science · **Category:** Applied DS Practice

**Signature:** `(X: list[list[float]], y: list[int]) → list[float]`

## What it does

Cross-validation data leakage from preprocessing before splitting.

Feature selection fit on the FULL dataset before train-test split leaks
information from test into train, inflating CV scores. Correct approach:
fit feature selection inside each fold on training data only.

Use: detecting CV score inflation, validating proper cross-validation pipelines.

## Guarantee

When it runs, cross validation leakage guarantees mean_leaky > mean_correct; mean_leaky - mean_correct > 0.05 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `mean_leaky > mean_correct`
- `mean_leaky - mean_correct > 0.05`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `def univariate_correlation(X: list[list[float]], y: list[int]) -> list[float]:`, `def select_top_features(X: list[list[float]], y: list[int], k: int) -> list[int]:`, `def knn_classify(X_train: list[list[float]], y_train: list[int], X_test: list[list[float]], k: int = 3) -> list[int]:`, `def accuracy(y_true: list[int], y_pred: list[int]) -> float:`
**Valid input:** `X` non-empty, rectangular; `y` same length as `X`; `k >= 1`. Feature selection and k-NN operate on binary labels {0, 1}.
**Core:** Demonstrates data leakage: univariate feature selection fit on the full dataset (including the test fold) inflates CV accuracy compared to fitting feature selection inside each train fold. Uses k-NN and accuracy as a downstream classifier.
**Assert:** On 200 samples with 100 noise + 5 weak signal features, leaky CV accuracy exceeds train-only CV accuracy by at least 0.05; both scores are reported and compared.
**✔ Retrofitted:** a defect noted in the 2026-07-20 audit was corrected by the AURA-E retrofit pass; the current signed code reflects the fix.

---
*△ AURA Pattern Library — © Reality Optimizer*
