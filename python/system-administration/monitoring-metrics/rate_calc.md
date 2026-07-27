# rate calc

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 14 · Monitoring & metrics

**Signature:** `(timestamp: int, counter_value: int) → ?`

## What it does

rate_calc: calculate rate (e.g., requests per second) from counter.

## Guarantee

When it runs, rate calc guarantees rate_at_30 == 100.0; rate_10_to_20 == 100.0; rate_at_20 == 10.0 (proven by run).

**Checkable constraints:**

- `rate_at_30 == 100.0`
- `rate_10_to_20 == 100.0`
- `rate_at_20 == 10.0`
- `rate_static == 0.0`
- `rate_insufficient == 0.0`
- `rate_final == 100.0`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
