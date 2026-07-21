"""
Count-Min Sketch for Frequency Estimation

Core idea: A streaming data structure using hash functions to estimate item frequencies
with bounded error. Memory-efficient alternative to exact counts.

When to use: You have a massive stream and need approximate frequency estimates with
formal error bounds, especially for detecting heavy hitters.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import random
import hashlib
from typing import List, Tuple


class CountMinSketch:
    """
    Count-Min Sketch: 2D array with multiple hash functions.
    Supports increment and query operations with bounded error.
    """

    def __init__(self, width: int = 100, depth: int = 5, epsilon: float = 0.01):
        self.width = width
        self.depth = depth
        self.epsilon = epsilon
        self.table = [[0] * width for _ in range(depth)]
        self.seeds = [42 + i for i in range(depth)]

    def _hash(self, item: str, seed: int) -> int:
        """Hash item to an index in [0, width)."""
        h = hashlib.md5(f"{seed}{item}".encode()).hexdigest()
        return int(h, 16) % self.width

    def increment(self, item: str, count: int = 1) -> None:
        """Increment count for item in all hash functions."""
        for d in range(self.depth):
            idx = self._hash(item, self.seeds[d])
            self.table[d][idx] += count

    def query(self, item: str) -> int:
        """Estimate count for item (returns minimum across hash functions)."""
        estimates = []
        for d in range(self.depth):
            idx = self._hash(item, self.seeds[d])
            estimates.append(self.table[d][idx])
        return min(estimates)

    def find_heavy_hitters(self, candidates: List[str], threshold: int) -> List[str]:
        """Return candidate ITEMS whose estimated count is >= threshold.

        A Count-Min Sketch is keyless — it stores no item names, only hashed counts —
        so heavy-hitter detection must be given the set of candidate items to query.
        (The previous version scanned raw cell COUNTS and returned integers, not items.)
        """
        return sorted(c for c in candidates if self.query(c) >= threshold)


if __name__ == "__main__":
    random.seed(42)

    # Create stream with planted heavy hitters
    stream = []

    # Heavy hitter 1: "cat" appears 50 times
    for _ in range(50):
        stream.append("cat")

    # Heavy hitter 2: "dog" appears 40 times
    for _ in range(40):
        stream.append("dog")

    # Light items: scattered items with low frequency
    light_items = ["bird", "fish", "lion", "tiger", "ant", "bee", "fox", "owl"]
    for item in light_items:
        for _ in range(random.randint(1, 5)):
            stream.append(item)

    # Shuffle stream
    random.shuffle(stream)

    # Process stream
    sketch = CountMinSketch(width=100, depth=5)
    for item in stream:
        sketch.increment(item)

    # Query estimates
    cat_est = sketch.query("cat")
    dog_est = sketch.query("dog")

    print(f"Estimate for 'cat' (true 50): {cat_est}")
    print(f"Estimate for 'dog' (true 40): {dog_est}")

    # The sketch provides upper bounds: estimate >= true count
    # Assertion: estimates are within bounds (no under-counting)
    assert cat_est >= 50, f"Estimate should not under-count: {cat_est} < 50"
    assert dog_est >= 40, f"Estimate should not under-count: {dog_est} < 40"

    # Verify epsilon error bound (rough check)
    total_stream = len(stream)
    max_allowed_error = int(sketch.epsilon * total_stream) + 5  # Allow some slack
    assert cat_est - 50 <= max_allowed_error, f"Error too large: {cat_est - 50}"

    # Heavy-hitter detection: CMS is keyless, so we pass the candidate items to query.
    all_items = ["cat", "dog"] + light_items
    heavy = sketch.find_heavy_hitters(all_items, threshold=30)
    print(f"Heavy hitters (>=30): {heavy}")
    assert set(heavy) == {"cat", "dog"}, f"Expected {{cat, dog}}, got {heavy}"

    print("✓ Count-Min Sketch: PASS")
