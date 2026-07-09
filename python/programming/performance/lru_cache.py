# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import time
import threading
from collections import OrderedDict
from typing import Any, Optional, Dict, Tuple
from dataclasses import dataclass

@dataclass
class CacheEntry:
    """Represents a cache entry with value and metadata."""
    value: Any
    timestamp: float
    ttl: Optional[float] = None

class TTLPolicy:
    """Time-to-live policy manager for cache entries."""
    
    @staticmethod
    def is_expired(entry: CacheEntry, current_time: float) -> bool:
        """Check if a cache entry has expired based on its TTL."""
        if entry.ttl is None:
            return False
        return current_time > (entry.timestamp + entry.ttl)
    
    @staticmethod
    def get_ttl_seconds(ttl: Optional[float]) -> Optional[float]:
        """Normalize TTL to seconds."""
        return ttl if ttl is None or ttl > 0 else None

class LRUCache:
    """LRU Cache implementation with TTL support."""
    
    def __init__(self, capacity: int = 100, default_ttl: Optional[float] = None):
        """
        Initialize the LRU cache.
        
        Args:
            capacity: Maximum number of items in cache
            default_ttl: Default time-to-live in seconds for entries (None means no expiration)
        """
        if capacity <= 0:
            raise ValueError("Capacity must be positive")
        
        self._capacity = capacity
        self._default_ttl = TTLPolicy.get_ttl_seconds(default_ttl)
        self._cache: OrderedDict[str, CacheEntry] = OrderedDict()
        self._lock = threading.RLock()
        self._ttl_policy = TTLPolicy()
    
    @property
    def capacity(self) -> int:
        """Get the cache capacity."""
        return self._capacity
    
    @property
    def size(self) -> int:
        """Get the current number of items in cache."""
        with self._lock:
            return len(self._cache)
    
    def get(self, key: str) -> Optional[Any]:
        """
        Get a value from the cache.
        
        Args:
            key: Cache key to retrieve
            
        Returns:
            Cached value or None if not found or expired
        """
        if not isinstance(key, str):
            raise TypeError("Key must be a string")
        
        current_time = time.time()
        
        with self._lock:
            if key not in self._cache:
                return None
            
            entry = self._cache[key]
            
            # Check if entry has expired
            if self._ttl_policy.is_expired(entry, current_time):
                del self._cache[key]
                return None
            
            # Move to end (mark as recently used)
            self._cache.move_to_end(key)
            return entry.value
    
    def put(self, key: str, value: Any, ttl: Optional[float] = None) -> None:
        """
        Put a value in the cache.
        
        Args:
            key: Cache key
            value: Value to cache
            ttl: Time-to-live in seconds (None uses default, 0 or negative means no expiration)
        """
        if not isinstance(key, str):
            raise TypeError("Key must be a string")
        
        current_time = time.time()
        effective_ttl = ttl if ttl is not None else self._default_ttl
        effective_ttl = TTLPolicy.get_ttl_seconds(effective_ttl)
        
        with self._lock:
            # Remove expired entries first
            self._remove_expired(current_time)
            
            # If key exists, remove it to update position
            if key in self._cache:
                del self._cache[key]
            # If at capacity, remove least recently used
            elif len(self._cache) >= self._capacity:
                self._cache.popitem(last=False)
            
            # Add new entry
            self._cache[key] = CacheEntry(value, current_time, effective_ttl)
            self._cache.move_to_end(key)
    
    def delete(self, key: str) -> bool:
        """
        Delete a key from the cache.
        
        Args:
            key: Key to delete
            
        Returns:
            True if key was deleted, False if not found
        """
        if not isinstance(key, str):
            raise TypeError("Key must be a string")
        
        with self._lock:
            if key in self._cache:
                del self._cache[key]
                return True
            return False
    
    def clear(self) -> None:
        """Clear all entries from the cache."""
        with self._lock:
            self._cache.clear()
    
    def keys(self) -> list:
        """Get all keys in the cache (does not remove expired entries)."""
        with self._lock:
            return list(self._cache.keys())
    
    def _remove_expired(self, current_time: float) -> None:
        """Remove expired entries from the cache."""
        expired_keys = [
            key for key, entry in self._cache.items()
            if self._ttl_policy.is_expired(entry, current_time)
        ]
        
        for key in expired_keys:
            del self._cache[key]

def _worker(cache: LRUCache, worker_id: int, results: Dict[int, list]) -> None:
    """Worker function for concurrent access testing."""
    results[worker_id] = []
    
    # Put some values
    for i in range(5):
        key = f"worker{worker_id}_key{i}"
        cache.put(key, f"value_{worker_id}_{i}", ttl=2.0)
        results[worker_id].append(f"Put {key}")
    
    # Get some values
    for i in range(3):
        key = f"worker{worker_id}_key{i}"
        value = cache.get(key)
        results[worker_id].append(f"Got {key}: {value}")
    
    # Let some entries expire
    time.sleep(1.1)
    
    # Try to get expired values
    for i in range(5):
        key = f"worker{worker_id}_key{i}"
        value = cache.get(key)
        results[worker_id].append(f"Got {key} after sleep: {value}")

if __name__ == "__main__":
    # Basic usage demo
    print("=== LRU Cache with TTL Demo ===")
    
    # Create cache with capacity 3 and default TTL of 1 second
    cache = LRUCache(capacity=3, default_ttl=1.0)
    
    print(f"Cache capacity: {cache.capacity}")
    
    # Add some items
    cache.put("key1", "value1")
    cache.put("key2", "value2", ttl=0.5)  # Shorter TTL
    cache.put("key3", "value3")
    cache.put("key4", "value4")  # This should evict key1 (LRU)
    
    print(f"Cache size after 4 inserts: {cache.size}")
    print(f"Keys in cache: {cache.keys()}")
    
    # Retrieve items
    print(f"Get key1 (should be None, evicted): {cache.get('key1')}")
    print(f"Get key2: {cache.get('key2')}")
    print(f"Get key3: {cache.get('key3')}")
    print(f"Get key4: {cache.get('key4')}")
    
    # Wait for key2 to expire
    print("Waiting for key2 to expire (0.5s)...")
    time.sleep(0.6)
    
    print(f"Get key2 after expiration (should be None): {cache.get('key2')}")
    
    # Test capacity eviction
    cache.put("key5", "value5")
    cache.put("key6", "value6")
    print(f"Cache size after 2 more inserts: {cache.size}")
    print(f"Keys in cache: {cache.keys()}")
    print(f"Get key3 (should be None, evicted by capacity): {cache.get('key3')}")
    
    # Concurrent access demo
    print("\n=== Concurrent Access Demo ===")
    concurrent_cache = LRUCache(capacity=10)
    
    threads = []
    results: Dict[int, list] = {}
    
    # Start 3 worker threads
    for i in range(3):
        thread = threading.Thread(target=_worker, args=(concurrent_cache, i, results))
        threads.append(thread)
        thread.start()
    
    # Wait for all threads to complete
    for thread in threads:
        thread.join()
    
    # Print results
    for worker_id, worker_results in results.items():
        print(f"Worker {worker_id} results:")
        for result in worker_results:
            print(f"  {result}")
    
    print(f"Final cache size: {concurrent_cache.size}")
    print(f"Final cache keys: {concurrent_cache.keys()}")
    
    print("\n=== Demo completed ===")