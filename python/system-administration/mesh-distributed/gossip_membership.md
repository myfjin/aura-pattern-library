# gossip membership

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 20 · Mesh / distributed coordination

**Signature:** `(other_node: GossipNode) → ?`

## What it does

Gossip Membership Protocol
Nodes periodically exchange membership list.
Simulate: node joins/leaves, gossip propagates change.
Assert: membership eventually consistent across cluster.

## Guarantee

When it runs, gossip membership guarantees node_a.membership == {'A'}; node_b.membership == {'B'}; node_a.membership == {'A', 'B'} (weak-grade: directional, proven by run).

**Checkable constraints:**

- `node_a.membership == {'A'}`
- `node_b.membership == {'B'}`
- `node_a.membership == {'A', 'B'}`
- `node_b.membership == {'A', 'B'}`
- `node_a.membership == {'A', 'B'}`
- `node_b.membership == {'A', 'B'}`
- `node_c.membership == {'C'}`
- `node_b.membership == {'A', 'B', 'C'}`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
