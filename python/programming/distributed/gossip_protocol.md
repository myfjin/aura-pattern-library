# gossip protocol

**Language:** Python · **Sphere:** programming · **Category:** Distributed

## What it does

Gossip Protocol Membership List Implementation

This module implements a gossip protocol for maintaining membership lists in distributed systems.
It includes features for member management, failure detection, and gossip-based information
dissemination using both infect and anti-entropy mechanisms.

## Guarantee

When it runs, gossip protocol guarantees n_members == 5; node.members['node-2'].incarnation == 5; node.members['node-2'].incarnation == 5 (proven by run).

**Checkable constraints:**

- `alive >= {f'node-{i}' for i in range(1, 5)}`
- `n_members == 5`
- `len(node.get_membership_list()) == 5`
- `node.mark_suspect('node-4') is True`
- `node.mark_suspect('ghost') is False`
- `{m.id for m in node.get_suspect_members()} == {'node-4'}`
- `'node-4' not in {m.id for m in node.get_alive_members()}`
- `node.get_dead_members() == []`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
