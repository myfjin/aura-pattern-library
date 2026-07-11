#!/usr/bin/env python3
"""
Fenwick Tree (Binary Indexed Tree) implementation with comprehensive functionality.
Supports point updates and prefix/range sum queries in O(log n) time.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

from typing import List, Union
import random


class FenwickTree:
    """
    A Fenwick Tree (Binary Indexed Tree) implementation for efficient prefix sum queries
    and point updates.
    
    The Fenwick Tree allows:
    - Point updates in O(log n) time
    - Prefix sum queries in O(log n) time
    - Range sum queries in O(log n) time
    """
    
    def __init__(self, size: int) -> None:
        """
        Initialize a Fenwick Tree with the given size.
        
        Args:
            size: The size of the Fenwick Tree (number of elements)
            
        Raises:
            ValueError: If size is not positive
        """
        if size <= 0:
            raise ValueError("Size must be positive")
        
        self._size: int = size
        self._tree: List[int] = [0] * (size + 1)  # 1-indexed array
    
    @property
    def size(self) -> int:
        """Get the size of the Fenwick Tree."""
        return self._size
    
    def _lsb(self, index: int) -> int:
        """
        Get the least significant bit of an integer.
        
        Args:
            index: The integer to get LSB for
            
        Returns:
            The least significant bit
        """
        return index & (-index)
    
    def point_update(self, index: int, delta: int) -> None:
        """
        Add delta to the element at the given index.
        
        Args:
            index: 0-based index of the element to update
            delta: Value to add to the element
            
        Raises:
            IndexError: If index is out of bounds
        """
        if index < 0 or index >= self._size:
            raise IndexError(f"Index {index} out of bounds for size {self._size}")
        
        # Convert to 1-based indexing
        i = index + 1
        while i <= self._size:
            self._tree[i] += delta
            i += self._lsb(i)
    
    def prefix_sum(self, index: int) -> int:
        """
        Calculate the sum of elements from index 0 to the given index (inclusive).
        
        Args:
            index: 0-based index up to which to calculate the prefix sum
            
        Returns:
            The prefix sum from index 0 to the given index
            
        Raises:
            IndexError: If index is out of bounds
        """
        if index < 0 or index >= self._size:
            raise IndexError(f"Index {index} out of bounds for size {self._size}")
        
        # Convert to 1-based indexing
        i = index + 1
        result = 0
        while i > 0:
            result += self._tree[i]
            i -= self._lsb(i)
        return result
    
    def range_sum(self, left: int, right: int) -> int:
        """
        Calculate the sum of elements from left index to right index (inclusive).
        
        Args:
            left: 0-based left index of the range
            right: 0-based right index of the range
            
        Returns:
            The sum of elements in the given range
            
        Raises:
            IndexError: If indices are out of bounds or left > right
        """
        if left < 0 or right >= self._size:
            raise IndexError(f"Range [{left}, {right}] out of bounds for size {self._size}")
        if left > right:
            raise IndexError(f"Left index {left} cannot be greater than right index {right}")
        
        if left == 0:
            return self.prefix_sum(right)
        else:
            return self.prefix_sum(right) - self.prefix_sum(left - 1)
    
    def __str__(self) -> str:
        """String representation of the Fenwick Tree."""
        return f"FenwickTree(size={self._size}, tree={self._tree})"


def main() -> None:
    """Self-test: exact planted sums (0-indexed) + a 1000-op ASSERTED oracle
    fuzz (the old demo printed mismatches instead of failing on them)."""
    random.seed(42)

    # Planted values: [2, 7, 1, 8, 2, 8] at indices 0..5.
    ft = FenwickTree(10)
    for i, v in enumerate([2, 7, 1, 8, 2, 8]):
        ft.point_update(i, v)
    assert ft.prefix_sum(5) == 28, f"2+7+1+8+2+8 must be 28, got {ft.prefix_sum(5)}"
    assert ft.range_sum(1, 3) == 16, f"7+1+8 must be 16, got {ft.range_sum(1, 3)}"
    assert ft.range_sum(0, 0) == 2 and ft.range_sum(5, 5) == 8
    assert ft.prefix_sum(9) == 28, "untouched tail changed the total"

    # Negative deltas subtract exactly.
    ft.point_update(3, -8)
    assert ft.range_sum(3, 3) == 0 and ft.prefix_sum(9) == 20

    # THE OLD DEMO'S HOLE: mismatches were printed, not fatal. Now they fail.
    size = 100
    fresh = FenwickTree(size)
    arr = [0] * size
    for _ in range(1000):
        op = random.choice(["update", "prefix", "range"])
        if op == "update":
            idx, val = random.randint(0, size - 1), random.randint(-100, 100)
            fresh.point_update(idx, val)
            arr[idx] += val
        elif op == "prefix":
            idx = random.randint(0, size - 1)
            assert fresh.prefix_sum(idx) == sum(arr[:idx + 1]), \
                f"prefix_sum({idx}) diverged from the oracle"
        else:
            left = random.randint(0, size - 1)
            right = random.randint(left, size - 1)
            assert fresh.range_sum(left, right) == sum(arr[left:right + 1]), \
                f"range_sum({left},{right}) diverged from the oracle"
    # Full final sweep: every prefix agrees.
    for i in range(size):
        assert fresh.prefix_sum(i) == sum(arr[:i + 1]), f"final prefix {i} diverged"

    # Refusals.
    for call in (lambda: ft.point_update(10, 1), lambda: ft.point_update(-1, 1),
                 lambda: ft.prefix_sum(10), lambda: ft.range_sum(5, 2),
                 lambda: FenwickTree(0)):
        try:
            call()
            assert False, "invalid call accepted"
        except (IndexError, ValueError):
            pass

    print("fenwick_tree: planted sums 28/16 exact, negative delta, 1000-op "
          "oracle asserted, 100 final prefixes agreed — PASS")


if __name__ == "__main__":
    main()