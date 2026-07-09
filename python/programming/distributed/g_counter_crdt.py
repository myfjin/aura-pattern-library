"""
Distributed Counter Implementation

This module provides two types of distributed counters:
- GCounter (Grow-only Counter): Only supports increment operations
- PNCounter (Positive-Negative Counter): Supports both increment and decrement

Both counters implement state-based convergence through merging operations.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

from typing import Dict, Any, Set
import uuid


class GCounter:
    """
    Grow-only Counter (G-Counter)
    
    A distributed counter that only supports increment operations.
    Each node maintains its own count, and the total is the sum of all nodes' counts.
    Merging takes the maximum value for each node to ensure convergence.
    """
    
    def __init__(self, node_id: str = None) -> None:
        """
        Initialize a GCounter.
        
        Args:
            node_id: Unique identifier for this node. If None, a UUID is generated.
        """
        self.node_id: str = node_id if node_id else str(uuid.uuid4())
        self.counts: Dict[str, int] = {self.node_id: 0}
    
    def increment(self, amount: int = 1) -> None:
        """
        Increment the counter for this node.
        
        Args:
            amount: The amount to increment by (must be non-negative)
            
        Raises:
            ValueError: If amount is negative
        """
        if amount < 0:
            raise ValueError("GCounter only supports non-negative increments")
        
        if self.node_id in self.counts:
            self.counts[self.node_id] += amount
        else:
            self.counts[self.node_id] = amount
    
    def value(self) -> int:
        """
        Get the total value of the counter (sum of all nodes' counts).
        
        Returns:
            The total count across all nodes
        """
        return sum(self.counts.values())
    
    def merge(self, other: 'GCounter') -> None:
        """
        Merge this counter with another GCounter.
        
        For each node, takes the maximum count between the two counters.
        
        Args:
            other: Another GCounter to merge with
        """
        for node_id, count in other.counts.items():
            if node_id in self.counts:
                self.counts[node_id] = max(self.counts[node_id], count)
            else:
                self.counts[node_id] = count
    
    def get_nodes(self) -> Set[str]:
        """
        Get all node IDs in this counter.
        
        Returns:
            A set of node identifiers
        """
        return set(self.counts.keys())
    
    def __str__(self) -> str:
        """
        String representation of the counter.
        
        Returns:
            A string showing the total value and node counts
        """
        return f"GCounter(value={self.value()}, nodes={self.counts})"


class PNCounter:
    """
    Positive-Negative Counter (PN-Counter)
    
    A distributed counter that supports both increment and decrement operations.
    Internally uses two GCounters: one for positive increments and one for negative increments.
    The total value is the difference between the positive and negative totals.
    """
    
    def __init__(self, node_id: str = None) -> None:
        """
        Initialize a PNCounter.
        
        Args:
            node_id: Unique identifier for this node. If None, a UUID is generated.
        """
        self.node_id: str = node_id if node_id else str(uuid.uuid4())
        self.p_counter: GCounter = GCounter(self.node_id)  # Positive counter
        self.n_counter: GCounter = GCounter(self.node_id)  # Negative counter
    
    def increment(self, amount: int = 1) -> None:
        """
        Increment the counter.
        
        Args:
            amount: The amount to increment by (can be negative to decrement)
        """
        if amount >= 0:
            self.p_counter.increment(amount)
        else:
            self.n_counter.increment(-amount)
    
    def decrement(self, amount: int = 1) -> None:
        """
        Decrement the counter.
        
        Args:
            amount: The amount to decrement by (must be non-negative)
            
        Raises:
            ValueError: If amount is negative
        """
        if amount < 0:
            raise ValueError("Decrement amount must be non-negative")
        self.p_counter.increment(0)  # Ensure node exists in p_counter
        self.n_counter.increment(amount)
    
    def value(self) -> int:
        """
        Get the current value of the counter.
        
        Returns:
            The difference between positive and negative counts
        """
        return self.p_counter.value() - self.n_counter.value()
    
    def merge(self, other: 'PNCounter') -> None:
        """
        Merge this counter with another PNCounter.
        
        Merges both the positive and negative counters.
        
        Args:
            other: Another PNCounter to merge with
        """
        self.p_counter.merge(other.p_counter)
        self.n_counter.merge(other.n_counter)
    
    def get_nodes(self) -> Set[str]:
        """
        Get all node IDs in this counter.
        
        Returns:
            A set of node identifiers from both positive and negative counters
        """
        return self.p_counter.get_nodes() | self.n_counter.get_nodes()
    
    def __str__(self) -> str:
        """
        String representation of the counter.
        
        Returns:
            A string showing the total value and component counters
        """
        return f"PNCounter(value={self.value()}, P={self.p_counter.counts}, N={self.n_counter.counts})"


def _demo() -> None:
    """Demonstrate the distributed counters with 3 nodes."""
    print("=== GCounter Demo ===")
    
    # Create 3 nodes
    node1 = GCounter("node1")
    node2 = GCounter("node2")
    node3 = GCounter("node3")
    
    # Each node does some increments
    node1.increment(5)
    node2.increment(3)
    node3.increment(7)
    
    print(f"Initial states:")
    print(f"  {node1}")
    print(f"  {node2}")
    print(f"  {node3}")
    
    # Simulate network communication by merging states
    print("\nAfter node1 merges with node2:")
    node1.merge(node2)
    print(f"  {node1}")
    
    print("\nAfter node3 merges with updated node1:")
    node3.merge(node1)
    print(f"  {node3}")
    
    print("\nAfter node2 merges with updated node3 (all should converge):")
    node2.merge(node3)
    print(f"  {node2}")
    
    print(f"\nAll nodes have value: {node1.value()} (node1), {node2.value()} (node2), {node3.value()} (node3)")
    
    print("\n=== PNCounter Demo ===")
    
    # Create 3 nodes for PNCounter
    pn1 = PNCounter("pn1")
    pn2 = PNCounter("pn2")
    pn3 = PNCounter("pn3")
    
    # Perform various operations
    pn1.increment(10)  # pn1: +10
    pn2.decrement(5)   # pn2: -5
    pn3.increment(3)   # pn3: +3
    pn1.decrement(2)   # pn1: +10-2=+8
    
    print(f"Initial states:")
    print(f"  {pn1}")
    print(f"  {pn2}")
    print(f"  {pn3}")
    
    # Merge states
    print("\nAfter pn1 merges with pn2:")
    pn1.merge(pn2)
    print(f"  {pn1}")
    
    print("\nAfter pn3 merges with updated pn1:")
    pn3.merge(pn1)
    print(f"  {pn3}")
    
    print("\nAfter pn2 merges with updated pn3 (all should converge):")
    pn2.merge(pn3)
    print(f"  {pn2}")
    
    print(f"\nAll nodes have value: {pn1.value()} (pn1), {pn2.value()} (pn2), {pn3.value()} (pn3)")


if __name__ == "__main__":
    _demo()