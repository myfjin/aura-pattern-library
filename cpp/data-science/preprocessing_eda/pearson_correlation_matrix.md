# pearson correlation matrix

**Language:** C++ · **Oracle sphere:** data-science (this file is the C++ twin) · **Category:** Preprocessing & EDA

## What it does

pearson_correlation_matrix.cpp
Pairwise Pearson correlation matrix from scratch.

## Guarantee

When it runs, pearson correlation matrix guarantees abs(corr_mat[i][i] - 1.0) < 1e-06; abs(corr_mat[0][1] - 1.0) < 1e-06; abs(corr_mat[1][0] - 1.0) < 1e-06 (proven by run on the PY original).

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
- **Independent oracle:** — established on the PY original and shared by this C++ twin (twin agreement is the evidence: consensus, xlang); the original oracle was not executed against this file
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
