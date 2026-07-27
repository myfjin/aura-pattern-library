# adaboost

**Language:** Python · **Sphere:** data-science · **Category:** Ensembles & Robust Methods

**Signature:** `(X: List[Tuple[float, float]], y: List[int], n_rounds: int) → List[Tuple]`

## What it does

AdaBoost Classification with Decision Stumps.

AdaBoost sequentially fits weak learners (decision stumps) by reweighting
training examples: samples misclassified by the current stump get higher
weight in the next round. The ensemble combines weak learners with weights
based on their accuracy.

Use when: iterative ensemble for classification, balancing examples hard to classify.

## Guarantee

When it runs, adaboost guarantees ada_acc > single_stump_acc (weak-grade: directional, proven by run).

**Checkable constraints:**

- `ada_acc > single_stump_acc`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `adaboost(X, y, n_rounds=10) → list of (stump, alpha)`
**Valid input:** `X: List[Tuple[float, float]]` — 2D features. `y: List[int]` with values 0 or 1. `n_rounds ≥ 1`.
**Core:** AdaBoost with decision stumps. Initialize sample weights wᵢ = 1/n. For each round: fit weighted stump (minimize weighted error), compute ε, set α = ½·ln((1-ε)/ε), reweight misclassified samples by exp(α), renormalize. Final prediction = sign(Σ αₜ·hₜ(x)).
**Assert:** On 2-class 2D synthetic data (40 per class, overlapping Gaussians at (4,4) and (6,6) with σ=2.5), ensemble accuracy > single stump accuracy.
**⚠️ Defect:** The `predict_ensemble` function converts stump predictions {0,1} to {-1,+1} for the weighted sum, but the conversion `1 if pred == 1 else -1` is fragile — if a stump ever returns a value other than 0 or 1 (e.g., due to a bug or extension), the sign flips silently. Also, the test only checks that AdaBoost beats a single stump, not that it achieves a meaningful accuracy level.

---
*△ AURA Pattern Library — © Reality Optimizer*
