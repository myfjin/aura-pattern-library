# seasonal decomposition

**Language:** C++ · **Sphere:** data-science · **Category:** Time Series

**Signature:** `(series: List[float], window: int) → List[float]`

## What it does

Seasonal Decomposition (naive additive)
C++17 self-contained implementation.

## Guarantee

When it runs, seasonal decomposition guarantees len(trend) == len(series); len(seasonal) == len(series); len(residual) == len(series) (weak-grade: directional, proven by run on the PY original).

**Checkable constraints:**

- `len(trend) == len(series)`
- `len(seasonal) == len(series)`
- `len(residual) == len(series)`
- `trend_var < series_var`
- `between_season_var > 0`
- `residual_var < series_var`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — established on the PY original and shared by this C++ twin (twin agreement is the evidence: consensus, xlang); the original oracle was not executed against this file
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
