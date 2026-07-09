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
    """Demo of the interval tree functionality."""
    # Create interval tree
    tree = IntervalTree()
    
    # Insert 50 intervals
    intervals = []
    for i in range(50):
        start = i * 2
        end = start + (i % 5) + 1
        interval = Interval(start, end, f"data_{i}")
        intervals.append(interval)
        tree.insert(interval)
    
    print(f"Inserted {len(intervals)} intervals")
    
    # Test query_overlap with a few test intervals
    test_intervals = [
        Interval(5, 10),
        Interval(20, 25),
        Interval(0, 1),
        Interval(95, 100)
    ]
    
    for test_interval in test_intervals:
        overlapping = tree.query_overlap(test_interval)
        print(f"Intervals overlapping with {test_interval}: {len(overlapping)} found")
        if len(overlapping) <= 5:  # Only print if not too many
            for interval in overlapping:
                print(f"  {interval}")
    
    # Test deletion
    print("\nTesting deletion:")
    delete_count = 0
    for i in range(0, len(intervals), 10):  # Delete every 10th interval
        if tree.delete(intervals[i]):
            delete_count += 1
    print(f"Deleted {delete_count} intervals")
    
    # Verify deletion by querying
    remaining = tree.inorder_traversal()
    print(f"Remaining intervals in tree: {len(remaining)}")
    
    # Final verification - query a known interval
    final_query = Interval(4, 8)
    final_overlaps = tree.query_overlap(final_query)
    print(f"\nFinal query for {final_query}: {len(final_overlaps)} overlapping intervals")


if __name__ == "__main__":
    main()