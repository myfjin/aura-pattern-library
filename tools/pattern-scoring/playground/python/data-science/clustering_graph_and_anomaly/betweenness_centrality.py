"""
Betweenness Centrality from scratch.

Measures how often a node lies on shortest paths between other nodes. High betweenness
indicates a "bridge" or connector node. Core idea: for each pair of nodes, count shortest
paths passing through the target node, normalize by total paths between those nodes.

Use when: identifying critical nodes in networks (e.g., bridges, key influencers).
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

from typing import Dict, List, Tuple
from collections import deque

def betweenness_centrality(graph: Dict[int, List[int]]) -> Dict[int, float]:
    """
    Compute betweenness centrality for all nodes.

    For each node v, count how many shortest paths between all pairs (s,t) pass through v.
    Use BFS to find all shortest paths, then accumulate via path counting.

    Args:
        graph: Adjacency list representation {node: [neighbors]}

    Returns:
        Dictionary mapping node -> betweenness score (normalized)
    """
    nodes = list(graph.keys())
    n = len(nodes)
    betweenness = {node: 0.0 for node in nodes}

    # For each source node s
    for s in nodes:
        # BFS to find distances and count shortest paths
        distances = {node: float("inf") for node in nodes}
        distances[s] = 0
        path_counts = {node: 0 for node in nodes}
        path_counts[s] = 1
        predecessors = {node: [] for node in nodes}

        # BFS phase
        queue = deque([s])
        while queue:
            u = queue.popleft()
            for v in graph[u]:
                if distances[v] == float("inf"):
                    distances[v] = distances[u] + 1
                    queue.append(v)

                if distances[v] == distances[u] + 1:
                    predecessors[v].append(u)
                    path_counts[v] += path_counts[u]

        # Dependency accumulation (reverse topological order)
        dependency = {node: 0.0 for node in nodes}
        sorted_nodes = sorted(nodes, key=lambda x: distances[x], reverse=True)

        for w in sorted_nodes:
            if w != s:
                for v in predecessors[w]:
                    dependency[v] += (path_counts[v] / path_counts[w]) * (1 + dependency[w])

        for node in nodes:
            if node != s:
                betweenness[node] += dependency[node]

    # Normalize by (n-1)(n-2)/2 for undirected
    scale = 2.0 / ((n - 1) * (n - 2)) if n > 2 else 1.0
    betweenness = {node: score * scale for node, score in betweenness.items()}

    return betweenness

if __name__ == "__main__":
    # Create a graph with an obvious bridge: node 5 connects two clusters
    # Cluster 1: 0-1-2-3 (fully connected within)
    # Bridge: 5
    # Cluster 2: 6-7-8-9 (fully connected within)
    graph = {
        0: [1, 2, 3, 5],
        1: [0, 2, 3, 5],
        2: [0, 1, 3, 5],
        3: [0, 1, 2, 5],
        5: [0, 1, 2, 3, 6, 7, 8, 9],
        6: [5, 7, 8, 9],
        7: [5, 6, 8, 9],
        8: [5, 6, 7, 9],
        9: [5, 6, 7, 8],
    }

    betweenness = betweenness_centrality(graph)

    # Node 5 should have the highest betweenness (bridge between clusters)
    max_node = max(betweenness, key=betweenness.get)
    assert max_node == 5, f"Expected node 5 to have max betweenness, got node {max_node}"
    assert betweenness[5] > betweenness[0], f"Bridge node 5 should score higher than cluster node 0"
    assert betweenness[5] > betweenness[6], f"Bridge node 5 should score higher than cluster node 6"

    print(f"betweenness_centrality.py: bridge node 5 identified (score {betweenness[5]:.3f}) PASS")
