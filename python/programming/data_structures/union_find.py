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
    """Self-test: exact component counting, transitive connectivity, union-by-rank
    depth bound, and a graph-oracle fuzz."""
    import random
    random.seed(42)

    uf = UnionFind()
    for elem in "ABCDEFG":
        uf.make_set(elem)
    assert uf.components() == 7 and uf.size() == 7

    # Each productive union reduces components by exactly 1.
    for pair, expected_components in [(("A", "B"), 6), (("C", "D"), 5),
                                      (("E", "F"), 4), (("A", "C"), 3),
                                      (("E", "G"), 3 - 0)]:
        assert uf.union(*pair) is True
        # trace: after (E,G) → 2 components
    assert uf.components() == 2, f"5 productive unions on 7 must leave 2, got {uf.components()}"

    # A redundant union reports False and changes nothing.
    assert uf.union("A", "D") is False, "union within a component reported a merge"
    assert uf.components() == 2

    # Transitivity: A-B, C-D, A-C ⇒ A~D without ever unioning them directly.
    assert uf.connected("A", "D") is True, "transitive connectivity broken"
    assert uf.connected("A", "E") is False, "separate components reported connected"
    assert sorted(uf.get_component_elements("A")) == ["A", "B", "C", "D"]
    assert sorted(uf.get_component_elements("E")) == ["E", "F", "G"]

    # Union-by-rank: a balanced 16-way merge tree keeps root rank at log2(16)=4.
    big = UnionFind()
    for i in range(16):
        big.make_set(i)
    step = 1
    while step < 16:
        for i in range(0, 16, step * 2):
            big.union(i, i + step)
        step *= 2
    assert big.components() == 1
    assert big.find(0).rank == 4, f"balanced 16-merge must give rank 4, got {big.find(0).rank}"

    # Oracle fuzz: 400 random unions/queries vs brute-force component labels.
    n = 50
    fuzz = UnionFind()
    labels = list(range(n))          # label[i] = component id (brute-force oracle)
    for i in range(n):
        fuzz.make_set(i)
    for _ in range(400):
        a, b = random.randint(0, n - 1), random.randint(0, n - 1)
        if random.random() < 0.5:
            merged = fuzz.union(a, b)
            assert merged == (labels[a] != labels[b]), f"union({a},{b}) disagrees with oracle"
            if merged:
                old, new = labels[a], labels[b]
                labels = [new if l == old else l for l in labels]
        else:
            assert fuzz.connected(a, b) == (labels[a] == labels[b]), \
                f"connected({a},{b}) disagrees with oracle"
    assert fuzz.components() == len(set(labels)), "component count diverged from oracle"

    # Refusals: duplicate make_set, find on a missing key.
    try:
        uf.make_set("A")
        assert False, "duplicate make_set accepted"
    except ValueError:
        pass
    try:
        uf.find("Z")
        assert False, "find on missing element succeeded"
    except KeyError:
        pass
    assert uf.connected("A", "Z") is False, "connected() must be False for unknown elements"

    print(f"union_find: 7→2 components exact, transitivity held, rank 4 on balanced "
          f"16-merge, 400-op oracle agreed ({fuzz.components()} final) — PASS")


if __name__ == "__main__":
    main()