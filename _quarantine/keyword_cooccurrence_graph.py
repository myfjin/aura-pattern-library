"""Keyword co-occurrence graph: group words into topics via connected components.

Builds a graph where edges connect words appearing together within a window, then
extracts connected components (BFS). Disjoint topics form disjoint components. Core claim:
two planted topics with no shared words are recovered as two separate clusters, each
holding exactly its own words. (This is connected-components, not modularity-based
community detection — it separates disconnected topics but would not split a connected one.)
"""
from typing import Dict, List, Set
from collections import defaultdict

def cooccurrence_graph(documents: List[List[str]], window: int = 5) -> Dict[str, Set[str]]:
    """Build co-occurrence graph: edges between words within window."""
    graph = defaultdict(set)

    for doc in documents:
        for i, word in enumerate(doc):
            for j in range(max(0, i - window), min(len(doc), i + window + 1)):
                if i != j:
                    graph[word].add(doc[j])

    return dict(graph)

def detect_clusters_greedy(graph: Dict[str, Set[str]]) -> List[Set[str]]:
    """Greedy community detection: build clusters from high-degree nodes."""
    if not graph:
        return []

    visited = set()
    clusters = []

    for start_node in sorted(graph.keys(), key=lambda x: len(graph[x]), reverse=True):
        if start_node in visited:
            continue

        cluster = {start_node}
        visited.add(start_node)

        queue = [start_node]
        while queue:
            node = queue.pop(0)
            for neighbor in graph.get(node, set()):
                if neighbor not in visited:
                    cluster.add(neighbor)
                    visited.add(neighbor)
                    queue.append(neighbor)

        if len(cluster) > 1:
            clusters.append(cluster)

    return clusters

if __name__ == "__main__":
    import random
    random.seed(42)

    # Planted: two topics (sports, cooking) in separate documents.
    docs = [
        ["football", "soccer", "ball", "game", "team"],
        ["flour", "sugar", "bake", "cake", "recipe"],
    ]

    graph = cooccurrence_graph(docs, window=3)
    clusters = detect_clusters_greedy(graph)

    # Defining property: exactly TWO clusters, each holding its own topic's words.
    assert len(clusters) == 2, f"Expected 2 topic clusters, got {len(clusters)}: {clusters}"
    sports, cooking = set(docs[0]), set(docs[1])
    matched_sports = any(c == sports for c in clusters)
    matched_cooking = any(c == cooking for c in clusters)
    assert matched_sports and matched_cooking, \
        f"Clusters should recover the two planted topics exactly: {clusters}"

    print("PASS")
