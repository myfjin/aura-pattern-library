"""
Write-Ahead Log (WAL) implementation for data durability and crash recovery.

This module provides a complete WAL system that ensures data integrity through
logging operations before they are applied to the main data store.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import os
import struct
import pickle
import hashlib
from typing import Any, Callable, List, Optional, Tuple
from enum import Enum
from dataclasses import dataclass


class LogEntryType(Enum):
    """Types of log entries."""
    INSERT = 1
    UPDATE = 2
    DELETE = 3
    CHECKPOINT = 4


@dataclass
class LogEntry:
    """Represents a single entry in the write-ahead log."""
    entry_type: LogEntryType
    key: Any
    value: Any
    sequence_number: int
    checksum: str = ""
    
    def __post_init__(self) -> None:
        """Calculate checksum after initialization."""
        if not self.checksum:
            self.checksum = self._calculate_checksum()
    
    def _calculate_checksum(self) -> str:
        """Calculate checksum for integrity verification."""
        data = f"{self.entry_type.value}{self.key}{self.value}{self.sequence_number}".encode('utf-8')
        return hashlib.md5(data).hexdigest()
    
    def is_valid(self) -> bool:
        """Verify entry integrity."""
        return self.checksum == self._calculate_checksum()


class WAL:
    """Write-Ahead Log for data durability and crash recovery."""
    
    def __init__(self, log_file: str = "wal.log") -> None:
        """
        Initialize the WAL.
        
        Args:
            log_file: Path to the log file
        """
        self.log_file = log_file
        self.sequence_number = 0
        self._ensure_log_file()
        self._recover_sequence_number()
    
    def _ensure_log_file(self) -> None:
        """Create log file if it doesn't exist."""
        if not os.path.exists(self.log_file):
            with open(self.log_file, 'wb') as f:
                pass  # Create empty file
    
    def _recover_sequence_number(self) -> None:
        """Recover the last sequence number from existing log entries."""
        try:
            with open(self.log_file, 'rb') as f:
                while True:
                    entry = self._read_entry(f)
                    if entry is None:
                        break
                    self.sequence_number = max(self.sequence_number, entry.sequence_number)
        except (EOFError, FileNotFoundError):
            pass
    
    def _serialize_entry(self, entry: LogEntry) -> bytes:
        """Serialize log entry to bytes."""
        data = pickle.dumps(entry)
        size = len(data)
        return struct.pack('I', size) + data
    
    def _deserialize_entry(self, data: bytes) -> LogEntry:
        """Deserialize bytes to log entry."""
        return pickle.loads(data)
    
    def _read_entry(self, file_handle) -> Optional[LogEntry]:
        """Read a single entry from file handle."""
        size_bytes = file_handle.read(4)
        if len(size_bytes) < 4:
            return None
        
        size = struct.unpack('I', size_bytes)[0]
        data = file_handle.read(size)
        if len(data) < size:
            raise EOFError("Incomplete log entry")
        
        entry = self._deserialize_entry(data)
        if not entry.is_valid():
            raise ValueError("Log entry checksum mismatch")
        
        return entry
    
    def append(self, entry_type: LogEntryType, key: Any, value: Any) -> LogEntry:
        """
        Append a new entry to the log.
        
        Args:
            entry_type: Type of log entry
            key: Key for the operation
            value: Value for the operation
            
        Returns:
            The appended log entry
        """
        self.sequence_number += 1
        entry = LogEntry(
            entry_type=entry_type,
            key=key,
            value=value,
            sequence_number=self.sequence_number
        )
        
        with open(self.log_file, 'ab') as f:
            serialized = self._serialize_entry(entry)
            f.write(serialized)
            f.flush()
            os.fsync(f.fileno())
        
        return entry
    
    def replay(self, callback: Callable[[LogEntry], None], 
               start_sequence: int = 0) -> int:
        """
        Replay log entries from the beginning or a specific sequence number.
        
        Args:
            callback: Function to call for each log entry
            start_sequence: Sequence number to start replay from (0 for all)
            
        Returns:
            Number of entries replayed
        """
        count = 0
        try:
            with open(self.log_file, 'rb') as f:
                while True:
                    entry = self._read_entry(f)
                    if entry is None:
                        break
                    
                    if entry.sequence_number >= start_sequence:
                        callback(entry)
                        count += 1
        except (EOFError, FileNotFoundError):
            pass
        
        return count
    
    def checkpoint(self, state: Any) -> LogEntry:
        """
        Create a checkpoint entry in the log.
        
        Args:
            state: Application state to checkpoint
            
        Returns:
            The checkpoint log entry
        """
        return self.append(LogEntryType.CHECKPOINT, "CHECKPOINT", state)
    
    def truncate(self, sequence_number: int) -> bool:
        """
        Truncate log entries up to a specific sequence number.
        
        Args:
            sequence_number: Sequence number to truncate up to
            
        Returns:
            True if truncation was successful, False otherwise
        """
        if sequence_number <= 0:
            return False
        
        # Read all entries
        entries: List[LogEntry] = []
        try:
            with open(self.log_file, 'rb') as f:
                while True:
                    entry = self._read_entry(f)
                    if entry is None:
                        break
                    entries.append(entry)
        except (EOFError, FileNotFoundError):
            pass
        
        # Filter entries after the truncate point
        remaining_entries = [e for e in entries if e.sequence_number > sequence_number]
        
        if not remaining_entries and sequence_number >= self.sequence_number:
            # Truncate everything
            with open(self.log_file, 'wb') as f:
                pass
            self.sequence_number = 0
            return True
        
        # Rewrite log with remaining entries
        with open(self.log_file, 'wb') as f:
            for entry in remaining_entries:
                serialized = self._serialize_entry(entry)
                f.write(serialized)
        
        # Update sequence number if needed
        if remaining_entries:
            self.sequence_number = max(e.sequence_number for e in remaining_entries)
        else:
            self.sequence_number = 0
            
        return True
    
    def get_latest_checkpoint(self) -> Optional[Tuple[LogEntry, Any]]:
        """
        Find the latest checkpoint in the log.
        
        Returns:
            Tuple of (checkpoint_entry, state) or None if no checkpoint exists
        """
        latest_checkpoint: Optional[Tuple[LogEntry, Any]] = None
        
        try:
            with open(self.log_file, 'rb') as f:
                while True:
                    entry = self._read_entry(f)
                    if entry is None:
                        break
                    
                    if entry.entry_type == LogEntryType.CHECKPOINT:
                        latest_checkpoint = (entry, entry.value)
        except (EOFError, FileNotFoundError):
            pass
        
        return latest_checkpoint


