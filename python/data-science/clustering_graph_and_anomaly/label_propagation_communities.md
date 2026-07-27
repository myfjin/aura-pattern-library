# label propagation communities

**Language:** Python · **Sphere:** data-science · **Category:** Clustering, Graph & Anomaly

**Signature:** `(graph: Dict[int, List[int]], max_iterations: int, seed: int) → Dict[int, int]`

## What it does

Label Propagation for Community Detection from scratch.

Iteratively propagate node labels throughout a graph: each node adopts the label held
by most of its neighbors. Converges to stable partitions representing communities.
Core idea: similar nodes (connected) naturally converge to same label; few cross-edges
prevent full merging.

Use when: detecting communities with minimal tuning or finding natural partitions.

## Guarantee

When it runs, label propagation communities guarantees num_communities >= 2; c1_recovery >= 0.5; c2_recovery >= 0.5 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `num_communities >= 2`
- `c1_recovery >= 0.5`
- `c2_recovery >= 0.5`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `label_propagation(graph, max_iterations=100, seed=42) → Dict[int, int]`
**Valid input:** `graph: Dict[int, List[int]]` — adjacency list, undirected. At least 2 nodes.
**Core:** Label propagation for community detection. Each node starts with a unique label. Iteratively: randomize node order, each node adopts the most common label among its neighbors (ties broken randomly). Converges when no labels change. Two 4-node communities connected by a single cross-edge.
**Assert:** On 8-node graph (two communities 0-3 and 4-7, single cross-edge 3-4): at least 2 communities found, each original cluster recovered at ≥ 50%.
**⚠️ Defect:** Label propagation is non-deterministic due to random tie-breaking and random update order. The test uses `seed=42` for reproducibility, but different graph topologies can produce different results across runs. The recovery threshold of 50% is very lenient — a community detection that only recovers half the nodes is barely useful. Also, the algorithm can converge to a single community (all nodes same label) if the cross-edge is strong enough, which would fail the `num_communities >= 2` assertion.

---
*△ AURA Pattern Library — © Reality Optimizer*
