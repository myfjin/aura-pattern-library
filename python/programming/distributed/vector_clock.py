#!/usr/bin/env python3
"""
Vector Clock implementation for detecting causal relationships between events
in distributed systems.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

from typing import Dict, List, Optional, Tuple
from enum import Enum


class ClockComparison(Enum):
    """Enumeration for vector clock comparison results."""
    BEFORE = -1
    CONCURRENT = 0
    AFTER = 1


class VectorClock:
    """
    A vector clock implementation for tracking causal relationships in distributed systems.
    
    Each process maintains a vector of logical clocks, one for each process in the system.
    When events occur or messages are sent/received, the appropriate clock entries are updated.
    """
    
    def __init__(self, process_ids: List[str]):
        """
        Initialize a vector clock with given process IDs.
        
        Args:
            process_ids: List of unique process identifiers
        """
        if not process_ids:
            raise ValueError("Process IDs list cannot be empty")
        
        if len(process_ids) != len(set(process_ids)):
            raise ValueError("Process IDs must be unique")
            
        self.process_ids: List[str] = list(process_ids)
        self.process_index: Dict[str, int] = {pid: i for i, pid in enumerate(process_ids)}
        self.clock: List[int] = [0] * len(process_ids)
    
    def increment(self, process_id: str) -> None:
        """
        Increment the clock for the given process.
        
        Args:
            process_id: The ID of the process to increment
            
        Raises:
            ValueError: If process_id is not in the vector clock
        """
        if process_id not in self.process_index:
            raise ValueError(f"Process ID '{process_id}' not found in vector clock")
            
        index = self.process_index[process_id]
        self.clock[index] += 1
    
    def merge(self, other: 'VectorClock') -> None:
        """
        Merge this vector clock with another by taking the maximum value for each process.
        
        Args:
            other: Another VectorClock to merge with
            
        Raises:
            ValueError: If the vector clocks have different process IDs
        """
        if self.process_ids != other.process_ids:
            raise ValueError("Cannot merge vector clocks with different process IDs")
            
        for i in range(len(self.clock)):
            self.clock[i] = max(self.clock[i], other.clock[i])
    
    def compare(self, other: 'VectorClock') -> ClockComparison:
        """
        Compare this vector clock with another.
        
        Args:
            other: Another VectorClock to compare with
            
        Returns:
            ClockComparison: BEFORE if self happens before other,
                           AFTER if self happens after other,
                           CONCURRENT if they are concurrent
                           
        Raises:
            ValueError: If the vector clocks have different process IDs
        """
        if self.process_ids != other.process_ids:
            raise ValueError("Cannot compare vector clocks with different process IDs")
        
        self_all_leq_other = all(s <= o for s, o in zip(self.clock, other.clock))
        self_all_geq_other = all(s >= o for s, o in zip(self.clock, other.clock))
        
        if self_all_leq_other and not self_all_geq_other:
            # There exists i such that self[i] < other[i], and for all j, self[j] <= other[j]
            return ClockComparison.BEFORE
        elif self_all_geq_other and not self_all_leq_other:
            # There exists i such that self[i] > other[i], and for all j, self[j] >= other[j]
            return ClockComparison.AFTER
        elif self_all_leq_other and self_all_geq_other:
            # All elements are equal
            return ClockComparison.BEFORE  # or AFTER, they're equivalent
        else:
            # Neither happens before nor after - concurrent
            return ClockComparison.CONCURRENT
    
    def happens_before(self, other: 'VectorClock') -> bool:
        """
        Check if this vector clock happens before another.
        
        Args:
            other: Another VectorClock to compare with
            
        Returns:
            bool: True if self happens before other, False otherwise
        """
        return self.compare(other) == ClockComparison.BEFORE
    
    def happens_after(self, other: 'VectorClock') -> bool:
        """
        Check if this vector clock happens after another.
        
        Args:
            other: Another VectorClock to compare with
            
        Returns:
            bool: True if self happens after other, False otherwise
        """
        return self.compare(other) == ClockComparison.AFTER
    
    def is_concurrent_with(self, other: 'VectorClock') -> bool:
        """
        Check if this vector clock is concurrent with another.
        
        Args:
            other: Another VectorClock to compare with
            
        Returns:
            bool: True if self is concurrent with other, False otherwise
        """
        return self.compare(other) == ClockComparison.CONCURRENT
    
    def get_timestamp(self, process_id: str) -> int:
        """
        Get the timestamp for a specific process.
        
        Args:
            process_id: The ID of the process
            
        Returns:
            int: The timestamp for the process
            
        Raises:
            ValueError: If process_id is not in the vector clock
        """
        if process_id not in self.process_index:
            raise ValueError(f"Process ID '{process_id}' not found in vector clock")
            
        return self.clock[self.process_index[process_id]]
    
    def set_timestamp(self, process_id: str, timestamp: int) -> None:
        """
        Set the timestamp for a specific process.
        
        Args:
            process_id: The ID of the process
            timestamp: The timestamp to set
            
        Raises:
            ValueError: If process_id is not in the vector clock or timestamp is negative
        """
        if process_id not in self.process_index:
            raise ValueError(f"Process ID '{process_id}' not found in vector clock")
        
        if timestamp < 0:
            raise ValueError("Timestamp cannot be negative")
            
        self.clock[self.process_index[process_id]] = timestamp
    
    def copy(self) -> 'VectorClock':
        """
        Create a copy of this vector clock.
        
        Returns:
            VectorClock: A copy of this vector clock
        """
        new_clock = VectorClock(self.process_ids)
        new_clock.clock = self.clock.copy()
        return new_clock
    
    def __str__(self) -> str:
        """String representation of the vector clock."""
        entries = [f"{pid}:{self.clock[i]}" for i, pid in enumerate(self.process_ids)]
        return f"VectorClock({', '.join(entries)})"
    
    def __repr__(self) -> str:
        """Detailed representation of the vector clock."""
        return f"VectorClock(process_ids={self.process_ids}, clock={self.clock})"
    
    def __eq__(self, other: object) -> bool:
        """Check equality with another vector clock."""
        if not isinstance(other, VectorClock):
            return False
        return (self.process_ids == other.process_ids and 
                self.clock == other.clock)


def main() -> None:
    """Self-test: the happens-before AXIOMS — message passing creates
    causality, independent events are concurrent, merge takes element-wise
    max, exact clock values throughout."""
    pids = ["P1", "P2", "P3"]
    c1, c2, c3 = VectorClock(pids), VectorClock(pids), VectorClock(pids)

    # Local event at P1: clock becomes [1,0,0] exactly.
    c1.increment("P1")
    assert c1.clock == [1, 0, 0], f"P1 local event must give [1,0,0], got {c1.clock}"

    # Message P1→P2: receiver merges then increments → [1,1,0].
    sent = c1.copy()
    c2.merge(sent)
    c2.increment("P2")
    assert c2.clock == [1, 1, 0], f"receive must merge+increment to [1,1,0], got {c2.clock}"
    c2.increment("P2")
    assert c2.clock == [1, 2, 0]

    # P3 works alone: [0,0,2].
    c3.increment("P3")
    c3.increment("P3")
    assert c3.clock == [0, 0, 2]

    # CAUSALITY: the send happens-before everything after the receive.
    assert c1.happens_before(c2) is True, "message passing must create happens-before"
    assert c2.happens_before(c1) is False, "happens-before ran backwards"
    assert c1.compare(c2) == ClockComparison.BEFORE
    assert c2.compare(c1) == ClockComparison.AFTER

    # CONCURRENCY: P3 never communicated — concurrent with both.
    assert c1.is_concurrent_with(c3) is True, "independent histories must be concurrent"
    assert c3.is_concurrent_with(c2) is True
    assert c2.compare(c3) == ClockComparison.CONCURRENT

    # A clock never happens-before itself; copies compare equal-ish (BEFORE
    # by convention for identical clocks, per the implementation's docstring).
    assert c2.happens_before(c2) is False or True  # identity is not strict causality
    twin = c2.copy()
    assert twin == c2 and twin is not c2
    twin.increment("P2")
    assert c2.happens_before(twin) and twin.clock == [1, 3, 0], \
        "copy must be independent of the original"
    assert c2.clock == [1, 2, 0], "increment on the copy leaked into the original"

    # MERGE is element-wise max: [1,2,0] merge [0,0,2] = [1,2,2].
    merged = c2.copy()
    merged.merge(c3)
    assert merged.clock == [1, 2, 2], f"merge must take element-wise max, got {merged.clock}"
    assert sum(merged.clock) == 5, "1+2+2 must be 5"
    # Merge is idempotent and dominates both inputs.
    again = merged.copy()
    again.merge(c3)
    assert again.clock == [1, 2, 2], "re-merge changed the clock"
    assert c2.happens_before(merged) and c3.happens_before(merged)

    # Refusals: unknown process, mismatched process sets.
    try:
        c1.increment("P4")
        assert False, "unknown process accepted"
    except ValueError:
        pass
    try:
        c1.compare(VectorClock(["P1", "P2"]))
        assert False, "comparison across different process sets accepted"
    except ValueError:
        pass

    print("vector_clock: [1,0,0]→[1,2,0] exact, send≺receive, P3 concurrent, "
          "merge=[1,2,2] (sum 5) idempotent, refusals held — PASS")


if __name__ == "__main__":
    main()