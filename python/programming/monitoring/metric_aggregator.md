# metric aggregator

**Language:** Python · **Sphere:** programming · **Category:** Monitoring

## What it does

Metric aggregator with tags for counters, gauges, and histograms.
Supports percentile calculations and tagged metrics.

## Guarantee

When it runs, metric aggregator guarantees agg.get_counter('requests') == 4; agg.get_counter('errors', {'type': 'timeout'}) == 3; agg.get_counter('requests') + agg.get_counter('errors', {'type': 'timeout'}) == 7 (proven by run).

**Checkable constraints:**

- `agg.get_counter('requests') == 4`
- `agg.get_counter('errors', {'type': 'timeout'}) == 3`
- `agg.get_counter('errors', {'type': 'validation'}) == 1`
- `agg.get_counter('requests') + agg.get_counter('errors', {'type': 'timeout'}) == 7`
- `agg.get_gauge('cpu') == 67.8`
- `stats['count'] == 20`
- `stats['sum'] == 950`
- `stats['min'] == 0 and stats['max'] == 95`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
