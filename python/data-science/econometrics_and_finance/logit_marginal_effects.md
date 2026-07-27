# logit marginal effects

**Language:** Python · **Sphere:** data-science · **Category:** Econometrics & Finance

**Signature:** `(x: float, beta: float) → float`

## What it does

Logit marginal effects: average partial derivatives of predicted probability.

AME = E[dP/dx]. Core claim: analytical gradient matches finite-difference check.
Planted logit model; derivatives verified against numerical gradient.

## Guarantee

When it runs, logit marginal effects guarantees abs(ame_analytical - ame_numerical) < 0.01; ame_analytical > 0 (proven by run).

**Checkable constraints:**

- `abs(ame_analytical - ame_numerical) < 0.01`
- `ame_analytical > 0`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
