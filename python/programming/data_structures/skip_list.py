# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import random
from typing import Optional, List, Iterator, Tuple

class Node:
    """Node class for the skip list."""
    
    def __init__(self, key: int, value: any, level: int):
        self.key = key
        self.value = value
        self.forward: List[Optional['Node']] = [None] * (level + 1)

class SkipList:
    """Skip list implementation with probabilistic balancing."""
    
    def __init__(self, max_level: int = 16, p: float = 0.5):
        self.max_level = max_level
        self.p = p
        self.header = Node(-1, None, max_level)
        self.level = 0
        self.size = 0
    
    def _random_level(self) -> int:
        """Generate a random level for a new node."""
        level = 0
        while random.random() < self.p and level < self.max_level:
            level += 1
        return level
    
    def insert(self, key: int, value: any) -> None:
        """Insert a key-value pair into the skip list."""
        update: List[Optional[Node]] = [None] * (self.max_level + 1)
        current = self.header
        
        # Find the position to insert
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]
            update[i] = current
        
        current = current.forward[0]
        
        # If key already exists, update value
        if current and current.key == key:
            current.value = value
            return
        
        # Create new node
        new_level = self._random_level()
        if new_level > self.level:
            for i in range(self.level + 1, new_level + 1):
                update[i] = self.header
            self.level = new_level
        
        new_node = Node(key, value, new_level)
        
        # Insert node
        for i in range(new_level + 1):
            new_node.forward[i] = update[i].forward[i]
            update[i].forward[i] = new_node
        
        self.size += 1
    
    def search(self, key: int) -> Optional[any]:
        """Search for a key in the skip list and return its value."""
        current = self.header
        
        # Traverse the skip list
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]
        
        current = current.forward[0]
        
        # Check if key was found
        if current and current.key == key:
            return current.value
        
        return None
    
    def delete(self, key: int) -> bool:
        """Delete a key from the skip list. Returns True if deleted."""
        update: List[Optional[Node]] = [None] * (self.max_level + 1)
        current = self.header
        
        # Find the node to delete
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]
            update[i] = current
        
        current = current.forward[0]
        
        # If key was found, delete it
        if current and current.key == key:
            for i in range(self.level + 1):
                if update[i].forward[i] != current:
                    break
                update[i].forward[i] = current.forward[i]
            
            # Update level if needed
            while self.level > 0 and self.header.forward[self.level] is None:
                self.level -= 1
            
            self.size -= 1
            return True
        
        return False
    
    def range_query(self, start: int, end: int) -> List[Tuple[int, any]]:
        """Return all key-value pairs in the given range [start, end]."""
        result = []
        current = self.header
        
        # Find the starting position
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].key < start:
                current = current.forward[i]
        
        current = current.forward[0]
        
        # Collect all elements in range
        while current and current.key <= end:
            result.append((current.key, current.value))
            current = current.forward[0]
        
        return result
    
    def __len__(self) -> int:
        """Return the number of elements in the skip list."""
        return self.size
    
    def __iter__(self) -> Iterator[Tuple[int, any]]:
        """Iterate over all key-value pairs in sorted order."""
        current = self.header.forward[0]
        while current:
            yield (current.key, current.value)
            current = current.forward[0]

if __name__ == "__main__":
    # Self-test: exact search/range/delete semantics + a dict oracle fuzz.
    random.seed(42)
    sl = SkipList()

    # Insert 100 keys in shuffled order; the list must still be fully sorted.
    keys = list(range(100))
    random.shuffle(keys)
    for k in keys:
        sl.insert(k, f"value_{k}")
    assert len(sl) == 100, f"100 inserts must give size 100, got {len(sl)}"
    assert [k for k, _ in sl] == list(range(100)), "iteration is not sorted"

    # Exact hits and misses.
    assert sl.search(50) == "value_50"
    assert sl.search(150) is None, "search invented a missing key"
    assert sl.range_query(10, 13) == [(10, "value_10"), (11, "value_11"),
                                      (12, "value_12"), (13, "value_13")], \
        "range [10,13] must return exactly those 4 pairs in order"
    assert sum(k for k, _ in sl.range_query(10, 13)) == 46, \
        "keys in range [10,13] must sum to 10+11+12+13 = 46"
    assert sl.range_query(200, 300) == [], "empty range returned items"

    # Insert on an existing key UPDATES, never duplicates.
    sl.insert(50, "replaced")
    assert len(sl) == 100 and sl.search(50) == "replaced", "update-in-place broke"

    # Delete: removes exactly the key, reports honestly.
    assert sl.delete(25) is True
    assert sl.delete(25) is False, "double delete reported success"
    assert sl.delete(150) is False, "deleting a missing key reported success"
    assert sl.search(25) is None and len(sl) == 99

    # THE STRUCTURAL CLAIM: skip list agrees with a dict oracle over 600
    # random mixed operations (insert/delete/search).
    oracle = {k: ("replaced" if k == 50 else f"value_{k}") for k in range(100) if k != 25}
    for _ in range(600):
        op = random.random()
        k = random.randint(0, 149)
        if op < 0.5:
            sl.insert(k, k * 7)
            oracle[k] = k * 7
        elif op < 0.8:
            assert sl.delete(k) == (k in oracle), f"delete({k}) disagrees with oracle"
            oracle.pop(k, None)
        else:
            assert sl.search(k) == oracle.get(k), f"search({k}) disagrees with oracle"
    assert list(sl) == sorted(oracle.items()), "final state diverged from the oracle"
    assert len(sl) == len(oracle)

    print(f"skip_list: sorted after shuffle, exact range, update-in-place, "
          f"600-op oracle fuzz agreed, final size {len(sl)} — PASS")