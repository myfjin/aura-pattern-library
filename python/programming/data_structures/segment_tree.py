# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
from typing import List, Optional, Union
import sys


class Node:
    """Represents a node in the segment tree."""
    
    def __init__(self, start: int, end: int) -> None:
        self.start = start
        self.end = end
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None
        self.sum = 0
        self.min = sys.maxsize


class SegmentTree:
    """A segment tree implementation supporting range sum and range minimum queries."""
    
    def __init__(self, data: List[Union[int, float]]) -> None:
        """
        Initialize the segment tree with the given data.
        
        Args:
            data: List of numbers to build the segment tree from.
            
        Raises:
            ValueError: If data is empty.
        """
        if not data:
            raise ValueError("Data cannot be empty")
        
        self.data = data[:]
        self.root = self._build_tree(0, len(data) - 1)
    
    def _build_tree(self, start: int, end: int) -> Node:
        """Build the segment tree recursively."""
        node = Node(start, end)
        
        # Leaf node
        if start == end:
            node.sum = self.data[start]
            node.min = self.data[start]
            return node
        
        # Internal node
        mid = (start + end) // 2
        node.left = self._build_tree(start, mid)
        node.right = self._build_tree(mid + 1, end)
        
        node.sum = node.left.sum + node.right.sum
        node.min = min(node.left.min, node.right.min)
        
        return node
    
    def update(self, index: int, value: Union[int, float]) -> None:
        """
        Update the value at the given index.
        
        Args:
            index: Index to update.
            value: New value.
            
        Raises:
            IndexError: If index is out of bounds.
        """
        if index < 0 or index >= len(self.data):
            raise IndexError("Index out of bounds")
        
        self._update_helper(self.root, index, value)
        self.data[index] = value
    
    def _update_helper(self, node: Node, index: int, value: Union[int, float]) -> None:
        """Helper method for updating the segment tree."""
        # Leaf node
        if node.start == node.end:
            node.sum = value
            node.min = value
            return
        
        # Internal node
        mid = (node.start + node.end) // 2
        if index <= mid:
            self._update_helper(node.left, index, value)
        else:
            self._update_helper(node.right, index, value)
        
        node.sum = node.left.sum + node.right.sum
        node.min = min(node.left.min, node.right.min)
    
    def range_sum(self, start: int, end: int) -> Union[int, float]:
        """
        Calculate the sum of elements in the range [start, end].
        
        Args:
            start: Start index (inclusive).
            end: End index (inclusive).
            
        Returns:
            Sum of elements in the range.
            
        Raises:
            IndexError: If start or end indices are out of bounds.
            ValueError: If start > end.
        """
        if start < 0 or end >= len(self.data):
            raise IndexError("Range indices out of bounds")
        if start > end:
            raise ValueError("Start index cannot be greater than end index")
        
        return self._range_sum_helper(self.root, start, end)
    
    def _range_sum_helper(self, node: Node, start: int, end: int) -> Union[int, float]:
        """Helper method for range sum query."""
        # Total overlap
        if node.start >= start and node.end <= end:
            return node.sum
        
        # No overlap
        if node.start > end or node.end < start:
            return 0
        
        # Partial overlap
        return (self._range_sum_helper(node.left, start, end) + 
                self._range_sum_helper(node.right, start, end))
    
    def range_min(self, start: int, end: int) -> Union[int, float]:
        """
        Find the minimum element in the range [start, end].
        
        Args:
            start: Start index (inclusive).
            end: End index (inclusive).
            
        Returns:
            Minimum element in the range.
            
        Raises:
            IndexError: If start or end indices are out of bounds.
            ValueError: If start > end.
        """
        if start < 0 or end >= len(self.data):
            raise IndexError("Range indices out of bounds")
        if start > end:
            raise ValueError("Start index cannot be greater than end index")
        
        return self._range_min_helper(self.root, start, end)
    
    def _range_min_helper(self, node: Node, start: int, end: int) -> Union[int, float]:
        """Helper method for range minimum query."""
        # Total overlap
        if node.start >= start and node.end <= end:
            return node.min
        
        # No overlap
        if node.start > end or node.end < start:
            return sys.maxsize
        
        # Partial overlap
        return min(self._range_min_helper(node.left, start, end),
                   self._range_min_helper(node.right, start, end))


if __name__ == "__main__":
    # Self-test: the old demo SAID "Should be 55" in comments and never checked.
    # Every planted truth is now asserted, plus an oracle fuzz.
    import random
    random.seed(42)

    st = SegmentTree(list(range(1, 101)))  # [1..100]
    assert st.range_sum(0, 9) == 55, f"1+..+10 must be 55, got {st.range_sum(0, 9)}"
    assert st.range_sum(10, 19) == 155
    assert st.range_sum(0, 99) == 5050, "Gauss disagrees: 1..100 must sum to 5050"
    assert st.range_min(0, 9) == 1
    assert st.range_min(10, 19) == 11
    assert st.range_min(50, 99) == 51

    # Point update propagates to sums AND mins along the path.
    assert st.range_sum(0, 4) == 15
    st.update(2, 100)
    assert st.range_sum(0, 4) == 112, f"15 - 3 + 100 must be 112, got {st.range_sum(0, 4)}"
    assert st.range_min(0, 4) == 1, "min corrupted by an unrelated update"
    st.update(0, -7)
    assert st.range_min(0, 4) == -7, "negative update must become the new min"
    assert st.range_sum(0, 0) == -7

    # Single-element ranges are their own truth.
    assert st.range_sum(5, 5) == 6 and st.range_min(5, 5) == 6

    # Oracle fuzz: 600 mixed update/sum/min ops against a plain list.
    data = [random.randint(-50, 50) for _ in range(60)]
    tree = SegmentTree(data)
    for _ in range(600):
        op = random.random()
        if op < 0.4:
            i, v = random.randint(0, 59), random.randint(-50, 50)
            tree.update(i, v)
            data[i] = v
        else:
            l = random.randint(0, 59)
            r = random.randint(l, 59)
            if op < 0.7:
                assert tree.range_sum(l, r) == sum(data[l:r + 1]), \
                    f"range_sum({l},{r}) diverged from the oracle"
            else:
                assert tree.range_min(l, r) == min(data[l:r + 1]), \
                    f"range_min({l},{r}) diverged from the oracle"

    # Refusals: inverted and out-of-bounds ranges, empty construction.
    for call, exc in ((lambda: st.range_sum(5, 3), ValueError),
                      (lambda: st.range_min(5, 3), ValueError),
                      (lambda: st.range_sum(-1, 5), IndexError),
                      (lambda: st.update(100, 1), IndexError),
                      (lambda: SegmentTree([]), ValueError)):
        try:
            call()
            assert False, "invalid call accepted"
        except exc:
            pass

    print("segment_tree: 55/155/5050 exact, update → sum 112 & min -7, "
          "600-op sum+min oracle agreed — PASS")