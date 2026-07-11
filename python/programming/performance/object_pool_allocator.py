# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import threading
import time
from typing import Any, Callable, Optional, TypeVar, Generic
from contextlib import contextmanager
from collections import deque
import sqlite3

T = TypeVar('T')

class PooledObject(Generic[T]):
    """Wrapper for objects stored in the pool."""
    
    def __init__(self, obj: T, pool: 'ObjectPool[T]'):
        self._obj = obj
        self._pool = pool
        self._is_valid = True
        self._last_used = time.time()
    
    @property
    def obj(self) -> T:
        """Get the wrapped object."""
        return self._obj
    
    @property
    def is_valid(self) -> bool:
        """Check if the object is still valid."""
        return self._is_valid
    
    def invalidate(self) -> None:
        """Mark the object as invalid."""
        self._is_valid = False
    
    def update_last_used(self) -> None:
        """Update the last used timestamp."""
        self._last_used = time.time()
    
    def __enter__(self) -> T:
        return self._obj
    
    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self._pool.return_object(self)

class ObjectPool(Generic[T]):
    """Thread-safe object pool implementation."""
    
    def __init__(
        self,
        factory: Callable[[], T],
        validator: Callable[[T], bool],
        min_size: int = 1,
        max_size: int = 10,
        idle_timeout: float = 300.0
    ):
        """
        Initialize the object pool.
        
        Args:
            factory: Function to create new objects
            validator: Function to validate objects
            min_size: Minimum number of objects to keep in pool
            max_size: Maximum number of objects in pool
            idle_timeout: Time in seconds before idle objects are removed
        """
        if min_size < 0:
            raise ValueError("min_size must be non-negative")
        if max_size <= 0:
            raise ValueError("max_size must be positive")
        if min_size > max_size:
            raise ValueError("min_size cannot be greater than max_size")
        
        self._factory = factory
        self._validator = validator
        self._min_size = min_size
        self._max_size = max_size
        self._idle_timeout = idle_timeout
        
        self._pool: deque[PooledObject[T]] = deque()
        self._lock = threading.RLock()
        self._current_size = 0
        
        # Pre-populate with minimum objects
        self._ensure_min_size()
    
    def _ensure_min_size(self) -> None:
        """Ensure the pool contains at least min_size objects."""
        with self._lock:
            while self._current_size < self._min_size:
                obj = self._factory()
                pooled_obj = PooledObject(obj, self)
                self._pool.append(pooled_obj)
                self._current_size += 1
    
    def acquire(self, timeout: Optional[float] = None) -> PooledObject[T]:
        """
        Acquire an object from the pool.
        
        Args:
            timeout: Maximum time to wait for an object (None = wait forever)
            
        Returns:
            PooledObject wrapper
            
        Raises:
            TimeoutError: If timeout is exceeded
        """
        start_time = time.time()
        
        while True:
            with self._lock:
                # Clean up invalid and idle objects
                self._cleanup()
                
                # Try to get an existing valid object
                while self._pool:
                    pooled_obj = self._pool.popleft()
                    if pooled_obj.is_valid and self._validator(pooled_obj.obj):
                        pooled_obj.update_last_used()
                        return pooled_obj
                    else:
                        self._current_size -= 1
                
                # If no valid objects and we can create more, create a new one
                if self._current_size < self._max_size:
                    obj = self._factory()
                    pooled_obj = PooledObject(obj, self)
                    pooled_obj.update_last_used()
                    self._current_size += 1
                    return pooled_obj
            
            # If we get here, we're waiting for an object to be returned
            if timeout is not None:
                elapsed = time.time() - start_time
                if elapsed >= timeout:
                    raise TimeoutError("Timeout waiting for object from pool")
                time.sleep(0.01)  # Brief pause before retrying
            else:
                time.sleep(0.01)  # Brief pause before retrying
    
    @contextmanager
    def get(self, timeout: Optional[float] = None):
        """
        Context manager for acquiring and automatically returning objects.
        
        Args:
            timeout: Maximum time to wait for an object
        """
        pooled_obj = self.acquire(timeout)
        try:
            yield pooled_obj.obj
        finally:
            self.return_object(pooled_obj)
    
    def return_object(self, pooled_obj: PooledObject[T]) -> None:
        """
        Return an object to the pool.
        
        Args:
            pooled_obj: The object wrapper to return
        """
        with self._lock:
            if not pooled_obj.is_valid:
                self._current_size -= 1
                return
            
            # Validate before returning
            if self._validator(pooled_obj.obj):
                pooled_obj.update_last_used()
                self._pool.append(pooled_obj)
            else:
                pooled_obj.invalidate()
                self._current_size -= 1
    
    def _cleanup(self) -> None:
        """Remove invalid and idle objects from the pool."""
        now = time.time()
        valid_objects = deque()
        
        for pooled_obj in self._pool:
            # Check if object is valid
            if not pooled_obj.is_valid:
                self._current_size -= 1
                continue
            
            # Check if object is idle for too long
            if now - pooled_obj._last_used > self._idle_timeout:
                self._current_size -= 1
                continue
            
            # Check with validator
            if self._validator(pooled_obj.obj):
                valid_objects.append(pooled_obj)
            else:
                pooled_obj.invalidate()
                self._current_size -= 1
        
        self._pool = valid_objects
        
        # Ensure we maintain minimum size
        self._ensure_min_size()
    
    def size(self) -> int:
        """Get the current number of objects in the pool."""
        with self._lock:
            return self._current_size
    
    def available(self) -> int:
        """Get the number of available objects."""
        with self._lock:
            return len(self._pool)
    
    def close(self) -> None:
        """Close the pool and invalidate all objects."""
        with self._lock:
            while self._pool:
                pooled_obj = self._pool.popleft()
                pooled_obj.invalidate()
            self._current_size = 0

