# union find

**Language:** Python · **Sphere:** programming · **Category:** Data Structures

**Signature:** `() → None`

## What it does

Union-Find (disjoint-set) over arbitrary hashable values with path compression
and union by rank, tracking a live component count.

Use to maintain dynamic connectivity: make_set, union (returns whether a merge
happened), connected, and per-component enumeration.

Guarantees (self-test): productive unions each drop the component count by one,
connectivity is transitive, a balanced 16-way merge keeps root rank at 4, a
400-op fuzz agrees with a brute-force label oracle, and duplicate or missing keys
are refused.

## Guarantee

When it runs, union find guarantees uf.components() == 7 and uf.size() == 7; uf.components() == 2; uf.components() == 2 (proven by run).

**Checkable constraints:**

- `uf.components() == 7 and uf.size() == 7`
- `uf.union(*pair) is True`
- `uf.components() == 2`
- `uf.union('A', 'D') is False`
- `uf.components() == 2`
- `uf.connected('A', 'D') is True`
- `uf.connected('A', 'E') is False`
- `sorted(uf.get_component_elements('A')) == ['A', 'B', 'C', 'D']`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
