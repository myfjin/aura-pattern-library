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
    """Demonstrate DNS cache functionality."""
    print("DNS Cache Simulator Demo")
    print("=" * 30)
    
    # Create cache
    cache = DNSCache(max_size=5)
    
    # Insert some records
    records = [
        Record("example.com", "A", "93.184.216.34", 60),
        Record("google.com", "A", "142.250.74.110", 120),
        Record("github.com", "A", "140.82.114.3", 90),
        Record("example.com", "AAAA", "2606:2800:220:1:248:1893:25c8:1946", 60),
    ]
    
    print("Inserting records...")
    for record in records:
        cache.insert(record)
        print(f"  Inserted: {record.name} {record.record_type} -> {record.value}")
    
    print(f"\nCache size: {cache.size()}")
    
    # Lookup existing records
    print("\nLooking up records...")
    lookups = [
        ("example.com", "A"),
        ("google.com", "A"),
        ("nonexistent.com", "A"),
    ]
    
    for name, rtype in lookups:
        result = cache.lookup(name, rtype)
        if result:
            print(f"  Found: {name} {rtype} -> {result.value}")
        else:
            print(f"  Not found: {name} {rtype}")
            cache.insert_negative(name, rtype)
    
    print(f"\nCache size after negative caching: {cache.size()}")
    
    # Test LRU eviction
    print("\nTesting LRU eviction...")
    for i in range(3):
        record = Record(f"test{i}.com", "A", f"1.1.1.{i}", 300)
        cache.insert(record)
        print(f"  Inserted: {record.name}")
    
    print(f"Cache size: {cache.size()}")
    print("Current cache contents:")
    for key in cache._cache:
        print(f"  {key}")
    
    # Test cache clearing
    print("\nClearing expired entries...")
    removed = cache.clear_expired()
    print(f"Removed {removed} expired entries")
    print(f"Cache size: {cache.size()}")
    
    # Clear entire cache
    print("\nClearing entire cache...")
    cache.clear()
    print(f"Cache size: {cache.size()}")
    print("Demo completed successfully!")


if __name__ == "__main__":
    main()