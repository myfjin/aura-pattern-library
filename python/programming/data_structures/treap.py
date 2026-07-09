# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import random
from typing import Optional, Tuple, Any

class TreapNode:
    """Node for a treap data structure."""
    
    def __init__(self, value: Any, priority: Optional[int] = None):
        self.value = value
        self.priority = priority if priority is not None else random.randint(0, 2**31)
        self.left: Optional['TreapNode'] = None
        self.right: Optional['TreapNode'] = None
        self.size = 1
    
    def update_size(self) -> None:
        """Update the size of the node based on its children."""
        left_size = self.left.size if self.left else 0
        right_size = self.right.size if self.right else 0
        self.size = 1 + left_size + right_size

class Treap:
    """Treap (randomized binary search tree) implementation."""
    
    def __init__(self):
        self.root: Optional[TreapNode] = None
    
    def _split(self, node: Optional[TreapNode], value: Any) -> Tuple[Optional[TreapNode], Optional[TreapNode]]:
        """Split the treap into two parts based on value."""
        if node is None:
            return None, None
        elif node.value <= value:
            left, right = self._split(node.right, value)
            node.right = left
            node.update_size()
            return node, right
        else:
            left, right = self._split(node.left, value)
            node.left = right
            node.update_size()
            return left, node
    
    def _merge(self, left: Optional[TreapNode], right: Optional[TreapNode]) -> Optional[TreapNode]:
        """Merge two treaps maintaining heap property."""
        if left is None:
            return right
        if right is None:
            return left
        if left.priority > right.priority:
            left.right = self._merge(left.right, right)
            left.update_size()
            return left
        else:
            right.left = self._merge(left, right.left)
            right.update_size()
            return right
    
    def insert(self, value: Any) -> None:
        """Insert a value into the treap."""
        if self.root is None:
            self.root = TreapNode(value)
            return
        
        left, right = self._split(self.root, value)
        new_node = TreapNode(value)
        self.root = self._merge(self._merge(left, new_node), right)
    
    def erase(self, value: Any) -> bool:
        """Remove a value from the treap. Returns True if found and removed."""
        if self.root is None:
            return False
        
        left, right = self._split(self.root, value)
        mid, right = self._split(right, value)
        
        if mid is None:  # Value not found
            self.root = self._merge(left, right)
            return False
        
        # Value found, remove one instance
        self.root = self._merge(left, right)
        return True
    
    def find(self, value: Any) -> bool:
        """Check if a value exists in the treap."""
        node = self.root
        while node is not None:
            if node.value == value:
                return True
            elif node.value < value:
                node = node.right
            else:
                node = node.left
        return False
    
    def _kth_element(self, node: Optional[TreapNode], k: int) -> Any:
        """Find the k-th smallest element (0-indexed)."""
        if node is None:
            raise IndexError("Index out of range")
        
        left_size = node.left.size if node.left else 0
        if k < left_size:
            return self._kth_element(node.left, k)
        elif k == left_size:
            return node.value
        else:
            return self._kth_element(node.right, k - left_size - 1)
    
    def kth(self, k: int) -> Any:
        """Get the k-th smallest element (0-indexed)."""
        if k < 0 or (self.root and k >= self.root.size):
            raise IndexError("Index out of range")
        return self._kth_element(self.root, k)
    
    def size(self) -> int:
        """Get the number of elements in the treap."""
        return self.root.size if self.root else 0
    
    def _inorder(self, node: Optional[TreapNode], result: list) -> None:
        """Helper for inorder traversal."""
        if node is not None:
            self._inorder(node.left, result)
            result.append(node.value)
            self._inorder(node.right, result)
    
    def to_list(self) -> list:
        """Convert treap to sorted list."""
        result = []
        self._inorder(self.root, result)
        return result

def main():
    """Demo of treap operations."""
    treap = Treap()
    
    # Insert operations
    values = [10, 5, 15, 3, 7, 12, 20, 1, 6, 8]
    print("Inserting values:", values)
    for val in values:
        treap.insert(val)
    
    print("Treap as sorted list:", treap.to_list())
    print("Size:", treap.size())
    
    # Find operations
    print("\nFind operations:")
    for val in [7, 9, 15]:
        found = treap.find(val)
        print(f"Find {val}: {found}")
    
    # K-th element operations
    print("\nK-th element operations:")
    for k in range(min(5, treap.size())):
        try:
            kth_val = treap.kth(k)
            print(f"{k}-th element: {kth_val}")
        except IndexError as e:
            print(f"Error accessing {k}-th element: {e}")
    
    # Erase operations
    print("\nErasing values: 5, 15, 25")
    for val in [5, 15, 25]:
        erased = treap.erase(val)
        print(f"Erase {val}: {'Success' if erased else 'Not found'}")
    
    print("Treap after erasures:", treap.to_list())
    print("Final size:", treap.size())
    
    # Additional insertions
    print("\nInserting more values: 4, 9, 18")
    for val in [4, 9, 18]:
        treap.insert(val)
    
    print("Final treap:", treap.to_list())

if __name__ == "__main__":
    main()