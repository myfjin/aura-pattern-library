# astar pathfinding

**Language:** Go · **Oracle sphere:** programming (this file is the Go twin) · **Category:** Reasoning

## What it does

A* Pathfinding Algorithm Implementation

This file implements the A* pathfinding algorithm for grid-based navigation.
It includes node, grid, and A* algorithm types, and replicates the Python
self-tests exactly.

## Guarantee

When it runs, astar pathfinding guarantees len(p) - 1 == 18; len(a_path) - 1 == truth; agreements == 30 (proven by run on the PY-PROG original).

**Checkable constraints:**

- `path is not None`
- `_valid_path(path, maze, (0, 0), (9, 9))`
- `len(path) - 1 == oracle`
- `len(p) - 1 == 18`
- `AStar(g2).find_path((0, 0), (9, 9)) is None`
- `AStar(g2).find_path((0, 0), (9, 8)) is None`
- `a_path is None`
- `a_path is not None`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — established on the PY-PROG original and shared by this Go twin (twin agreement is the evidence: consensus, xlang); the original oracle was not executed against this file
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
