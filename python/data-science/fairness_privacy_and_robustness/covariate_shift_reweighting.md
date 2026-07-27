# covariate shift reweighting

**Language:** Python · **Sphere:** data-science · **Category:** Fairness, Privacy & Robustness

**Signature:** `() → None`

## What it does

Covariate Shift Reweighting: correct train/test distribution mismatch.

Plants a covariate shift between train and test sets, estimates importance weights
from density ratio, and shows that reweighting corrects the bias while unweighted
model remains biased.

## Guarantee

When it runs, covariate shift reweighting guarantees mse_weighted < mse_unweighted (weak-grade: directional, proven by run).

**Checkable constraints:**

- `mse_weighted < mse_unweighted`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
