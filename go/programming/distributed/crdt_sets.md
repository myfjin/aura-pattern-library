# crdt sets

**Language:** Go · **Oracle sphere:** programming (this file is the Go twin) · **Category:** Distributed

## What it does

crdt_sets: Conflict-free Replicated Data Types for sets (AWORSet, AddWinsSet, RemoveWinsSet).

## Guarantee

When it runs, crdt sets guarantees n_elems == 4; s1.elements() == {'a', 'c'}; s1.elements() == {'a', 'b', 'c', 'd'} (proven by run on the PY-PROG original).

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
- **Independent oracle:** — established on the PY-PROG original and shared by this Go twin (twin agreement is the evidence: consensus, xlang); the original oracle was not executed against this file
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
