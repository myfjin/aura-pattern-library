# consistent hash ring

**Language:** Python · **Oracle sphere:** rust (this file is the Python twin) · **Category:** distributed

## What it does

Consistent Hash Ring Implementation

This module provides a consistent hash ring implementation that distributes
keys across nodes in a way that minimizes redistribution when nodes are
added or removed.

## Guarantee

When it runs, consistent hash ring guarantees `len(ring.ring) == 120`; `all((v in nodes for v in before.values()))`; `before == {k: ring.get_node(k) for k in keys}` — read from this file's own self-test. The oracle behind this pattern was established on the rust original and is not claimed to have been run against this file.

**Checkable constraints:**

- `len(ring.ring) == 120`
- `all((v in nodes for v in before.values()))`
- `before == {k: ring.get_node(k) for k in keys}`
- `sum(counts.values()) == 1000`
- `all((150 <= c <= 550 for c in counts.values()))`
- `illegal == []`
- `0 < len(moved) < 500`
- `restored == before`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — established on the RUST original and shared by this Python twin (twin agreement is the evidence: consensus, xlang); the original oracle was not executed against this file
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
