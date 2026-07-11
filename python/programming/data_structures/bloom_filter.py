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

        # Probability a given bit is still 0 after k*n independent bit-sets:
        # (1 - 1/m)^(k*n). (The former version negated the exponent and divided
        # by m, yielding p_zero > 1 and a NEGATIVE false-positive rate.)
        p_zero = (1 - (1 / self.bit_count)) ** (self.hash_count * self.item_count)

        # False positive = all k probed bits are 1.
        return (1 - p_zero) ** self.hash_count
    
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
    """Self-test: the two Bloom guarantees, measured (md5 → fully deterministic):
    NO false negatives ever, and false positives near the configured rate."""
    bf = BloomFilter(capacity=1000, error_rate=0.01)

    # An empty filter contains nothing and reports fpr 0.
    assert bf.false_positive_rate() == 0.0
    assert sum(1 for i in range(50) if f"probe_{i}" in bf) == 0, \
        "empty filter claimed to contain items"

    # THE HARD GUARANTEE: zero false negatives — all 1000 added items found.
    items = [f"item_{i}" for i in range(1000)]
    for item in items:
        bf.add(item)
    assert len(bf) == 1000
    found = sum(1 for item in items if item in bf)
    assert found == 1000, f"FALSE NEGATIVE: only {found}/1000 added items found"

    # THE SOFT GUARANTEE: false-positive rate lands near the configured 1%.
    # 2000 never-added probes; deterministic count under md5. Allow 3x slack.
    fp = sum(1 for i in range(2000) if f"unknown_{i}" in bf)
    assert fp < 60, f"false-positive rate {fp}/2000 blows past 3x the 1% target"
    # The analytic estimate must also sit in a sane band around 1%.
    est = bf.false_positive_rate()
    assert 0.0 < est < 0.05, f"analytic FPR estimate {est} out of band"

    # Sizing math: more capacity or stricter error rate → more bits.
    assert BloomFilter(2000, 0.01).bit_count > bf.bit_count
    assert BloomFilter(1000, 0.001).bit_count > bf.bit_count

    # resize() grows the structure but (documented limitation) CLEARS content.
    bf.resize(new_capacity=2000)
    assert bf.capacity == 2000
    assert not any(bf.bit_array), "resize claims to clear, but bits survived"
    assert ("item_0" in bf) is False, "cleared filter still claims membership"
    try:
        bf.resize(new_capacity=100)
        assert False, "shrinking resize accepted"
    except ValueError:
        pass

    # Invalid construction refused.
    for cap, err in ((0, 0.01), (100, 0.0), (100, 1.0), (-5, 0.5)):
        try:
            BloomFilter(cap, err)
            assert False, f"BloomFilter({cap}, {err}) accepted"
        except ValueError:
            pass

    print(f"bloom_filter: 1000/1000 found (no false negatives), {fp}/2000 false "
          f"positives (≤1% target x3), sizing monotone, resize clears — PASS")


if __name__ == "__main__":
    main()