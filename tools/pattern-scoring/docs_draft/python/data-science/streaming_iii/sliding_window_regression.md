# Sliding Window Regression

**File:** `python/data-science/streaming_iii/sliding_window_regression.py`
**Sphere:** Data Science — Streaming and Sketches

---

## What it solves

**Track a time-varying regression coefficient on streaming data via windowed OLS.** Maintains a sliding window of (x, y) pairs and recomputes the OLS slope over the most recent window. When the underlying relationship changes (e.g., slope drifts from 2.0 to 0.5), the windowed estimate tracks the new regime while ignoring old data.

**When to use:** You need to detect and track non-stationary relationships — time-varying beta in finance, sensor calibration drift, any "is the relationship changing?" question.

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `stream` | List[Tuple[float, float]], (x, y) pairs | numeric only |
| `window_size` | int > 0 | larger = smoother, slower to adapt |

---

## How inputs shape the output

- **Windowed OLS:** recomputes the slope from scratch over each window — no incremental update, but exact.
- **Tracks regime changes:** when the slope drifts, the windowed estimate follows the new regime within one window length.
- **O(window_size) per step:** naive recomputation; fine for moderate window sizes.

---

## Worked example (real run)

```
$ python3 python/data-science/streaming_iii/sliding_window_regression.py
Final windowed slope: 0.5123
```

**Reading the output:** the stream has slope ≈ 2.0 for the first 100 points and slope ≈ 0.5 for the next 100. With a window of 50, the final estimate (~0.51) correctly reflects the second half's slope.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| window_size > stream length | uses all data | correct |
| constant x in window | division by near-zero | denominator clamped |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-20