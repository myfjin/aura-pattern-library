# quorum check

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 20 · Mesh / distributed coordination

**Signature:** `(alive_nodes: int, total_nodes: int) → ?`

## What it does

Quorum Check Pattern
Write requires quorum (majority of nodes).
Simulate: partition that loses majority can't write.
Assert: quorum_lost() returns True when alive < majority.

## Guarantee

When it runs, quorum check guarantees quorum == 3; quorum == 3; quorum == 3 (proven by run).

**Checkable constraints:**

- `quorum == 3`
- `can_write(alive, total)`
- `quorum == 3`
- `can_write(alive_p1, total)`
- `not can_write(alive_p2, total)`
- `quorum == 3`
- `not can_write(alive, total)`
- `quorum == 1`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
