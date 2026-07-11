"""
Connection Manager with Pooling

A module that provides connection pooling functionality with health checks
and thread-safe operations.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import threading
import time
from typing import Optional, Set
from collections import deque
import weakref


class Connection:
    """Represents a single connection with health tracking."""
    
    def __init__(self, connection_id: int):
        self.id = connection_id
        self.created_at = time.time()
        self.last_used = self.created_at
        self.is_healthy = True
        self._in_use = False
        
    def mark_as_used(self) -> None:
        """Mark connection as currently in use."""
        self.last_used = time.time()
        self._in_use = True
        
    def mark_as_available(self) -> None:
        """Mark connection as available for use."""
        self._in_use = False
        
    def is_in_use(self) -> bool:
        """Check if connection is currently in use."""
        return self._in_use
        
    def health_check(self) -> bool:
        """Perform a health check on the connection.
        
        Returns:
            bool: True if connection is healthy, False otherwise
        """
        # Simulate a health check that might fail occasionally
        # In a real implementation, this would check actual connection state
        if time.time() - self.created_at > 30:  # Expire after 30 seconds
            self.is_healthy = False
        return self.is_healthy
        
    def __str__(self) -> str:
        return f"Connection(id={self.id}, healthy={self.is_healthy}, in_use={self._in_use})"


class ConnectionPool:
    """Thread-safe connection pool with health checks and size management."""
    
    def __init__(self, max_size: int = 10):
        """Initialize the connection pool.
        
        Args:
            max_size: Maximum number of connections in the pool
        """
        if max_size <= 0:
            raise ValueError("Max pool size must be positive")
            
        self._max_size = max_size
        self._available_connections: deque = deque()
        self._in_use_connections: Set[Connection] = set()
        self._lock = threading.RLock()
        self._connection_counter = 0
        
    @property
    def max_size(self) -> int:
        """Get the maximum pool size."""
        return self._max_size
        
    @property
    def available_count(self) -> int:
        """Get the number of available connections."""
        with self._lock:
            return len(self._available_connections)
            
    @property
    def in_use_count(self) -> int:
        """Get the number of connections currently in use."""
        with self._lock:
            return len(self._in_use_connections)
            
    @property
    def total_count(self) -> int:
        """Get the total number of connections in the pool."""
        with self._lock:
            return len(self._available_connections) + len(self._in_use_connections)
            
    def _create_connection(self) -> Connection:
        """Create a new connection.
        
        Returns:
            Connection: A new connection instance
        """
        self._connection_counter += 1
        return Connection(self._connection_counter)
        
    def borrow_connection(self) -> Optional[Connection]:
        """Borrow a connection from the pool.
        
        Returns:
            Connection: A connection if available, None if pool is at max capacity
        """
        with self._lock:
            # First try to get an available connection
            while self._available_connections:
                connection = self._available_connections.popleft()
                
                # Perform health check
                if connection.health_check():
                    connection.mark_as_used()
                    self._in_use_connections.add(connection)
                    return connection
                # If unhealthy, it gets garbage collected
                
            # If no available connections, create a new one if under limit
            if self.total_count < self._max_size:
                connection = self._create_connection()
                connection.mark_as_used()
                self._in_use_connections.add(connection)
                return connection
                
            # Pool is at maximum capacity and all connections are in use
            return None
            
    def return_connection(self, connection: Connection) -> bool:
        """Return a connection to the pool.
        
        Args:
            connection: The connection to return
            
        Returns:
            bool: True if connection was successfully returned, False otherwise
        """
        with self._lock:
            if connection not in self._in_use_connections:
                return False
                
            connection.mark_as_available()
            self._in_use_connections.remove(connection)
            
            # Only add back to pool if healthy
            if connection.health_check():
                self._available_connections.append(connection)
                return True
            # If unhealthy, it gets garbage collected
            return True
            
    def close_all_connections(self) -> None:
        """Close all connections in the pool."""
        with self._lock:
            # Clear all connections
            self._available_connections.clear()
            self._in_use_connections.clear()
            
    def cleanup_unhealthy_connections(self) -> int:
        """Remove unhealthy connections from the pool.
        
        Returns:
            int: Number of unhealthy connections removed
        """
        with self._lock:
            # Check available connections
            healthy_available = deque()
            removed_count = 0
            
            while self._available_connections:
                conn = self._available_connections.popleft()
                if conn.health_check():
                    healthy_available.append(conn)
                else:
                    removed_count += 1
                    
            self._available_connections = healthy_available
            
            # Check in-use connections (we can't remove them, but we can mark them)
            unhealthy_in_use = []
            for conn in self._in_use_connections:
                if not conn.health_check():
                    unhealthy_in_use.append(conn)
                    removed_count += 1
                    
            # Note: We can't remove in-use connections, they'll be checked when returned
            return removed_count


def main():
    """Self-test on a fake clock: capacity exact, reuse-not-recreate,
    foreign returns refused, aged connections evicted not re-pooled."""
    _now = [1_000.0]
    _real_time = time.time
    time.time = lambda: _now[0]
    try:
        pool = ConnectionPool(max_size=3)

        # Capacity: exactly 3 borrows succeed, the 4th and 5th are refused.
        conns = [pool.borrow_connection() for _ in range(5)]
        granted = [c for c in conns if c is not None]
        assert len(granted) == 3, f"max_size=3 pool granted {len(granted)}"
        assert conns[3] is None and conns[4] is None
        assert pool.in_use_count == 3 and pool.available_count == 0

        # Return two: they become available, not destroyed.
        ids_returned = {granted[0].id, granted[1].id}
        assert pool.return_connection(granted[0]) is True
        assert pool.return_connection(granted[1]) is True
        assert pool.available_count == 2 and pool.in_use_count == 1

        # Re-borrow REUSES the returned connections (same ids, no new builds).
        re1 = pool.borrow_connection()
        re2 = pool.borrow_connection()
        assert {re1.id, re2.id} == ids_returned, \
            f"pool built new connections instead of reusing {ids_returned}"

        # A connection the pool never lent (or already returned) is refused.
        foreign = Connection(999)
        assert pool.return_connection(foreign) is False, "foreign connection accepted"
        pool.return_connection(re1)
        assert pool.return_connection(re1) is False, "double return accepted"

        # AGE-OUT: at +31s every existing connection fails its health check.
        # Returning an aged connection must NOT put it back in the pool.
        _now[0] += 31
        aged_in_use = pool.in_use_count            # re2 + granted[2]
        assert pool.return_connection(re2) is True
        assert pool.available_count == 1, \
            "aged (unhealthy) connection was re-pooled on return"
        # ...and cleanup evicts the aged available one (re1) too.
        removed = pool.cleanup_unhealthy_connections()
        assert removed >= 1, f"cleanup found no unhealthy connections, removed {removed}"
        assert pool.available_count == 0, "unhealthy connection survived cleanup"

        # Fresh borrows still work after eviction (new connections built).
        fresh = pool.borrow_connection()
        assert fresh is not None and fresh.health_check() is True

        # close_all empties both sides.
        pool.close_all_connections()
        assert pool.available_count == 0 and pool.in_use_count == 0
    finally:
        time.time = _real_time

    print("connection_pool: 3/5 granted at cap, reuse by id, foreign+double "
          "returns refused, 31s age-out evicted, close_all clean — PASS")


if __name__ == "__main__":
    main()