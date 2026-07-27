# seasonal decomposition

**Language:** Python · **Sphere:** data-science · **Category:** Time Series

**Signature:** `(series: List[float], window: int) → List[float]`

## What it does

Seasonal Decomposition (Naive Additive)

Decompose a time series into trend, seasonal, and residual components using
naive additive decomposition: y_t = trend_t + seasonal_t + residual_t.
Trend extracted via centered moving average; seasonal via period-wise means.
Use to understand and remove seasonal patterns from data.

## Guarantee

When it runs, seasonal decomposition guarantees len(trend) == len(series); len(seasonal) == len(series); len(residual) == len(series) (weak-grade: directional, proven by run).

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
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
