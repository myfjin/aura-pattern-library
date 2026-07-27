# throughput meter

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 16 · Text/stream processing for ops

**Signature:** `(item_count: int, byte_count: int) → ?`

## What it does

throughput_meter: Calculate throughput (items/sec or bytes/sec).
THE ONE LAW: Track time windows, calculate exact rate, handle zero-duration edge cases.

## Guarantee

When it runs, throughput meter guarantees abs(throughput['items_per_sec'] - 100) < 1; abs(throughput['bytes_per_sec'] - 10000) < 100; abs(throughput2['items_per_sec'] - 15) < 1 (proven by run).

**Checkable constraints:**

- `throughput is not None`
- `abs(throughput['items_per_sec'] - 100) < 1`
- `abs(throughput['bytes_per_sec'] - 10000) < 100`
- `throughput_empty is None`
- `throughput_fast is None or throughput_fast['items_per_sec'] > 0`
- `throughput2 is not None`
- `abs(throughput2['items_per_sec'] - 15) < 1`
- `abs(throughput2['bytes_per_sec'] - 1500) < 100`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
