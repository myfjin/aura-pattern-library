"""
Quadtree: spatial indexing for range queries on 2D point sets.

Core idea: recursively subdivide space into 4 quadrants; insert points;
range query recursively searches overlapping cells, much fewer distance
checks than brute force on large sets.

When to use: spatial search, collision detection, visibility culling.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

from typing import List, Tuple, Optional

class QuadTree:
    def __init__(self, bounds: Tuple[float, float, float, float], max_points: int = 4):
        """bounds = (minx, miny, maxx, maxy)"""
        self.bounds = bounds
        self.max_points = max_points
        self.points: List[Tuple[float, float]] = []
        self.children: List[Optional[QuadTree]] = [None] * 4
        self.is_leaf = True

    def insert(self, point: Tuple[float, float]) -> bool:
        minx, miny, maxx, maxy = self.bounds
        x, y = point
        if not (minx <= x <= maxx and miny <= y <= maxy):
            return False

        if self.is_leaf:
            self.points.append(point)
            if len(self.points) > self.max_points:
                self._subdivide()
            return True
        else:
            for child in self.children:
                if child and child.insert(point):
                    return True
        return False

    def _subdivide(self):
        minx, miny, maxx, maxy = self.bounds
        midx, midy = (minx + maxx) / 2, (miny + maxy) / 2
        quads = [
            (minx, midy, midx, maxy),  # top-left
            (midx, midy, maxx, maxy),  # top-right
            (minx, miny, midx, midy),  # bottom-left
            (midx, miny, maxx, midy),  # bottom-right
        ]
        self.children = [QuadTree(bounds, self.max_points) for bounds in quads]
        for p in self.points:
            for child in self.children:
                child.insert(p)
        self.is_leaf = False
        self.points = []

    def range_query(self, bounds: Tuple[float, float, float, float],
                    node_count: List[int]) -> List[Tuple[float, float]]:
        """Find all points within bounds; count nodes visited."""
        node_count[0] += 1
        minx, miny, maxx, maxy = self.bounds
        qx0, qy0, qx1, qy1 = bounds

        if not (qx1 >= minx and qx0 <= maxx and qy1 >= miny and qy0 <= maxy):
            return []

        result = []
        if self.is_leaf:
            for p in self.points:
                if qx0 <= p[0] <= qx1 and qy0 <= p[1] <= qy1:
                    result.append(p)
        else:
            for child in self.children:
                if child:
                    result.extend(child.range_query(bounds, node_count))
        return result

if __name__ == '__main__':
    import random
    random.seed(42)

    # Build tree with random points
    tree = QuadTree((0, 0, 100, 100), max_points=4)
    points = [(random.uniform(0, 100), random.uniform(0, 100)) for _ in range(100)]
    for p in points:
        tree.insert(p)

    # Test range query: should match brute force
    query_bounds = (20, 20, 50, 50)
    tree_nodes = [0]
    qt_result = tree.range_query(query_bounds, tree_nodes)
    bf_result = [p for p in points if query_bounds[0] <= p[0] <= query_bounds[2]
                                   and query_bounds[1] <= p[1] <= query_bounds[3]]

    assert len(qt_result) == len(bf_result), f"QT found {len(qt_result)}, brute force {len(bf_result)}"
    assert set(qt_result) == set(bf_result), "Results should match"

    # Tree should visit fewer nodes than full scan (not always, but typically for small query)
    # Just verify it doesn't crash and gives reasonable count
    assert tree_nodes[0] > 0, "Should visit at least 1 node"
    assert tree_nodes[0] <= 100, "Should not visit unreasonably many nodes"

    # Test small query
    small_bounds = (40, 40, 45, 45)
    small_nodes = [0]
    small_result = tree.range_query(small_bounds, small_nodes)
    small_bf = [p for p in points if 40 <= p[0] <= 45 and 40 <= p[1] <= 45]
    assert len(small_result) == len(small_bf), "Small query should match brute force"

    print("PASS")
