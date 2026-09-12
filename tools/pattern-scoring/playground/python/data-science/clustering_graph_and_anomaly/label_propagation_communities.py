"""
Label Propagation for Community Detection from scratch.

Iteratively propagate node labels throughout a graph: each node adopts the label held
by most of its neighbors. Converges to stable partitions representing communities.
Core idea: similar nodes (connected) naturally converge to same label; few cross-edges
prevent full merging.

Use when: detecting communities with minimal tuning or finding natural partitions.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import random
from typing import Dict, List

def label_propagation(
    graph: Dict[int, List[int]],
    max_iterations: int = 100,
    seed: int = 42
) -> Dict[int, int]:
    """
    Label propagation for community detection.

    Args:
        graph: Adjacency list representation {node: [neighbors]}
        max_iterations: Maximum iterations
        seed: Random seed

    Returns:
        Dictionary mapping node -> community label
    """
    random.seed(seed)
    nodes = list(graph.keys())
    labels = {node: node for node in nodes}  # Each node starts with unique label

    for iteration in range(max_iterations):
        old_labels = {node: labels[node] for node in nodes}

        # Randomize update order
        update_order = nodes.copy()
        random.shuffle(update_order)

        for node in update_order:
            # Get labels of neighbors
            neighbor_labels = [labels[neighbor] for neighbor in graph[node]]

            if neighbor_labels:
                # Count label frequencies
                label_counts = {}
                for label in neighbor_labels:
                    label_counts[label] = label_counts.get(label, 0) + 1

                # Adopt most common neighbor label (break ties randomly)
                max_count = max(label_counts.values())
                most_common_labels = [label for label, count in label_counts.items() if count == max_count]
                new_label = random.choice(most_common_labels)
                labels[node] = new_label

        # Check convergence
        if labels == old_labels:
            break

    return labels

if __name__ == "__main__":
    # Create a two-community graph with few cross-edges
    # Community 1: 0-1-2-3
    # Community 2: 4-5-6-7
    # Cross-edge: 3-4 (single bridge)
    graph = {
        0: [1, 2],
        1: [0, 2, 3],
        2: [0, 1, 3],
        3: [1, 2, 4],
        4: [3, 5, 6],
        5: [4, 6, 7],
        6: [4, 5, 7],
        7: [5, 6],
    }

    labels = label_propagation(graph, max_iterations=50, seed=42)

    # Extract communities
    communities = {}
    for node, label in labels.items():
        if label not in communities:
            communities[label] = []
        communities[label].append(node)

    num_communities = len(communities)

    # Should find 2 or 3 communities (single cross-edge may or may not hold)
    assert num_communities >= 2, f"Expected at least 2 communities, got {num_communities}"

    # Check that nodes within communities are mostly from their original clusters
    c1_nodes = {0, 1, 2, 3}
    c2_nodes = {4, 5, 6, 7}

    # Find which community has most of c1 and which has most of c2
    best_c1_match = max(communities.values(), key=lambda comm: len(set(comm) & c1_nodes))
    best_c2_match = max(communities.values(), key=lambda comm: len(set(comm) & c2_nodes))

    c1_recovery = len(set(best_c1_match) & c1_nodes) / len(c1_nodes)
    c2_recovery = len(set(best_c2_match) & c2_nodes) / len(c2_nodes)

    assert c1_recovery >= 0.5, f"Community 1 recovery too low: {c1_recovery}"
    assert c2_recovery >= 0.5, f"Community 2 recovery too low: {c2_recovery}"

    print(f"label_propagation_communities.py: {num_communities} communities, C1={c1_recovery:.1%}, C2={c2_recovery:.1%} PASS")
