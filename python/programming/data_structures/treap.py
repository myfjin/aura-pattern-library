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
        """Remove ONE instance of value from the treap. Returns True if removed.

        (The former split-based version split (<=v | >v) and then searched for
        v inside the >v half — it could never find it, so erase was a no-op
        that always returned False. Replaced with a recursive find-and-merge.)
        """
        def _erase(node: Optional[TreapNode]) -> Tuple[Optional[TreapNode], bool]:
            if node is None:
                return None, False
            if value == node.value:
                return self._merge(node.left, node.right), True
            if value < node.value:
                node.left, removed = _erase(node.left)
            else:
                node.right, removed = _erase(node.right)
            node.update_size()
            return node, removed

        self.root, removed = _erase(self.root)
        return removed
    
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

def _check_heap(node: Optional[TreapNode]) -> bool:
    """Every parent's priority must dominate its children (the treap invariant)."""
    if node is None:
        return True
    for child in (node.left, node.right):
        if child is not None and child.priority > node.priority:
            return False
    return _check_heap(node.left) and _check_heap(node.right)


def main():
    """Self-test: BST+heap invariants, kth vs sorted truth, multiset erase,
    and a sorted-list oracle fuzz."""
    random.seed(42)
    t = Treap()
    values = [10, 5, 15, 3, 7, 12, 20, 1, 6, 8]
    for v in values:
        t.insert(v)

    # In-order traversal must equal the sorted input; sizes must agree.
    assert t.to_list() == sorted(values), f"inorder {t.to_list()} != sorted input"
    assert t.size() == 10

    # Both invariants hold structurally: BST order (checked above via inorder)
    # AND the heap property on priorities.
    assert _check_heap(t.root), "heap property violated somewhere in the treap"

    # kth is exactly the sorted rank, over every valid k.
    truth = sorted(values)
    for k in range(10):
        assert t.kth(k) == truth[k], f"kth({k}) must be {truth[k]}, got {t.kth(k)}"
    for bad_k in (-1, 10):
        try:
            t.kth(bad_k)
            assert False, f"kth({bad_k}) accepted out-of-range index"
        except IndexError:
            pass

    # find: exact membership.
    assert t.find(7) is True and t.find(9) is False

    # Multiset semantics: duplicate inserts count, erase removes ONE instance.
    t.insert(7)
    assert t.size() == 11 and t.to_list().count(7) == 2
    assert t.erase(7) is True
    assert t.to_list().count(7) == 1, "erase removed more than one duplicate"
    assert t.erase(99) is False, "erasing a missing value reported success"
    assert t.size() == 10

    # Oracle fuzz: 500 random insert/erase ops against a plain sorted list.
    import bisect
    oracle = sorted(t.to_list())
    for _ in range(500):
        v = random.randint(0, 40)
        if random.random() < 0.6:
            t.insert(v)
            bisect.insort(oracle, v)
        else:
            expected = v in oracle
            assert t.erase(v) == expected, f"erase({v}) disagrees with oracle"
            if expected:
                oracle.remove(v)
    assert t.to_list() == oracle, "final treap diverged from the sorted oracle"
    assert t.size() == len(oracle)
    assert _check_heap(t.root), "heap property lost during the fuzz"

    print(f"treap: inorder sorted, heap invariant held, kth==rank for all k, "
          f"multiset erase-one, 500-op oracle agreed (size {t.size()}) — PASS")

if __name__ == "__main__":
    main()