# mahalanobis distance

**Language:** Python · **Sphere:** data-science · **Category:** Optimization & Distances

**Signature:** `(point: Tuple[float, float], mean: Tuple[float, float], cov_inv: List[List[float]]) → float`

## What it does

DISTANCE METRIC: Mahalanobis Distance

Core idea: Euclidean distance treats all dimensions equally; Mahalanobis accounts
for covariance structure, scaling by the inverse covariance matrix. On correlated
data, Mahalanobis distance can reveal structure that Euclidean misses.

When to use: Multivariate outlier detection, anomaly detection on correlated data,
or whenever covariance structure is meaningful (e.g., finance, quality control).

## Guarantee

When it runs, mahalanobis distance guarantees abs(det) > 1e-12; mdist_self < 1e-10; mdist_perp > mdist_aligned (weak-grade: directional, proven by run).

**Checkable constraints:**

- `abs(det) > 1e-12`
- `mdist_self < 1e-10`
- `mdist_perp > mdist_aligned`
- `abs(edist_aligned - edist_perp) < 1e-06`
- `mdist_aligned >= 0`
- `mdist_perp >= 0`
- `abs(cov[0][1] - cov[1][0]) < 1e-10`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:**
- `compute_covariance_2d(points: List[Tuple[float, float]]) -> List[List[float]]`
- `matrix_invert_2x2(M: List[List[float]]) -> List[List[float]]`
- `mahalanobis_distance(point: Tuple[float, float], mean: Tuple[float, float], cov_inv: List[List[float]]) -> float`
- `euclidean_distance(p: Tuple[float, float], q: Tuple[float, float]) -> float`
**Valid input:** `points` non-empty list of 2D points (need at least 2 non-identical points for invertible covariance); `cov_inv` inverse of a 2×2 covariance matrix.
**Core:** Computes 2×2 covariance, inverts it, and evaluates Mahalanobis distance `√((x-μ)^T Σ⁻¹ (x-μ))`. Also provides Euclidean distance for comparison.
**Assert:** On 5 correlated points along `x≈y`, verifies self-distance ≈ 0, perpendicular direction is penalized more than aligned direction, and Euclidean treats them equally.
**⚠️ Defect:** Hard-coded for 2D only. The module name and docstring do not warn that all helpers are 2×2. Passing a 3D point or a larger covariance matrix will silently fail or produce nonsense. Additionally, `matrix_invert_2x2` uses `assert` instead of raising a proper exception for singular matrices.

---
*△ AURA Pattern Library — © Reality Optimizer*
