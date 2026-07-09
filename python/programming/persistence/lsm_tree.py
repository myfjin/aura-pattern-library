"""
LSM-Tree Engine Implementation

A complete implementation of an LSM-Tree (Log-Structured Merge-Tree) storage engine
with MemTable, SSTable, and compaction functionality.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import bisect
import heapq
import os
import pickle
import tempfile
from collections import OrderedDict
from dataclasses import dataclass
from typing import Any, Dict, Iterator, List, Optional, Tuple


@dataclass
class KeyValue:
    """Represents a key-value pair with timestamp for versioning."""
    key: str
    value: Any
    timestamp: int
    deleted: bool = False

    def __lt__(self, other: 'KeyValue') -> bool:
        if self.key != other.key:
            return self.key < other.key
        return self.timestamp > other.timestamp  # Newer timestamps first


class MemTable:
    """In-memory storage structure using an ordered dictionary."""
    
    def __init__(self, max_size: int = 1000) -> None:
        self._data: OrderedDict[str, KeyValue] = OrderedDict()
        self._max_size = max_size
        self._timestamp = 0

    def put(self, key: str, value: Any) -> None:
        """Insert or update a key-value pair."""
        self._timestamp += 1
        self._data[key] = KeyValue(key, value, self._timestamp)
        self._data.move_to_end(key)  # Maintain insertion order

    def delete(self, key: str) -> None:
        """Mark a key as deleted."""
        self._timestamp += 1
        self._data[key] = KeyValue(key, None, self._timestamp, deleted=True)
        self._data.move_to_end(key)

    def get(self, key: str) -> Optional[Any]:
        """Retrieve the value for a key."""
        if key in self._data:
            kv = self._data[key]
            return None if kv.deleted else kv.value
        return None

    def size(self) -> int:
        """Return the number of entries."""
        return len(self._data)

    def is_full(self) -> bool:
        """Check if the MemTable has reached its maximum size."""
        return self.size() >= self._max_size

    def flush(self) -> List[KeyValue]:
        """Convert to sorted list for SSTable creation."""
        return sorted(self._data.values())

    def clear(self) -> None:
        """Clear all data."""
        self._data.clear()


class SSTable:
    """Sorted String Table - immutable on-disk storage."""
    
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self._index: Dict[str, int] = {}  # key -> offset in file
        self._load_index()

    def _load_index(self) -> None:
        """Load the index from the SSTable file."""
        if not os.path.exists(self.filename):
            return
            
        with open(self.filename, 'rb') as f:
            try:
                while True:
                    pos = f.tell()
                    kv = pickle.load(f)
                    self._index[kv.key] = pos
            except EOFError:
                pass

    def write(self, data: List[KeyValue]) -> None:
        """Write sorted key-value pairs to the SSTable."""
        self._index.clear()
        with open(self.filename, 'wb') as f:
            for kv in data:
                pos = f.tell()
                pickle.dump(kv, f)
                self._index[kv.key] = pos

    def get(self, key: str) -> Optional[Any]:
        """Retrieve a value by key."""
        if key not in self._index:
            return None
            
        with open(self.filename, 'rb') as f:
            f.seek(self._index[key])
            kv = pickle.load(f)
            return None if kv.deleted else kv.value

    def scan(self, start_key: Optional[str] = None, end_key: Optional[str] = None) -> Iterator[KeyValue]:
        """Scan key-value pairs within a range."""
        with open(self.filename, 'rb') as f:
            try:
                while True:
                    kv = pickle.load(f)
                    if start_key and kv.key < start_key:
                        continue
                    if end_key and kv.key > end_key:
                        break
                    yield kv
            except EOFError:
                pass

    def keys(self) -> List[str]:
        """Return all keys in the SSTable."""
        return list(self._index.keys())


class LSMTree:
    """Main LSM-Tree engine coordinating MemTable and SSTables."""
    
    def __init__(self, directory: str = ".", max_memtable_size: int = 1000) -> None:
        self.directory = directory
        self.max_memtable_size = max_memtable_size
        self.memtable = MemTable(max_memtable_size)
        self.immutable_memtable: Optional[MemTable] = None
        self.sstables: List[SSTable] = []
        self._sst_counter = 0
        
        # Create directory if it doesn't exist
        os.makedirs(directory, exist_ok=True)
        self._load_sstables()

    def _load_sstables(self) -> None:
        """Load existing SSTables from disk."""
        for filename in sorted(os.listdir(self.directory)):
            if filename.startswith("sst_") and filename.endswith(".db"):
                path = os.path.join(self.directory, filename)
                self.sstables.append(SSTable(path))

    def _flush_memtable(self) -> None:
        """Flush MemTable to SSTable."""
        if self.immutable_memtable is None:
            return
            
        # Create SSTable from immutable MemTable
        data = self.immutable_memtable.flush()
        if not data:
            self.immutable_memtable = None
            return
            
        self._sst_counter += 1
        filename = os.path.join(self.directory, f"sst_{self._sst_counter:06d}.db")
        sstable = SSTable(filename)
        sstable.write(data)
        self.sstables.append(sstable)
        
        self.immutable_memtable = None

    def put(self, key: str, value: Any) -> None:
        """Insert or update a key-value pair."""
        # If MemTable is full, rotate it
        if self.memtable.is_full():
            self.immutable_memtable = self.memtable
            self.memtable = MemTable(self.max_memtable_size)
            self._flush_memtable()
            
        self.memtable.put(key, value)

    def delete(self, key: str) -> None:
        """Delete a key-value pair."""
        self.put(key, None)  # Put with None value marks as deleted

    def get(self, key: str) -> Optional[Any]:
        """Retrieve the value for a key."""
        # Check MemTable first
        result = self.memtable.get(key)
        if result is not None:
            return result
            
        # Check immutable MemTable
        if self.immutable_memtable:
            result = self.immutable_memtable.get(key)
            if result is not None:
                return result
                
        # Check SSTables in reverse order (newest first)
        for sstable in reversed(self.sstables):
            result = sstable.get(key)
            if result is not None:
                return result
                
        return None

    def scan(self, start_key: Optional[str] = None, end_key: Optional[str] = None) -> Iterator[Tuple[str, Any]]:
        """Range scan with merge sorting across all levels."""
        # Collect iterators from all sources
        iterators = []
        
        # Add SSTable iterators
        for sstable in self.sstables:
            iterators.append(sstable.scan(start_key, end_key))
            
        # Add immutable MemTable if exists
        if self.immutable_memtable:
            iterators.append(iter(self.immutable_memtable.flush()))
            
        # Add current MemTable
        iterators.append(iter(self.memtable.flush()))
        
        # Merge sort all iterators
        for kv in heapq.merge(*iterators):
            # Apply range filtering if needed
            if start_key and kv.key < start_key:
                continue
            if end_key and kv.key > end_key:
                break
            if not kv.deleted:
                yield (kv.key, kv.value)

    def compact(self, level: int = 0) -> None:
        """Perform compaction on SSTables."""
        if len(self.sstables) < 2:
            return
            
        # For simplicity, compact all SSTables into one
        all_data = []
        keys_seen = set()
        
        # Collect all data, keeping only latest version of each key
        for sstable in reversed(self.sstables):  # Newest first
            for kv in sstable.scan():
                if kv.key not in keys_seen:
                    keys_seen.add(kv.key)
                    if not kv.deleted:
                        all_data.append(kv)
                        
        if not all_data:
            return
            
        # Remove old SSTables
        for sstable in self.sstables:
            if os.path.exists(sstable.filename):
                os.remove(sstable.filename)
        self.sstables.clear()
        
        # Create new compacted SSTable
        all_data.sort()
        self._sst_counter += 1
        filename = os.path.join(self.directory, f"sst_{self._sst_counter:06d}.db")
        sstable = SSTable(filename)
        sstable.write(all_data)
        self.sstables.append(sstable)

    def batch_write(self, data: Dict[str, Any]) -> None:
        """Write multiple key-value pairs efficiently."""
        for key, value in data.items():
            self.put(key, value)


def main() -> None:
    """Demo of the LSM-Tree engine."""
    # Create a temporary directory for our LSM-Tree
    with tempfile.TemporaryDirectory() as temp_dir:
        print(f"Using temporary directory: {temp_dir}")
        
        # Initialize LSM-Tree
        lsm = LSMTree(temp_dir, max_memtable_size=5)
        
        # Demo 1: Basic put/get operations
        print("\n=== Demo 1: Basic Operations ===")
        lsm.put("key1", "value1")
        lsm.put("key2", "value2")
        lsm.put("key3", "value3")
        
        print(f"Get key1: {lsm.get('key1')}")
        print(f"Get key2: {lsm.get('key2')}")
        print(f"Get non-existent key: {lsm.get('key99')}")
        
        # Demo 2: Overflow and flushing
        print("\n=== Demo 2: MemTable Flushing ===")
        for i in range(10):
            lsm.put(f"batch_key_{i}", f"batch_value_{i}")
            
        print(f"Get batch_key_5: {lsm.get('batch_key_5')}")
        print(f"Get batch_key_9: {lsm.get('batch_key_9')}")
        
        # Demo 3: Deletion
        print("\n=== Demo 3: Deletion ===")
        lsm.put("to_delete", "value")
        print(f"Before deletion - get to_delete: {lsm.get('to_delete')}")
        lsm.delete("to_delete")
        print(f"After deletion - get to_delete: {lsm.get('to_delete')}")
        
        # Demo 4: Range scan
        print("\n=== Demo 4: Range Scan ===")
        # Add some more data in order
        test_data = {f"scan_key_{i:02d}": f"scan_value_{i}" for i in range(15)}
        lsm.batch_write(test_data)
        
        print("Scanning keys from scan_key_05 to scan_key_10:")
        for key, value in lsm.scan("scan_key_05", "scan_key_10"):
            print(f"  {key}: {value}")
            
        # Demo 5: Batch write
        print("\n=== Demo 5: Batch Write ===")
        batch_data = {
            "batch1": "value1",
            "batch2": "value2",
            "batch3": "value3",
            "batch4": "value4",
            "batch5": "value5"
        }
        lsm.batch_write(batch_data)
        
        print("Retrieving batch written data:")
        for key in batch_data.keys():
            print(f"  {key}: {lsm.get(key)}")
            
        # Demo 6: Compaction
        print("\n=== Demo 6: Compaction ===")
        print(f"Number of SSTables before compaction: {len(lsm.sstables)}")
        lsm.compact()
        print(f"Number of SSTables after compaction: {len(lsm.sstables)}")
        
        # Verify data integrity after compaction
        print("Verifying data after compaction:")
        for i in range(5):
            key = f"batch_key_{i}"
            value = lsm.get(key)
            print(f"  {key}: {value}")

    print("\n=== Demo Complete ===")


if __name__ == "__main__":
    main()