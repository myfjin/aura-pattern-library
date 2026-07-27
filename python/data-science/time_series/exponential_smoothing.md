# exponential smoothing

**Language:** Python · **Sphere:** data-science · **Category:** Time Series

**Signature:** `(series: List[float], alpha: float) → List[float]`

## Guarantee

When it runs, exponential smoothing guarantees len(ses) == len(series); ses[0] == series[0]; ses_var < raw_var (weak-grade: directional, proven by run).

**Checkable constraints:**

- `len(ses) == len(series)`
- `ses[0] == series[0]`
- `ses_var < raw_var`
- `len(levels) == len(series)`
- `len(trends) == len(series)`
- `levels[0] == series[0]`
- `avg_trend > 0`
- `len(ses_fcst) == 5`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
