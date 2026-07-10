#!/usr/bin/env python3
"""sliding_aggregate: compute rolling aggregates (sum, avg, min, max)."""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import sys

class SlidingWindow:
    """Sliding window for rolling aggregates."""
    def __init__(self, window_size):
        self.window_size = window_size
        self.values = []

    def add(self, value):
        """Add value to window."""
        self.values.append(value)
        # Keep only last window_size values
        if len(self.values) > self.window_size:
            self.values.pop(0)

    def sum(self):
        """Get sum of values in window."""
        return sum(self.values)

    def average(self):
        """Get average of values in window."""
        if not self.values:
            return 0
        return sum(self.values) / len(self.values)

    def min(self):
        """Get minimum value in window."""
        if not self.values:
            return 0
        return min(self.values)

    def max(self):
        """Get maximum value in window."""
        if not self.values:
            return 0
        return max(self.values)

    def count(self):
        """Get number of values in window."""
        return len(self.values)

def test_sliding_aggregate():
    """Test: known sequence, verify sum/avg/min/max over window."""
    # Test 1: rolling sum with window=3
    window = SlidingWindow(window_size=3)

    # Add values: 1, 2, 3, 4, 5
    # After adding each:
    # [1]: sum=1
    # [1,2]: sum=3
    # [1,2,3]: sum=6 (window full)
    # [2,3,4]: sum=9 (1 dropped)
    # [3,4,5]: sum=12 (2 dropped)

    window.add(1)
    assert window.sum() == 1, f"Sum should be 1, got {window.sum()}"

    window.add(2)
    assert window.sum() == 3, f"Sum should be 3, got {window.sum()}"

    window.add(3)
    assert window.sum() == 6, f"Sum should be 6, got {window.sum()}"

    window.add(4)
    assert window.sum() == 9, f"Sum should be 9 (2+3+4), got {window.sum()}"

    window.add(5)
    assert window.sum() == 12, f"Sum should be 12 (3+4+5), got {window.sum()}"

    # Test 2: rolling average
    window_avg = SlidingWindow(window_size=4)

    window_avg.add(10)
    assert window_avg.average() == 10, f"Average should be 10, got {window_avg.average()}"

    window_avg.add(20)
    assert window_avg.average() == 15, f"Average should be 15, got {window_avg.average()}"

    window_avg.add(30)
    assert window_avg.average() == 20, f"Average should be 20, got {window_avg.average()}"

    window_avg.add(40)
    assert window_avg.average() == 25, f"Average should be 25 (10+20+30+40)/4, got {window_avg.average()}"

    window_avg.add(50)
    assert window_avg.average() == 35, f"Average should be 35 (20+30+40+50)/4, got {window_avg.average()}"

    # Test 3: rolling min/max
    window_minmax = SlidingWindow(window_size=3)

    values_seq = [5, 2, 8, 1, 9]
    for v in values_seq:
        window_minmax.add(v)

    # After adding all:
    # window = [1, 9] (last 3 are [1, 9] after dropping 8)
    # Actually: [8, 1, 9] are the last 3 values
    # min=1, max=9

    assert window_minmax.min() == 1, f"Min should be 1, got {window_minmax.min()}"
    assert window_minmax.max() == 9, f"Max should be 9, got {window_minmax.max()}"

    # Test 4: window size 1
    window_single = SlidingWindow(window_size=1)

    window_single.add(42)
    assert window_single.sum() == 42
    assert window_single.average() == 42
    assert window_single.min() == 42
    assert window_single.max() == 42

    window_single.add(100)
    assert window_single.sum() == 100, "Only newest value kept in size-1 window"
    assert window_single.average() == 100
    assert window_single.min() == 100
    assert window_single.max() == 100

    # Test 5: large window (no dropping)
    window_large = SlidingWindow(window_size=1000)

    for i in range(1, 11):
        window_large.add(i)

    assert window_large.count() == 10, f"Should have 10 values, got {window_large.count()}"
    assert window_large.sum() == 55, f"Sum of 1-10 should be 55, got {window_large.sum()}"
    assert window_large.average() == 5.5, f"Average of 1-10 should be 5.5, got {window_large.average()}"
    assert window_large.min() == 1, f"Min should be 1, got {window_large.min()}"
    assert window_large.max() == 10, f"Max should be 10, got {window_large.max()}"

    # Test 6: verify exactly 3 values in window at boundary
    window_boundary = SlidingWindow(window_size=3)
    for i in range(1, 6):
        window_boundary.add(i)
        if i >= 3:
            assert window_boundary.count() == 3, f"Window should have exactly 3 values after adding {i}"

if __name__ == "__main__":
    test_sliding_aggregate()
    print("✓ sliding_aggregate passed")
