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
    """Demo the FenwickTree with 1000 random operations."""
    print("Fenwick Tree Demo")
    print("=" * 50)
    
    # Initialize
    size = 100
    ft = FenwickTree(size)
    arr = [0] * size  # Parallel array to verify correctness
    
    print(f"Initialized Fenwick Tree with size {size}")
    
    # Perform 1000 random operations
    num_ops = 1000
    correct_ops = 0
    
    for i in range(num_ops):
        op_type = random.choice(['update', 'prefix_sum', 'range_sum'])
        
        try:
            if op_type == 'update':
                # Point update
                idx = random.randint(0, size - 1)
                val = random.randint(-100, 100)
                ft.point_update(idx, val)
                arr[idx] += val
                correct_ops += 1
                
            elif op_type == 'prefix_sum':
                # Prefix sum query
                idx = random.randint(0, size - 1)
                fenwick_result = ft.prefix_sum(idx)
                
                # Calculate expected result
                expected = sum(arr[:idx+1])
                
                if fenwick_result == expected:
                    correct_ops += 1
                else:
                    print(f"ERROR in prefix_sum: idx={idx}, got {fenwick_result}, expected {expected}")
                    
            elif op_type == 'range_sum':
                # Range sum query
                left = random.randint(0, size - 1)
                right = random.randint(left, size - 1)
                fenwick_result = ft.range_sum(left, right)
                
                # Calculate expected result
                expected = sum(arr[left:right+1])
                
                if fenwick_result == expected:
                    correct_ops += 1
                else:
                    print(f"ERROR in range_sum: [{left},{right}], got {fenwick_result}, expected {expected}")
                    
        except Exception as e:
            print(f"Exception in operation {op_type}: {e}")
    
    print(f"\nPerformed {num_ops} operations")
    print(f"Correct operations: {correct_ops}/{num_ops}")
    print(f"Success rate: {correct_ops/num_ops*100:.2f}%")
    
    # Final verification: check all prefix sums
    print("\nFinal verification:")
    all_correct = True
    for i in range(min(10, size)):  # Check first 10 elements
        fenwick_result = ft.prefix_sum(i)
        expected = sum(arr[:i+1])
        if fenwick_result != expected:
            print(f"MISMATCH at index {i}: got {fenwick_result}, expected {expected}")
            all_correct = False
    
    if all_correct:
        print("All verification checks passed!")
    else:
        print("Some verification checks failed!")
    
    # Show some example operations
    print("\nExample operations:")
    print(f"Initial array[0:10] = {arr[0:10]}")
    
    # Update some values
    ft.point_update(0, 5)
    arr[0] += 5
    ft.point_update(5, -3)
    arr[5] += -3
    
    print(f"After updates array[0:10] = {arr[0:10]}")
    print(f"Prefix sum [0..5] = {ft.prefix_sum(5)} (expected: {sum(arr[0:6])})")
    print(f"Range sum [2..7] = {ft.range_sum(2, 7)} (expected: {sum(arr[2:8])})")


if __name__ == "__main__":
    main()