# crdt sets

**Language:** Python · **Sphere:** programming · **Category:** Distributed

## What it does

CRDT Sets Implementation

This module implements three types of Conflict-free Replicated Data Types (CRDT) sets:
- AWORSet (Add-Wins Observed-Remove Set)
- AddWinsSet (Add-Wins Set)
- RemoveWinsSet (Remove-Wins Set)

Each implementation supports add, remove, query, and merge operations.

## Guarantee

When it runs, crdt sets guarantees n_elems == 4; s1.elements() == {'a', 'c'}; s1.elements() == {'a', 'b', 'c', 'd'} (proven by run).

**Checkable constraints:**

- `s1.elements() == {'a', 'c'}`
- `s1.elements() == {'a', 'b', 'c', 'd'}`
- `s1.query('b') is True and s1.query('ghost') is False`
- `n_elems == 4`
- `s1.elements() == {'a', 'c', 'd'}`
- `aw1.query('conflict') is True`
- `aw1.query('conflict') is False`
- `aw1.query('x') is False`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
