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

    def get_entry(self, key: str) -> Optional[KeyValue]:
        """Retrieve the raw entry (tombstones included) — lets the caller
        distinguish 'deleted here' from 'never seen here'."""
        return self._data.get(key)

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
        kv = self.get_entry(key)
        return None if kv is None or kv.deleted else kv.value

    def get_entry(self, key: str) -> Optional[KeyValue]:
        """Retrieve the raw entry (tombstones included)."""
        if key not in self._index:
            return None

        with open(self.filename, 'rb') as f:
            f.seek(self._index[key])
            return pickle.load(f)

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
        """Delete a key-value pair (a real tombstone, not a None value —
        `put(key, None)` left deleted=False and let older SSTable copies
        resurrect the key)."""
        if self.memtable.is_full():
            self.immutable_memtable = self.memtable
            self.memtable = MemTable(self.max_memtable_size)
            self._flush_memtable()

        self.memtable.delete(key)

    def get(self, key: str) -> Optional[Any]:
        """Retrieve the value for a key. The FIRST entry found (newest level)
        decides — a tombstone there means 'gone', never 'look deeper'."""
        sources = [self.memtable]
        if self.immutable_memtable:
            sources.append(self.immutable_memtable)
        sources.extend(reversed(self.sstables))

        for source in sources:
            kv = source.get_entry(key)
            if kv is not None:
                return None if kv.deleted else kv.value

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
        
        # Merge sort all iterators. Same-key versions arrive newest-first
        # (KeyValue.__lt__ orders by descending timestamp within a key), so
        # only the FIRST version of each key counts — without the dedup,
        # stale values and deleted keys leaked back into scans.
        last_key = None
        for kv in heapq.merge(*iterators):
            # Apply range filtering if needed
            if start_key and kv.key < start_key:
                continue
            if end_key and kv.key > end_key:
                break
            if kv.key == last_key:
                continue
            last_key = kv.key
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
    """Self-test: reads across memtable AND flushed SSTables, tombstones win
    over older SSTable values, overwrite freshest-wins, scan exact, and
    compaction preserves every live key while dropping the dead."""
    import random
    random.seed(42)

    with tempfile.TemporaryDirectory() as temp_dir:
        # Tiny memtable (5) so flushes to SSTables happen constantly.
        lsm = LSMTree(temp_dir, max_memtable_size=5)

        # Reads hit both the memtable and flushed SSTables.
        for i in range(13):
            lsm.put(f"k{i:02d}", i * 10)
        assert len(lsm.sstables) >= 2, "13 puts at memtable=5 must flush at least twice"
        for i in range(13):
            assert lsm.get(f"k{i:02d}") == i * 10, f"k{i:02d} lost across flush"
        assert lsm.get("ghost") is None

        assert lsm.get("k03") == 30, "k03 must read exactly 30"
        assert lsm.get("k12") == 120, "k12 must read exactly 120"

        # Overwrite: the NEWEST value must win even when older copies live
        # in flushed SSTables.
        lsm.put("k01", "fresh")
        assert lsm.get("k01") == "fresh", "stale SSTable value shadowed the fresh write"

        # THE LSM DISASTER: a delete must beat an older value that still
        # exists in an SSTable (tombstone semantics).
        lsm.delete("k02")
        assert lsm.get("k02") is None, "deleted key resurrected from an old SSTable"
        for _ in range(6):  # force the tombstone itself to flush
            lsm.put(f"pad{random.randint(0, 999)}", "x")
        assert lsm.get("k02") is None, "tombstone lost its power after flushing"

        # Range scan: exact keys, sorted, deletions excluded.
        got = [(k, v) for k, v in lsm.scan("k03", "k06")]
        assert got == [("k03", 30), ("k04", 40), ("k05", 50), ("k06", 60)], \
            f"scan [k03,k06] wrong: {got}"

        # Oracle check against a dict over mixed ops.
        oracle = {}
        fresh_dir = os.path.join(temp_dir, "fuzz")
        os.makedirs(fresh_dir)
        db = LSMTree(fresh_dir, max_memtable_size=4)
        for step in range(300):
            k = f"key{random.randint(0, 30):02d}"
            op = random.random()
            if op < 0.6:
                v = random.randint(0, 999)
                db.put(k, v)
                oracle[k] = v
            elif op < 0.8:
                db.delete(k)
                oracle.pop(k, None)
            else:
                assert db.get(k) == oracle.get(k), f"get({k}) diverged at step {step}"
        for k in {f"key{i:02d}" for i in range(31)}:
            assert db.get(k) == oracle.get(k), f"final get({k}) diverged"

        # Compaction: many SSTables become one; every live key survives,
        # every deleted key stays dead.
        n_before = len(db.sstables)
        assert n_before >= 2, "fuzz must have produced multiple SSTables"
        db.compact()
        assert len(db.sstables) == 1, f"compaction left {len(db.sstables)} SSTables"
        for k, v in oracle.items():
            # memtable entries flushed? compact() only merges SSTables; the
            # memtable still holds the newest writes — reads must still agree.
            assert db.get(k) == v, f"compaction lost {k}"
        assert db.get("key99") is None

    print(f"lsm_tree: reads across {n_before} SSTables, freshest-wins, tombstone "
          f"survived flush, scan exact, 300-op oracle + compaction to 1 — PASS")


if __name__ == "__main__":
    main()