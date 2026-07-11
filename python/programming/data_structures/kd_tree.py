"""
A complete k-d tree implementation for 2D points with insert, nearest neighbor,
and range search functionality.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

from typing import List, Optional, Tuple, Union
import math
import random


class KDNode:
    """Represents a node in the k-d tree."""
    
    def __init__(self, point: Tuple[float, float], depth: int = 0):
        """
        Initialize a KDNode.
        
        Args:
            point: A 2D point as a tuple (x, y)
            depth: The depth of this node in the tree
        """
        self.point: Tuple[float, float] = point
        self.left: Optional[KDNode] = None
        self.right: Optional[KDNode] = None
        self.depth: int = depth
    
    def __repr__(self) -> str:
        """String representation of the node."""
        return f"KDNode(point={self.point}, depth={self.depth})"


class KDTree:
    """A k-d tree for 2D points supporting insert, nearest neighbor, and range search."""
    
    def __init__(self):
        """Initialize an empty k-d tree."""
        self.root: Optional[KDNode] = None
    
    def insert(self, point: Tuple[float, float]) -> None:
        """
        Insert a point into the k-d tree.
        
        Args:
            point: A 2D point as a tuple (x, y)
        """
        if not isinstance(point, tuple) or len(point) != 2:
            raise ValueError("Point must be a tuple of two numbers")
        
        if not all(isinstance(coord, (int, float)) for coord in point):
            raise ValueError("Point coordinates must be numbers")
            
        self.root = self._insert_recursive(self.root, point, 0)
    
    def _insert_recursive(self, node: Optional[KDNode], point: Tuple[float, float], depth: int) -> KDNode:
        """
        Recursively insert a point into the tree.
        
        Args:
            node: Current node in the recursion
            point: Point to insert
            depth: Current depth in the tree
            
        Returns:
            Updated node after insertion
        """
        # If tree is empty, create root node
        if node is None:
            return KDNode(point, depth)
        
        # Calculate current dimension (0 for x, 1 for y)
        dim = depth % 2
        
        # Insert in left or right subtree based on current dimension
        if point[dim] < node.point[dim]:
            node.left = self._insert_recursive(node.left, point, depth + 1)
        else:
            node.right = self._insert_recursive(node.right, point, depth + 1)
            
        return node
    
    def nearest_neighbor(self, query_point: Tuple[float, float]) -> Optional[Tuple[float, float]]:
        """
        Find the nearest neighbor to a query point.
        
        Args:
            query_point: The point to find nearest neighbor for
            
        Returns:
            The nearest point in the tree, or None if tree is empty
        """
        if not isinstance(query_point, tuple) or len(query_point) != 2:
            raise ValueError("Query point must be a tuple of two numbers")
            
        if not all(isinstance(coord, (int, float)) for coord in query_point):
            raise ValueError("Query point coordinates must be numbers")
            
        if self.root is None:
            return None
            
        _, nearest = self._nearest_neighbor_recursive(
            self.root, query_point, self.root.point, float('inf'), 0
        )
        return nearest
    
    def _nearest_neighbor_recursive(
        self, 
        node: Optional[KDNode], 
        query_point: Tuple[float, float],
        best: Tuple[float, float], 
        best_dist: float, 
        depth: int
    ) -> Tuple[float, Tuple[float, float]]:
        """
        Recursively find the nearest neighbor.
        
        Args:
            node: Current node in recursion
            query_point: Point to find nearest neighbor for
            best: Current best point
            best_dist: Distance to current best point
            depth: Current depth in tree
            
        Returns:
            Tuple of (best distance, best point)
        """
        if node is None:
            return best_dist, best
            
        # Calculate distance to current node
        current_dist = self._euclidean_distance(query_point, node.point)
        
        # Update best if current node is closer
        if current_dist < best_dist:
            best = node.point
            best_dist = current_dist
            
        # Determine current splitting dimension
        dim = depth % 2
        
        # Determine which side to search first
        if query_point[dim] < node.point[dim]:
            best_dist, best = self._nearest_neighbor_recursive(
                node.left, query_point, best, best_dist, depth + 1
            )
            # Check if we need to search the other side
            if abs(query_point[dim] - node.point[dim]) < best_dist:
                best_dist, best = self._nearest_neighbor_recursive(
                    node.right, query_point, best, best_dist, depth + 1
                )
        else:
            best_dist, best = self._nearest_neighbor_recursive(
                node.right, query_point, best, best_dist, depth + 1
            )
            # Check if we need to search the other side
            if abs(query_point[dim] - node.point[dim]) < best_dist:
                best_dist, best = self._nearest_neighbor_recursive(
                    node.left, query_point, best, best_dist, depth + 1
                )
                
        return best_dist, best
    
    def range_search(
        self, 
        min_point: Tuple[float, float], 
        max_point: Tuple[float, float]
    ) -> List[Tuple[float, float]]:
        """
        Find all points within a given rectangular range.
        
        Args:
            min_point: Bottom-left corner of the range (min_x, min_y)
            max_point: Top-right corner of the range (max_x, max_y)
            
        Returns:
            List of points within the range
        """
        if self.root is None:
            return []
            
        # Validate inputs
        if not (isinstance(min_point, tuple) and len(min_point) == 2):
            raise ValueError("min_point must be a tuple of two numbers")
        if not (isinstance(max_point, tuple) and len(max_point) == 2):
            raise ValueError("max_point must be a tuple of two numbers")
            
        if not all(isinstance(coord, (int, float)) for coord in min_point + max_point):
            raise ValueError("Range coordinates must be numbers")
            
        if min_point[0] > max_point[0] or min_point[1] > max_point[1]:
            raise ValueError("min_point must be less than or equal to max_point in both dimensions")
            
        result: List[Tuple[float, float]] = []
        self._range_search_recursive(self.root, min_point, max_point, result, 0)
        return result
    
    def _range_search_recursive(
        self, 
        node: Optional[KDNode],
        min_point: Tuple[float, float], 
        max_point: Tuple[float, float],
        result: List[Tuple[float, float]], 
        depth: int
    ) -> None:
        """
        Recursively search for points within a range.
        
        Args:
            node: Current node in recursion
            min_point: Bottom-left corner of the range
            max_point: Top-right corner of the range
            result: List to accumulate results
            depth: Current depth in tree
        """
        if node is None:
            return
            
        # Check if current point is within range
        if (min_point[0] <= node.point[0] <= max_point[0] and 
            min_point[1] <= node.point[1] <= max_point[1]):
            result.append(node.point)
            
        # Determine current splitting dimension
        dim = depth % 2
        
        # Search left subtree if it could contain points in range
        if min_point[dim] <= node.point[dim]:
            self._range_search_recursive(node.left, min_point, max_point, result, depth + 1)
            
        # Search right subtree if it could contain points in range
        if max_point[dim] >= node.point[dim]:
            self._range_search_recursive(node.right, min_point, max_point, result, depth + 1)
    
    @staticmethod
    def _euclidean_distance(point1: Tuple[float, float], point2: Tuple[float, float]) -> float:
        """
        Calculate Euclidean distance between two points.
        
        Args:
            point1: First point
            point2: Second point
            
        Returns:
            Euclidean distance between the points
        """
        return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)


def main():
    """Self-test: nearest-neighbor and range search proven against brute-force
    scans over 200 random points — the k-d pruning must never lose a point."""
    random.seed(42)
    points = [(round(random.uniform(0, 100), 2), round(random.uniform(0, 100), 2))
              for _ in range(200)]
    tree = KDTree()
    for p in points:
        tree.insert(p)

    # Planted exactness: a point in the set is its own nearest neighbor.
    assert tree.nearest_neighbor(points[17]) == points[17], \
        "a stored point must be its own nearest neighbor"

    # THE STRUCTURAL CLAIM: NN via the tree == NN via brute force, 100 queries.
    # (A wrong prune silently returns a near-but-not-nearest point.)
    for _ in range(100):
        q = (random.uniform(-10, 110), random.uniform(-10, 110))
        got = tree.nearest_neighbor(q)
        best = min(points, key=lambda p: KDTree._euclidean_distance(p, q))
        d_got = KDTree._euclidean_distance(got, q)
        d_true = KDTree._euclidean_distance(best, q)
        assert abs(d_got - d_true) < 1e-9, \
            f"NN({q}) returned {got} at {d_got:.4f}, brute-force found {best} at {d_true:.4f}"

    # Range search == brute-force rectangle filter, 100 random rectangles.
    for _ in range(100):
        x1, x2 = sorted((random.uniform(0, 100), random.uniform(0, 100)))
        y1, y2 = sorted((random.uniform(0, 100), random.uniform(0, 100)))
        got = sorted(tree.range_search((x1, y1), (x2, y2)))
        want = sorted(p for p in points if x1 <= p[0] <= x2 and y1 <= p[1] <= y2)
        assert got == want, f"range ({x1:.1f},{y1:.1f})-({x2:.1f},{y2:.1f}) lost/added points"

    # Whole-plane range returns everything; empty rectangle returns nothing.
    assert len(tree.range_search((0, 0), (100, 100))) == 200
    assert tree.range_search((200, 200), (300, 300)) == []

    # Empty tree behaves.
    assert KDTree().nearest_neighbor((1, 1)) is None

    # Refusals: wrong dimensionality / types / inverted rectangle.
    for call in (lambda: tree.insert((1, 2, 3)), lambda: tree.nearest_neighbor("bad"),
                 lambda: tree.range_search((5, 5), (1, 1))):
        try:
            call()
            assert False, "invalid call accepted"
        except ValueError:
            pass

    print("kd_tree: 100 NN queries == brute force, 100 range queries == brute "
          "force over 200 points, self-NN exact — PASS")


if __name__ == "__main__":
    main()