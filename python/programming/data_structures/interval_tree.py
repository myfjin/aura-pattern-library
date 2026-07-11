# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
from typing import List, Optional, Tuple
import sys


class Interval:
    """Represents an interval with start and end points."""
    
    def __init__(self, start: float, end: float, data: Optional[object] = None):
        if start > end:
            raise ValueError("Interval start must be less than or equal to end")
        self.start = start
        self.end = end
        self.data = data
    
    def __repr__(self):
        return f"Interval({self.start}, {self.end}, {self.data})"
    
    def __eq__(self, other):
        if not isinstance(other, Interval):
            return False
        return (self.start == other.start and 
                self.end == other.end and 
                self.data == other.data)
    
    def overlaps(self, other: 'Interval') -> bool:
        """Check if this interval overlaps with another interval."""
        return self.start <= other.end and other.start <= self.end


class IntervalNode:
    """Node in the interval tree."""
    
    def __init__(self, interval: Interval):
        self.interval = interval
        self.max_end = interval.end
        self.left: Optional['IntervalNode'] = None
        self.right: Optional['IntervalNode'] = None


class IntervalTree:
    """Interval tree implementation for efficient interval queries."""
    
    def __init__(self):
        self.root: Optional[IntervalNode] = None
    
    def insert(self, interval: Interval) -> None:
        """Insert an interval into the tree."""
        if not isinstance(interval, Interval):
            raise TypeError("Expected Interval object")
        self.root = self._insert(self.root, interval)
    
    def _insert(self, node: Optional[IntervalNode], interval: Interval) -> IntervalNode:
        """Helper method to insert an interval recursively."""
        if node is None:
            return IntervalNode(interval)
        
        # Insert in left or right subtree
        if interval.start < node.interval.start:
            node.left = self._insert(node.left, interval)
        else:
            node.right = self._insert(node.right, interval)
        
        # Update max_end
        node.max_end = max(node.max_end, interval.end)
        return node
    
    def query_overlap(self, interval: Interval) -> List[Interval]:
        """Find all intervals that overlap with the given interval."""
        if not isinstance(interval, Interval):
            raise TypeError("Expected Interval object")
        result = []
        self._query_overlap(self.root, interval, result)
        return result
    
    def _query_overlap(self, node: Optional[IntervalNode], interval: Interval, result: List[Interval]) -> None:
        """Helper method to query overlapping intervals recursively."""
        if node is None:
            return
        
        # If interval overlaps with current node's interval, add to result
        if node.interval.overlaps(interval):
            result.append(node.interval)
        
        # Check left subtree if it might contain overlapping intervals
        if node.left is not None and node.left.max_end >= interval.start:
            self._query_overlap(node.left, interval, result)
        
        # Check right subtree if it might contain overlapping intervals
        if node.right is not None and node.interval.start <= interval.end:
            self._query_overlap(node.right, interval, result)
    
    def delete(self, interval: Interval) -> bool:
        """Delete an interval from the tree. Returns True if found and deleted."""
        if not isinstance(interval, Interval):
            raise TypeError("Expected Interval object")
        self.root, deleted = self._delete(self.root, interval)
        return deleted
    
    def _delete(self, node: Optional[IntervalNode], interval: Interval) -> Tuple[Optional[IntervalNode], bool]:
        """Helper method to delete an interval recursively."""
        if node is None:
            return None, False
        
        deleted = False
        if interval.start < node.interval.start:
            node.left, deleted = self._delete(node.left, interval)
        elif interval.start > node.interval.start:
            node.right, deleted = self._delete(node.right, interval)
        else:  # interval.start == node.interval.start
            if interval.end == node.interval.end and interval.data == node.interval.data:
                # Found the node to delete
                # Case 1: Node with only one child or no child
                if node.left is None:
                    return node.right, True
                elif node.right is None:
                    return node.left, True
                
                # Case 2: Node with two children
                # Get inorder successor (smallest in right subtree)
                successor = self._min_value_node(node.right)
                
                # Copy the successor's data to this node
                node.interval = successor.interval
                
                # Delete the successor
                node.right, _ = self._delete(node.right, successor.interval)
                deleted = True
            else:
                # Start matches but other properties don't, search in right subtree
                node.right, deleted = self._delete(node.right, interval)
        
        # Update max_end if node still exists
        if node is not None:
            left_max = node.left.max_end if node.left else float('-inf')
            right_max = node.right.max_end if node.right else float('-inf')
            node.max_end = max(node.interval.end, left_max, right_max)
        
        return node, deleted
    
    def _min_value_node(self, node: IntervalNode) -> IntervalNode:
        """Find the node with the minimum start value."""
        current = node
        while current.left is not None:
            current = current.left
        return current
    
    def inorder_traversal(self) -> List[Interval]:
        """Return all intervals in sorted order."""
        result = []
        self._inorder_traversal(self.root, result)
        return result
    
    def _inorder_traversal(self, node: Optional[IntervalNode], result: List[Interval]) -> None:
        """Helper method for inorder traversal."""
        if node is not None:
            self._inorder_traversal(node.left, result)
            result.append(node.interval)
            self._inorder_traversal(node.right, result)


