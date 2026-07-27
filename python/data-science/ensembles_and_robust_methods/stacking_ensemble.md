# stacking ensemble

**Language:** Python · **Sphere:** data-science · **Category:** Ensembles & Robust Methods

**Signature:** `(X_base: List[List[float]], y: List[float]) → Tuple[float, float]`

## What it does

Stacking Ensemble with Meta-Learner.

Stacking trains a meta-learner on predictions from base models trained
via out-of-fold cross-validation. The meta-learner learns to combine the
base models' strengths, often outperforming the base models individually.

Use when: combining diverse base models, high-dimensional feature space, complex patterns.

## Guarantee

When it runs, stacking ensemble guarantees stack_acc > avg_base_acc (weak-grade: directional, proven by run).

**Checkable constraints:**

- `stack_acc > avg_base_acc`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **hard** — positive, xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `fit_stacking(X, y, base_models, k_folds=5) → (base_models, b0, coef)`
**Valid input:** `X: List[Tuple[float, float]]` — 2D features. `y: List[int]` binary. `k_folds ≥ 2`.
**Core:** Stacking with out-of-fold meta-features. Split data into k_folds. For each fold: train base models (threshold classifiers on x[0] and x[1]) on out-of-fold data, predict on held-out fold. Collect meta-features. Train linear meta-learner on meta-features. Final: retrain base models on full data.
**Assert:** On 2-class synthetic data (50 per class, Gaussians at (2,2) and (8,8) with σ=2.5), stacking accuracy > average base model accuracy.
**⚠️ Defect:** The meta-learner's `fit_linear_model` only uses `X_base[i][0]` (line 28) — it fits the slope using only the first base model's predictions. The second coefficient is always 0.0. So stacking effectively only uses one base model, defeating the purpose of combining diverse models. The test still passes because the single base model is good enough, but the ensemble isn't actually stacking.

---
*△ AURA Pattern Library — © Reality Optimizer*
