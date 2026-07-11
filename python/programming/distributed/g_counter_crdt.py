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
    """Self-test: the CRDT LAWS — commutativity, idempotence, convergence —
    plus exact values, for both GCounter and PNCounter."""
    # GCounter: independent increments converge to the exact global sum.
    n1, n2, n3 = GCounter("node1"), GCounter("node2"), GCounter("node3")
    n1.increment(5)
    n2.increment(3)
    n3.increment(7)
    assert (n1.value(), n2.value(), n3.value()) == (5, 3, 7)

    # Anti-entropy gossip: after full exchange, every replica reads 15.
    n1.merge(n2)
    assert n1.value() == 8, f"5+3 must be 8, got {n1.value()}"
    n3.merge(n1)
    assert n3.value() == 15, f"5+3+7 must be 15, got {n3.value()}"
    n2.merge(n3)
    n1.merge(n3)
    assert n1.value() == n2.value() == n3.value() == 15, \
        f"replicas diverged: {n1.value()}/{n2.value()}/{n3.value()}"

    # IDEMPOTENCE: re-merging the same state changes nothing.
    n1.merge(n3)
    n1.merge(n3)
    assert n1.value() == 15, "merge is not idempotent"

    # COMMUTATIVITY: A·merge(B) == B·merge(A), state-wise.
    a, b = GCounter("A"), GCounter("B")
    a.increment(4)
    b.increment(9)
    ab, ba = GCounter("A"), GCounter("B")
    ab.increment(4); ba.increment(9)
    a.merge(b)
    ba.merge(ab)
    assert a.value() == ba.value() == 13, "merge order changed the result"
    assert a.counts == ba.counts, f"states differ: {a.counts} vs {ba.counts}"

    # Merge NEVER loses increments that happened concurrently: after a
    # merge, further local increments still count.
    a.increment(1)
    assert a.value() == 14

    # GCounter is grow-only: negative increments refused.
    try:
        a.increment(-1)
        assert False, "grow-only counter accepted a negative increment"
    except ValueError:
        pass

    # PNCounter: increments and decrements converge to the exact net value.
    pn1, pn2, pn3 = PNCounter("pn1"), PNCounter("pn2"), PNCounter("pn3")
    pn1.increment(10)
    pn2.decrement(5)
    pn3.increment(3)
    pn1.decrement(2)
    assert pn1.value() == 8 and pn2.value() == -5 and pn3.value() == 3

    pn1.merge(pn2)
    assert pn1.value() == 3, f"8 + (-5) must be 3, got {pn1.value()}"
    pn3.merge(pn1)
    pn2.merge(pn3)
    pn1.merge(pn3)
    assert pn1.value() == pn2.value() == pn3.value() == 6, \
        f"PN replicas diverged: {pn1.value()}/{pn2.value()}/{pn3.value()}"
    assert pn1.value() == 10 - 5 + 3 - 2, "net value must be the sum of all ops"

    # Node bookkeeping and refusals.
    assert pn1.get_nodes() >= {"pn1", "pn2", "pn3"}
    try:
        pn1.decrement(-3)
        assert False, "negative decrement accepted"
    except ValueError:
        pass

    print("g_counter_crdt: GCounter converged to 15 on all replicas "
          "(idempotent, commutative), PNCounter net 6 everywhere — PASS")


if __name__ == "__main__":
    _demo()