def main():
    """Self-test: overlap queries vs a brute-force oracle, exact planted hits,
    delete correctness, and max_end augmentation integrity."""
    import random
    random.seed(42)

    # Planted layout: [0,3], [2,5], [6,8], [10,15].
    tree = IntervalTree()
    a, b, c, d = (Interval(0, 3, "a"), Interval(2, 5, "b"),
                  Interval(6, 8, "c"), Interval(10, 15, "d"))
    for iv in (a, b, c, d):
        tree.insert(iv)

    # Exact overlap sets (touching endpoints count: start <= end).
    hits = tree.query_overlap(Interval(2, 3))
    assert sorted(h.data for h in hits) == ["a", "b"], f"[2,3] must hit a+b, got {hits}"
    assert [h.data for h in tree.query_overlap(Interval(9, 9))] == [], "gap [9,9] hit something"
    assert sorted(h.data for h in tree.query_overlap(Interval(5, 6))) == ["b", "c"], \
        "touching endpoints [5,6] must hit b and c"
    assert sorted(h.data for h in tree.query_overlap(Interval(-10, 100))) == list("abcd")

    # Delete removes exactly the matching interval; queries update.
    assert tree.delete(b) is True
    assert tree.delete(b) is False, "double delete reported success"
    assert sorted(h.data for h in tree.query_overlap(Interval(2, 3))) == ["a"]
    assert len(tree.inorder_traversal()) == 3
    assert sum(h.start for h in tree.query_overlap(Interval(-10, 100))) == 16, \
        "remaining intervals must start at 0+6+10 = 16"

    # Inorder is sorted by start.
    starts = [iv.start for iv in tree.inorder_traversal()]
    assert starts == sorted(starts), "inorder traversal not sorted by start"

    # THE STRUCTURAL CLAIM: tree query == brute-force scan over 300 random
    # queries against 80 random intervals (including duplicates and nesting).
    ivs = []
    big = IntervalTree()
    for i in range(80):
        s = random.randint(0, 200)
        e = s + random.randint(0, 30)
        iv = Interval(s, e, i)
        ivs.append(iv)
        big.insert(iv)
    for _ in range(300):
        qs = random.randint(-10, 220)
        qe = qs + random.randint(0, 40)
        q = Interval(qs, qe)
        got = sorted(h.data for h in big.query_overlap(q))
        want = sorted(iv.data for iv in ivs if iv.overlaps(q))
        assert got == want, f"query [{qs},{qe}]: tree {got} != brute-force {want}"

    # Deleting half the intervals keeps the oracle agreement (max_end must
    # be recomputed correctly on the way up, or queries go blind).
    for iv in ivs[::2]:
        assert big.delete(iv) is True, f"failed to delete {iv}"
    kept = ivs[1::2]
    for _ in range(200):
        qs = random.randint(-10, 220)
        qe = qs + random.randint(0, 40)
        q = Interval(qs, qe)
        got = sorted(h.data for h in big.query_overlap(q))
        want = sorted(iv.data for iv in kept if iv.overlaps(q))
        assert got == want, f"post-delete query [{qs},{qe}] diverged (max_end stale?)"
    assert len(big.inorder_traversal()) == 40

    # Refusals: inverted interval, non-Interval arguments.
    try:
        Interval(5, 2)
        assert False, "inverted interval accepted"
    except ValueError:
        pass
    for call in (lambda: tree.insert("x"), lambda: tree.query_overlap((1, 2)),
                 lambda: tree.delete(42)):
        try:
            call()
            assert False, "non-Interval argument accepted"
        except TypeError:
            pass

    print("interval_tree: planted overlaps exact (touch counts), 300+200-query "
          "oracle agreed through 40 deletes, refusals held — PASS")


if __name__ == "__main__":
    main()