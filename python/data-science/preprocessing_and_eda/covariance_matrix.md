# covariance matrix

**Language:** Python · **Sphere:** data-science · **Category:** Preprocessing & EDA

**Signature:** `(data: List[List[float]]) → List[List[float]]`

## What it does

Covariance Matrix Pattern.

Computes sample covariance between all numeric columns. Core idea: covariance
measures how two variables jointly vary (sign = direction of relationship,
magnitude = strength). Diagonal contains variance of each variable.

When to use: understanding variance structure, multivariate analysis, principal
component analysis setup, detecting correlations with magnitude awareness.

## Guarantee

When it runs, covariance matrix guarantees abs(cov_mat[i][j] - cov_mat[j][i]) < 1e-06; cov_mat[i][i] > 0; cov_mat[0][1] > 0 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `abs(cov_mat[i][j] - cov_mat[j][i]) < 1e-06`
- `cov_mat[i][i] > 0`
- `cov_mat[0][1] > 0`
- `cov_mat[1][0] > 0`
- `abs(cov_mat[0][2]) < abs(cov_mat[0][1])`
- `abs(cov_mat[0][0] - var_x) < 1e-06`
- `abs(cov_mat[1][1] - var_y) < 1e-06`
- `abs(cov_mat[2][2] - var_z) < 1e-06`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
