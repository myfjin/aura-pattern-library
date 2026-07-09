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
    # Create test data
    test_data = list(range(1, 101))  # [1, 2, 3, ..., 100]
    
    # Build segment tree
    seg_tree = SegmentTree(test_data)
    
    # Test range sum queries
    print("Testing range sum queries:")
    print(f"Sum of elements [0, 9]: {seg_tree.range_sum(0, 9)}")  # Should be 55
    print(f"Sum of elements [10, 19]: {seg_tree.range_sum(10, 19)}")  # Should be 155
    print(f"Sum of elements [0, 99]: {seg_tree.range_sum(0, 99)}")  # Should be 5050
    
    # Test range min queries
    print("\nTesting range min queries:")
    print(f"Min of elements [0, 9]: {seg_tree.range_min(0, 9)}")  # Should be 1
    print(f"Min of elements [10, 19]: {seg_tree.range_min(10, 19)}")  # Should be 11
    print(f"Min of elements [50, 99]: {seg_tree.range_min(50, 99)}")  # Should be 51
    
    # Test updates
    print("\nTesting updates:")
    print(f"Sum of elements [0, 4]: {seg_tree.range_sum(0, 4)}")  # Should be 15
    seg_tree.update(2, 100)  # Update index 2 (value 3) to 100
    print(f"After updating index 2 to 100, sum of elements [0, 4]: {seg_tree.range_sum(0, 4)}")  # Should be 112
    print(f"After updating index 2 to 100, min of elements [0, 4]: {seg_tree.range_min(0, 4)}")  # Should be 1
    
    # Test edge cases
    print("\nTesting edge cases:")
    print(f"Sum of single element [5, 5]: {seg_tree.range_sum(5, 5)}")  # Should be 6
    print(f"Min of single element [5, 5]: {seg_tree.range_min(5, 5)}")  # Should be 6
    
    # Test error handling
    print("\nTesting error handling:")
    try:
        seg_tree.range_sum(5, 3)  # Should raise ValueError
    except ValueError as e:
        print(f"Caught expected error: {e}")
    
    try:
        seg_tree.range_sum(-1, 5)  # Should raise IndexError
    except IndexError as e:
        print(f"Caught expected error: {e}")