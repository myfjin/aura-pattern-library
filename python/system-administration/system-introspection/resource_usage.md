# resource usage

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 15 · Process/system introspection

**Signature:** `(status_text: str) → ?`

## What it does

resource_usage: Extract memory/CPU metrics from /proc/[pid]/status.
THE ONE LAW: Parse real data, assert exact values; simulate missing fields, assert error.

## Guarantee

When it runs, resource usage guarantees metrics['rss_kb'] == 102400; metrics['peak_kb'] == 204800; metrics['threads'] == 4 (proven by run).

**Checkable constraints:**

- `metrics['rss_kb'] == 102400`
- `metrics['peak_kb'] == 204800`
- `metrics['threads'] == 4`
- `'rss_kb' in str(e) or 'VmRSS' in str(e)`
- `len(metrics) == 3`
- `isinstance(metrics['rss_kb'], int)`
- `isinstance(metrics['threads'], int)`
- `boundary['rss_kb'] == 1`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
