# reachability matrix

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 8 · Network reachability & health

**Signature:** `(nodes: List[str], endpoints: List[tuple], timeout_sec: float) → ?`

## What it does

reachability_matrix: probe all nodes against all endpoints; build a matrix of reachability.
Failure simulated: 3 nodes with 3 endpoints each; after one endpoint fails, matrix changes.
Recovery asserted: matrix correctly reflects which nodes can reach which endpoints (binary/bool).

## Guarantee

When it runs, reachability matrix guarantees all_reachable_up == 9; all_reachable_down == 6; all_reachable_up == 9 and all_reachable_down == 6 (proven by run).

**Checkable constraints:**

- `reachable is True`
- `all_reachable_up == 9`
- `matrix_down[node_id][0] is False`
- `matrix_down[node_id][1] is True`
- `matrix_down[node_id][2] is True`
- `all_reachable_down == 6`
- `all_reachable_up == 9 and all_reachable_down == 6`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
