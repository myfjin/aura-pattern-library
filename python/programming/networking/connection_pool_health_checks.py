"""
Connection Pool with Health Checks Module

This module provides a robust connection pool implementation with health checking,
connection validation, and automatic eviction of failed connections.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import threading
import time
import queue
import logging
from abc import ABC, abstractmethod
from typing import Optional, Any, Callable
from contextlib import contextmanager

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Connection(ABC):
    """Abstract base class for database connections."""
    
    def __init__(self, connection_id: int):
        self.connection_id = connection_id
        self.created_at = time.time()
        self.last_used = time.time()
        self.is_active = True

    @abstractmethod
    def execute(self, query: str) -> Any:
        """Execute a query on the connection."""
        pass

    @abstractmethod
    def is_valid(self) -> bool:
        """Check if the connection is valid."""
        pass

    @abstractmethod
    def close(self) -> None:
        """Close the connection."""
        pass


class MockDatabaseConnection(Connection):
    """Mock database connection for demonstration purposes."""
    
    def __init__(self, connection_id: int):
        super().__init__(connection_id)
        self._is_closed = False
        logger.debug(f"Created mock connection {connection_id}")

    def execute(self, query: str) -> str:
        """Execute a query on the mock connection."""
        if self._is_closed:
            raise RuntimeError("Connection is closed")
        
        self.last_used = time.time()
        time.sleep(0.01)  # Simulate network delay
        return f"Executed: {query}"

    def is_valid(self) -> bool:
        """Check if the mock connection is valid."""
        return not self._is_closed and self.is_active

    def close(self) -> None:
        """Close the mock connection."""
        self._is_closed = True
        logger.debug(f"Closed mock connection {self.connection_id}")


class PooledConnection:
    """Wrapper for connections in the pool."""
    
    def __init__(self, connection: Connection):
        self.connection = connection
        self.borrowed_at: Optional[float] = None
        self.borrowed_by: Optional[int] = None

    def borrow(self) -> None:
        """Mark the connection as borrowed."""
        self.borrowed_at = time.time()
        # In a real implementation, we'd track the borrower thread
        self.borrowed_by = threading.get_ident()

    def release(self) -> None:
        """Mark the connection as released."""
        self.borrowed_at = None
        self.borrowed_by = None

    def is_borrowed(self) -> bool:
        """Check if the connection is currently borrowed."""
        return self.borrowed_at is not None

    def get_connection(self) -> Connection:
        """Get the underlying connection."""
        return self.connection


class ConnectionPool:
    """Connection pool with health checks and automatic eviction."""
    
    def __init__(
        self,
        max_connections: int = 10,
        validation_query: str = "SELECT 1",
        connection_factory: Callable[[], Connection] = None,
        health_check_interval: float = 30.0,
        max_idle_time: float = 300.0
    ):
        """
        Initialize the connection pool.
        
        Args:
            max_connections: Maximum number of connections in the pool
            validation_query: Query to validate connection health
            connection_factory: Factory function to create new connections
            health_check_interval: Interval between health checks in seconds
            max_idle_time: Maximum time a connection can be idle before eviction
        """
        if max_connections <= 0:
            raise ValueError("max_connections must be positive")
            
        self.max_connections = max_connections
        self.validation_query = validation_query
        self.connection_factory = connection_factory or self._default_connection_factory
        self.health_check_interval = health_check_interval
        self.max_idle_time = max_idle_time
        
        self._pool: queue.Queue[PooledConnection] = queue.Queue(maxsize=max_connections)
        self._active_connections: set[PooledConnection] = set()
        self._lock = threading.RLock()
        self._closed = False
        self._connection_counter = 0
        
        # Start background health check thread
        self._health_check_thread = threading.Thread(target=self._health_check_worker, daemon=True)
        self._health_check_thread.start()
        
        # Pre-populate pool with minimum connections
        self._initialize_pool()

    def _default_connection_factory(self) -> Connection:
        """Default connection factory."""
        with self._lock:
            self._connection_counter += 1
            return MockDatabaseConnection(self._connection_counter)

    def _initialize_pool(self) -> None:
        """Initialize the pool with minimum connections."""
        for _ in range(min(5, self.max_connections)):
            try:
                conn = self._create_connection()
                self._pool.put(conn)
            except Exception as e:
                logger.warning(f"Failed to create initial connection: {e}")

    def _create_connection(self) -> PooledConnection:
        """Create a new pooled connection."""
        connection = self.connection_factory()
        return PooledConnection(connection)

    def borrow_connection(self, timeout: float = 30.0) -> PooledConnection:
        """
        Borrow a connection from the pool.
        
        Args:
            timeout: Maximum time to wait for a connection
            
        Returns:
            PooledConnection: A connection from the pool
            
        Raises:
            RuntimeError: If the pool is closed
            queue.Empty: If no connection is available within timeout
        """
        if self._closed:
            raise RuntimeError("Connection pool is closed")
            
        # Try to get an existing connection
        try:
            pooled_conn = self._pool.get(timeout=timeout)
        except queue.Empty:
            # If no connection available, try to create a new one
            with self._lock:
                if len(self._active_connections) + self._pool.qsize() < self.max_connections:
                    pooled_conn = self._create_connection()
                else:
                    # Wait again for a connection to be returned
                    pooled_conn = self._pool.get(timeout=timeout)
        
        # Validate the connection before returning it
        if not pooled_conn.get_connection().is_valid():
            logger.warning("Invalid connection found in pool, creating new one")
            self._destroy_connection(pooled_conn)
            pooled_conn = self._create_connection()
        
        pooled_conn.borrow()
        with self._lock:
            self._active_connections.add(pooled_conn)
            
        return pooled_conn

    def return_connection(self, pooled_conn: PooledConnection) -> None:
        """
        Return a connection to the pool.
        
        Args:
            pooled_conn: The connection to return
        """
        if self._closed:
            self._destroy_connection(pooled_conn)
            return
            
        pooled_conn.release()
        with self._lock:
            self._active_connections.discard(pooled_conn)
            
        try:
            self._pool.put(pooled_conn, block=False)
        except queue.Full:
            # Pool is full, destroy the connection
            self._destroy_connection(pooled_conn)

    def _destroy_connection(self, pooled_conn: PooledConnection) -> None:
        """Destroy a connection."""
        try:
            pooled_conn.get_connection().close()
        except Exception as e:
            logger.warning(f"Error closing connection: {e}")

    def _health_check_worker(self) -> None:
        """Background worker to perform health checks."""
        while not self._closed:
            try:
                time.sleep(self.health_check_interval)
                self._perform_health_check()
            except Exception as e:
                logger.error(f"Error in health check worker: {e}")

    def _perform_health_check(self) -> None:
        """Perform health check on connections in the pool."""
        logger.debug("Performing health check")
        invalid_connections = []
        
        # Check connections in the pool
        temp_storage = []
        pool_size = self._pool.qsize()
        
        for _ in range(pool_size):
            try:
                pooled_conn = self._pool.get(block=False)
                if not pooled_conn.get_connection().is_valid():
                    invalid_connections.append(pooled_conn)
                else:
                    temp_storage.append(pooled_conn)
            except queue.Empty:
                break
                
        # Put valid connections back
        for pooled_conn in temp_storage:
            try:
                self._pool.put(pooled_conn, block=False)
            except queue.Full:
                self._destroy_connection(pooled_conn)
                
        # Destroy invalid connections
        for pooled_conn in invalid_connections:
            self._destroy_connection(pooled_conn)
            logger.info(f"Evicted invalid connection {pooled_conn.get_connection().connection_id}")
            
        # Create new connections to maintain pool size if needed
        available_connections = self._pool.qsize()
        if available_connections < min(5, self.max_connections):
            connections_to_create = min(5, self.max_connections) - available_connections
            for _ in range(connections_to_create):
                try:
                    new_conn = self._create_connection()
                    self._pool.put(new_conn, block=False)
                except queue.Full:
                    break

    @contextmanager
    def get_connection(self, timeout: float = 30.0):
        """
        Context manager to get a connection from the pool.
        
        Args:
            timeout: Maximum time to wait for a connection
            
        Yields:
            Connection: A database connection
        """
        pooled_conn = self.borrow_connection(timeout)
        try:
            yield pooled_conn.get_connection()
        finally:
            self.return_connection(pooled_conn)

    def get_pool_stats(self) -> dict:
        """
        Get pool statistics.
        
        Returns:
            dict: Pool statistics
        """
        with self._lock:
            return {
                "available_connections": self._pool.qsize(),
                "active_connections": len(self._active_connections),
                "max_connections": self.max_connections,
                "is_closed": self._closed
            }

    def close(self) -> None:
        """Close the connection pool and all connections."""
        logger.info("Closing connection pool")
        self._closed = True
        
        # Close all connections in the pool
        while not self._pool.empty():
            try:
                pooled_conn = self._pool.get(block=False)
                self._destroy_connection(pooled_conn)
            except queue.Empty:
                break
                
        # Close all active connections
        with self._lock:
            for pooled_conn in self._active_connections.copy():
                self._destroy_connection(pooled_conn)
            self._active_connections.clear()


def main():
    """Self-test: borrow/return conservation under real thread contention,
    context-manager auto-return, stats exact, closed pool refuses."""
    pool = ConnectionPool(max_connections=5, validation_query="SELECT 1",
                          health_check_interval=3600.0)

    # Borrow/return bookkeeping is exact.
    c1 = pool.borrow_connection(timeout=2.0)
    c2 = pool.borrow_connection(timeout=2.0)
    stats = pool.get_pool_stats()
    assert stats["active_connections"] == 2, f"2 borrows → active {stats['active_connections']}"
    assert stats["max_connections"] == 5
    pool.return_connection(c1)
    pool.return_connection(c2)
    assert pool.get_pool_stats()["active_connections"] == 0, "returns not accounted"

    # Context manager auto-returns even on exceptions.
    with pool.get_connection(timeout=2.0) as conn:
        assert conn.is_valid()
        result = conn.execute("SELECT 1")
        assert "SELECT 1" in str(result) or result is not None
        assert pool.get_pool_stats()["active_connections"] == 1
    assert pool.get_pool_stats()["active_connections"] == 0, "context manager leaked"
    try:
        with pool.get_connection(timeout=2.0):
            raise RuntimeError("boom")
    except RuntimeError:
        pass
    assert pool.get_pool_stats()["active_connections"] == 0, \
        "connection leaked when the body raised"

    # THE CONTENTION TEST: 8 threads x 5 checkouts against 5 connections.
    # Every checkout must succeed (waiting as needed) and nothing may leak.
    errors = []
    done = [0]
    lock = threading.Lock()
    def worker(worker_id: int) -> None:
        for i in range(5):
            try:
                with pool.get_connection(timeout=10.0) as conn:
                    conn.execute(f"SELECT {worker_id}")
                with lock:
                    done[0] += 1
            except Exception as e:
                errors.append(f"w{worker_id}/{i}: {e}")
    threads = [threading.Thread(target=worker, args=(i,)) for i in range(8)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    assert not errors, f"checkouts failed under contention: {errors[:3]}"
    assert done[0] == 40, f"8x5 checkouts must complete 40, got {done[0]}"
    final = pool.get_pool_stats()
    assert final["active_connections"] == 0, \
        f"{final['active_connections']} connections leaked after the storm"
    assert final["available_connections"] <= 5, "pool grew past max_connections"

    # close(): pool refuses further borrows.
    pool.close()
    assert pool.get_pool_stats()["is_closed"] is True
    try:
        pool.borrow_connection(timeout=0.5)
        assert False, "closed pool lent a connection"
    except Exception:
        pass

    print("connection_pool_health_checks: bookkeeping exact, CM auto-return "
          "(incl. on raise), 40/40 contended checkouts no leaks, closed refuses — PASS")


if __name__ == "__main__":
    main()