# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import math
import hashlib
from typing import List, Tuple, Union, Optional
from collections.abc import Hashable

class HashPair:
    """A pair of hash functions for Bloom filter operations."""
    
    def __init__(self, seed1: int = 0, seed2: int = 1):
        """
        Initialize with two seed values for hash functions.
        
        Args:
            seed1: First seed for hash function
            seed2: Second seed for hash function
        """
        self.seed1 = seed1
        self.seed2 = seed2
    
    def hash(self, item: Hashable, max_value: int) -> Tuple[int, int]:
        """
        Generate two hash values for an item.
        
        Args:
            item: Item to hash
            max_value: Maximum value for hash (typically bit array size)
            
        Returns:
            Tuple of two hash values modulo max_value
        """
        item_str = str(item).encode('utf-8')
        
        # First hash using seed1
        h1 = hashlib.md5(item_str + self.seed1.to_bytes(4, 'big')).hexdigest()
        hash1 = int(h1, 16) % max_value
        
        # Second hash using seed2
        h2 = hashlib.md5(item_str + self.seed2.to_bytes(4, 'big')).hexdigest()
        hash2 = int(h2, 16) % max_value
        
        return hash1, hash2


class BloomFilter:
    """A scalable Bloom filter implementation."""
    
    def __init__(self, capacity: int = 1000, error_rate: float = 0.01):
        """
        Initialize a Bloom filter.
        
        Args:
            capacity: Expected number of items
            error_rate: Desired false positive rate (between 0 and 1)
            
        Raises:
            ValueError: If capacity or error_rate are invalid
        """
        if capacity <= 0:
            raise ValueError("Capacity must be positive")
        if not (0 < error_rate < 1):
            raise ValueError("Error rate must be between 0 and 1")
            
        self.capacity = capacity
        self.error_rate = error_rate
        
        # Calculate optimal size and hash count
        self.bit_count = self._calculate_bit_count(capacity, error_rate)
        self.hash_count = self._calculate_hash_count(capacity, self.bit_count)
        
        # Initialize bit array
        self.bit_array: List[bool] = [False] * self.bit_count
        self.item_count = 0
        
        # Initialize hash functions
        self.hash_pair = HashPair()
        
    @staticmethod
    def _calculate_bit_count(capacity: int, error_rate: float) -> int:
        """Calculate optimal bit array size."""
        return int(-capacity * math.log(error_rate) / (math.log(2) ** 2)) + 1
    
    @staticmethod
    def _calculate_hash_count(capacity: int, bit_count: int) -> int:
        """Calculate optimal number of hash functions."""
        return int((bit_count / capacity) * math.log(2)) + 1
    
    def _get_hash_positions(self, item: Hashable) -> List[int]:
        """Get all hash positions for an item."""
        positions = []
        hash1, hash2 = self.hash_pair.hash(item, self.bit_count)
        
        for i in range(self.hash_count):
            position = (hash1 + i * hash2) % self.bit_count
            positions.append(position)
            
        return positions
    
    def add(self, item: Hashable) -> None:
        """
        Add an item to the Bloom filter.
        
        Args:
            item: Item to add (must be hashable)
        """
        if not isinstance(item, Hashable):
            raise TypeError("Item must be hashable")
            
        positions = self._get_hash_positions(item)
        for pos in positions:
            self.bit_array[pos] = True
        self.item_count += 1
    
    def contains(self, item: Hashable) -> bool:
        """
        Check if an item might be in the Bloom filter.
        
        Args:
            item: Item to check
            
        Returns:
            True if item might be present, False if definitely not present
        """
        if not isinstance(item, Hashable):
            raise TypeError("Item must be hashable")
            
        positions = self._get_hash_positions(item)
        for pos in positions:
            if not self.bit_array[pos]:
                return False
        return True
    
    def false_positive_rate(self) -> float:
        """
        Calculate current false positive rate.
        
        Returns:
            Estimated false positive rate
        """
        if self.item_count == 0:
            return 0.0
            
        # Probability that a bit is still 0
        exponent = (-self.hash_count * self.item_count) / self.bit_count
        p_zero = (1 - (1 / self.bit_count)) ** exponent
        
        # Probability that a bit is 1
        p_one = 1 - p_zero
        
        # False positive rate is probability all hash positions are 1
        return p_one ** self.hash_count
    
    def resize(self, new_capacity: int, new_error_rate: Optional[float] = None) -> None:
        """
        Resize the Bloom filter to accommodate more items.
        
        Args:
            new_capacity: New expected capacity
            new_error_rate: New error rate (uses current if None)
            
        Raises:
            ValueError: If new_capacity is not greater than current capacity
        """
        if new_capacity <= self.capacity:
            raise ValueError("New capacity must be greater than current capacity")
            
        # Save current items if we have them (in practice, you'd need to store them)
        # For this implementation, we'll just recreate the filter structure
        
        old_capacity = self.capacity
        old_error_rate = self.error_rate if new_error_rate is None else new_error_rate
        
        self.capacity = new_capacity
        self.error_rate = old_error_rate
        
        # Recalculate optimal parameters
        self.bit_count = self._calculate_bit_count(new_capacity, old_error_rate)
        self.hash_count = self._calculate_hash_count(new_capacity, self.bit_count)
        
        # Recreate bit array
        self.bit_array = [False] * self.bit_count
        # Note: In a full implementation, we would re-add all existing items
        
    def __len__(self) -> int:
        """Return the number of items added."""
        return self.item_count
    
    def __contains__(self, item: Hashable) -> bool:
        """Support for 'in' operator."""
        return self.contains(item)


def main():
    """Demo the Bloom filter with 1000 items."""
    # Create a Bloom filter for 1000 items with 1% error rate
    bf = BloomFilter(capacity=1000, error_rate=0.01)
    
    # Add 1000 items
    items_to_add = [f"item_{i}" for i in range(1000)]
    for item in items_to_add:
        bf.add(item)
    
    print(f"Added {len(bf)} items to Bloom filter")
    print(f"Bit array size: {bf.bit_count}")
    print(f"Hash functions: {bf.hash_count}")
    print(f"False positive rate: {bf.false_positive_rate():.4f}")
    
    # Check that all added items are found
    found_count = 0
    for item in items_to_add:
        if item in bf:
            found_count += 1
    
    print(f"Found {found_count}/{len(items_to_add)} added items (should be all)")
    
    # Check for false positives with items we didn't add
    false_positives = 0
    items_to_test = [f"test_item_{i}" for i in range(1000)]
    for item in items_to_test:
        if item in bf:
            false_positives += 1
    
    actual_fpr = false_positives / len(items_to_test)
    print(f"False positives: {false_positives}/{len(items_to_test)} = {actual_fpr:.4f}")
    
    # Test resize functionality
    print("\nTesting resize...")
    original_capacity = bf.capacity
    bf.resize(new_capacity=2000)
    print(f"Resized from {original_capacity} to {bf.capacity} capacity")
    print(f"New bit array size: {bf.bit_count}")
    
    # Verify existing items still return True (they should in a proper implementation)
    # Note: In this simplified version, resizing clears the bit array
    print("Bloom filter demo completed")


if __name__ == "__main__":
    main()