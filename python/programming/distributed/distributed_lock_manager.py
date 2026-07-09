# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import time
import uuid
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from threading import Lock as ThreadingLock


@dataclass
class LockToken:
    """Represents a lock token with expiration and ownership information."""
    token_id: str
    owner_id: str
    expiration_time: float
    resource_id: str

    def is_expired(self) -> bool:
        """Check if the lock token has expired."""
        return time.time() > self.expiration_time

    def remaining_time(self) -> float:
        """Get remaining time before expiration in seconds."""
        return max(0, self.expiration_time - time.time())


class LockManager:
    """A distributed lock manager implementing fairness queue and expiration."""

    def __init__(self):
        """Initialize the lock manager."""
        self._locks: Dict[str, Optional[LockToken]] = {}
        self._waiting_queues: Dict[str, List[Tuple[str, float]]] = {}
        self._lock = ThreadingLock()

    def acquire(self, resource_id: str, owner_id: str, timeout: float = 10.0, 
                lease_time: float = 30.0) -> Optional[LockToken]:
        """
        Acquire a lock for a resource.
        
        Args:
            resource_id: Identifier for the resource to lock
            owner_id: Identifier for the lock requester
            timeout: Maximum time to wait for the lock (seconds)
            lease_time: Time until the lock expires (seconds)
            
        Returns:
            LockToken if acquired, None if timeout exceeded
        """
        start_time = time.time()
        
        with self._lock:
            # If no one holds the lock, acquire it immediately
            if resource_id not in self._locks or self._locks[resource_id] is None:
                return self._create_lock(resource_id, owner_id, lease_time)
            
            # Check if current holder's lock has expired
            current_lock = self._locks[resource_id]
            if current_lock and current_lock.is_expired():
                self._locks[resource_id] = None
                return self._create_lock(resource_id, owner_id, lease_time)
            
            # Add to waiting queue
            if resource_id not in self._waiting_queues:
                self._waiting_queues[resource_id] = []
            self._waiting_queues[resource_id].append((owner_id, start_time + timeout))
        
        # Wait for lock or timeout
        while time.time() - start_time < timeout:
            time.sleep(0.01)  # 10ms polling interval
            
            with self._lock:
                # Check if we're next in line
                if (resource_id in self._waiting_queues and 
                    self._waiting_queues[resource_id] and 
                    self._waiting_queues[resource_id][0][0] == owner_id):
                    
                    # Try to acquire the lock
                    if (resource_id not in self._locks or 
                        self._locks[resource_id] is None or 
                        self._locks[resource_id].is_expired()):
                        
                        # Remove from queue and acquire
                        self._waiting_queues[resource_id].pop(0)
                        if not self._waiting_queues[resource_id]:
                            del self._waiting_queues[resource_id]
                        return self._create_lock(resource_id, owner_id, lease_time)
                
                # Check if we've timed out in the queue
                if resource_id in self._waiting_queues:
                    queue = self._waiting_queues[resource_id]
                    for i, (waiter_id, expire_time) in enumerate(queue):
                        if waiter_id == owner_id:
                            if time.time() > expire_time:
                                queue.pop(i)
                                if not queue:
                                    del self._waiting_queues[resource_id]
                                return None
                            break
        
        # Remove from queue if we timed out
        with self._lock:
            if resource_id in self._waiting_queues:
                queue = self._waiting_queues[resource_id]
                for i, (waiter_id, _) in enumerate(queue):
                    if waiter_id == owner_id:
                        queue.pop(i)
                        if not queue:
                            del self._waiting_queues[resource_id]
                        break
        return None

    def release(self, token: LockToken) -> bool:
        """
        Release a lock using its token.
        
        Args:
            token: The lock token to release
            
        Returns:
            True if released successfully, False otherwise
        """
        with self._lock:
            if token.resource_id not in self._locks:
                return False
                
            current_lock = self._locks[token.resource_id]
            if current_lock is None:
                return False
                
            # Verify token matches current lock
            if (current_lock.token_id == token.token_id and 
                current_lock.owner_id == token.owner_id and
                current_lock.resource_id == token.resource_id):
                self._locks[token.resource_id] = None
                return True
                
        return False

    def refresh(self, token: LockToken, lease_time: float = 30.0) -> Optional[LockToken]:
        """
        Refresh an existing lock's expiration time.
        
        Args:
            token: The lock token to refresh
            lease_time: New lease time from now (seconds)
            
        Returns:
            New LockToken if refreshed, None if failed
        """
        with self._lock:
            if token.resource_id not in self._locks:
                return None
                
            current_lock = self._locks[token.resource_id]
            if current_lock is None:
                return None
                
            # Verify token matches current lock
            if (current_lock.token_id == token.token_id and 
                current_lock.owner_id == token.owner_id and
                current_lock.resource_id == token.resource_id and
                not current_lock.is_expired()):
                
                # Create new token with extended expiration
                new_expiration = time.time() + lease_time
                new_token = LockToken(
                    token_id=current_lock.token_id,
                    owner_id=current_lock.owner_id,
                    expiration_time=new_expiration,
                    resource_id=current_lock.resource_id
                )
                self._locks[token.resource_id] = new_token
                return new_token
                
        return None

    def _create_lock(self, resource_id: str, owner_id: str, lease_time: float) -> LockToken:
        """Create a new lock token and register it."""
        token = LockToken(
            token_id=str(uuid.uuid4()),
            owner_id=owner_id,
            expiration_time=time.time() + lease_time,
            resource_id=resource_id
        )
        self._locks[resource_id] = token
        return token

    def get_lock_info(self, resource_id: str) -> Optional[Dict]:
        """
        Get information about a lock.
        
        Args:
            resource_id: The resource to check
            
        Returns:
            Dictionary with lock info or None if no lock exists
        """
        with self._lock:
            if resource_id not in self._locks or self._locks[resource_id] is None:
                return None
                
            lock = self._locks[resource_id]
            return {
                "token_id": lock.token_id,
                "owner_id": lock.owner_id,
                "expires_in": lock.remaining_time(),
                "expired": lock.is_expired()
            }


