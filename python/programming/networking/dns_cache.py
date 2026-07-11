# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import time
from typing import Dict, Optional, List, Tuple
from dataclasses import dataclass
from collections import OrderedDict


@dataclass
class Record:
    """DNS record data structure."""
    name: str
    record_type: str
    value: str
    ttl: int


class CacheEntry:
    """Represents a cached DNS entry with metadata."""
    
    def __init__(self, record: Optional[Record], is_negative: bool = False):
        self.record = record
        self.is_negative = is_negative
        self.timestamp = time.time()
        self.last_accessed = time.time()
    
    def is_expired(self) -> bool:
        """Check if the cache entry has expired based on TTL."""
        if self.is_negative:
            # Negative entries expire after 30 seconds by default
            return time.time() - self.timestamp > 30
        if self.record is None:
            return True
        return time.time() - self.timestamp > self.record.ttl
    
    def update_access_time(self) -> None:
        """Update the last accessed timestamp."""
        self.last_accessed = time.time()


class DNSCache:
    """LRU-based DNS cache with TTL support and negative caching."""
    
    def __init__(self, max_size: int = 100):
        if max_size <= 0:
            raise ValueError("max_size must be positive")
        self.max_size = max_size
        self._cache: OrderedDict[str, CacheEntry] = OrderedDict()
    
    def _evict_if_needed(self) -> None:
        """Remove the least recently used entry if cache is full."""
        while len(self._cache) >= self.max_size:
            self._cache.popitem(last=False)
    
    def _refresh_entry_position(self, key: str) -> None:
        """Move an entry to the end to mark it as recently used."""
        self._cache.move_to_end(key)
    
    def lookup(self, name: str, record_type: str) -> Optional[Record]:
        """
        Lookup a DNS record in the cache.
        
        Args:
            name: Domain name to lookup
            record_type: Type of DNS record (A, AAAA, etc.)
            
        Returns:
            Record if found and not expired, None otherwise
        """
        key = f"{name}:{record_type}"
        
        if key not in self._cache:
            return None
        
        entry = self._cache[key]
        entry.update_access_time()
        self._refresh_entry_position(key)
        
        if entry.is_expired():
            del self._cache[key]
            return None
            
        if entry.is_negative:
            return None
            
        return entry.record
    
    def insert(self, record: Record) -> None:
        """
        Insert a DNS record into the cache.
        
        Args:
            record: DNS record to cache
        """
        key = f"{record.name}:{record.record_type}"
        
        if key in self._cache:
            del self._cache[key]
        else:
            self._evict_if_needed()
            
        self._cache[key] = CacheEntry(record)
        self._refresh_entry_position(key)
    
    def insert_negative(self, name: str, record_type: str) -> None:
        """
        Insert a negative cache entry for a non-existent record.
        
        Args:
            name: Domain name that doesn't exist
            record_type: Type of DNS record that doesn't exist
        """
        key = f"{name}:{record_type}"
        
        if key in self._cache:
            del self._cache[key]
        else:
            self._evict_if_needed()
            
        self._cache[key] = CacheEntry(None, is_negative=True)
        self._refresh_entry_position(key)
    
    def clear_expired(self) -> int:
        """
        Remove all expired entries from the cache.
        
        Returns:
            Number of entries removed
        """
        expired_keys = [
            key for key, entry in self._cache.items() 
            if entry.is_expired()
        ]
        
        for key in expired_keys:
            del self._cache[key]
            
        return len(expired_keys)
    
    def size(self) -> int:
        """Return the current number of entries in the cache."""
        return len(self._cache)
    
    def clear(self) -> None:
        """Clear all entries from the cache."""
        self._cache.clear()


def main():
    """Self-test on a fake clock: TTL expiry exact, negative caching with its
    30s lifetime, (name,type) keying, LRU eviction, clear_expired count."""
    _now = [100_000.0]
    _real_time = time.time
    time.time = lambda: _now[0]
    try:
        cache = DNSCache(max_size=5)
        cache.insert(Record("example.com", "A", "93.184.216.34", 60))
        cache.insert(Record("google.com", "A", "142.250.74.110", 120))
        cache.insert(Record("example.com", "AAAA", "2606::1946", 60))
        assert cache.size() == 3

        # (name, type) are independent keys.
        assert cache.lookup("example.com", "A").value == "93.184.216.34"
        assert cache.lookup("example.com", "AAAA").value == "2606::1946"
        assert cache.lookup("example.com", "MX") is None
        assert cache.lookup("nonexistent.com", "A") is None

        # TTL: at +59s example/A (ttl 60) lives; at +61s it's gone,
        # while google/A (ttl 120) still answers.
        _now[0] += 59
        assert cache.lookup("example.com", "A") is not None, "record died before its TTL"
        _now[0] += 2
        assert cache.lookup("example.com", "A") is None, "record survived past its TTL"
        assert cache.lookup("google.com", "A") is not None, "longer TTL record wrongly expired"

        # Negative caching: remembered for 30s, then re-askable.
        cache.insert_negative("missing.com", "A")
        assert cache.lookup("missing.com", "A") is None
        neg_key = "missing.com:A"
        assert neg_key in cache._cache, "negative entry not stored"
        _now[0] += 31
        cache.clear_expired()
        assert neg_key not in cache._cache, "negative entry outlived its 30s window"

        # clear_expired reports the exact count.
        fresh = DNSCache(max_size=10)
        for i in range(4):
            fresh.insert(Record(f"h{i}.com", "A", f"1.1.1.{i}", 50))
        fresh.insert(Record("long.com", "A", "9.9.9.9", 500))
        _now[0] += 60
        removed = fresh.clear_expired()
        assert removed == 4, f"exactly 4 of 5 records expired, clear removed {removed}"
        assert fresh.size() == 1 and fresh.lookup("long.com", "A") is not None

        # LRU eviction: capacity 3, touch A so B is the eviction victim.
        lru = DNSCache(max_size=3)
        lru.insert(Record("a.com", "A", "1.0.0.1", 500))
        lru.insert(Record("b.com", "A", "1.0.0.2", 500))
        lru.insert(Record("c.com", "A", "1.0.0.3", 500))
        lru.lookup("a.com", "A")                       # refresh A
        lru.insert(Record("d.com", "A", "1.0.0.4", 500))
        assert lru.size() == 3, f"capacity-3 cache holds {lru.size()}"
        assert lru.lookup("b.com", "A") is None, "LRU victim should be the untouched b.com"
        assert lru.lookup("a.com", "A") is not None, "recently-used a.com was evicted"
        assert lru.lookup("d.com", "A") is not None

        # clear() empties.
        lru.clear()
        assert lru.size() == 0
    finally:
        time.time = _real_time

    print("dns_cache: TTL exact (59s alive/61s dead), negative 30s window, "
          "clear_expired 4/5, LRU evicted the right victim — PASS")


if __name__ == "__main__":
    main()