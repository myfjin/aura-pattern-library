"""PageRank via power iteration.

Core idea: iterate score propagation through a directed graph where each node
distributes its score equally to outgoing neighbors, with damping (teleport
probability) to handle dangling nodes. Convergence is tested.

When to use: when you need to rank nodes in a directed graph by importance
(e.g., web pages, citations, social networks).
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import random
import math
from typing import Dict, List, Set


def pagerank_power_iteration(
    graph: Dict[int, List[int]],
    damping: float = 0.85,
    tol: float = 1e-6,
    max_iter: int = 100,
) -> Dict[int, float]:
    """
    Compute PageRank via power iteration.
    graph: adjacency list (int -> list of outgoing neighbors)
    Returns: dict mapping node -> pagerank score
    """
    nodes = set(graph.keys())
    for neighbors in graph.values():
        nodes.update(neighbors)
    nodes = sorted(nodes)
    n = len(nodes)

    # Initialize
    rank = {node: 1.0 / n for node in nodes}

    # Dangling nodes (no outgoing edges)
    dangling = {node: 1.0 / n for node in nodes if node not in graph or not graph[node]}

    for _ in range(max_iter):
        new_rank = {node: (1 - damping) / n for node in nodes}

        # Propagate from each node
        for node in nodes:
            neighbors = graph.get(node, [])
            if neighbors:
                score_per_neighbor = rank[node] / len(neighbors)
                for neighbor in neighbors:
                    new_rank[neighbor] += damping * score_per_neighbor

        # Handle dangling nodes
        dangling_sum = sum(rank[node] for node in dangling)
        for node in nodes:
            new_rank[node] += damping * dangling_sum / n

        # Check convergence
        diff = sum(abs(new_rank[node] - rank[node]) for node in nodes)
        rank = new_rank
        if diff < tol:
            break

    return rank


if __name__ == "__main__":
    random.seed(42)

    # Synthetic directed graph: 5 nodes with clear hierarchy
    # Structure: nodes 1,2,3,4 all point to node 0 (hub)
    # Node 0 should accumulate high rank from multiple inbound edges
    graph: Dict[int, List[int]] = {
        0: [4],      # 0 points to 4 only
        1: [0],      # 1 -> 0
        2: [0],      # 2 -> 0
        3: [0],      # 3 -> 0
        4: [1, 2, 3],  # 4 distributes to 1,2,3
    }

    ranks = pagerank_power_iteration(graph, damping=0.85, tol=1e-6)

    # Verify properties
    # Sum should be approximately 1
    total = sum(ranks.values())
    assert abs(total - 1.0) < 0.01, f"Sum of ranks {total} != 1"

    # Node 0 (has inbound edges from 3) should rank above the mean
    mean_rank = total / len(ranks)
    assert ranks[0] > mean_rank, f"Node 0 ({ranks[0]:.4f}) should rank > mean ({mean_rank:.4f})"

    # All ranks should be positive
    assert all(r > 0 for r in ranks.values()), "All ranks should be positive"

    print(f"pagerank_power_iteration.py: ranks={{{0}: {ranks[0]:.4f}, {4}: {ranks[4]:.4f}}}, mean={mean_rank:.4f} PASS")
