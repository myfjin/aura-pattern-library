# mutual information matrix

**Language:** Python · **Sphere:** data-science · **Category:** Composed Tools

**Signature:** `(values: List[float], n_bins: int) → List[int]`

## What it does

Mutual-Information Matrix — the dependence heatmap Pearson cannot draw.

COMPOSED PATTERN: nonlinear_dependence_mi (Information Theory) x
pearson_correlation_matrix (Preprocessing/EDA) — embedding bridge 0.503,
found 2026-07-06. Every notebook on earth draws the Pearson heatmap; it is
blind to any relationship that is not monotone-linear. This tool computes the
SAME feature-by-feature matrix with normalized mutual information (binned),
side by side with |Pearson| — so y = x^2 lights up where the classic heatmap
shows nothing.

Use when: first-look EDA on features whose relationships may be nonlinear.

## Guarantee

When it runs, mutual information matrix guarantees PE['A']['B_linear'] > 0.7 and MI['A']['B_linear'] > 0.25; PE['A']['C_square'] < 0.15; MI['A']['C_square'] > 3 * MI['A']['D_noise'] and MI['A']['C_square'] > 0.2 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `PE['A']['B_linear'] > 0.7 and MI['A']['B_linear'] > 0.25`
- `PE['A']['C_square'] < 0.15`
- `MI['A']['C_square'] > 3 * MI['A']['D_noise'] and MI['A']['C_square'] > 0.2`
- `all((MI[a][b] == MI[b][a] for a in names for b in names))`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
