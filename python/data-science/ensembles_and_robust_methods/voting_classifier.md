# voting classifier

**Language:** Python · **Sphere:** data-science · **Category:** Ensembles & Robust Methods

**Signature:** `(X: List[Tuple[float, float]], y: List[int], split_dim: int) → float`

## What it does

Voting Classifier with Multiple Weak Learners.

Voting combines predictions from multiple different base classifiers
using hard voting (majority vote) or soft voting (average probabilities).
The ensemble's accuracy typically exceeds the average individual accuracy.

Use when: combining diverse classifiers, leveraging different model strengths.

## Guarantee

When it runs, voting classifier guarantees voting_acc > avg_individual_acc (weak-grade: directional, proven by run).

**Checkable constraints:**

- `voting_acc > avg_individual_acc`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `hard_voting(X, classifiers) → list of int`
**Valid input:** `X: List[Tuple[float, float]]` — 2D features. `classifiers: List` of trained weak classifiers.
**Core:** Hard voting classifier. Train multiple threshold-based weak classifiers (each splits on a different feature: x₁, x₂, x₁-x₂). Predict by majority vote across all classifiers. Ensemble accuracy exceeds average individual accuracy.
**Assert:** On 2-class 2D synthetic data (40 per class, Gaussians at (2,2) and (8,8) with σ=1.5), voting accuracy > average individual accuracy.
**⚠️ Defect:** The `hard_voting` and `soft_voting` functions are identical — both use `sum(votes) / len(votes)` thresholded at 0.5 on binary predictions. True soft voting would average probability estimates, not binary votes. The "soft voting" here is just hard voting with a different name. Also, the test only checks that voting beats the average, not that it achieves a meaningful accuracy level.

---
*△ AURA Pattern Library — © Reality Optimizer*
