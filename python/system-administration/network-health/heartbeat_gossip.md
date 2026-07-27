# heartbeat gossip

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 8 · Network reachability & health

**Signature:** `(node_id: str) → ?`

## What it does

heartbeat_gossip: gossip protocol where nodes exchange heartbeats to detect failures.
Failure simulated: node_1 sends heartbeats; node_2 stops sending; node_1 should detect node_2 as down.
Recovery asserted: node_2 marked down after missing heartbeats; node_1 correctly tracks node_2 status.

## Guarantee

When it runs, heartbeat gossip guarantees alive_count_initial == 3; alive_count_after == 2; alive_count_initial == 3 and alive_count_after == 2 (proven by run).

**Checkable constraints:**

- `alive_count_initial == 3`
- `'node_2' in dead_nodes`
- `'node_1' not in dead_nodes and 'node_3' not in dead_nodes`
- `alive_count_after == 2`
- `alive_count_initial == 3 and alive_count_after == 2`
- `node_1_alive is True and node_3_alive is True`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
