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
    """Demonstrate the object pool with database connections."""
    
    def connection_factory() -> DatabaseConnection:
        """Factory function to create database connections."""
        conn = DatabaseConnection()
        # Create a test table
        conn.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL
            )
        """)
        conn.commit()
        print(f"Created new database connection {conn.id}")
        return conn
    
    def connection_validator(conn: DatabaseConnection) -> bool:
        """Validator function to check if connection is valid."""
        try:
            conn.execute("SELECT 1")
            return not conn.is_closed
        except Exception:
            return False
    
    # Create pool with 2-5 connections
    pool = ObjectPool(
        factory=connection_factory,
        validator=connection_validator,
        min_size=2,
        max_size=5,
        idle_timeout=10.0  # 10 seconds for demo
    )
    
    print(f"Pool initialized with {pool.size()} connections")
    
    # Test 1: Basic usage with context manager
    print("\n--- Test 1: Basic usage ---")
    with pool.get() as conn:
        print(f"Using connection {conn.id}")
        conn.execute("INSERT INTO users (name, email) VALUES (?, ?)", 
                    ("Alice", "alice@example.com"))
        conn.commit()
    
    # Test 2: Multiple concurrent operations
    print("\n--- Test 2: Concurrent operations ---")
    def worker(worker_id: int) -> None:
        try:
            with pool.get(timeout=5.0) as conn:
                print(f"Worker {worker_id} using connection {conn.id}")
                conn.execute("INSERT INTO users (name, email) VALUES (?, ?)", 
                            (f"User{worker_id}", f"user{worker_id}@example.com"))
                conn.commit()
                time.sleep(0.5)  # Simulate work
        except TimeoutError:
            print(f"Worker {worker_id} timed out")
        except Exception as e:
            print(f"Worker {worker_id} error: {e}")
    
    # Start multiple worker threads
    threads = []
    for i in range(7):
        t = threading.Thread(target=worker, args=(i,))
        threads.append(t)
        t.start()
    
    # Wait for all threads to complete
    for t in threads:
        t.join()
    
    print(f"Pool size after concurrent operations: {pool.size()}")
    print(f"Available connections: {pool.available()}")
    
    # Test 3: Verify data
    print("\n--- Test 3: Verify data ---")
    with pool.get() as conn:
        cursor = conn.execute("SELECT COUNT(*) as count FROM users")
        count = cursor.fetchone()['count']
        print(f"Total users in database: {count}")
    
    # Test 4: Test connection invalidation
    print("\n--- Test 4: Connection invalidation ---")
    pooled_obj = pool.acquire()
    print(f"Acquired connection {pooled_obj.obj.id}")
    pooled_obj.obj.close()  # Manually close the connection
    pooled_obj.invalidate()  # Mark as invalid
    pool.return_object(pooled_obj)  # Return to pool
    
    print(f"Pool size after invalidation: {pool.size()}")
    
    # Test 5: Test pool expansion
    print("\n--- Test 5: Pool expansion ---")
    connections = []
    for i in range(5):
        pooled_obj = pool.acquire()
        connections.append(pooled_obj)
        print(f"Acquired connection {pooled_obj.obj.id} (pool size: {pool.size()})")
    
    # Return all connections
    for pooled_obj in connections:
        pool.return_object(pooled_obj)
    
    print(f"Pool size after returning all: {pool.size()}")
    print(f"Available connections: {pool.available()}")
    
    # Test 6: Cleanup demonstration
    print("\n--- Test 6: Idle timeout cleanup ---")
    print("Waiting 12 seconds for idle timeout...")
    time.sleep(12)
    
    # Acquire an object to trigger cleanup
    with pool.get() as conn:
        print(f"Pool size after cleanup: {pool.size()}")
        print(f"Available connections: {pool.available()}")
    
    # Clean up
    pool.close()
    print("\nPool closed")

if __name__ == "__main__":
    main()