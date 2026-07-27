# interrupted time series

**Language:** Python · **Sphere:** data-science · **Category:** Causal Inference & Experimentation

**Signature:** `(times: List[int], Y: List[float], cutoff: int) → Tuple[float, float, float, float]`

## What it does

Interrupted Time Series (ITS) Segmented Regression.

Time series with a pre-intervention trend; at a cutoff, intervention introduces
a level change and/or slope change. Segmented regression detects both.
Y = β0 + β1*t + β2*intervention + β3*t*intervention + noise.
β2 = level change, β3 = slope change. We plant and recover both.

## Guarantee

When it runs, interrupted time series guarantees abs(level_change - true_level_change) < 2.0; abs(slope_change - true_slope_change) < 0.5 (proven by run).

**Checkable constraints:**

- `abs(level_change - true_level_change) < 2.0`
- `abs(slope_change - true_slope_change) < 0.5`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
