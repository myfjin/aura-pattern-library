# Windowed Distinct Count

**File:** `python/data-science/streaming_iii/windowed_distinct_count.py`
**Sphere:** Data Science — Streaming and Sketches

---

## What it solves

**Count the exact number of distinct elements in the most recent N items of a stream.** Maintains a deque of the last `window_size` elements and computes `len(set(window))` at query time. Simple, exact, O(window_size) memory.

**When to use:** You need exact distinct counts over a fixed-size sliding window and the window is small enough to store — real-time dashboards, monitoring unique users in the last hour, any "how many distinct values recently?" question.

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `stream` | List (any hashable type) | duplicates are fine |
| `window_size` | int > 0 | larger = more memory |

---

## How inputs shape the output

- **Exact, not approximate:** the streaming window matches the batch distinct count exactly.
- **O(window_size) memory:** stores the last N elements in a deque.
- **O(window_size) per query:** builds a set from the window each time.

---

## Worked example (real run)

```
$ python3 python/data-science/streaming_iii/windowed_distinct_count.py
Windowed distinct: 42, True: 42
```

**Reading the output:** on 200 random integers in [0, 50] with a window of 100, the streaming distinct count matches the exact batch count.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| window_size > stream length | uses all available data | correct |
| all identical values | distinct count = 1 | correct |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-20