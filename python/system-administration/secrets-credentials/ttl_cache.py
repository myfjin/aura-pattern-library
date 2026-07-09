"""TTL cache: expire items based on logical clock TTL, not wall-clock.
Failure simulated: cache item at clock=0 with TTL=100; access at clock=50 (hit),
then clock=150 (miss/expired). Assert hit/miss based on logical time only.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import json

class LogicalClock:
    """Logical timestamp holder for deterministic TTL checks."""
    def __init__(self):
        self.now = 0

    def advance(self, delta):
        self.now += delta

    def current(self):
        return self.now

def ttl_cache(ttl_seconds=100, clock=None):
    """Cache with time-to-live expiry based on logical clock."""
    if clock is None:
        clock = LogicalClock()

    class TTLCache:
        def __init__(self, ttl, clk):
            self.ttl = ttl
            self.clock = clk
            self.cache = {}  # key -> (value, insertion_time)

        def set(self, key, value):
            """Store value with current logical time."""
            self.cache[key] = (value, self.clock.current())

        def get(self, key):
            """Retrieve value if not expired, else return None."""
            if key not in self.cache:
                return None
            value, insertion_time = self.cache[key]
            age = self.clock.current() - insertion_time
            if age > self.ttl:
                # Expired
                del self.cache[key]
                return None
            return value

        def size(self):
            """Return count of non-expired items."""
            return len(self.cache)

    return TTLCache(ttl_seconds, clock)

if __name__ == "__main__":
    import random
    random.seed(42)

    clock = LogicalClock()
    cache = ttl_cache(ttl_seconds=100, clock=clock)

    # Store item at clock=0
    cache.set("key1", "value1")
    cache.set("key2", "value2")

    # CHECK 1: at clock=50, both items should be cached
    clock.advance(50)
    result1 = cache.get("key1")
    assert result1 == "value1", f"Expected 'value1' at clock=50, got {result1}"
    result2 = cache.get("key2")
    assert result2 == "value2", f"Expected 'value2' at clock=50, got {result2}"

    # CHECK 2: at clock=100 (exactly at TTL boundary), still cached
    clock.advance(50)  # now clock = 100
    result3 = cache.get("key1")
    assert result3 == "value1", f"Expected 'value1' at clock=100 (boundary), got {result3}"

    # CHECK 3: at clock=101, items are expired
    clock.advance(1)  # now clock = 101
    result4 = cache.get("key1")
    assert result4 is None, f"Expected None (expired) at clock=101, got {result4}"
    result5 = cache.get("key2")
    assert result5 is None, f"Expected None (expired) at clock=101, got {result5}"

    # CHECK 4: cache size is 0 after expiry
    size = cache.size()
    assert size == 0, f"Expected cache size 0, got {size}"

    # CHECK 5: storing new item at clock=101 (after expiry)
    cache.set("key3", "value3")
    result6 = cache.get("key3")
    assert result6 == "value3", f"Expected 'value3' from fresh item, got {result6}"

    # CHECK 6: determinism - replay clock from start
    clock2 = LogicalClock()
    cache2 = ttl_cache(ttl_seconds=100, clock=clock2)
    cache2.set("key_test", "value_test")
    clock2.advance(50)
    result7 = cache2.get("key_test")
    assert result7 == "value_test", "Replay should match: logical clock is deterministic"

    print("ttl_cache PASS")
