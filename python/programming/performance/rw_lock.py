# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import threading
from typing import Optional
from contextlib import contextmanager


class RWLock:
    """
    A read-write lock implementation with writer preference and upgrade/downgrade capabilities.
    
    This lock allows multiple readers or a single writer to access a resource.
    Writers have preference over readers to prevent writer starvation.
    Readers can upgrade to writers and writers can downgrade to readers.
    """
    
    def __init__(self) -> None:
        """Initialize the read-write lock."""
        self._read_ready = threading.Condition(threading.RLock())
        self._readers = 0
        self._writers = 0
        self._pending_writers = 0
        self._writer_thread: Optional[threading.Thread] = None
    
    @contextmanager
    def read_lock(self):
        """
        Context manager for acquiring a read lock.
        
        Yields:
            None: While holding the read lock
        """
        self.acquire_read()
        try:
            yield
        finally:
            self.release_read()
    
    @contextmanager
    def write_lock(self):
        """
        Context manager for acquiring a write lock.
        
        Yields:
            None: While holding the write lock
        """
        self.acquire_write()
        try:
            yield
        finally:
            self.release_write()
    
    def acquire_read(self) -> None:
        """Acquire a read lock."""
        with self._read_ready:
            # Wait while there are writers or pending writers (writer preference)
            while self._writers > 0 or self._pending_writers > 0:
                self._read_ready.wait()
            self._readers += 1
    
    def release_read(self) -> None:
        """Release a read lock."""
        with self._read_ready:
            self._readers -= 1
            if self._readers == 0:
                self._read_ready.notify_all()
    
    def acquire_write(self) -> None:
        """Acquire a write lock."""
        thread_id = threading.current_thread()
        with self._read_ready:
            self._pending_writers += 1
            # Wait while there are readers or writers
            while self._readers > 0 or self._writers > 0:
                self._read_ready.wait()
            self._pending_writers -= 1
            self._writers += 1
            self._writer_thread = thread_id
    
    def release_write(self) -> None:
        """Release a write lock."""
        with self._read_ready:
            self._writers -= 1
            self._writer_thread = None
            self._read_ready.notify_all()
    
    def upgrade(self) -> bool:
        """
        Upgrade from read lock to write lock.
        
        Returns:
            bool: True if upgrade was successful, False otherwise
        """
        thread_id = threading.current_thread()
        with self._read_ready:
            # Check if we're the only reader
            if self._readers == 1 and self._writers == 0 and self._pending_writers == 0:
                # Atomically upgrade: remove read lock and add write lock
                self._readers -= 1
                self._writers += 1
                self._writer_thread = thread_id
                return True
            else:
                return False
    
    def downgrade(self) -> None:
        """Downgrade from write lock to read lock."""
        with self._read_ready:
            if self._writers > 0 and self._writer_thread == threading.current_thread():
                # Atomically downgrade: remove write lock and add read lock
                self._writers -= 1
                self._writer_thread = None
                self._readers += 1
                self._read_ready.notify_all()


class ReadLock:
    """
    A context manager for read locks.
    
    This class provides a convenient way to acquire and release read locks.
    """
    
    def __init__(self, rwlock: RWLock) -> None:
        """
        Initialize the read lock.
        
        Args:
            rwlock: The RWLock instance to use
        """
        self._rwlock = rwlock
    
    def __enter__(self) -> 'ReadLock':
        """
        Enter the runtime context and acquire the read lock.
        
        Returns:
            ReadLock: This instance
        """
        self._rwlock.acquire_read()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """
        Exit the runtime context and release the read lock.
        
        Args:
            exc_type: Exception type
            exc_val: Exception value
            exc_tb: Exception traceback
        """
        self._rwlock.release_read()


class WriteLock:
    """
    A context manager for write locks.
    
    This class provides a convenient way to acquire and release write locks.
    """
    
    def __init__(self, rwlock: RWLock) -> None:
        """
        Initialize the write lock.
        
        Args:
            rwlock: The RWLock instance to use
        """
        self._rwlock = rwlock
    
    def __enter__(self) -> 'WriteLock':
        """
        Enter the runtime context and acquire the write lock.
        
        Returns:
            WriteLock: This instance
        """
        self._rwlock.acquire_write()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """
        Exit the runtime context and release the write lock.
        
        Args:
            exc_type: Exception type
            exc_val: Exception value
            exc_tb: Exception traceback
        """
        self._rwlock.release_write()


def _demo_reader(rwlock: RWLock, reader_id: int, data: list) -> None:
    """Demo reader function."""
    with ReadLock(rwlock):
        print(f"Reader {reader_id} reading data: {data}")
        # Try to upgrade (should fail if there are other readers)
        if rwlock.upgrade():
            print(f"Reader {reader_id} upgraded to writer")
            data.append(f"Modified by reader {reader_id}")
            rwlock.downgrade()
            print(f"Reader {reader_id} downgraded to reader")
        else:
            print(f"Reader {reader_id} could not upgrade")


def _demo_writer(rwlock: RWLock, writer_id: int, data: list) -> None:
    """Demo writer function."""
    with WriteLock(rwlock):
        print(f"Writer {writer_id} writing to data")
        data.append(f"Written by writer {writer_id}")
        # Try to downgrade (should work)
        rwlock.downgrade()
        print(f"Writer {writer_id} downgraded to reader")
        print(f"Writer {writer_id} reading data: {data}")
        # Try to upgrade back (should work since we're the only reader)
        if rwlock.upgrade():
            print(f"Writer {writer_id} upgraded back to writer")
            data.append(f"Re-modified by writer {writer_id}")
        rwlock.release_write()  # Need to manually release since we upgraded


if __name__ == "__main__":
    # Create shared data and lock
    shared_data = ["initial"]
    lock = RWLock()
    
    # Create threads
    threads = []
    
    # Create reader threads
    for i in range(3):
        t = threading.Thread(target=_demo_reader, args=(lock, i, shared_data))
        threads.append(t)
    
    # Create writer threads
    for i in range(2):
        t = threading.Thread(target=_demo_writer, args=(lock, i, shared_data))
        threads.append(t)
    
    # Start all threads
    for t in threads:
        t.start()
    
    # Wait for all threads to complete
    for t in threads:
        t.join()
    
    print(f"Final data: {shared_data}")
    
    # Demonstrate context managers
    print("\nDemonstrating context managers:")
    with lock.read_lock():
        print("Inside read lock context manager")
    
    with lock.write_lock():
        print("Inside write lock context manager")