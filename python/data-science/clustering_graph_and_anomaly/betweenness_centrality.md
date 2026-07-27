# betweenness centrality

**Language:** Python · **Sphere:** data-science · **Category:** Clustering, Graph & Anomaly

**Signature:** `(graph: Dict[int, List[int]]) → Dict[int, float]`

## What it does

Betweenness Centrality from scratch.

Measures how often a node lies on shortest paths between other nodes. High betweenness
indicates a "bridge" or connector node. Core idea: for each pair of nodes, count shortest
paths passing through the target node, normalize by total paths between those nodes.

Use when: identifying critical nodes in networks (e.g., bridges, key influencers).

## Guarantee

When it runs, betweenness centrality guarantees max_node == 5; betweenness[5] > betweenness[0]; betweenness[5] > betweenness[6] (proven by run).

**Checkable constraints:**

- `max_node == 5`
- `betweenness[5] > betweenness[0]`
- `betweenness[5] > betweenness[6]`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `betweenness_centrality(graph) → Dict[int, float]`
**Valid input:** `graph: Dict[int, List[int]]` — adjacency list, undirected. At least 3 nodes.
**Core:** Brandes' algorithm for betweenness centrality. For each source node s: BFS to find shortest path distances and counts, then dependency accumulation in reverse topological order. Normalized by (n-1)(n-2)/2 for undirected graphs. Bridge node between two clusters should have highest score.
**Assert:** On a 10-node graph with two 4-node clusters connected by a bridge node (5): node 5 has the highest betweenness, higher than any cluster node.
**⚠️ Defect:** The normalization factor `2.0 / ((n-1)*(n-2))` is correct for undirected graphs, but the code uses `n = len(nodes)` which counts all nodes including the source. The standard Brandes algorithm excludes the source node from normalization, so for n=10, the factor should be 2/(9×8) = 1/36, which matches. However, the code doesn't handle directed graphs or weighted edges.

---
*△ AURA Pattern Library — © Reality Optimizer*
