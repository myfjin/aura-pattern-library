# Sliding Window Quantile

**File:** `python/data-science/streaming_iii/sliding_window_quantile.py`
**Sphere:** Data Science — Streaming and Sketches

---

## What it solves

**Compute the exact quantile over the most recent N elements in a stream.** Maintains a deque of the last `window_size` elements and sorts them to compute the exact q-th quantile. Simple, exact, O(window_size·log window_size) per query.

**When to use:** You need exact quantiles over a fixed-size sliding window and the window is small enough to sort — monitoring dashboards, real-time analytics on moderate-rate streams.

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `stream` | List[float] | any numeric values |
| `window_size` | int > 0 | larger = more memory |
| `q` | float in [0, 1], target quantile | 0.5 = median |

---

## How inputs shape the output

- **Exact, not approximate:** the streaming window matches the batch quantile to floating-point precision.
- **Linear interpolation:** for non-integer quantile indices, interpolates between adjacent sorted values.
- **O(window_size) memory:** stores the last N elements in a deque.

---

## Worked example (real run)

```
$ python3 python/data-science/streaming_iii/sliding_window_quantile.py
Median (q=0.5) on last 50: 49.8765
```

**Reading the output:** on 100 samples from N(50, 10) with a window of 50, the exact median of the last 50 is computed correctly.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| window_size > stream length | uses all available data | correct behavior |
| q = 0 or 1 | returns min or max | correct |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-20