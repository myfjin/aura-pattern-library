# linear discriminant analysis

**Language:** Python · **Sphere:** data-science · **Category:** Clustering, Graph & Anomaly

**Signature:** `(m: List[List[float]]) → List[List[float]]`

## What it does

Linear Discriminant Analysis (LDA) from scratch.

Two-class dimensionality reduction: find the linear projection that maximizes
between-class variance relative to within-class variance. Core idea: compute class
means, pooled within-class scatter, then solve generalized eigenvalue problem.

Use when: projecting high-dimensional data to lower dims while preserving class separability.

## Guarantee

When it runs, linear discriminant analysis guarantees accuracy >= 0.9; weights[0] ** 2 + weights[1] ** 2 > 0 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `accuracy >= 0.9`
- `weights[0] ** 2 + weights[1] ** 2 > 0`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `lda_2d(points, labels) → (weights, threshold)`
**Valid input:** `points: List[Tuple[float, float]]` — 2D points. `labels: List[int]` — binary (0 or 1). At least 1 point per class.
**Core:** Two-class LDA in 2D. Compute class means, within-class scatter matrices S_w, between-class scatter S_b. Solve S_w⁻¹ S_b w = λw via power iteration on the 2×2 matrix. Projection threshold at midpoint of projected means.
**Assert:** On 2 Gaussian classes (30 pts each, means at (1,1) and (4,4), σ=0.5): classification accuracy ≥ 90%, weights non-zero.
**⚠️ Defect:** The power iteration for the 2×2 matrix uses a fixed initial vector [1.0, 1.0] with no random restart. If the true eigenvector is orthogonal to [1, 1] (e.g., [1, -1]), power iteration would converge slowly or not at all. The eigenvalue computation on line 52 is inside the loop but uses the updated `v`, which is correct but the indentation suggests it was meant to be after the loop. Also, the 2×2 matrix inverse returns identity if singular, silently hiding numerical issues.

---
*△ AURA Pattern Library — © Reality Optimizer*
