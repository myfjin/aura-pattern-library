# tornado sensitivity

**Language:** Python · **Sphere:** data-science · **Category:** Simulation & Decision Science

**Signature:** `() → None`

## What it does

Tornado Sensitivity: one-at-a-time sensitivity analysis.

Simple profit model: profit = (revenue - cost - overhead).
OAT sensitivity varies each input by +/- 10% and measures profit impact.
Ranked bar (via sorted list) identifies the dominant driver.

## Guarantee

When it runs, tornado sensitivity guarantees overhead_impact > 0; cost_impact > 0 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `top_driver in ['price', 'volume']`
- `overhead_impact > 0`
- `cost_impact > 0`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `def tornado_sensitivity() -> None:`, `def profit(price: float, volume: float, cost: float, overhead: float) -> float:`
**Valid input:** Numeric inputs; `volume` ≥ 0 is implied for meaningful profit.
**Core:** Tornado (one-at-a-time) sensitivity analysis on a simple profit model. Each input is varied ±10% while others are held at base values, and the resulting profit impact is ranked to identify the dominant driver.
**Assert:** The top driver is either `price` or `volume`; both `cost` and `overhead` have nonzero impacts.
**⚠️ Defect:** The analysis is one-at-a-time, so it ignores interaction effects between variables. The ranking is based on absolute profit range, which conflates variable scale (e.g., `volume = 1000`) with true elasticity. No validation that base inputs are positive or that the model makes business sense.

---

## Category: survival_and_reliability

---
*△ AURA Pattern Library — © Reality Optimizer*