def main() -> None:
    """Self-test: THE DISASTER MUST HAPPEN — the process dies, a fresh WAL on
    the same file must replay every committed operation in order; plus
    checkpoint recovery, truncation, and torn-tail behavior."""
    import tempfile
    tmpdir = tempfile.mkdtemp(prefix="wal_")
    path = os.path.join(tmpdir, "wal.log")

    # Write operations + a checkpoint + post-checkpoint operations.
    wal = WAL(path)
    assert wal.sequence_number == 0
    wal.append(LogEntryType.INSERT, "user:1", {"name": "Alice", "age": 30})
    wal.append(LogEntryType.INSERT, "user:2", {"name": "Bob", "age": 25})
    wal.append(LogEntryType.UPDATE, "user:1", {"name": "Alice", "age": 31})
    wal.append(LogEntryType.DELETE, "user:2", None)
    checkpoint = wal.checkpoint({"users_count": 1, "last_user_id": 1})
    wal.append(LogEntryType.INSERT, "user:3", {"name": "Charlie", "age": 35})
    assert wal.sequence_number == 6, f"6 entries must leave seq 6, got {wal.sequence_number}"

    # THE CRASH: drop the instance; recover from disk alone.
    del wal
    recovered = WAL(path)
    assert recovered.sequence_number == 6, \
        f"recovered WAL lost its sequence: {recovered.sequence_number}"
    replayed = []
    count = recovered.replay(lambda e: replayed.append(e))
    assert count == 6, f"must replay exactly 6 entries, got {count}"
    assert [e.sequence_number for e in replayed] == [1, 2, 3, 4, 5, 6], \
        "replay order broken"
    assert replayed[0].entry_type == LogEntryType.INSERT and replayed[0].key == "user:1"
    assert replayed[2].value == {"name": "Alice", "age": 31}, "payload corrupted"
    assert replayed[3].entry_type == LogEntryType.DELETE

    # Applying the replay rebuilds the exact database state.
    db = {}
    for e in replayed:
        if e.entry_type == LogEntryType.INSERT or e.entry_type == LogEntryType.UPDATE:
            db[e.key] = e.value
        elif e.entry_type == LogEntryType.DELETE:
            db.pop(e.key, None)
    assert db == {"user:1": {"name": "Alice", "age": 31},
                  "user:3": {"name": "Charlie", "age": 35}}, f"rebuilt state wrong: {db}"

    # Checkpoint retrieval finds the latest checkpoint payload.
    entry, state = recovered.get_latest_checkpoint()
    assert entry.sequence_number == checkpoint.sequence_number == 5
    assert state == {"users_count": 1, "last_user_id": 1}

    # Truncation keeps only post-checkpoint entries.
    assert recovered.truncate(checkpoint.sequence_number) is True
    tail = []
    assert recovered.replay(lambda e: tail.append(e)) == 1
    assert tail[0].key == "user:3", f"truncation kept the wrong tail: {tail[0].key}"
    assert recovered.truncate(0) is False, "truncate(0) must be refused"

    # TORN TAIL: chop bytes off the last record (mid-write crash). Recovery
    # must still yield the intact prefix rather than exploding.
    p2 = os.path.join(tmpdir, "torn.log")
    w2 = WAL(p2)
    w2.append(LogEntryType.INSERT, "a", 1)
    w2.append(LogEntryType.INSERT, "b", 2)
    size = os.path.getsize(p2)
    with open(p2, "r+b") as f:
        f.truncate(size - 3)
    survivors = []
    WAL(p2).replay(lambda e: survivors.append(e.key))
    assert survivors == ["a"], f"torn tail must leave exactly the intact prefix: {survivors}"

    for fn in os.listdir(tmpdir):
        os.remove(os.path.join(tmpdir, fn))
    os.rmdir(tmpdir)
    print("write_ahead_log: crash-replayed 6/6 in order, state rebuilt exact, "
          "checkpoint@5 found, truncate kept 1, torn tail survived — PASS")


if __name__ == "__main__":
    main()