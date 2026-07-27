# quorum consensus

**Language:** Python · **Sphere:** programming · **Category:** Distributed

**Signature:** `() → None`

## What it does

Quorum consensus simulator module.

This module implements a simple quorum consensus system with nodes that can
propose values, accept proposals, and learn consensus decisions.

## Guarantee

When it runs, quorum consensus guarantees quorum.majority == 3; quorum.check_consensus(pid_b) == 42; quorum.get_learned_value(pid_b) == 42 (proven by run).

**Checkable constraints:**

- `quorum.majority == 3`
- `quorum.has_majority(3) and (not quorum.has_majority(2))`
- `quorum.check_consensus(pid_a) == 'A'`
- `node.get_learned_value(pid_a) == 'A'`
- `quorum.get_learned_value(pid_a) == 'A'`
- `quorum.check_consensus(pid_b) == 42`
- `quorum.get_learned_value(pid_b) == 42`
- `quorum.check_consensus(minority_pid) is None`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
