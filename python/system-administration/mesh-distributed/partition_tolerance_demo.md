# partition tolerance demo

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 20 · Mesh / distributed coordination

**Signature:** `(other_nodes: List[int]) → ?`

## What it does

Partition Tolerance Demo
Simulate network partition: cluster splits into two.
Assert: majority partition proceeds, minority blocks (quorum lost).
Partitions later rejoin: data merges (eventual consistency).

## Guarantee

When it runs, partition tolerance demo guarantees quorum == 3; quorum == 3; nodes[0].can_write() (proven by run).

**Checkable constraints:**

- `quorum == 3`
- `nodes[0].can_write()`
- `nodes[0].write('x', 1)`
- `not nodes[3].can_write()`
- `not nodes[3].write('x', 1)`
- `nodes[0].data['shared_key'] == 'version_1_majority'`
- `nodes[3].data['shared_key'] == 'version_0'`
- `nodes[0].can_write()`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
