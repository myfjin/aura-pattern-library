#!/usr/bin/env python3
"""counter_gauge_histogram: implement counter, gauge, and histogram metric types."""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import sys

class Counter:
    """Monotonically increasing counter."""
    def __init__(self, name, initial=0):
        self.name = name
        self.value = initial

    def increment(self, delta=1):
        if delta < 0:
            raise ValueError("Counter can only increase")
        self.value += delta

    def get(self):
        return self.value

class Gauge:
    """Value that can go up or down."""
    def __init__(self, name, initial=0):
        self.name = name
        self.value = initial

    def set(self, value):
        self.value = value

    def increment(self, delta=1):
        self.value += delta

    def decrement(self, delta=1):
        self.value -= delta

    def get(self):
        return self.value

class Histogram:
    """Record values in buckets."""
    def __init__(self, name, buckets=None):
        self.name = name
        if buckets is None:
            buckets = [0.1, 0.5, 1.0, 5.0, 10.0]
        self.buckets = sorted(buckets)
        self.bucket_counts = {b: 0 for b in self.buckets}
        self.bucket_counts["+Inf"] = 0
        self.sum = 0
        self.count = 0

    def observe(self, value):
        """Record an observation."""
        self.sum += value
        self.count += 1
        for bucket in self.buckets:
            if value <= bucket:
                self.bucket_counts[bucket] += 1
        self.bucket_counts["+Inf"] += 1

    def get_percentile(self, percentile):
        """Calculate percentile from histogram."""
        # Returns approximate percentile
        if self.count == 0:
            return 0
        target_count = int((percentile / 100.0) * self.count)
        cumulative = 0
        for bucket in self.buckets + ["+Inf"]:
            cumulative += self.bucket_counts[bucket]
            if cumulative >= target_count:
                return bucket if bucket != "+Inf" else self.sum / self.count
        return self.sum / self.count

    def get_average(self):
        """Get average value."""
        if self.count == 0:
            return 0
        return self.sum / self.count

def test_counter_gauge_histogram():
    """Test: counter increases, gauge changes, histogram buckets, percentile calc."""
    # Test Counter
    counter = Counter("requests_total", initial=0)
    assert counter.get() == 0, "Counter should start at 0"

    counter.increment(5)
    assert counter.get() == 5, "Counter should be 5 after +5"

    counter.increment(3)
    assert counter.get() == 8, "Counter should be 8 after +3"

    # Test Counter rejects negative deltas
    try:
        counter.increment(-1)
        assert False, "Counter should reject negative increment"
    except ValueError:
        pass  # Expected

    # Test Gauge
    gauge = Gauge("temperature_celsius", initial=20)
    assert gauge.get() == 20, "Gauge should start at 20"

    gauge.set(25)
    assert gauge.get() == 25, "Gauge should be 25 after set(25)"

    gauge.increment(5)
    assert gauge.get() == 30, "Gauge should be 30 after +5"

    gauge.decrement(10)
    assert gauge.get() == 20, "Gauge should be 20 after -10"

    # Test Histogram with known data
    histogram = Histogram("request_latency_ms", buckets=[1, 5, 10, 50, 100])

    # Observe known sequence
    values = [0.5, 2, 4, 8, 15, 25, 50, 75, 100, 150]
    for v in values:
        histogram.observe(v)

    # Verify counts
    assert histogram.count == 10, f"Histogram should have 10 observations, got {histogram.count}"
    assert histogram.bucket_counts[1] == 1, "1 value (0.5) <= 1"
    assert histogram.bucket_counts[5] == 3, "3 values (0.5, 2, 4) <= 5"
    assert histogram.bucket_counts[10] == 4, "4 values (0.5, 2, 4, 8) <= 10"
    assert histogram.bucket_counts[100] == 9, "9 values <= 100"
    assert histogram.bucket_counts["+Inf"] == 10, "All 10 values in +Inf bucket"

    # Verify sum and average
    expected_sum = sum(values)
    assert histogram.sum == expected_sum, f"Sum should be {expected_sum}, got {histogram.sum}"
    expected_avg = expected_sum / 10
    assert histogram.get_average() == expected_avg, f"Average should be {expected_avg}, got {histogram.get_average()}"

    # Test percentile (50th should be roughly middle)
    p50 = histogram.get_percentile(50)
    assert p50 > 0, "50th percentile should be positive"

    # Test empty histogram
    empty_hist = Histogram("empty_metric")
    assert empty_hist.get_average() == 0, "Empty histogram average should be 0"
    assert empty_hist.count == 0, "Empty histogram count should be 0"

    # Test histogram with single bucket
    single_bucket_hist = Histogram("tiny_metric", buckets=[10])
    single_bucket_hist.observe(5)
    single_bucket_hist.observe(15)
    assert single_bucket_hist.bucket_counts[10] == 1, "1 value (5) <= 10"
    assert single_bucket_hist.bucket_counts["+Inf"] == 2, "2 values total in +Inf"

if __name__ == "__main__":
    test_counter_gauge_histogram()
    print("✓ counter_gauge_histogram passed")
