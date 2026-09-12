# Latency Percentile Monitor

**File:** `python/data-science/composed_tools/latency_percentile_monitor.py`
**Sphere:** Data Science — Composed Tools

---

## What it solves

**p99 tracking in five floats per quantile.** Observability aggregators track means and counts; means are BLIND to tail regressions. Welding the P² five-marker estimator into the aggregator gives per-service p50/p99 in O(1) memory — and the demo plants exactly the failure means cannot see: a tail-only regression, invisible at p50, screaming at p99.

**When to use:** Service latency monitoring where the tail IS the product.

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `service` | str, service name | any |
| `latency_ms` | float, latency in ms | positive |

---

## How inputs shape the output

- **Streaming p99 tracks exact p99** within 15% relative error.
- **Tail regression is invisible at p50** (<25% shift) but **loud at p99** (>2× increase).
- **O(1) memory:** five markers per quantile, no stored stream.

---

## Worked example (real run)

```
$ python3 python/data-science/composed_tools/latency_percentile_monitor.py
phase1: p50 48 · p99 152 (exact 148) · mean 52
phase2: p50 51 · p99 412 (exact 398) · mean 58
latency_percentile_monitor.py PASS
```

**Reading the output:** p50 barely moves (48→51) and mean barely moves (52→58) — both blind to the tail regression. p99 screams from 152→412 — a 2.7× increase.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| very long tail | P² may lag behind exact p99 | estimator needs warm-up |
| all identical latencies | p50 = p99 | correct |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-20