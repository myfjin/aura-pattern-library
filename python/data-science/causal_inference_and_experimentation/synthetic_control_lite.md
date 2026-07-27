# synthetic control lite

**Language:** Python · **Sphere:** data-science · **Category:** Causal Inference & Experimentation

**Signature:** `(pre_treated: List[float], pre_controls: List[List[float]]) → List[float]`

## What it does

Synthetic Control Method (Lite).

A treated unit's outcome is compared to a weighted average of control units.
Weights are chosen to match the treated unit's pre-intervention trends.
Post-intervention, any gap between treated and synthetic control is the treatment effect.
We plant pre-period trends and a treatment shock; SC recovers the gap.

## Guarantee

When it runs, synthetic control lite guarantees abs(sum(weights) - 1.0) < 0.01; bias < 2.0; all((w >= 0 for w in weights)) (proven by run).

**Checkable constraints:**

- `bias < 2.0`
- `all((w >= 0 for w in weights))`
- `abs(sum(weights) - 1.0) < 0.01`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
