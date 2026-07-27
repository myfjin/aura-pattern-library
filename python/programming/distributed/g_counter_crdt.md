# g counter crdt

**Language:** Python · **Sphere:** programming · **Category:** Distributed

**Signature:** `() → None`

## What it does

Distributed Counter Implementation

This module provides two types of distributed counters:
- GCounter (Grow-only Counter): Only supports increment operations
- PNCounter (Positive-Negative Counter): Supports both increment and decrement

Both counters implement state-based convergence through merging operations.

## Guarantee

When it runs, g counter crdt guarantees n1.value() == 8; n3.value() == 15; n1.value() == 15 (proven by run).

**Checkable constraints:**

- `(n1.value(), n2.value(), n3.value()) == (5, 3, 7)`
- `n1.value() == 8`
- `n3.value() == 15`
- `n1.value() == n2.value() == n3.value() == 15`
- `n1.value() == 15`
- `a.value() == ba.value() == 13`
- `a.counts == ba.counts`
- `a.value() == 14`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
