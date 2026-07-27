# ring buffer log

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 5 · Log management

**Signature:** `(max_size: int) → ?`

## What it does

Ring buffer logger: hold max N log entries, evict oldest on overflow.
Failure simulated: push N+100 entries, assert exactly N held, oldest evicted.
Defended outcome: buffer size never exceeds N, FIFO eviction holds.

## Guarantee

When it runs, ring buffer log guarantees len(all_entries) == max_entries; before_overflow == max_entries; len(all_entries) == max_entries (weak-grade: directional, proven by run).

**Checkable constraints:**

- `len(all_entries) == max_entries`
- `before_overflow == max_entries`
- `len(all_entries) == max_entries`
- `first_entry == f'entry {max_entries}'`
- `last_entry == f'entry {2 * max_entries - 1}'`
- `i not in entry_indices`
- `idx >= max_entries`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