class DatabaseConnection:
    """Simple database connection wrapper for demonstration."""
    
    def __init__(self, db_path: str = ":memory:"):
        self._connection = sqlite3.connect(db_path, check_same_thread=False)
        self._connection.row_factory = sqlite3.Row
        self._is_closed = False
        self.id = id(self)  # For demonstration purposes
    
    def execute(self, query: str, params: tuple = ()) -> sqlite3.Cursor:
        """Execute a query."""
        if self._is_closed:
            raise RuntimeError("Connection is closed")
        return self._connection.execute(query, params)
    
    def commit(self) -> None:
        """Commit the transaction."""
        if self._is_closed:
            raise RuntimeError("Connection is closed")
        self._connection.commit()
    
    def close(self) -> None:
        """Close the connection."""
        if not self._is_closed:
            self._connection.close()
            self._is_closed = True
    
    @property
    def is_closed(self) -> bool:
        """Check if connection is closed."""
        return self._is_closed

def main():
    """Self-test: exact create counts, reuse identity, max-size refusal,
    invalidation accounting, idle reaping on a fake clock, sqlite round-trip."""

    class Thing:
        def __init__(self) -> None:
            self.alive = True

    made = {"n": 0}
    def factory() -> "Thing":
        made["n"] += 1
        return Thing()
    validator = lambda t: t.alive

    # min_size prefills exactly, no more.
    pool = ObjectPool(factory, validator, min_size=2, max_size=4, idle_timeout=3600.0)
    assert made["n"] == 2, f"min_size=2 must create exactly 2, created {made['n']}"
    assert pool.size() == 2 and pool.available() == 2

    # Reuse: the pool is FIFO, so identity rotates among the prefilled two —
    # the reuse claim is that NO new object is ever created while stock exists.
    prefilled = {id(p._obj) for p in pool._pool}
    po = pool.acquire()
    pool.return_object(po)
    po2 = pool.acquire()
    assert id(po2.obj) in prefilled, "acquire returned an object the pool never held"
    assert made["n"] == 2, f"reuse must not create; created {made['n']}"
    pool.return_object(po2)

    # Expansion stops at max_size: 4 concurrent holds = 4 objects, the 5th
    # acquire must TIME OUT (the failure the cap exists for).
    held = [pool.acquire() for _ in range(4)]
    assert made["n"] == 4 and pool.size() == 4
    try:
        pool.acquire(timeout=0.05)
        assert False, "5th acquire succeeded past max_size=4"
    except TimeoutError:
        pass
    # Returning one frees exactly one slot, and it's the same instance back.
    freed = held.pop()
    pool.return_object(freed)
    again = pool.acquire(timeout=0.05)
    assert again.obj is freed.obj, "freed slot not reused"
    pool.return_object(again)
    for h in held:
        pool.return_object(h)

    # Invalidation shrinks the pool; the next acquire builds a replacement.
    po = pool.acquire()
    po.invalidate()
    pool.return_object(po)
    assert pool.size() == 3, f"invalidated return must shrink pool to 3, got {pool.size()}"
    before = made["n"]
    dead = pool.acquire()          # pops a pooled survivor, no create needed
    assert made["n"] == before, "acquire created despite available objects"
    # A validator rejection on return also evicts.
    dead.obj.alive = False
    pool.return_object(dead)
    assert pool.size() == 2, f"validator-rejected return must evict, size {pool.size()}"

    # Idle reaping: jump the clock past idle_timeout; acquire must discard the
    # idle survivors and rebuild to min_size with FRESH objects.
    reap = ObjectPool(factory, validator, min_size=2, max_size=4, idle_timeout=100.0)
    originals = {id(p._obj) for p in reap._pool}
    base_created = made["n"]
    _real_time = time.time
    time.time = lambda: _real_time() + 3600.0
    try:
        po = reap.acquire()
        assert id(po.obj) not in originals, "idle-expired object handed back out"
        assert made["n"] > base_created, "no fresh objects built after idle reap"
        assert reap.size() == 2, f"pool must hold min_size=2 after reap, got {reap.size()}"
        reap.return_object(po)
    finally:
        time.time = _real_time

    # close() empties everything.
    pool.close()
    assert pool.size() == 0 and pool.available() == 0, "close left objects behind"

    # Invalid configuration is refused.
    for kwargs in ({"min_size": -1}, {"max_size": 0}, {"min_size": 5, "max_size": 2}):
        try:
            ObjectPool(factory, validator, **kwargs)
            assert False, f"ObjectPool({kwargs}) accepted"
        except ValueError:
            pass

    # The DatabaseConnection wrapper really guards a closed connection.
    conn = DatabaseConnection()
    conn.execute("CREATE TABLE t (x INTEGER)")
    conn.execute("INSERT INTO t VALUES (41), (1)")
    conn.commit()
    total = conn.execute("SELECT SUM(x) AS s FROM t").fetchone()["s"]
    assert total == 42, f"sqlite round-trip must sum to 42, got {total}"
    conn.close()
    try:
        conn.execute("SELECT 1")
        assert False, "closed connection still executed a query"
    except RuntimeError:
        pass

    print("object_pool_allocator: prefill 2, reuse-by-identity, cap@4 times out, "
          "invalidation 4→3→2, idle reap rebuilt 2 fresh, sqlite sum 42 — PASS")


if __name__ == "__main__":
    main()