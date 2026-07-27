# walk forward validation

**Language:** Python · **Sphere:** data-science · **Category:** Time Series

**Signature:** `(series: List[float], initial_window: int, forecast_func: Callable[[List[float]], List[float]]) → Tuple[List[float], List[float]]`

## Guarantee

When it runs, walk forward validation guarantees len(actuals_mean) == len(preds_mean); len(actuals_mean) == len(series) - 30; mae_mean > 0 and mae_last > 0 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `len(actuals_mean) == len(preds_mean)`
- `len(actuals_mean) == len(series) - 30`
- `mae_mean > 0 and mae_last > 0`
- `isinstance(mae_mean, float) and isinstance(mae_last, float)`
- `series_mean - 3 * series_std < pred < series_mean + 3 * series_std`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
