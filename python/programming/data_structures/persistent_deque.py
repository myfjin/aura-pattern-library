# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import os
import json
import pickle
from typing import Any, Optional, Iterator
from collections import deque


class Node:
    """Node class for the doubly linked list implementation."""
    
    def __init__(self, data: Any) -> None:
        self.data: Any = data
        self.prev: Optional['Node'] = None
        self.next: Optional['Node'] = None


class PersistentDeque:
    """A persistent deque that maintains state in a file.
    
    The deque supports appendleft, append, popleft, and pop operations,
    with automatic serialization to disk after each modification.
    """
    
    def __init__(self, filename: str, maxlen: Optional[int] = None) -> None:
        """Initialize a PersistentDeque.
        
        Args:
            filename: Path to the file used for persistence
            maxlen: Maximum length of the deque (None for unlimited)
        """
        self.filename: str = filename
        self.maxlen: Optional[int] = maxlen
        self._head: Optional[Node] = None
        self._tail: Optional[Node] = None
        self._size: int = 0
        
        # Load existing data if file exists
        if os.path.exists(self.filename):
            self._load_from_file()
    
    def _save_to_file(self) -> None:
        """Serialize the deque to the backing file."""
        data = list(self)
        try:
            with open(self.filename, 'wb') as f:
                pickle.dump(data, f)
        except IOError as e:
            raise IOError(f"Failed to save deque to {self.filename}: {e}")
    
    def _load_from_file(self) -> None:
        """Load the deque from the backing file."""
        try:
            with open(self.filename, 'rb') as f:
                data = pickle.load(f)
                # Rebuild the doubly linked list
                for item in data:
                    self.append(item)
        except (IOError, pickle.PickleError) as e:
            raise IOError(f"Failed to load deque from {self.filename}: {e}")
    
    def appendleft(self, item: Any) -> None:
        """Add an item to the left side of the deque.
        
        Args:
            item: Item to add to the deque
        """
        new_node = Node(item)
        
        if self._head is None:  # Empty deque
            self._head = self._tail = new_node
        else:
            new_node.next = self._head
            self._head.prev = new_node
            self._head = new_node
            
        self._size += 1
        
        # Handle maxlen constraint
        if self.maxlen is not None and self._size > self.maxlen:
            self.pop()  # Remove from right
            
        self._save_to_file()
    
    def append(self, item: Any) -> None:
        """Add an item to the right side of the deque.
        
        Args:
            item: Item to add to the deque
        """
        new_node = Node(item)
        
        if self._tail is None:  # Empty deque
            self._head = self._tail = new_node
        else:
            new_node.prev = self._tail
            self._tail.next = new_node
            self._tail = new_node
            
        self._size += 1
        
        # Handle maxlen constraint
        if self.maxlen is not None and self._size > self.maxlen:
            self.popleft()  # Remove from left
            
        self._save_to_file()
    
    def popleft(self) -> Any:
        """Remove and return an item from the left side of the deque.
        
        Returns:
            The leftmost item in the deque
            
        Raises:
            IndexError: If the deque is empty
        """
        if self._head is None:
            raise IndexError("pop from an empty deque")
            
        data = self._head.data
        
        if self._head == self._tail:  # Only one element
            self._head = self._tail = None
        else:
            self._head = self._head.next
            self._head.prev = None
            
        self._size -= 1
        self._save_to_file()
        return data
    
    def pop(self) -> Any:
        """Remove and return an item from the right side of the deque.
        
        Returns:
            The rightmost item in the deque
            
        Raises:
            IndexError: If the deque is empty
        """
        if self._tail is None:
            raise IndexError("pop from an empty deque")
            
        data = self._tail.data
        
        if self._head == self._tail:  # Only one element
            self._head = self._tail = None
        else:
            self._tail = self._tail.prev
            self._tail.next = None
            
        self._size -= 1
        self._save_to_file()
        return data
    
    def __len__(self) -> int:
        """Return the length of the deque."""
        return self._size
    
    def __bool__(self) -> bool:
        """Return True if the deque is not empty."""
        return self._size > 0
    
    def __iter__(self) -> Iterator[Any]:
        """Iterate over the deque from left to right."""
        current = self._head
        while current:
            yield current.data
            current = current.next
    
    def __repr__(self) -> str:
        """Return a string representation of the deque."""
        items = list(self)
        return f"PersistentDeque({items}, maxlen={self.maxlen})"
    
    def clear(self) -> None:
        """Remove all elements from the deque."""
        self._head = self._tail = None
        self._size = 0
        self._save_to_file()
    
    def close(self) -> None:
        """Save and close the deque, removing the backing file."""
        self._save_to_file()
        try:
            os.remove(self.filename)
        except OSError:
            pass  # File might not exist


