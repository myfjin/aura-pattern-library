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


if __name__ == "__main__":
    # Self-test: writer exclusion under real contention, reader concurrency,
    # reader/writer overlap detection, upgrade/downgrade semantics.

    # 1. Readers genuinely share: 4 readers must be INSIDE the read section
    #    at the same instant (a barrier only passes if all 4 overlap).
    lock = RWLock()
    barrier = threading.Barrier(4, timeout=10.0)
    barrier_ok = [0]
    def _concurrent_reader() -> None:
        with lock.read_lock():
            barrier.wait()          # deadlocks (→ timeout) if readers serialize
            barrier_ok[0] += 1      # safe: all 4 are read-side, bump is pre-join-checked
    readers = [threading.Thread(target=_concurrent_reader) for _ in range(4)]
    for t in readers:
        t.start()
    for t in readers:
        t.join()
    assert barrier_ok[0] == 4, "4 readers failed to hold the read lock concurrently"

    # 2. THE DISASTER: writers without exclusion lose increments, and a reader
    #    inside a writer's critical section is corruption. Force both to be
    #    attempted and prove neither happens.
    state = {"value": 0, "readers_in": 0, "writers_in": 0, "overlap": False}
    meta = threading.Lock()
    def _writer() -> None:
        for _ in range(200):
            with lock.write_lock():
                with meta:
                    state["writers_in"] += 1
                    if state["writers_in"] > 1 or state["readers_in"] > 0:
                        state["overlap"] = True
                v = state["value"]          # deliberately non-atomic read-modify-write:
                state["value"] = v + 1      # only writer exclusion makes this safe
                with meta:
                    state["writers_in"] -= 1
    def _reader() -> None:
        for _ in range(200):
            with lock.read_lock():
                with meta:
                    state["readers_in"] += 1
                    if state["writers_in"] > 0:
                        state["overlap"] = True
                with meta:
                    state["readers_in"] -= 1
    workers = ([threading.Thread(target=_writer) for _ in range(8)]
               + [threading.Thread(target=_reader) for _ in range(4)])
    for t in workers:
        t.start()
    for t in workers:
        t.join()
    assert state["value"] == 1600, \
        f"8 writers x 200 increments must equal 1600, got {state['value']} (lost updates)"
    assert not state["overlap"], "reader or second writer observed inside a write section"

    # 3. Upgrade: the sole reader may upgrade; one of two readers may not.
    solo = RWLock()
    solo.acquire_read()
    assert solo.upgrade() is True, "sole reader denied upgrade"
    solo.release_write()
    solo.acquire_read()
    solo.acquire_read()                     # second read hold
    assert solo.upgrade() is False, "upgrade granted while another reader holds the lock"
    solo.release_read()
    assert solo.upgrade() is True, "sole remaining reader denied upgrade"
    solo.release_write()

    # 4. Downgrade: writer becomes reader without releasing, then upgrades back.
    solo.acquire_write()
    solo.downgrade()
    assert solo._readers == 1 and solo._writers == 0, "downgrade did not convert writer to reader"
    assert solo.upgrade() is True, "downgraded writer could not upgrade back"
    solo.release_write()

    print("rw_lock: 4 readers concurrent, 1600/1600 writes exclusive, no overlap, "
          "upgrade/downgrade honored — PASS")