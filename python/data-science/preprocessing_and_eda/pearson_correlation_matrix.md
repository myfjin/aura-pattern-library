# pearson correlation matrix

**Language:** Python · **Sphere:** data-science · **Category:** Preprocessing & EDA

**Signature:** `(data: List[float]) → Tuple[float, float]`

## What it does

Pearson Correlation Matrix Pattern.

Computes pairwise Pearson correlation coefficients between all numeric columns
from scratch. Core idea: measure linear association; correlation is covariance
normalized by standard deviations. Symmetric matrix with 1s on diagonal.

When to use: exploratory data analysis to identify relationships, feature
selection (drop highly correlated features), multicollinearity detection.

## Guarantee

When it runs, pearson correlation matrix guarantees abs(corr_mat[i][i] - 1.0) < 1e-06; abs(corr_mat[0][1] - 1.0) < 1e-06; abs(corr_mat[1][0] - 1.0) < 1e-06 (proven by run).

**Checkable constraints:**

- `abs(corr_mat[i][i] - 1.0) < 1e-06`
- `abs(corr_mat[i][j] - corr_mat[j][i]) < 1e-06`
- `abs(corr_mat[0][1] - 1.0) < 1e-06`
- `abs(corr_mat[1][0] - 1.0) < 1e-06`
- `abs(corr_mat[0][2]) < 0.4`
- `abs(corr_mat[1][2]) < 0.4`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
