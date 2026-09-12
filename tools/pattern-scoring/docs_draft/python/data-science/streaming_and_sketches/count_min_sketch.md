# Count-Min Sketch for Frequency Estimation

**File:** `python/data-science/streaming_and_sketches/count_min_sketch.py`
**Sphere:** Data Science — Streaming and Sketches

---

## What it solves

**Count the frequency of every item in a massive stream, using almost no memory.** The Count-Min Sketch is a probabilistic data structure: a 2D array of counters with multiple hash functions. To increment an item, hash it with each function and increment the corresponding counter. To query, take the minimum across all hash functions. The estimate is guaranteed to be an upper bound (never under-counts), with error bounded by ε·total.

**When to use:** You have a massive data stream and need approximate frequency estimates with formal error bounds. Classic use: finding heavy hitters in network traffic, trending topics on Twitter, frequent items in a data stream.

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `width` | int > 0, number of counters per hash | larger = more accurate |
| `depth` | int > 0, number of hash functions | larger = more accurate |
| `epsilon` | float > 0, error bound | — |

---

## How inputs shape the output

- **The sketch never under-counts:** the minimum across hash functions is always ≥ the true count (hash collisions can only increase counts).
- **Width controls accuracy:** wider tables = fewer collisions = tighter estimates. The demo's width=100 with 50 "cat" insertions gives an estimate close to 50.
- **Depth controls confidence:** more hash functions = lower probability of worst-case collision.

---

## Worked example (real run)

```
$ python3 python/data-science/streaming_and_sketches/count_min_sketch.py
Estimate for 'cat' (true 50): 50
Estimate for 'dog' (true 40): 40
✓ Count-Min Sketch: PASS
```

**Reading the output:** both heavy hitters are estimated exactly (no over-count in this run). The sketch never under-counts — the estimates are ≥ true counts.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| empty stream | all estimates = 0 | correct |
| `width = 0` | IndexError | needs guard |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-18
