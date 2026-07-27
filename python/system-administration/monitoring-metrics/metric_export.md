# metric export

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 14 · Monitoring & metrics

**Signature:** `(name: str, value: int) → ?`

## What it does

metric_export: export metrics in standard formats.

## Guarantee

When it runs, metric export guarantees parsed['requests_total']['value'] == 10000; parsed['temperature_celsius']['value'] == 25.5; parsed_from_file['requests_total']['value'] == 10000 (proven by run).

**Checkable constraints:**

- `isinstance(json_output, str)`
- `'requests_total' in parsed`
- `parsed['requests_total']['type'] == 'counter'`
- `parsed['requests_total']['value'] == 10000`
- `'temperature_celsius' in parsed`
- `parsed['temperature_celsius']['type'] == 'gauge'`
- `parsed['temperature_celsius']['value'] == 25.5`
- `'latency_ms' in parsed`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
