# Exponential Histogram / DGIM Windowed Count

**File:** `python/data-science/streaming_iii/exponential_histogram_count.py`
**Sphere:** Data Science — Streaming and Sketches

---

## What it solves

**Count the number of 1-bits in the last N arrivals using O((1/ε)·log N) space instead of O(N).** The DGIM algorithm (Datar-Gionis-Indyk-Motwani) keeps buckets holding power-of-2 counts with timestamps. When a size overflows its cap (k/2+1 where k = ceil(1/ε)), the two oldest buckets of that size merge into one double-size bucket. Old buckets that fall out of the window expire. The estimate = sum of bucket sizes − half the oldest in-window bucket, with relative error ≤ ε.

**When to use:** You need to count events in a sliding window but can't afford O(N) memory — network traffic monitoring, sensor event counting, any "how many in the last hour?" on a high-volume stream.

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `stream` | List[int] (0/1 bits) | binary only |
| `window` | int > 0, sliding window size N | larger = more memory |
| `eps` | float in (0, 1), target relative error | smaller = more buckets |

---

## How inputs shape the output

- **Relative error guarantee:** the estimate is within ε of the true count. The demo's ε=0.1 means ≤10% error.
- **Space compression:** uses O((1/ε)·log N) buckets — far less than storing the full window. The demo asserts this explicitly.
- **Merge-then-expire:** buckets merge from smallest size upward when a size overflows. The oldest in-window bucket is halved in the estimate (the half that's outside the window).

---

## Worked example (real run)

```
$ python3 python/data-science/streaming_iii/exponential_histogram_count.py
DGIM windowed count: est=298, true=301, rel_err=0.0100 (eps=0.1)
Exponential histogram (DGIM) PASS
```

**Reading the output:** with a 1000-sample window on a Bernoulli(0.3) stream, DGIM estimates 298 ones vs. 301 true — relative error of 1%, well within the 10% guarantee.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| all-zero stream | estimate = 0 | correct |
| window larger than stream | counts everything seen so far | correct behavior |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-20