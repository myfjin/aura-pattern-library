#!/usr/bin/env python3
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

from typing import List, Union

class BinaryIndexedTree:
    """A Binary Indexed Tree (Fenwick Tree) implementation for efficient prefix sum queries and updates."""
    
    def __init__(self, size: int) -> None:
        """
        Initialize a Binary Indexed Tree with the given size.
        
        Args:
            size: The number of elements the tree can hold (1-indexed)
            
        Raises:
            ValueError: If size is not positive
        """
        if size <= 0:
            raise ValueError("Size must be positive")
        
        self._size = size
        self._tree: List[int] = [0] * (size + 1)  # 1-indexed array
    
    @property
    def size(self) -> int:
        """Return the size of the tree."""
        return self._size
    
    def _lsb(self, index: int) -> int:
        """Get the least significant bit of index."""
        return index & (-index)
    
    def update(self, index: int, delta: int) -> None:
        """
        Update the value at the given index by adding delta.
        
        Args:
            index: 1-based index to update
            delta: Value to add to the element at index
            
        Raises:
            IndexError: If index is out of bounds
        """
        if index < 1 or index > self._size:
            raise IndexError(f"Index {index} out of bounds for size {self._size}")
        
        while index <= self._size:
            self._tree[index] += delta
            index += self._lsb(index)
    
    def prefix_sum(self, index: int) -> int:
        """
        Calculate the prefix sum from index 1 to the given index.
        
        Args:
            index: 1-based index up to which to calculate the prefix sum
            
        Returns:
            The sum of elements from index 1 to index
            
        Raises:
            IndexError: If index is out of bounds
        """
        if index < 0 or index > self._size:
            raise IndexError(f"Index {index} out of bounds for size {self._size}")
        
        result = 0
        while index > 0:
            result += self._tree[index]
            index -= self._lsb(index)
        return result
    
    def range_sum(self, left: int, right: int) -> int:
        """
        Calculate the sum of elements in the range [left, right] (inclusive).
        
        Args:
            left: 1-based left index of the range
            right: 1-based right index of the range
            
        Returns:
            The sum of elements from index left to right
            
        Raises:
            IndexError: If indices are out of bounds
            ValueError: If left > right
        """
        if left > right:
            raise ValueError("Left index cannot be greater than right index")
        if left < 1 or right > self._size:
            raise IndexError(f"Range [{left}, {right}] out of bounds for size {self._size}")
        
        if left == 1:
            return self.prefix_sum(right)
        return self.prefix_sum(right) - self.prefix_sum(left - 1)
    
    def __str__(self) -> str:
        """String representation of the Binary Indexed Tree."""
        return f"BinaryIndexedTree(size={self._size}, tree={self._tree[1:]})"


class Query:
    """A class to represent and execute queries on a Binary Indexed Tree."""
    
    def __init__(self, bit: BinaryIndexedTree) -> None:
        """
        Initialize a Query object with a Binary Indexed Tree.
        
        Args:
            bit: The Binary Indexed Tree to query
        """
        self._bit = bit
    
    def update(self, index: int, value: int) -> None:
        """
        Update the value at the given index.
        
        Args:
            index: 1-based index to update
            value: New value to set at the index
        """
        # First, we need to know the current value to compute the delta
        # For simplicity in this implementation, we assume the initial array is all zeros
        # In a more complete implementation, we would store the original array
        current_prefix = self._bit.prefix_sum(index)
        if index > 1:
            current_value = current_prefix - self._bit.prefix_sum(index - 1)
        else:
            current_value = current_prefix
            
        delta = value - current_value
        self._bit.update(index, delta)
    
    def prefix_sum(self, index: int) -> int:
        """
        Calculate the prefix sum up to the given index.
        
        Args:
            index: 1-based index up to which to calculate the prefix sum
            
        Returns:
            The prefix sum
        """
        return self._bit.prefix_sum(index)
    
    def range_sum(self, left: int, right: int) -> int:
        """
        Calculate the sum of elements in the range [left, right].
        
        Args:
            left: 1-based left index of the range
            right: 1-based right index of the range
            
        Returns:
            The sum of elements in the range
        """
        return self._bit.range_sum(left, right)


def main() -> None:
    """Self-test: exact sums on a planted array, set-vs-delta semantics,
    and an 800-op oracle fuzz against a plain list."""
    import random
    random.seed(42)

    # Planted array [3,1,4,1,5] at indices 1..5 via the set-value Query wrapper.
    bit = BinaryIndexedTree(20)
    q = Query(bit)
    for i, v in enumerate([3, 1, 4, 1, 5], start=1):
        q.update(i, v)
    assert q.prefix_sum(5) == 14, f"3+1+4+1+5 must be 14, got {q.prefix_sum(5)}"
    assert q.range_sum(2, 4) == 6, f"1+4+1 must be 6, got {q.range_sum(2, 4)}"
    assert q.range_sum(1, 20) == 14, "untouched tail changed the total"

    # Query.update is SET (not add): overwriting index 3 with 10 must land exactly.
    q.update(3, 10)
    assert q.range_sum(3, 3) == 10, "set-semantics update failed to overwrite"
    assert q.prefix_sum(5) == 20, f"total after overwrite must be 20, got {q.prefix_sum(5)}"

    # Raw BIT.update is DELTA: +5 at index 1 shifts every prefix by exactly 5.
    before = bit.prefix_sum(20)
    bit.update(1, 5)
    assert bit.prefix_sum(20) == before + 5, "delta update did not shift the total by 5"

    # Oracle fuzz: 800 random delta-updates and queries vs a plain list.
    oracle = [0] * 21
    fresh = BinaryIndexedTree(20)
    for _ in range(800):
        op = random.random()
        if op < 0.5:
            i, d = random.randint(1, 20), random.randint(-50, 50)
            fresh.update(i, d)
            oracle[i] += d
        elif op < 0.75:
            i = random.randint(1, 20)
            assert fresh.prefix_sum(i) == sum(oracle[1:i + 1]), f"prefix_sum({i}) diverged"
        else:
            l = random.randint(1, 20)
            r = random.randint(l, 20)
            assert fresh.range_sum(l, r) == sum(oracle[l:r + 1]), f"range_sum({l},{r}) diverged"

    # Refusals: out-of-bounds and inverted ranges.
    for call in (lambda: bit.prefix_sum(25), lambda: bit.update(0, 1),
                 lambda: bit.update(21, 1), lambda: BinaryIndexedTree(0)):
        try:
            call()
            assert False, "invalid call accepted"
        except (IndexError, ValueError):
            pass
    try:
        bit.range_sum(15, 10)
        assert False, "inverted range accepted"
    except ValueError:
        pass

    print("binary_indexed_tree: planted sums 14/6/20 exact, set-vs-delta held, "
          "800-op oracle agreed, bounds refused — PASS")


if __name__ == "__main__":
    main()