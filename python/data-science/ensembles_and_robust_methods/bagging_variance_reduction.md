# bagging variance reduction

**Language:** Python · **Sphere:** data-science · **Category:** Ensembles & Robust Methods

**Signature:** `(x: float) → float`

## What it does

Bagging for Variance Reduction.

Bagging (bootstrap aggregating) trains many copies of an UNSTABLE base learner
on bootstrap resamples and averages them. The averaged predictor has markedly
lower variance across retrainings than a single base learner — that reduction,
measured at fixed test points over many independent training draws, is the
whole point of the method. (A stable learner like plain linear regression
barely benefits; instability is bagging's fuel.)

Use when: high-variance base learners (deep trees, stumps on small data),
prediction stability across retrainings matters.

## Guarantee

When it runs, bagging variance reduction guarantees bagged_var < 0.5 * single_var (weak-grade: directional, proven by run).

**Checkable constraints:**

- `bagged_var < 0.5 * single_var`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `bagging_predict(X_train, y_train, X_test, n_bags=50) → list of float`
**Valid input:** `X_train, y_train` from `make_training_set`. `n_bags ≥ 1`.
**Core:** Bootstrap aggregating. Generate n_bags bootstrap resamples of training data. Fit a decision stump (depth-1 tree, minimizing SSE) on each. Average predictions across all bags. Key claim: bagging reduces prediction variance across retrainings compared to a single stump.
**Assert:** On y = 2x + N(0,3) with 60 training points, measured over 30 independent retrainings at 5 fixed test points, bagging (25 stumps) variance < 50% of single stump variance.
**✔ Retrofitted:** a defect noted in the 2026-07-20 audit was corrected by the AURA-E retrofit pass; the current signed code reflects the fix.

---
*△ AURA Pattern Library — © Reality Optimizer*
