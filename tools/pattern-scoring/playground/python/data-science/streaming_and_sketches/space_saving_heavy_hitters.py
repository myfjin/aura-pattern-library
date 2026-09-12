"""
Space-Saving Algorithm for Top-K Heavy Hitters

Core idea: Maintain exactly k counters for the top-k most frequent items seen so far.
When a new item arrives, either increment an existing counter or replace the smallest one.

When to use: You need the top-k most frequent items from a stream with minimal memory
(only k counters, not a full frequency table).
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import random
from typing import List, Tuple, Dict


class SpaceSavingTopK:
    """Space-Saving algorithm for maintaining top-k heavy hitters."""

    def __init__(self, k: int = 5):
        self.k = k
        self.counters: Dict[str, int] = {}  # item -> count (may overestimate)

    def process(self, item: str) -> None:
        """Process a new item. The defining Space-Saving move: when full, the
        minimum-count item is ALWAYS evicted and the newcomer INHERITS min+1 —
        the inherited count is the overestimate that keeps a late-arriving
        heavy hitter from being starved out. (Dropping newcomers instead
        degenerates to 'first k distinct items win', which is not the
        algorithm at all.)"""
        if item in self.counters:
            self.counters[item] += 1
        elif len(self.counters) < self.k:
            self.counters[item] = 1
        else:
            min_item = min(self.counters, key=self.counters.get)
            min_count = self.counters[min_item]
            del self.counters[min_item]
            self.counters[item] = min_count + 1

    def get_top_k(self) -> List[Tuple[str, int]]:
        """Return top-k items sorted by count."""
        return sorted(self.counters.items(), key=lambda x: x[1], reverse=True)


if __name__ == "__main__":
    random.seed(42)

    # Simulate a Zipfian stream: some items are very frequent, others rare
    # Zipf distribution: P(i) ~ 1/i^alpha
    items = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew"]

    stream = []
    # Generate stream following rough Zipf: item 0 appears ~100 times, item 1 ~50 times, etc.
    for i, item in enumerate(items):
        freq = max(1, 100 // (i + 1))  # Zipf-like: 1/i
        for _ in range(freq):
            stream.append(item)

    # Shuffle
    random.shuffle(stream)

    # Space-Saving with HEADROOM: the top-k guarantee needs counters >> k of
    # interest (with counters == k, tail churn erodes the summary).
    m = 6                        # counters, for a top-3 query over 8 items
    ss = SpaceSavingTopK(k=m)
    for item in stream:
        ss.process(item)

    top3 = ss.get_top_k()[:3]
    print(f"Stream length: {len(stream)} · counters: {m}")
    print(f"Top-3 (Space-Saving): {top3}")

    # Exact counts for ground truth
    exact_counts = {}
    for item in stream:
        exact_counts[item] = exact_counts.get(item, 0) + 1
    exact_top3 = sorted(exact_counts.items(), key=lambda x: x[1], reverse=True)[:3]
    print(f"Top-3 (exact):        {exact_top3}")

    # The claimed quantity, measured: the FULL top-3 recovered — identities
    # AND order — with every estimate inside the Space-Saving bound:
    # exact <= estimate <= exact + N/m.
    err_bound = len(stream) / m
    for rank in range(3):
        est_id, est_cnt = top3[rank]
        tru_id, tru_cnt = exact_top3[rank]
        assert est_id == tru_id, \
            f"rank {rank+1} identity should match: {est_id} vs {tru_id}"
        assert tru_cnt <= est_cnt <= tru_cnt + err_bound, \
            f"rank {rank+1} estimate outside bound: {est_cnt} vs {tru_cnt} (+{err_bound:.0f})"

    print("✓ Space-Saving Heavy Hitters: PASS")
