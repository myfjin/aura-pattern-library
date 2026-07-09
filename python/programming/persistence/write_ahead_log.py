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
    """Demo of WAL with crash recovery simulation."""
    print("=== Write-Ahead Log Demo ===")
    
    # Initialize WAL
    wal = WAL("demo_wal.log")
    print(f"Initialized WAL with sequence number: {wal.sequence_number}")
    
    # Simulate database operations
    print("\n1. Simulating database operations...")
    wal.append(LogEntryType.INSERT, "user:1", {"name": "Alice", "age": 30})
    wal.append(LogEntryType.INSERT, "user:2", {"name": "Bob", "age": 25})
    wal.append(LogEntryType.UPDATE, "user:1", {"name": "Alice", "age": 31})
    wal.append(LogEntryType.DELETE, "user:2", None)
    
    print(f"Current sequence number: {wal.sequence_number}")
    
    # Create a checkpoint
    print("\n2. Creating checkpoint...")
    app_state = {"users_count": 1, "last_user_id": 1}
    checkpoint = wal.checkpoint(app_state)
    print(f"Checkpoint created at sequence {checkpoint.sequence_number}")
    
    # More operations after checkpoint
    print("\n3. More operations after checkpoint...")
    wal.append(LogEntryType.INSERT, "user:3", {"name": "Charlie", "age": 35})
    wal.append(LogEntryType.UPDATE, "user:1", {"name": "Alice Smith", "age": 31})
    print(f"Current sequence number: {wal.sequence_number}")
    
    # Simulate crash and recovery
    print("\n4. Simulating crash and recovery...")
    print("Replaying log from beginning:")
    
    recovered_state = {"users_count": 0, "last_user_id": 0}
    operations_applied = []
    
    def recovery_callback(entry: LogEntry) -> None:
        if entry.entry_type == LogEntryType.CHECKPOINT:
            recovered_state.update(entry.value)
            print(f"  Restored checkpoint: {entry.value}")
        else:
            operations_applied.append(entry)
            print(f"  Applied {entry.entry_type.name}: {entry.key} -> {entry.value}")
    
    count = wal.replay(recovery_callback)
    print(f"Replayed {count} entries")
    print(f"Recovered state: {recovered_state}")
    print(f"Operations applied: {len(operations_applied)}")
    
    # Test truncation
    print("\n5. Testing log truncation...")
    print(f"Before truncation, sequence number: {wal.sequence_number}")
    wal.truncate(checkpoint.sequence_number)
    print(f"After truncation to checkpoint {checkpoint.sequence_number}, sequence number: {wal.sequence_number}")
    
    # Verify truncation
    print("Replaying remaining log entries:")
    count = wal.replay(lambda e: print(f"  {e.entry_type.name}: {e.key} -> {e.value}"))
    print(f"Replayed {count} entries after truncation")
    
    # Test latest checkpoint retrieval
    print("\n6. Testing checkpoint retrieval...")
    latest_checkpoint = wal.get_latest_checkpoint()
    if latest_checkpoint:
        entry, state = latest_checkpoint
        print(f"Latest checkpoint at sequence {entry.sequence_number}: {state}")
    else:
        print("No checkpoint found")
    
    # Clean up
    if os.path.exists("demo_wal.log"):
        os.remove("demo_wal.log")
        print("\nCleaned up demo log file")
    
    print("\n=== Demo completed successfully ===")


if __name__ == "__main__":
    main()