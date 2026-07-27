# minimax game search

**Language:** Python · **Sphere:** programming · **Category:** Reasoning

## What it does

A complete minimax game solver with alpha-beta pruning and depth limiting.

## Guarantee

When it runs, minimax game search guarantees solver.nodes_explored == 36; score == 0; move is not None and solver.nodes_explored > 9 (proven by run).

**Checkable constraints:**

- `score == 0`
- `move is not None and solver.nodes_explored > 9`
- `move == (0, 2)`
- `score == 1`
- `solver.nodes_explored == 36`
- `move == (0, 2)`
- `score == -1`
- `line.get_result() == -1`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
