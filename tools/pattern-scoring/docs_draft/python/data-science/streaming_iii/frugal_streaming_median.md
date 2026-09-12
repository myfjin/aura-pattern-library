# Frugal Streaming Median (Frugal-1)

**File:** `python/data-science/streaming_iii/frugal_streaming_median.py`
**Sphere:** Data Science — Streaming and Sketches

---

## What it solves

**Estimate the median of a stream using a single integer of state.** Frugal-1 (Ma, Muthukrishnan, Sandler) keeps one estimate m. For each element, with a coin flip gated by the target quantile q=0.5, it steps m up by 1 if the element is above m, down by 1 if below. At the true quantile, the up-pressure and down-pressure balance, so m random-walks to the median.

**When to use:** You need a quantile estimate on an unbounded stream with O(1) memory — embedded systems, sensor networks, any environment where every byte counts.

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `stream` | List[float], any scale | step should match data scale |
| `step` | float > 0, increment size | too small = slow convergence |

---

## How inputs shape the output

- **O(1) memory:** one float of state, period. No arrays, no buckets, no histograms.
- **Converges by random walk:** starts at 0 (far from the answer) and walks to the median. The demo proves convergence from a cold start — no cheating by initializing near the answer.
- **Step size controls precision:** the estimate oscillates within O(step) of the true median. The demo's step=1.0 on a ~50-scale stream gives error < 3.0.

---

## Worked example (real run)

```
$ python3 python/data-science/streaming_iii/frugal_streaming_median.py
Frugal-1 median: est=49.000, true=50.015, err=1.015
Frugal median PASS
```

**Reading the output:** on 20,000 samples from N(50, 15), Frugal-1 converges to within ~1 unit of the true median using only one float of state, starting from 0.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| step too large relative to data | estimate oscillates widely | tune step to data scale |
| very short stream | may not converge | needs enough samples to walk to median |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-20