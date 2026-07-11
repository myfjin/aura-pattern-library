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

if __name__ == "__main__":
    # Self-test: LRU eviction order, recency-on-get, TTL expiry on a fake clock,
    # type/capacity enforcement, and thread-safety under real contention.
    _now = [10_000.0]
    _real_time = time.time
    time.time = lambda: _now[0]
    try:
        cache = LRUCache(capacity=3)

        # Fill to capacity, then overflow: the LEAST recently used key must go.
        cache.put("k1", "v1")
        cache.put("k2", "v2")
        cache.put("k3", "v3")
        cache.put("k4", "v4")                     # evicts k1
        assert cache.size == 3, f"capacity-3 cache holds {cache.size}"
        assert cache.get("k1") is None, "k1 survived eviction at capacity"
        assert cache.get("k2") == "v2"

        # THE FAILURE the pattern exists to prevent: get() must refresh recency.
        # k2 was just read, so inserting k5 must evict k3 (now the LRU), not k2.
        cache.put("k5", "v5")
        assert cache.get("k3") is None, "recency not updated on get: k3 should have been evicted"
        assert cache.get("k2") == "v2", "recently-read k2 was wrongly evicted"

        # TTL expiry, driven by the fake clock, not sleeps.
        cache.put("short", "s", ttl=0.5)
        assert cache.get("short") == "s"
        _now[0] += 0.6
        assert cache.get("short") is None, "entry readable 0.6s past a 0.5s TTL"
        # ttl=None with default_ttl=None means no expiration, ever.
        cache.put("forever", "f")
        _now[0] += 1_000_000.0
        assert cache.get("forever") == "f", "no-TTL entry expired"

        # delete() reports what it did.
        assert cache.delete("forever") is True
        assert cache.delete("forever") is False, "double delete reported success"

        # Invalid usage is refused.
        try:
            LRUCache(capacity=0)
            assert False, "capacity=0 accepted"
        except ValueError:
            pass
        try:
            cache.get(42)  # type: ignore[arg-type]
            assert False, "non-string key accepted"
        except TypeError:
            pass
    finally:
        time.time = _real_time

    # Real contention: 8 threads × 50 distinct keys into a capacity-400 cache.
    # Every write must survive (no lost updates, no corruption, exact final size).
    big = LRUCache(capacity=400)
    def _hammer(wid: int) -> None:
        for i in range(50):
            big.put(f"w{wid}_k{i}", wid * 1000 + i)
    threads = [threading.Thread(target=_hammer, args=(w,)) for w in range(8)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    assert big.size == 400, f"8x50 distinct puts into capacity 400 left size {big.size}"
    for w in range(8):
        for i in range(50):
            got = big.get(f"w{w}_k{i}")
            assert got == w * 1000 + i, f"lost/corrupt entry w{w}_k{i}: {got}"

    print("lru_cache: LRU order held, get-refreshes-recency, TTL on fake clock, "
          "400/400 concurrent entries intact — PASS")