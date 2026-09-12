#!/usr/bin/env python3
"""rate_calc: calculate rate (e.g., requests per second) from counter."""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import sys

class RateCalculator:
    """Calculate rate of change from counter values."""
    def __init__(self, window_size_seconds=60):
        self.window_size = window_size_seconds
        self.observations = []  # List of (timestamp, counter_value)

    def observe(self, timestamp, counter_value):
        """Record counter value at timestamp."""
        self.observations.append((timestamp, counter_value))

    def calculate_rate(self, current_timestamp):
        """Calculate rate for the current window (per second)."""
        # Find observations within window
        window_start = current_timestamp - self.window_size

        relevant = [(ts, val) for ts, val in self.observations if ts >= window_start]

        if len(relevant) < 2:
            return 0.0  # Not enough data

        # Get first and last value in window
        first_ts, first_val = relevant[0]
        last_ts, last_val = relevant[-1]

        if last_ts == first_ts:
            return 0.0  # No time elapsed

        delta_counter = last_val - first_val
        delta_time = last_ts - first_ts

        # Rate per second
        if delta_time > 0:
            return delta_counter / delta_time
        else:
            return 0.0

def test_rate_calc():
    """Test: feed known counter values, calculate exact rate."""
    # Test 1: constant rate
    calculator = RateCalculator(window_size_seconds=60)

    # Simulate counter incrementing at 100 per second
    # t=0s: counter=0
    # t=10s: counter=1000 (100 per second * 10s)
    # t=20s: counter=2000
    # t=30s: counter=3000
    # Rate should be 100 per second

    calculator.observe(0, 0)
    calculator.observe(10, 1000)
    calculator.observe(20, 2000)
    calculator.observe(30, 3000)

    rate_at_30 = calculator.calculate_rate(30)
    assert rate_at_30 == 100.0, f"Rate should be 100 per second, got {rate_at_30}"

    # Test 2: varying rate
    calculator2 = RateCalculator(window_size_seconds=15)

    # t=0s: counter=0
    # t=10s: counter=500 (50 per second * 10s)
    # t=20s: counter=1500 (100 per second * 10s)
    # With window=15s at t=20s: window starts at t=5s
    # Only observations t=10 and t=20 are in window
    # Rate = (1500 - 500) / (20 - 10) = 1000 / 10 = 100

    calculator2.observe(0, 0)
    calculator2.observe(10, 500)
    calculator2.observe(20, 1500)

    rate_10_to_20 = calculator2.calculate_rate(20)
    assert rate_10_to_20 == 100.0, f"Rate should be 100 per second, got {rate_10_to_20}"

    # Test 3: window filtering
    calculator3 = RateCalculator(window_size_seconds=10)

    # t=0s: counter=0
    # t=5s: counter=50
    # t=10s: counter=100
    # t=15s: counter=150
    # t=20s: counter=200

    # At t=20s with window=10s, should only see t=10-20s
    # Rate = (200 - 100) / (20 - 10) = 100 / 10 = 10 per second

    for t in [0, 5, 10, 15, 20]:
        calculator3.observe(t, t * 10)

    rate_at_20 = calculator3.calculate_rate(20)
    assert rate_at_20 == 10.0, f"Rate should be 10 per second in 10s window, got {rate_at_20}"

    # Test 4: no rate (counter not changing)
    calculator4 = RateCalculator(window_size_seconds=60)

    calculator4.observe(0, 1000)
    calculator4.observe(10, 1000)
    calculator4.observe(20, 1000)

    rate_static = calculator4.calculate_rate(20)
    assert rate_static == 0.0, f"Rate should be 0 when counter not changing, got {rate_static}"

    # Test 5: insufficient data
    calculator5 = RateCalculator(window_size_seconds=60)

    calculator5.observe(0, 0)
    rate_insufficient = calculator5.calculate_rate(5)
    assert rate_insufficient == 0.0, f"Rate should be 0 with insufficient data, got {rate_insufficient}"

    # Test 6: counter with recent values only
    calculator6 = RateCalculator(window_size_seconds=15)

    calculator6.observe(0, 0)
    calculator6.observe(10, 1000)
    calculator6.observe(20, 2000)  # +1000 in 10s = 100 per second
    calculator6.observe(30, 3000)  # +1000 in 10s = 100 per second

    # With window=15s at t=30s: only observations t=20 and t=30 are in window
    # Rate = (3000 - 2000) / (30 - 20) = 1000 / 10 = 100 per second
    rate_final = calculator6.calculate_rate(30)
    assert rate_final == 100.0, f"Rate should be 100 per second, got {rate_final}"

if __name__ == "__main__":
    test_rate_calc()
    print("✓ rate_calc passed")
