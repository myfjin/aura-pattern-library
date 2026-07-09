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
    """Demo the connection pool functionality."""
    print("=== Connection Pool Demo ===")
    
    # Create a pool with max size of 3
    pool = ConnectionPool(max_size=3)
    print(f"Created pool with max size: {pool.max_size}")
    
    # Borrow connections
    connections = []
    for i in range(5):  # Try to borrow 5 connections
        conn = pool.borrow_connection()
        if conn:
            connections.append(conn)
            print(f"Borrowed {conn}")
        else:
            print(f"Failed to borrow connection {i+1} - pool at capacity")
    
    print(f"Pool status: {pool.available_count} available, {pool.in_use_count} in use")
    
    # Return some connections
    for i in range(2):
        if connections:
            conn = connections.pop()
            pool.return_connection(conn)
            print(f"Returned {conn}")
    
    print(f"Pool status: {pool.available_count} available, {pool.in_use_count} in use")
    
    # Borrow more connections (should succeed now)
    for i in range(2):
        conn = pool.borrow_connection()
        if conn:
            connections.append(conn)
            print(f"Borrowed {conn}")
    
    print(f"Pool status: {pool.available_count} available, {pool.in_use_count} in use")
    
    # Cleanup demo
    removed = pool.cleanup_unhealthy_connections()
    print(f"Cleaned up {removed} unhealthy connections")
    
    # Return all remaining connections
    while connections:
        conn = connections.pop()
        pool.return_connection(conn)
        print(f"Returned {conn}")
    
    print(f"Final pool status: {pool.available_count} available, {pool.in_use_count} in use")
    print("=== Demo Complete ===")


if __name__ == "__main__":
    main()