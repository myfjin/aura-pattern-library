# consistent hashing

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 20 · Mesh / distributed coordination

**Signature:** `(key: str, num_nodes: int) → ?`

## What it does

Consistent Hashing Pattern
When a node leaves/joins, only ~1/N keys are remapped (not all keys).
Assert: Key -> Node mapping changes minimally on membership change.

## Guarantee

When it runs, consistent hashing guarantees all((v is not None for v in mapping.values())); 0 < remapped < len(keys) * 0.33; mapping_after[k] == 'D' (weak-grade: directional, proven by run).

**Checkable constraints:**

- `all((v is not None for v in mapping.values()))`
- `len(nodes_used) > 1`
- `0 < remapped < len(keys) * 0.33`
- `mapping_after[k] == 'D'`
- `naive_remapped > 2 * remapped`
- `mapping_after[k] in ['B', 'C', 'D']`
- `remapped == a_count_before`
- `mapping_1 == mapping_3`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
