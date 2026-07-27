# huber robust regression

**Language:** Python · **Sphere:** data-science · **Category:** Ensembles & Robust Methods

**Signature:** `(residual: float, delta: float) → float`

## What it does

Huber Loss Robust Regression.

Huber loss is a hybrid of squared loss (for small residuals) and absolute
loss (for large residuals). It reduces sensitivity to outliers compared to
OLS while staying smooth. Coefficients estimated under Huber loss are closer
to ground truth under heavy-tailed noise.

Use when: data with heavy-tailed noise, outlier robustness, smooth gradients.

## Guarantee

When it runs, huber robust regression guarantees huber_error < ols_error (weak-grade: directional, proven by run).

**Checkable constraints:**

- `huber_error < ols_error`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `fit_line_huber(X, y, delta=1.5, learning_rate=0.05, iterations=300) → (m, b)`
**Valid input:** `X: List[float]` non-empty. `y: List[float]` same length. `delta > 0`. `learning_rate > 0`.
**Core:** Huber loss regression via gradient descent. Huber loss: L(r) = ½r² for |r| ≤ δ, δ(|r| - ½δ) for |r| > δ. Gradient: g(r) = r for |r| ≤ δ, δ·sign(r) for |r| > δ. Initialized with OLS estimate. Adaptive learning rate: lr / (1 + iter/100).
**Assert:** On y = 2x + 1 with 50 points (80% N(0,0.5), 20% heavy-tailed outliers ±[5,20]), Huber slope error < OLS slope error.
**✔ Retrofitted:** a defect noted in the 2026-07-20 audit was corrected by the AURA-E retrofit pass; the current signed code reflects the fix.

---
*△ AURA Pattern Library — © Reality Optimizer*
