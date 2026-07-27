# pagerank power iteration

**Language:** Python · **Sphere:** data-science · **Category:** Recommenders & Graph Sampling

**Signature:** `(graph: Dict[int, List[int]], damping: float, tol: float, max_iter: int) → Dict[int, float]`

## What it does

PageRank via power iteration.

Core idea: iterate score propagation through a directed graph where each node
distributes its score equally to outgoing neighbors, with damping (teleport
probability) to handle dangling nodes. Convergence is tested.

When to use: when you need to rank nodes in a directed graph by importance
(e.g., web pages, citations, social networks).

## Guarantee

When it runs, pagerank power iteration guarantees abs(total - 1.0) < 0.01; ranks[0] > mean_rank; all((r > 0 for r in ranks.values())) (proven by run).

**Checkable constraints:**

- `abs(total - 1.0) < 0.01`
- `ranks[0] > mean_rank`
- `all((r > 0 for r in ranks.values()))`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `def pagerank_power_iteration(graph: Dict[int, List[int]], damping: float = 0.85, tol: float = 1e-6, max_iter: int = 100,) -> Dict[int, float]:`
**Valid input:** `graph` is a non-empty adjacency list of outgoing neighbors; `0 <= damping <= 1`; `tol` > 0; `max_iter` > 0.
**Core:** PageRank via power iteration: each node distributes its score uniformly to outgoing neighbors, with damping factor teleportation to all nodes and special handling of dangling nodes (nodes with no out-edges).
**Assert:** Ranks sum to ≈1; all ranks positive; the hub node with multiple inbound links ranks above the mean in the planted graph.
**⚠️ Defect:** Dangling-node mass is redistributed equally to all nodes, which is one valid convention, but the code does not document or validate this choice. `max_iter=100` may be insufficient for some graphs, and the function silently returns the last iterate without indicating non-convergence.

---
*△ AURA Pattern Library — © Reality Optimizer*
