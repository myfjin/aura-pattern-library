"""
HyperLogLog probabilistic cardinality estimator implementation.

This module provides a HyperLogLog class for estimating the cardinality
(number of distinct elements) of large datasets with minimal memory usage.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import hashlib
import math
import sys
from typing import List, Optional, Union


class Register:
    """A single register in the HyperLogLog algorithm."""
    
    def __init__(self, value: int = 0) -> None:
        """Initialize a register with a given value."""
        self.value = value
    
    def update(self, new_value: int) -> None:
        """Update the register if the new value is greater."""
        if new_value > self.value:
            self.value = new_value


class HyperLogLog:
    """HyperLogLog probabilistic cardinality estimator."""
    
    def __init__(self, precision: int = 14) -> None:
        """
        Initialize a HyperLogLog estimator.
        
        Args:
            precision: Number of bits for register addressing (affects accuracy and memory).
                      Must be between 4 and 16. Default is 14.
        """
        if not 4 <= precision <= 16:
            raise ValueError("Precision must be between 4 and 16")
        
        self.precision = precision
        self.m = 1 << precision  # Number of registers (2^precision)
        self.alpha = 0.7213 / (1 + 1.079 / self.m) if self.m >= 128 else (
            0.673 if self.m == 64 else (
                0.697 if self.m == 32 else 0.709
            )
        )
        self.registers: List[Register] = [Register() for _ in range(self.m)]
        self._hash_func = hashlib.sha1
    
    def _hash(self, item: Union[str, int, bytes]) -> bytes:
        """Hash an item to get a fixed-size byte representation."""
        if isinstance(item, str):
            item_bytes = item.encode('utf-8')
        elif isinstance(item, int):
            item_bytes = str(item).encode('utf-8')
        else:
            item_bytes = item
        return self._hash_func(item_bytes).digest()
    
    def _get_register_index_and_rank(self, item: Union[str, int, bytes]) -> tuple[int, int]:
        """Get register index and rank of the first 1-bit from hash of item."""
        hash_bytes = self._hash(item)
        
        # Convert first few bytes to an integer for register indexing
        # We need 'precision' bits for the register index
        bytes_needed = (self.precision + 7) // 8  # Ceiling division
        index_bytes = hash_bytes[:bytes_needed]
        
        # Convert bytes to integer
        index_int = int.from_bytes(index_bytes, byteorder='big')
        # Mask to get only the required number of bits
        register_index = index_int & ((1 << self.precision) - 1)
        
        # For rank, we look at the remaining bits after the precision bits
        # We need to find the position of the first 1-bit in the remaining bits
        # Start with the byte after the index bytes
        rank = 1
        remaining_bits_offset = self.precision
        
        # Process bit by bit
        for i in range(remaining_bits_offset, len(hash_bytes) * 8):
            byte_index = i // 8
            bit_index = 7 - (i % 8)  # MSB first
            if byte_index < len(hash_bytes):
                byte_val = hash_bytes[byte_index]
                if (byte_val >> bit_index) & 1:
                    break
            rank += 1
        else:
            # If we didn't find a 1-bit, use a large rank
            rank = 64  # Should be sufficient for practical purposes
        
        return register_index, rank
    
    def add(self, item: Union[str, int, bytes]) -> None:
        """
        Add an item to the estimator.
        
        Args:
            item: The item to add (string, integer, or bytes).
        """
        register_index, rank = self._get_register_index_and_rank(item)
        self.registers[register_index].update(rank)
    
    def estimate_cardinality(self) -> float:
        """
        Estimate the cardinality of the set.
        
        Returns:
            Estimated cardinality as a float.
        """
        # Calculate harmonic mean of register values
        sum_inverse = sum(2.0 ** (-reg.value) for reg in self.registers)
        estimate = self.alpha * self.m * self.m / sum_inverse
        
        # Apply small range correction
        if estimate <= 2.5 * self.m:
            # Count registers with value 0
            zeros = sum(1 for reg in self.registers if reg.value == 0)
            if zeros != 0:
                estimate = self.m * math.log(self.m / zeros)
        
        # Apply large range correction (not needed for typical use cases)
        
        return estimate
    
    def merge(self, other: 'HyperLogLog') -> None:
        """
        Merge another HyperLogLog estimator into this one.
        
        Args:
            other: Another HyperLogLog instance to merge with.
            
        Raises:
            ValueError: If the precisions don't match.
        """
        if self.precision != other.precision:
            raise ValueError("Cannot merge HyperLogLog structures with different precisions")
        
        for i in range(self.m):
            self.registers[i].update(other.registers[i].value)
    
    def __len__(self) -> int:
        """Return the number of registers."""
        return self.m


def _demo() -> None:
    """Self-test: estimate accuracy vs known cardinalities (sha1 → fully deterministic)."""
    hll = HyperLogLog(precision=10)

    # 1000 known-distinct items: estimate must land within 5% of the truth.
    items = [f"item_{i}" for i in range(1000)]
    for item in items:
        hll.add(item)
    est = hll.estimate_cardinality()
    assert abs(est - 1000.0) < 50.0, f"estimate {est:.1f} off true cardinality 1000 by >5%"

    # Duplicates cannot move a single register: the estimate is bit-identical.
    for i in range(500):
        hll.add(f"item_{i}")
    est_after = hll.estimate_cardinality()
    assert est_after == est, "duplicate adds changed the estimate"

    # Merge with an overlapping set (500..1499): union truth is 1500.
    hll2 = HyperLogLog(precision=10)
    for i in range(500, 1500):
        hll2.add(f"item_{i}")
    est2 = hll2.estimate_cardinality()
    assert abs(est2 - 1000.0) < 50.0, f"hll2 estimate {est2:.1f} off true 1000 by >5%"
    hll.merge(hll2)
    merged = hll.estimate_cardinality()
    assert abs(merged - 1500.0) < 75.0, f"merged estimate {merged:.1f} off union truth 1500 by >5%"

    # Merge is idempotent (register-wise max): merging again changes nothing.
    hll.merge(hll2)
    assert hll.estimate_cardinality() == merged, "re-merge moved the estimate"

    # THE FAILURE: invalid precisions and mismatched merges must be refused.
    for bad in (3, 17):
        try:
            HyperLogLog(precision=bad)
            assert False, f"precision={bad} accepted outside [4, 16]"
        except ValueError:
            pass
    try:
        hll.merge(HyperLogLog(precision=8))
        assert False, "merge across precisions accepted"
    except ValueError:
        pass

    print(f"hyperloglog: est {est:.0f}/1000, merged {merged:.0f}/1500, dup-stable, "
          f"bad precision refused — PASS")


if __name__ == "__main__":
    _demo()