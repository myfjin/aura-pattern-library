# metrics formatter

**Language:** Python · **Sphere:** programming · **Category:** Monitoring

**Signature:** `() → None`

## What it does

Prometheus / OpenMetrics text-exposition formatter.

Use to serialize metrics into the Prometheus text format: build Metric objects
(name, value, type, labels, optional help/timestamp) and render them grouped by
name with one HELP and one TYPE line per family, followed by the samples.
Metric names and label keys are validated on construction. Guarantees (proven by
self-test): exposition lines are byte-exact; HELP precedes TYPE precedes samples,
TYPE appears once per family; label values have quotes, backslashes, and newlines
escaped (so one hostile label can't corrupt the exposition); invalid names/keys
raise ValueError; an empty formatter emits an explicit "no metrics" line.

## Guarantee

When it runs, metrics formatter guarantees s == 2; 'http_requests_total{method="GET",endpoint="/api/users"} 42' in lines; 'http_requests_total{method="POST",endpoint="/api/users"} 17' in lines (proven by run).

**Checkable constraints:**

- `'http_requests_total{method="GET",endpoint="/api/users"} 42' in lines`
- `'http_requests_total{method="POST",endpoint="/api/users"} 17' in lines`
- `'cpu_usage_percent{instance="server01"} 75.5' in lines`
- `lines.count('# TYPE http_requests_total counter') == 1`
- `'# HELP http_requests_total Total number of HTTP requests' in lines`
- `h < t < s`
- `s == 2`
- `'\\"' in esc_out`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
