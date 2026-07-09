#!/usr/bin/env python3
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

from typing import Dict, Optional, List, Any


class Element:
    """
    Represents an element in the Union-Find data structure.
    
    Attributes:
        value: The value stored in the element.
        parent: Reference to the parent element.
        rank: The rank of the element (used for union by rank).
    """
    
    def __init__(self, value: Any) -> None:
        """
        Initialize an Element.
        
        Args:
            value: The value to store in the element.
        """
        self.value: Any = value
        self.parent: Optional['Element'] = self
        self.rank: int = 0

    def __repr__(self) -> str:
        return f"Element({self.value})"


class UnionFind:
    """
    Disjoint-set (Union-Find) data structure with path compression and union by rank.
    
    This implementation supports efficient union and find operations with
    near-constant time complexity.
    """
    
    def __init__(self) -> None:
        """Initialize an empty Union-Find structure."""
        self._elements: Dict[Any, Element] = {}
        self._components: int = 0

    def make_set(self, value: Any) -> Element:
        """
        Create a new set containing a single element.
        
        Args:
            value: The value to add as a new set.
            
        Returns:
            The created Element.
            
        Raises:
            ValueError: If the value already exists in the structure.
        """
        if value in self._elements:
            raise ValueError(f"Element {value} already exists")
        
        element = Element(value)
        self._elements[value] = element
        self._components += 1
        return element

    def find(self, value: Any) -> Element:
        """
        Find the representative (root) of the set containing the given value.
        
        Implements path compression to optimize future queries.
        
        Args:
            value: The value whose set representative to find.
            
        Returns:
            The representative Element of the set.
            
        Raises:
            KeyError: If the value does not exist in the structure.
        """
        if value not in self._elements:
            raise KeyError(f"Element {value} not found")
            
        element = self._elements[value]
        if element.parent != element:
            # Path compression: point directly to the root
            element.parent = self.find(element.parent.value)
        return element.parent

    def union(self, value1: Any, value2: Any) -> bool:
        """
        Unite the sets containing the two given values.
        
        Implements union by rank to keep trees shallow.
        
        Args:
            value1: First value.
            value2: Second value.
            
        Returns:
            True if the sets were merged, False if they were already in the same set.
            
        Raises:
            KeyError: If either value does not exist in the structure.
        """
        root1 = self.find(value1)
        root2 = self.find(value2)
        
        # Already in the same set
        if root1 == root2:
            return False
            
        # Union by rank: attach smaller tree under root of larger tree
        if root1.rank < root2.rank:
            root1.parent = root2
        elif root1.rank > root2.rank:
            root2.parent = root1
        else:
            root2.parent = root1
            root1.rank += 1
            
        self._components -= 1
        return True

    def connected(self, value1: Any, value2: Any) -> bool:
        """
        Check if two values belong to the same set.
        
        Args:
            value1: First value.
            value2: Second value.
            
        Returns:
            True if the values are in the same set, False otherwise.
        """
        try:
            return self.find(value1) == self.find(value2)
        except KeyError:
            return False

    def components(self) -> int:
        """
        Get the number of connected components.
        
        Returns:
            The number of disjoint sets.
        """
        return self._components

    def size(self) -> int:
        """
        Get the total number of elements.
        
        Returns:
            The number of elements in the structure.
        """
        return len(self._elements)

    def get_elements(self) -> List[Any]:
        """
        Get a list of all element values.
        
        Returns:
            A list of all values in the structure.
        """
        return list(self._elements.keys())

    def get_component_elements(self, value: Any) -> List[Any]:
        """
        Get all elements in the same component as the given value.
        
        Args:
            value: The value whose component elements to retrieve.
            
        Returns:
            A list of values in the same component.
        """
        if value not in self._elements:
            raise KeyError(f"Element {value} not found")
            
        root = self.find(value)
        return [v for v in self._elements if self.find(v) == root]


def main() -> None:
    """Demo the UnionFind data structure."""
    print("UnionFind Demo")
    print("=" * 40)
    
    # Create a UnionFind instance
    uf = UnionFind()
    
    # Add elements
    elements = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    for elem in elements:
        uf.make_set(elem)
    
    print(f"Initial state: {uf.components()} components")
    print(f"Elements: {uf.get_elements()}")
    
    # Perform some unions
    print("\nPerforming unions:")
    operations = [('A', 'B'), ('C', 'D'), ('E', 'F'), ('A', 'C'), ('E', 'G')]
    
    for op in operations:
        result = uf.union(op[0], op[1])
        print(f"Union({op[0]}, {op[1]}) -> {result}")
        print(f"  Components: {uf.components()}")
    
    # Check connections
    print("\nChecking connections:")
    connections = [('A', 'B'), ('A', 'D'), ('A', 'E'), ('F', 'G')]
    
    for conn in connections:
        result = uf.connected(conn[0], conn[1])
        print(f"Connected({conn[0]}, {conn[1]}) -> {result}")
    
    # Show component elements
    print("\nComponent elements:")
    for elem in ['A', 'E']:
        component = uf.get_component_elements(elem)
        print(f"Component of {elem}: {component}")
    
    print(f"\nFinal state: {uf.components()} components, {uf.size()} elements")


if __name__ == "__main__":
    main()