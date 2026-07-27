# leader election lite

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 20 · Mesh / distributed coordination

**Signature:** `(candidate_id: int, candidate_term: int) → ?`

## What it does

Leader Election (Lite) Pattern
N nodes, each with ID and term number.
Simulate: a node gets term majority, becomes leader.
Assert: exactly ONE leader at any term, term number only increases.

## Guarantee

When it runs, leader election lite guarantees node.term == 5; node.term == 5; node.term == 6 (proven by run).

**Checkable constraints:**

- `votes >= majority`
- `len(leaders) == 1`
- `leaders[0].node_id == 0`
- `votes >= majority`
- `nodes[0].leader_id != 0 or nodes[0] not in active_nodes`
- `nodes[1].leader_id == 1`
- `node.term == 5`
- `node.term == 5`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
