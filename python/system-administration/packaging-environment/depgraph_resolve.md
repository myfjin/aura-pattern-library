# depgraph resolve

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 17 · Packaging & environment

**Signature:** `(node: str, path: list) → ?`

## What it does

depgraph_resolve: resolve a dependency graph and detect cycles. Must name the cycle.
A broken cycle detector would either miss it or crash. This one catches it and reports
the exact names in the cycle.

## Guarantee

When it runs, depgraph resolve guarantees not has_cycle; cycle[0] == cycle[-1]; cycle_nodes == {'a', 'b', 'c'} (weak-grade: directional, proven by run).

**Checkable constraints:**

- `not has_cycle`
- `has_cycle`
- `len(cycle) == 4`
- `cycle[0] == cycle[-1]`
- `cycle_nodes == {'a', 'b', 'c'}`
- `cycle == ['a', 'b', 'c', 'a']`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
