# sliding aggregate

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 14 · Monitoring & metrics

**Signature:** `(value: int) → ?`

## What it does

sliding_aggregate: compute rolling aggregates (sum, avg, min, max).

## Guarantee

When it runs, sliding aggregate guarantees window.sum() == 3; window.sum() == 6; window.sum() == 9 (proven by run).

**Checkable constraints:**

- `window.sum() == 1`
- `window.sum() == 3`
- `window.sum() == 6`
- `window.sum() == 9`
- `window.sum() == 12`
- `window_avg.average() == 10`
- `window_avg.average() == 15`
- `window_avg.average() == 20`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
