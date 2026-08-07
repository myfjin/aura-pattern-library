# partial dependence data

**Language:** Python · **Sphere:** data-science · **Category:** Model Understanding & Tuning

**Signature:** `(X: List[List[float]], y: List[float]) → Tuple[float, List[float]]`

## What it does

Partial Dependence Plot (PD) — Data Generation

Core idea: For each feature, marginalize over other features and plot the average model
prediction as that feature varies. Linear features show monotone curves; noise features show flat.

When to use: You want to understand the marginal effect of a feature on predictions, holding
other features constant in aggregate.

## Guarantee

When it runs, partial dependence data guarantees is_monotone_increasing(pd_f1); is_flat(pd_f2) (weak-grade: directional, proven by run).

**Checkable constraints:**

- `is_monotone_increasing(pd_f1)`
- `is_flat(pd_f2)`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
