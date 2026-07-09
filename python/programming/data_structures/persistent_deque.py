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
    # Demo: Create a persistent deque and perform operations
    filename = "demo_deque.pkl"
    
    # Clean up any existing file
    if os.path.exists(filename):
        os.remove(filename)
    
    # Create a new persistent deque
    print("Creating PersistentDeque with maxlen=5...")
    dq = PersistentDeque(filename, maxlen=5)
    
    # Add elements
    print("\nAdding elements with append and appendleft:")
    for i in range(3):
        dq.append(i)
        print(f"  append({i}) -> {list(dq)}")
    
    for i in range(3, 5):
        dq.appendleft(i)
        print(f"  appendleft({i}) -> {list(dq)}")
    
    print(f"\nDeque size: {len(dq)}")
    print(f"Deque representation: {dq}")
    
    # Test persistence by creating a new instance
    print("\nTesting persistence by creating a new instance:")
    dq2 = PersistentDeque(filename, maxlen=5)
    print(f"Loaded deque: {list(dq2)}")
    
    # Pop elements
    print("\nPopping elements:")
    while dq2:
        try:
            item = dq2.pop()
            print(f"  pop() -> {item}, remaining: {list(dq2)}")
        except IndexError:
            break
    
    # Test maxlen behavior
    print("\nTesting maxlen behavior:")
    dq3 = PersistentDeque(filename, maxlen=3)
    for i in range(5):
        dq3.append(i)
        print(f"  append({i}) -> {list(dq3)}")
    
    # Clean up
    dq3.close()
    print(f"\nCleaned up file: {filename}")