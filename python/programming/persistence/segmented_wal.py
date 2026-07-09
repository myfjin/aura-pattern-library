"""
Write-Ahead Log (WAL) implementation for durable transaction logging.

This module provides a complete WAL system with:
- Append-only writes for durability
- Checksum verification for data integrity
- Segment-based log rotation
- Crash recovery and replay functionality
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import os
import struct
import hashlib
from typing import List, Optional, Iterator, Tuple
from pathlib import Path
import shutil


class WALEntry:
    """
    Represents a single entry in the Write-Ahead Log.
    
    Each entry contains:
    - Length of the data (4 bytes)
    - Checksum of the data (32 bytes)
    - Data payload (variable length)
    """
    
    HEADER_FORMAT = "!I32s"  # Length (4 bytes) + Checksum (32 bytes)
    HEADER_SIZE = struct.calcsize(HEADER_FORMAT)
    
    def __init__(self, data: bytes, checksum: Optional[bytes] = None):
        """
        Initialize a WAL entry.
        
        Args:
            data: The data payload to store
            checksum: Optional precomputed checksum. If None, computed automatically.
        """
        self.data = data
        if checksum is None:
            self.checksum = hashlib.sha256(data).digest()
        else:
            self.checksum = checksum
            
    @property
    def length(self) -> int:
        """Get the length of the data payload."""
        return len(self.data)
        
    def serialize(self) -> bytes:
        """
        Serialize the entry to bytes for storage.
        
        Returns:
            Serialized entry as bytes
        """
        header = struct.pack(self.HEADER_FORMAT, self.length, self.checksum)
        return header + self.data
        
    @classmethod
    def deserialize(cls, data: bytes) -> Tuple['WALEntry', int]:
        """
        Deserialize a WAL entry from bytes.
        
        Args:
            data: Bytes containing the serialized entry
            
        Returns:
            Tuple of (WALEntry, bytes_consumed)
            
        Raises:
            ValueError: If data is corrupted or checksum doesn't match
        """
        if len(data) < cls.HEADER_SIZE:
            raise ValueError("Insufficient data for entry header")
            
        length, checksum = struct.unpack(cls.HEADER_FORMAT, data[:cls.HEADER_SIZE])
        
        if len(data) < cls.HEADER_SIZE + length:
            raise ValueError("Insufficient data for entry payload")
            
        payload = data[cls.HEADER_SIZE:cls.HEADER_SIZE + length]
        
        # Verify checksum
        computed_checksum = hashlib.sha256(payload).digest()
        if computed_checksum != checksum:
            raise ValueError("Checksum mismatch - data corruption detected")
            
        entry = cls(payload, checksum)
        return entry, cls.HEADER_SIZE + length
        
    def __eq__(self, other) -> bool:
        """Check equality based on data and checksum."""
        if not isinstance(other, WALEntry):
            return False
        return self.data == other.data and self.checksum == other.checksum


class WALSegment:
    """
    Represents a single segment file in the WAL.
    
    Segments are append-only files that store WAL entries sequentially.
    Each segment has a maximum size to enable log rotation.
    """
    
    def __init__(self, filepath: Path, max_size: int = 1024*1024):
        """
        Initialize a WAL segment.
        
        Args:
            filepath: Path to the segment file
            max_size: Maximum size of the segment in bytes
        """
        self.filepath = filepath
        self.max_size = max_size
        self._file = None
        self._position = 0
        
        # Create file if it doesn't exist
        if not self.filepath.exists():
            self.filepath.parent.mkdir(parents=True, exist_ok=True)
            self.filepath.touch()
            
        # Determine current position
        self._position = self.filepath.stat().st_size
        
    def open_for_append(self) -> None:
        """Open the segment file for appending."""
        if self._file is None or self._file.closed:
            self._file = self.filepath.open('ab')
            
    def close(self) -> None:
        """Close the segment file."""
        if self._file and not self._file.closed:
            self._file.close()
            self._file = None
            
    def append(self, entry: WALEntry) -> int:
        """
        Append an entry to the segment.
        
        Args:
            entry: The entry to append
            
        Returns:
            Position where the entry was written
            
        Raises:
            IOError: If segment is full or write fails
        """
        if self._position >= self.max_size:
            raise IOError("Segment is full")
            
        self.open_for_append()
        serialized = entry.serialize()
        
        # Ensure we don't exceed max size
        if self._position + len(serialized) > self.max_size:
            raise IOError("Entry too large for remaining segment space")
            
        position = self._position
        self._file.write(serialized)
        self._file.flush()
        os.fsync(self._file.fileno())
        self._position += len(serialized)
        
        return position
        
    def read_entries(self) -> Iterator[WALEntry]:
        """
        Read all valid entries from the segment.
        
        Yields:
            WALEntry objects in order
            
        Raises:
            ValueError: If corruption is detected
        """
        if not self.filepath.exists():
            return
            
        with self.filepath.open('rb') as f:
            data = f.read()
            
        position = 0
        while position < len(data):
            try:
                entry, consumed = WALEntry.deserialize(data[position:])
                yield entry
                position += consumed
            except ValueError as e:
                # Stop at first corruption
                print(f"Warning: Corruption detected at position {position}: {e}")
                break
                
    def size(self) -> int:
        """Get the current size of the segment."""
        return self._position
        
    def is_full(self) -> bool:
        """Check if the segment is full."""
        return self._position >= self.max_size
        
    def __enter__(self):
        """Context manager entry."""
        self.open_for_append()
        return self
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.close()


class WriteAheadLog:
    """
    Write-Ahead Log implementation for durable transaction logging.
    
    Provides append-only writes, checksum verification, and crash recovery.
    """
    
    def __init__(self, directory: Path, segment_size: int = 1024*1024):
        """
        Initialize the WAL.
        
        Args:
            directory: Directory to store WAL segments
            segment_size: Maximum size of each segment file
        """
        self.directory = Path(directory)
        self.segment_size = segment_size
        self.directory.mkdir(parents=True, exist_ok=True)
        
        # Find existing segments
        self.segments: List[WALSegment] = []
        self._load_segments()
        
        # Create initial segment if needed
        if not self.segments:
            self._create_new_segment()
            
    def _load_segments(self) -> None:
        """Load existing segments from the directory."""
        segment_files = sorted(self.directory.glob("*.wal"))
        for segment_file in segment_files:
            segment = WALSegment(segment_file, self.segment_size)
            self.segments.append(segment)
            
    def _create_new_segment(self) -> WALSegment:
        """Create a new segment file."""
        segment_number = len(self.segments)
        filename = f"segment_{segment_number:06d}.wal"
        filepath = self.directory / filename
        segment = WALSegment(filepath, self.segment_size)
        self.segments.append(segment)
        return segment
        
    def append(self, data: bytes) -> Tuple[int, int]:
        """
        Append data to the WAL.
        
        Args:
            data: Data to append
            
        Returns:
            Tuple of (segment_index, position) where entry was written
            
        Raises:
            IOError: If write fails
        """
        entry = WALEntry(data)
        
        # Get current segment
        if not self.segments:
            current_segment = self._create_new_segment()
        else:
            current_segment = self.segments[-1]
            
        # If current segment is full, create new one
        if current_segment.is_full():
            current_segment = self._create_new_segment()
            
        try:
            position = current_segment.append(entry)
            return len(self.segments) - 1, position
        except IOError:
            # If append fails, try creating a new segment
            current_segment = self._create_new_segment()
            position = current_segment.append(entry)
            return len(self.segments) - 1, position
            
    def replay(self) -> Iterator[bytes]:
        """
        Replay all entries in the WAL in order.
        
        Yields:
            Data payloads from all valid entries
            
        This method is used for crash recovery.
        """
        for segment in self.segments:
            try:
                for entry in segment.read_entries():
                    yield entry.data
            except Exception as e:
                print(f"Warning: Error reading segment {segment.filepath}: {e}")
                break
                
    def truncate(self, segment_index: int, position: int) -> None:
        """
        Truncate the WAL at the specified position.
        
        Args:
            segment_index: Index of the segment to truncate at
            position: Position within the segment to truncate at
        """
        # Close all segments first
        for segment in self.segments:
            segment.close()
            
        # Remove segments after the truncate point
        segments_to_remove = self.segments[segment_index + 1:]
        for segment in segments_to_remove:
            if segment.filepath.exists():
                segment.filepath.unlink()
                
        self.segments = self.segments[:segment_index + 1]
        
        # Truncate the specified segment
        if self.segments:
            segment = self.segments[segment_index]
            if segment.filepath.exists():
                with open(segment.filepath, 'r+b') as f:
                    f.truncate(position)
                segment._position = position
                
    def sync(self) -> None:
        """Sync all segments to disk."""
        for segment in self.segments:
            segment.close()  # Closing flushes and syncs
            
    def close(self) -> None:
        """Close the WAL and all segments."""
        for segment in self.segments:
            segment.close()


def simulate_crash(wal: WriteAheadLog) -> None:
    """
    Simulate a crash by forcefully terminating without proper cleanup.
    
    This function demonstrates how the WAL can recover from crashes.
    """
    # Write some entries
    wal.append(b"Transaction 1")
    wal.append(b"Transaction 2")
    wal.append(b"Transaction 3")
    
    # Simulate crash by not calling close() and not syncing
    # In a real crash, the process would just terminate
    print("Simulated crash - WAL not properly closed")


def recover_from_crash(wal_directory: Path) -> List[bytes]:
    """
    Recover transactions from a crashed WAL.
    
    Args:
        wal_directory: Directory containing WAL segments
        
    Returns:
        List of recovered transaction data
    """
    wal = WriteAheadLog(wal_directory)
    recovered_data = list(wal.replay())
    wal.close()
    return recovered_data


def main():
    """Demo of WAL functionality including crash recovery."""
    # Create temporary directory for WAL
    wal_dir = Path("wal_demo")
    if wal_dir.exists():
        shutil.rmtree(wal_dir)
    
    print("=== Write-Ahead Log Demo ===\n")
    
    # Create WAL
    wal = WriteAheadLog(wal_dir, segment_size=1024)  # Small segments for demo
    
    print("1. Writing transactions to WAL...")
    transactions = [
        b"BEGIN TRANSACTION",
        b"INSERT INTO users (id, name) VALUES (1, 'Alice')",
        b"INSERT INTO users (id, name) VALUES (2, 'Bob')",
        b"COMMIT TRANSACTION",
        b"BEGIN TRANSACTION",
        b"UPDATE users SET name = 'Alice Smith' WHERE id = 1",
        b"COMMIT TRANSACTION"
    ]
    
    positions = []
    for i, tx in enumerate(transactions):
        segment_idx, pos = wal.append(tx)
        positions.append((segment_idx, pos))
        print(f"   Wrote transaction {i+1} to segment {segment_idx} at position {pos}")
    
    print(f"\n2. WAL state: {len(wal.segments)} segments created")
    for i, segment in enumerate(wal.segments):
        print(f"   Segment {i}: {segment.size()} bytes")
    
    # Demonstrate normal replay
    print("\n3. Normal replay of all transactions:")
    wal.sync()  # Ensure all data is written
    replayed = list(wal.replay())
    for i, data in enumerate(replayed):
        print(f"   Transaction {i+1}: {data.decode()}")
    
    # Simulate crash
    print("\n4. Simulating system crash...")
    wal2 = WriteAheadLog(wal_dir, segment_size=1024)
    simulate_crash(wal2)  # This doesn't close the WAL properly
    
    # Recovery
    print("\n5. Recovering from crash...")
    recovered = recover_from_crash(wal_dir)
    print(f"   Recovered {len(recovered)} transactions:")
    for i, data in enumerate(recovered):
        print(f"   Transaction {i+1}: {data.decode()}")
    
    # Verify recovery
    print("\n6. Verifying recovery...")
    if len(recovered) >= len(transactions):
        match = all(r == t for r, t in zip(recovered, transactions))
        if match:
            print("   ✓ All transactions recovered correctly")
        else:
            print("   ✗ Transaction data mismatch")
    else:
        print(f"   ✗ Expected {len(transactions)} transactions, got {len(recovered)}")
    
    # Clean up
    wal.close()
    if wal_dir.exists():
        shutil.rmtree(wal_dir)
    
    print("\n=== Demo completed ===")


if __name__ == "__main__":
    main()