# counter gauge histogram

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 14 · Monitoring & metrics

**Signature:** `(delta: int) → ?`

## What it does

counter_gauge_histogram: implement counter, gauge, and histogram metric types.

## Guarantee

When it runs, counter gauge histogram guarantees counter.get() == 5; counter.get() == 8; gauge.get() == 20 (proven by run).

**Checkable constraints:**

- `counter.get() == 0`
- `counter.get() == 5`
- `counter.get() == 8`
- `gauge.get() == 20`
- `gauge.get() == 25`
- `gauge.get() == 30`
- `gauge.get() == 20`
- `histogram.count == 10`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
