# sliding window regression

**Language:** Python · **Sphere:** data-science · **Category:** Streaming III

**Signature:** `(stream: List[Tuple[float, float]], window_size: int) → float`

## What it does

Sliding window regression: track time-varying coefficient on streaming data via windowed OLS.
Core idea: maintain running statistics in a window; recompute OLS coefficients as stream progresses.
When: detect and track non-stationary relationships (e.g., time-varying slope).

## Guarantee

When it runs, sliding window regression guarantees abs(final_slope - true_slope_second) < 0.5; abs(final_slope - true_slope_second) < 0.3 (proven by run).

**Checkable constraints:**

- `abs(final_slope - true_slope_second) < 0.5`
- `abs(final_slope - true_slope_second) < 0.3`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