if __name__ == "__main__":
    # Self-test: collections.deque oracle fuzz, crash-recovery from disk
    # (the reason this pattern exists), exact maxlen eviction.
    import random
    import tempfile
    random.seed(42)
    tmpdir = tempfile.mkdtemp(prefix="pdeque_")
    path = os.path.join(tmpdir, "state.pkl")

    # Exact end semantics: append→right, appendleft→left.
    dq = PersistentDeque(path)
    dq.append(1)
    dq.append(2)
    dq.appendleft(0)
    assert list(dq) == [0, 1, 2], f"end semantics wrong: {list(dq)}"
    assert dq.pop() == 2 and dq.popleft() == 0 and list(dq) == [1]

    # THE DISASTER: the process "dies" (instance dropped); a fresh instance
    # on the same file must recover the EXACT state, in order.
    dq.append(7)
    dq.appendleft(-1)          # state on disk: [-1, 1, 7]
    del dq
    recovered = PersistentDeque(path)
    assert list(recovered) == [-1, 1, 7], \
        f"crash recovery lost state: {list(recovered)}"
    assert len(recovered) == 3

    # Oracle fuzz: 200 random ops mirrored against collections.deque,
    # RELOADING FROM DISK every 20 ops to prove persistence continuously.
    oracle = deque([-1, 1, 7])
    d = recovered
    for step in range(200):
        op = random.random()
        if op < 0.35:
            v = random.randint(0, 999)
            d.append(v); oracle.append(v)
        elif op < 0.6:
            v = random.randint(0, 999)
            d.appendleft(v); oracle.appendleft(v)
        elif op < 0.8 and oracle:
            assert d.pop() == oracle.pop(), f"pop diverged at step {step}"
        elif oracle:
            assert d.popleft() == oracle.popleft(), f"popleft diverged at step {step}"
        if step % 20 == 19:
            d = PersistentDeque(path)   # simulate a crash + reload
            assert list(d) == list(oracle), f"reload at step {step} diverged"
    assert list(d) == list(oracle) and len(d) == len(oracle)

    # maxlen eviction is exact: append evicts LEFT, appendleft evicts RIGHT.
    path3 = os.path.join(tmpdir, "capped.pkl")
    capped = PersistentDeque(path3, maxlen=3)
    for i in range(5):
        capped.append(i)
    assert list(capped) == [2, 3, 4], f"append past maxlen must keep newest: {list(capped)}"
    capped.appendleft(99)
    assert list(capped) == [99, 2, 3], f"appendleft must evict from the right: {list(capped)}"

    # Empty pops refuse loudly.
    capped.clear()
    assert len(capped) == 0 and not capped
    for call in (capped.pop, capped.popleft):
        try:
            call()
            assert False, "pop from empty deque succeeded"
        except IndexError:
            pass

    # close() removes the backing file; a new instance starts empty.
    capped.close()
    assert not os.path.exists(path3), "close() left the backing file"
    assert list(PersistentDeque(path3)) == []

    d.close()
    os.rmdir(tmpdir) if not os.listdir(tmpdir) else None
    print("persistent_deque: crash-recovered [-1,1,7] exact, 200-op deque oracle "
          "with 10 reloads agreed, maxlen evicts correct end — PASS")