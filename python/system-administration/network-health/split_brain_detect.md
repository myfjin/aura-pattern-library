# split brain detect

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 8 · Network reachability & health

**Signature:** `(node_id: str, all_nodes: List[str], node_addresses: dict, quorum_size: int) → ?`

## What it does

split_brain_detect: detect network partitions by checking if a quorum can reach each other.
Failure simulated: 3-node cluster where node_3 becomes isolated; quorum detection should flag split brain.
Recovery asserted: healthy partition has quorum (2/3 reach each other); partitioned node cannot reach majority.

## Guarantee

When it runs, split brain detect guarantees is_healthy is True; healthy_1 is False; healthy_2 is False (weak-grade: directional, proven by run).

**Checkable constraints:**

- `is_healthy is True`
- `healthy_1 is False`
- `healthy_2 is False`
- `split_brain_detected`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
