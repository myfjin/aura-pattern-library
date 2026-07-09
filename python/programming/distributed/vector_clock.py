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
    """Demo of the VectorClock implementation."""
    print("Vector Clock Demo")
    print("=" * 50)
    
    # Create vector clocks for three processes
    process_ids = ["P1", "P2", "P3"]
    clock1 = VectorClock(process_ids)
    clock2 = VectorClock(process_ids)
    clock3 = VectorClock(process_ids)
    
    print(f"Initial clocks:")
    print(f"Clock1: {clock1}")
    print(f"Clock2: {clock2}")
    print(f"Clock3: {clock3}")
    print()
    
    # Simulate events in process P1
    print("P1 performs local event")
    clock1.increment("P1")
    print(f"Clock1: {clock1}")
    print()
    
    # P1 sends message to P2
    print("P1 sends message to P2")
    sent_clock = clock1.copy()  # Capture clock when sending
    print(f"Sent clock: {sent_clock}")
    print()
    
    # P2 receives message from P1
    print("P2 receives message from P1")
    clock2.merge(sent_clock)  # Merge the received clock
    clock2.increment("P2")    # Process the message
    print(f"Clock2: {clock2}")
    print()
    
    # P2 performs another local event
    print("P2 performs local event")
    clock2.increment("P2")
    print(f"Clock2: {clock2}")
    print()
    
    # P3 performs local events
    print("P3 performs two local events")
    clock3.increment("P3")
    clock3.increment("P3")
    print(f"Clock3: {clock3}")
    print()
    
    # Compare clocks
    print("Clock comparisons:")
    comparison = clock1.compare(clock2)
    print(f"Clock1 vs Clock2: {comparison.name}")
    
    comparison = clock2.compare(clock3)
    print(f"Clock2 vs Clock3: {comparison.name}")
    
    comparison = clock1.compare(clock3)
    print(f"Clock1 vs Clock3: {comparison.name}")
    print()
    
    # Check happens-before relationships
    print("Happens-before checks:")
    print(f"Clock1 happens before Clock2: {clock1.happens_before(clock2)}")
    print(f"Clock2 happens before Clock1: {clock2.happens_before(clock1)}")
    print(f"Clock1 concurrent with Clock3: {clock1.is_concurrent_with(clock3)}")
    print()
    
    # Demonstrate error handling
    print("Error handling demo:")
    try:
        clock1.increment("P4")  # Non-existent process
    except ValueError as e:
        print(f"Caught expected error: {e}")
    
    try:
        other_clock = VectorClock(["P1", "P2"])  # Different processes
        clock1.compare(other_clock)
    except ValueError as e:
        print(f"Caught expected error: {e}")
    
    print("\nDemo completed successfully!")


if __name__ == "__main__":
    main()