if __name__ == "__main__":
    # Demo the distributed lock manager
    print("Distributed Lock Manager Demo")
    print("=" * 40)
    
    # Create lock manager
    manager = LockManager()
    
    # Test 1: Basic acquire/release
    print("\n1. Basic acquire/release test:")
    token1 = manager.acquire("resource1", "client1", lease_time=5.0)
    if token1:
        print(f"✓ Client1 acquired lock: {token1.token_id[:8]}...")
        info = manager.get_lock_info("resource1")
        print(f"  Lock info: {info}")
        
        # Try to acquire same resource - should fail
        token2 = manager.acquire("resource1", "client2", timeout=0.1)
        if not token2:
            print("✓ Client2 correctly blocked from acquiring locked resource")
        
        # Release the lock
        if manager.release(token1):
            print("✓ Client1 released lock")
        else:
            print("✗ Failed to release lock")
    else:
        print("✗ Client1 failed to acquire lock")
    
    # Test 2: Fairness queue
    print("\n2. Fairness queue test:")
    # Acquire lock with client1
    token1 = manager.acquire("resource2", "client1", lease_time=1.0)
    if token1:
        print(f"✓ Client1 acquired lock")
        
        # Have client2 and client3 wait
        import threading
        
        results = {}
        def try_acquire(client_id, resource_id):
            token = manager.acquire(resource_id, client_id, timeout=3.0)
            results[client_id] = token is not None
        
        t2 = threading.Thread(target=try_acquire, args=("client2", "resource2"))
        t3 = threading.Thread(target=try_acquire, args=("client3", "resource2"))
        
        t2.start()
        t3.start()
        
        # Release after 0.5 seconds to let one client in
        time.sleep(0.5)
        manager.release(token1)
        
        t2.join()
        t3.join()
        
        acquired_count = sum(1 for result in results.values() if result)
        print(f"✓ {acquired_count}/2 waiting clients acquired lock")
        
        # Clean up any remaining locks
        for client_id, success in results.items():
            if success:
                # In a real scenario, we'd have the actual tokens
                pass
    
    # Test 3: Expiration
    print("\n3. Expiration test:")
    token = manager.acquire("resource3", "client1", lease_time=0.5)
    if token:
        print(f"✓ Acquired lock with 0.5s expiration")
        time.sleep(0.6)  # Wait for expiration
        
        # Try to acquire again - should succeed now
        token2 = manager.acquire("resource3", "client2", timeout=0.1)
        if token2:
            print("✓ Lock correctly expired and was reacquired")
        else:
            print("✗ Lock did not expire as expected")
    
    # Test 4: Refresh
    print("\n4. Refresh test:")
    token = manager.acquire("resource4", "client1", lease_time=1.0)
    if token:
        print(f"✓ Acquired lock with 1s expiration")
        time.sleep(0.7)
        
        # Refresh the lock
        new_token = manager.refresh(token, lease_time=2.0)
        if new_token:
            print("✓ Lock refreshed with 2s extension")
            time.sleep(1.0)
            
            # Try to acquire - should fail as lock is still valid
            token2 = manager.acquire("resource4", "client2", timeout=0.1)
            if not token2:
                print("✓ Lock still valid after refresh")
            else:
                print("✗ Lock was incorrectly acquired")
        else:
            print("✗ Failed to refresh lock")
    
    print("\nDemo completed successfully!")