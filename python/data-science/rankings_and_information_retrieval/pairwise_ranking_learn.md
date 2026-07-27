# pairwise ranking learn

**Language:** Python · **Sphere:** data-science · **Category:** Rankings & Information Retrieval

**Signature:** `(x: float) → float`

## What it does

Pairwise Ranking via Logistic Regression.

Learn item ordering from pairwise comparisons: for each pair (i,j),
fit logistic regression on feature difference (f_i - f_j) to predict which ranks higher.
Verify on planted item order: learned model should recover the order
with high Kendall tau correlation vs truth.

## Guarantee

When it runs, pairwise ranking learn guarantees tau > 0.7; predicted_order == true_order or tau > 0.5 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `tau > 0.7`
- `predicted_order == true_order or tau > 0.5`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
