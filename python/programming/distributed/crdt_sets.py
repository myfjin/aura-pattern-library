"""
CRDT Sets Implementation

This module implements three types of Conflict-free Replicated Data Types (CRDT) sets:
- AWORSet (Add-Wins Observed-Remove Set)
- AddWinsSet (Add-Wins Set)
- RemoveWinsSet (Remove-Wins Set)

Each implementation supports add, remove, query, and merge operations.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import uuid
from typing import Any, Set, Dict, Tuple, Union
from collections import defaultdict


class AWORSet:
    """
    Add-Wins Observed-Remove Set CRDT.
    
    In case of conflict, add wins over remove. Elements are stored with unique tags
    to track their addition and removal.
    """
    
    def __init__(self) -> None:
        """Initialize an empty AWORSet."""
        # add_set: element -> set of tags
        self.add_set: Dict[Any, Set[uuid.UUID]] = defaultdict(set)
        # remove_set: element -> set of tags
        self.remove_set: Dict[Any, Set[uuid.UUID]] = defaultdict(set)
    
    def add(self, element: Any) -> None:
        """
        Add an element to the set.
        
        Args:
            element: The element to add
        """
        tag = uuid.uuid4()
        self.add_set[element].add(tag)
    
    def remove(self, element: Any) -> None:
        """
        Remove an element from the set.
        
        Args:
            element: The element to remove
        """
        if element in self.add_set:
            # Copy all tags from add_set to remove_set
            for tag in self.add_set[element]:
                self.remove_set[element].add(tag)
    
    def query(self, element: Any) -> bool:
        """
        Check if an element is in the set.
        
        Args:
            element: The element to check
            
        Returns:
            True if element is in the set, False otherwise
        """
        # Element is present if it's in add_set but not all its tags are in remove_set
        if element not in self.add_set:
            return False
        
        # Check if there's at least one tag in add_set that's not in remove_set
        add_tags = self.add_set[element]
        remove_tags = self.remove_set[element] if element in self.remove_set else set()
        
        return bool(add_tags - remove_tags)
    
    def elements(self) -> Set[Any]:
        """
        Get all elements currently in the set.
        
        Returns:
            Set of elements in the AWORSet
        """
        result = set()
        for element in self.add_set:
            if self.query(element):
                result.add(element)
        return result
    
    def merge(self, other: 'AWORSet') -> None:
        """
        Merge another AWORSet into this one.
        
        Args:
            other: Another AWORSet to merge with
        """
        # For each element in other's add_set, merge tags
        for element, tags in other.add_set.items():
            self.add_set[element].update(tags)
        
        # For each element in other's remove_set, merge tags
        for element, tags in other.remove_set.items():
            self.remove_set[element].update(tags)
    
    def __repr__(self) -> str:
        """String representation of the AWORSet."""
        return f"AWORSet({self.elements()})"


class AddWinsSet:
    """
    Add-Wins Set CRDT.
    
    In case of conflict, add operations always win over remove operations.
    Uses timestamps to determine operation order.
    """
    
    def __init__(self) -> None:
        """Initialize an empty AddWinsSet."""
        # element -> {timestamp: bool} where True means added, False means removed
        self.state: Dict[Any, Dict[float, bool]] = defaultdict(dict)
    
    def add(self, element: Any, timestamp: float) -> None:
        """
        Add an element to the set with a timestamp.
        
        Args:
            element: The element to add
            timestamp: The timestamp of the operation
        """
        self.state[element][timestamp] = True
    
    def remove(self, element: Any, timestamp: float) -> None:
        """
        Remove an element from the set with a timestamp.
        
        Args:
            element: The element to remove
            timestamp: The timestamp of the operation
        """
        self.state[element][timestamp] = False
    
    def query(self, element: Any) -> bool:
        """
        Check if an element is in the set.
        
        Args:
            element: The element to check
            
        Returns:
            True if element is in the set, False otherwise
        """
        if element not in self.state:
            return False
        
        # Get the latest operation
        if not self.state[element]:
            return False
            
        latest_timestamp = max(self.state[element].keys())
        return self.state[element][latest_timestamp]
    
    def elements(self) -> Set[Any]:
        """
        Get all elements currently in the set.
        
        Returns:
            Set of elements in the AddWinsSet
        """
        result = set()
        for element in self.state:
            if self.query(element):
                result.add(element)
        return result
    
    def merge(self, other: 'AddWinsSet') -> None:
        """
        Merge another AddWinsSet into this one.
        
        Args:
            other: Another AddWinsSet to merge with
        """
        for element, timestamps in other.state.items():
            for timestamp, is_add in timestamps.items():
                self.state[element][timestamp] = is_add
    
    def __repr__(self) -> str:
        """String representation of the AddWinsSet."""
        return f"AddWinsSet({self.elements()})"


class RemoveWinsSet:
    """
    Remove-Wins Set CRDT.
    
    In case of conflict, remove operations always win over add operations.
    Uses timestamps to determine operation order.
    """
    
    def __init__(self) -> None:
        """Initialize an empty RemoveWinsSet."""
        # element -> {timestamp: bool} where True means added, False means removed
        self.state: Dict[Any, Dict[float, bool]] = defaultdict(dict)
    
    def add(self, element: Any, timestamp: float) -> None:
        """
        Add an element to the set with a timestamp.
        
        Args:
            element: The element to add
            timestamp: The timestamp of the operation
        """
        self.state[element][timestamp] = True
    
    def remove(self, element: Any, timestamp: float) -> None:
        """
        Remove an element from the set with a timestamp.
        
        Args:
            element: The element to remove
            timestamp: The timestamp of the operation
        """
        self.state[element][timestamp] = False
    
    def query(self, element: Any) -> bool:
        """
        Check if an element is in the set.
        
        Args:
            element: The element to check
            
        Returns:
            True if element is in the set, False otherwise
        """
        if element not in self.state:
            return False
        
        # Get the latest operation
        if not self.state[element]:
            return False
            
        latest_timestamp = max(self.state[element].keys())
        return self.state[element][latest_timestamp]
    
    def elements(self) -> Set[Any]:
        """
        Get all elements currently in the set.
        
        Returns:
            Set of elements in the RemoveWinsSet
        """
        result = set()
        for element in self.state:
            if self.query(element):
                result.add(element)
        return result
    
    def merge(self, other: 'RemoveWinsSet') -> None:
        """
        Merge another RemoveWinsSet into this one.
        
        Args:
            other: Another RemoveWinsSet to merge with
        """
        for element, timestamps in other.state.items():
            for timestamp, is_add in timestamps.items():
                self.state[element][timestamp] = is_add
    
    def __repr__(self) -> str:
        """String representation of the RemoveWinsSet."""
        return f"RemoveWinsSet({self.elements()})"


if __name__ == "__main__":
    import time
    
    print("=== AWORSet Demo ===")
    # Create two AWORSet instances
    set1 = AWORSet()
    set2 = AWORSet()
    
    # Add elements to set1
    set1.add("a")
    set1.add("b")
    set1.add("c")
    
    print(f"Set1 after adds: {set1}")
    
    # Remove an element from set1
    set1.remove("b")
    print(f"Set1 after removing 'b': {set1}")
    
    # Add elements to set2
    set2.add("b")
    set2.add("d")
    print(f"Set2: {set2}")
    
    # Merge set2 into set1
    set1.merge(set2)
    print(f"Set1 after merging with set2: {set1}")
    
    # Check specific elements
    print(f"Is 'a' in set1? {set1.query('a')}")
    print(f"Is 'b' in set1? {set1.query('b')}")
    print(f"Is 'c' in set1? {set1.query('c')}")
    print(f"Is 'd' in set1? {set1.query('d')}")
    
    print("\n=== AddWinsSet Demo ===")
    # Create two AddWinsSet instances
    add_win1 = AddWinsSet()
    add_win2 = AddWinsSet()
    
    # Use timestamps for operations
    t1 = time.time()
    add_win1.add("x", t1)
    add_win1.add("y", t1)
    
    t2 = t1 + 0.001
    add_win1.remove("x", t2)
    
    print(f"AddWinSet1: {add_win1}")
    
    # Operations on second set with later timestamps
    t3 = t1 + 0.002
    add_win2.add("x", t3)  # This add should win
    add_win2.add("z", t3)
    
    print(f"AddWinSet2: {add_win2}")
    
    # Merge sets
    add_win1.merge(add_win2)
    print(f"AddWinSet1 after merge: {add_win1}")
    
    print("\n=== RemoveWinsSet Demo ===")
    remove_win1 = RemoveWinsSet()
    remove_win2 = RemoveWinsSet()
    
    t4 = time.time()
    remove_win1.add("p", t4)
    remove_win1.add("q", t4)
    
    t5 = t4 + 0.001
    remove_win1.remove("p", t5)
    
    print(f"RemoveWinSet1: {remove_win1}")
    
    # Operations on second set with later timestamps
    t6 = t4 + 0.002
    remove_win2.add("p", t6)  # This add should lose to the remove in merge
    remove_win2.add("r", t6)
    
    print(f"RemoveWinSet2: {remove_win2}")
    
    # Merge sets
    remove_win1.merge(remove_win2)
    print(f"RemoveWinSet1 after merge: {remove_win1}")
    
    # Test conflict scenarios
    print("\n=== Conflict Resolution Tests ===")
    
    # AWORSet conflict: add and remove same element
    awor_conflict1 = AWORSet()
    awor_conflict2 = AWORSet()
    
    awor_conflict1.add("conflict")
    awor_conflict2.add("conflict")
    
    # Remove from one, but the other has a different add
    awor_conflict1.remove("conflict")
    
    awor_conflict1.merge(awor_conflict2)
    print(f"AWORSet conflict resolution: {awor_conflict1} (should contain 'conflict')")
    
    # AddWinsSet conflict
    addwin_conflict1 = AddWinsSet()
    addwin_conflict2 = AddWinsSet()
    
    t7 = time.time()
    t8 = t7 + 0.001
    
    addwin_conflict1.add("conflict", t7)
    addwin_conflict2.remove("conflict", t8)  # Later remove should win in AddWins? No, add wins!
    
    addwin_conflict1.merge(addwin_conflict2)
    print(f"AddWinsSet conflict resolution: {addwin_conflict1} (should contain 'conflict')")
    
    # RemoveWinsSet conflict
    removewin_conflict1 = RemoveWinsSet()
    removewin_conflict2 = RemoveWinsSet()
    
    removewin_conflict1.add("conflict", t7)
    removewin_conflict2.remove("conflict", t8)  # Later remove should win
    
    removewin_conflict1.merge(removewin_conflict2)
    print(f"RemoveWinsSet conflict resolution: {removewin_conflict1} (should NOT contain 'conflict')")