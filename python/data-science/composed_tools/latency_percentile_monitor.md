# latency percentile monitor

**Language:** Python · **Sphere:** data-science · **Category:** Composed Tools

**Signature:** `(base: float, tail: float) → float`

## What it does

Latency Percentile Monitor — p99 tracking in five floats per quantile.

CROSS-SPHERE COMPOSED PATTERN: metric_aggregator (programming sphere,
awesome-python-patterns) x p2_quantile_estimator (DS Streaming & Sketches) —
embedding bridge 0.470, found 2026-07-06. Observability aggregators track
means and counts; means are BLIND to tail regressions. Welding the P²
five-marker estimator into the aggregator gives per-service p50/p99 in O(1)
memory — and the demo plants exactly the failure means cannot see: a
tail-only regression, invisible at p50, screaming at p99.

Use when: service latency monitoring where the tail IS the product.

## Guarantee

When it runs, latency percentile monitor guarantees abs(snap1['p99'] - exact_p99_1) / exact_p99_1 < 0.15; abs(snap2['p99'] - exact_p99_2) / exact_p99_2 < 0.15; abs(snap2['p50'] - snap1['p50']) / snap1['p50'] < 0.25 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `abs(snap1['p99'] - exact_p99_1) / exact_p99_1 < 0.15`
- `abs(snap2['p99'] - exact_p99_2) / exact_p99_2 < 0.15`
- `abs(snap2['p50'] - snap1['p50']) / snap1['p50'] < 0.25`
- `snap2['p99'] > 2.0 * snap1['p99']`
- `len(mon2.services['api']['p99'].q) == 5`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
