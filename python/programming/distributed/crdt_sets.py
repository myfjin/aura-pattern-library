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
        """Add an element with a timestamp. An add always claims its slot."""
        self.state[element][timestamp] = True

    def remove(self, element: Any, timestamp: float) -> None:
        """Remove an element with a timestamp. If an add already occupies the
        same timestamp, the ADD keeps the slot (this is the add-wins bias —
        the plain dict write used to let whichever op landed last clobber
        the other)."""
        if not self.state[element].get(timestamp, False):
            self.state[element][timestamp] = False
    
    def query(self, element: Any) -> bool:
        """
        Check if an element is in the set.
        
        Args:
            element: The element to check
            
        Returns:
            True if element is in the set, False otherwise
        """
        if element not in self.state or not self.state[element]:
            return False

        # ADD WINS: present iff the newest add is at least as new as the
        # newest remove (ties/conflicts go to the add). The former code was
        # pure last-writer-wins — identical to RemoveWinsSet — so the class
        # name was a claim the code did not honor.
        adds = [t for t, is_add in self.state[element].items() if is_add]
        removes = [t for t, is_add in self.state[element].items() if not is_add]
        if not adds:
            return False
        if not removes:
            return True
        return max(adds) >= max(removes)
    
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
                # add-wins on same-timestamp collision
                self.state[element][timestamp] = \
                    self.state[element].get(timestamp, False) or is_add
    
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
        """Add an element with a timestamp. If a remove already occupies the
        same timestamp, the REMOVE keeps the slot (remove-wins bias)."""
        if self.state[element].get(timestamp, True):
            self.state[element][timestamp] = True

    def remove(self, element: Any, timestamp: float) -> None:
        """Remove an element with a timestamp. A remove always claims its slot."""
        self.state[element][timestamp] = False
    
    def query(self, element: Any) -> bool:
        """
        Check if an element is in the set.
        
        Args:
            element: The element to check
            
        Returns:
            True if element is in the set, False otherwise
        """
        if element not in self.state or not self.state[element]:
            return False

        # REMOVE WINS: present only if the newest add is STRICTLY newer than
        # the newest remove (ties/conflicts go to the remove).
        adds = [t for t, is_add in self.state[element].items() if is_add]
        removes = [t for t, is_add in self.state[element].items() if not is_add]
        if not adds:
            return False
        if not removes:
            return True
        return max(adds) > max(removes)
    
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
                # remove-wins on same-timestamp collision
                self.state[element][timestamp] = \
                    self.state[element].get(timestamp, True) and is_add
    
    def __repr__(self) -> str:
        """String representation of the RemoveWinsSet."""
        return f"RemoveWinsSet({self.elements()})"


if __name__ == "__main__":
    # Self-test: each set's conflict semantics proven with explicit
    # timestamps — observed-remove, add-wins, remove-wins — plus
    # convergence of both merge directions.

    # AWORSet: observed-remove — a remove only kills adds it has SEEN.
    s1, s2 = AWORSet(), AWORSet()
    s1.add("a")
    s1.add("b")
    s1.add("c")
    s1.remove("b")
    assert s1.elements() == {"a", "c"}, f"local remove failed: {s1.elements()}"
    s2.add("b")            # a concurrent, UNOBSERVED add of b
    s2.add("d")
    s1.merge(s2)
    assert s1.elements() == {"a", "b", "c", "d"}, \
        f"unobserved concurrent add must survive the remove: {s1.elements()}"
    assert s1.query("b") is True and s1.query("ghost") is False
    n_elems = len(s1.elements())
    assert n_elems == 4, f"AWOR merge must hold exactly 4 elements, got {n_elems}"

    # The observed-remove counterpart: a remove AFTER merging kills all
    # observed tags, so b really goes.
    s1.remove("b")
    assert s1.elements() == {"a", "c", "d"}, "observed remove failed post-merge"

    # AddWinsSet: concurrent add|remove of the same element → ADD WINS,
    # even when the remove has the LATER timestamp.
    aw1, aw2 = AddWinsSet(), AddWinsSet()
    t0 = 1000.0
    aw1.add("conflict", t0)
    aw2.remove("conflict", t0)         # CONCURRENT (equal-timestamp) remove
    aw1.merge(aw2)
    assert aw1.query("conflict") is True, \
        "AddWins must keep the element in an add/remove tie"
    # A strictly LATER remove is sequential, not a conflict — it removes.
    aw1.remove("conflict", t0 + 1)
    assert aw1.query("conflict") is False, "strictly later remove must apply"
    # Sequential semantics still hold: a remove after the add's arrival,
    # followed by a LATER re-add, resurrects it.
    aw1.add("x", t0)
    aw1.remove("x", t0 + 1)
    assert aw1.query("x") is False, "sequential remove failed in AddWins"
    aw1.add("x", t0 + 2)
    assert aw1.query("x") is True, "later re-add must win"

    # RemoveWinsSet: the same concurrent conflict → REMOVE WINS.
    rw1, rw2 = RemoveWinsSet(), RemoveWinsSet()
    rw1.add("conflict", t0)
    rw2.remove("conflict", t0)         # equal-timestamp conflict
    rw1.merge(rw2)
    assert rw1.query("conflict") is False, \
        "RemoveWins must drop the element in an add/remove tie"
    # A strictly later add resurrects it even in RemoveWins.
    rw1.add("conflict", t0 + 1)
    assert rw1.query("conflict") is True, "strictly later add must apply"
    rw1.remove("conflict", t0 + 1)     # tie at t0+1 → remove wins again
    assert rw1.query("conflict") is False
    rw1.add("p", t0)
    rw1.add("q", t0)
    assert rw1.elements() == {"p", "q"}

    # CONVERGENCE: merging in both directions yields identical element sets.
    x1, x2 = AddWinsSet(), AddWinsSet()
    x1.add("m", t0)
    x1.remove("m", t0 + 1)
    x2.add("m", t0 + 2)
    x2.add("n", t0)
    y1, y2 = AddWinsSet(), AddWinsSet()
    y1.add("m", t0)
    y1.remove("m", t0 + 1)
    y2.add("m", t0 + 2)
    y2.add("n", t0)
    x1.merge(x2)           # A <- B
    y2.merge(y1)           # B <- A
    assert x1.elements() == y2.elements() == {"m", "n"}, \
        f"merge directions diverged: {x1.elements()} vs {y2.elements()}"

    # Idempotence: re-merge changes nothing.
    before = x1.elements()
    x1.merge(x2)
    assert x1.elements() == before, "merge not idempotent"

    print("crdt_sets: AWOR unobserved-add survived (4 elems), AddWins kept "
          "vs later remove, RemoveWins dropped, merge directions equal — PASS")
