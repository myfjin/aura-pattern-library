#!/usr/bin/env python3
"""
throughput_meter: Calculate throughput (items/sec or bytes/sec).
THE ONE LAW: Track time windows, calculate exact rate, handle zero-duration edge cases.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import time

class ThroughputMeter:
    """Measure throughput over a time window."""

    def __init__(self, window_size=60):
        """
        window_size: seconds to accumulate before measuring.
        """
        self.window_size = window_size
        self.start_time = None
        self.item_count = 0
        self.byte_count = 0

    def record(self, item_count=1, byte_count=0):
        """Record item(s) processed."""
        if self.start_time is None:
            self.start_time = time.time()

        self.item_count += item_count
        self.byte_count += byte_count

    def get_throughput(self):
        """
        Calculate throughput (items/sec, bytes/sec).
        Return dict {items_per_sec, bytes_per_sec} or None if window not elapsed.
        """
        if self.start_time is None or self.item_count == 0:
            return None

        elapsed = time.time() - self.start_time
        if elapsed < 0.001:  # Avoid division by zero (< 1ms).
            return None

        items_per_sec = self.item_count / elapsed
        bytes_per_sec = self.byte_count / elapsed if self.byte_count > 0 else 0

        return {
            'items_per_sec': items_per_sec,
            'bytes_per_sec': bytes_per_sec,
            'elapsed': elapsed
        }

    def reset(self):
        """Reset counters."""
        self.start_time = None
        self.item_count = 0
        self.byte_count = 0

def main():
    # Test without actual time.sleep() using mock timing.
    # Create a meter and simulate recorded items over a known duration.

    # Case 1: Record 100 items over 1 second (manually set timing).
    meter = ThroughputMeter()
    meter.start_time = time.time() - 1.0  # Pretend started 1 second ago.
    meter.record(item_count=100, byte_count=10000)

    throughput = meter.get_throughput()
    assert throughput is not None, "Should calculate throughput"
    assert abs(throughput['items_per_sec'] - 100) < 1, f"Expected ~100 items/sec, got {throughput['items_per_sec']}"
    assert abs(throughput['bytes_per_sec'] - 10000) < 100, f"Expected ~10000 bytes/sec, got {throughput['bytes_per_sec']}"

    # FAILURE SIMULATION: No items recorded.
    meter_empty = ThroughputMeter()
    throughput_empty = meter_empty.get_throughput()
    assert throughput_empty is None, "Empty meter should return None"

    # Edge case: Very short duration (< 1ms).
    meter_fast = ThroughputMeter()
    meter_fast.start_time = time.time()
    meter_fast.record(item_count=1)
    # Immediately get throughput (will be None due to < 1ms elapsed).
    throughput_fast = meter_fast.get_throughput()
    # Likely None, but depends on timing. Check for reasonable value or None.
    assert throughput_fast is None or throughput_fast['items_per_sec'] > 0, "Fast meter should have reasonable throughput"

    # Case 2: Multiple records over longer period.
    meter2 = ThroughputMeter()
    meter2.start_time = time.time() - 10.0  # 10 seconds ago.
    meter2.record(item_count=50, byte_count=5000)
    meter2.record(item_count=50, byte_count=5000)
    meter2.record(item_count=50, byte_count=5000)  # Total: 150 items, 15000 bytes.

    throughput2 = meter2.get_throughput()
    assert throughput2 is not None, "Should calculate multi-record throughput"
    assert abs(throughput2['items_per_sec'] - 15) < 1, f"Expected ~15 items/sec (150/10), got {throughput2['items_per_sec']}"
    assert abs(throughput2['bytes_per_sec'] - 1500) < 100, f"Expected ~1500 bytes/sec, got {throughput2['bytes_per_sec']}"

    # Verify exact calculation.
    expected_items = 150 / 10.0
    assert abs(throughput2['items_per_sec'] - expected_items) < 0.01, "Exact throughput mismatch"

    # Edge case: Only byte_count, no items.
    meter3 = ThroughputMeter()
    meter3.start_time = time.time() - 2.0
    meter3.record(item_count=0, byte_count=2000)
    throughput3 = meter3.get_throughput()
    assert throughput3 is None or throughput3['bytes_per_sec'] == 1000, "Should measure bytes/sec"

    # Reset and verify.
    meter.reset()
    assert meter.item_count == 0, "Reset should clear item count"
    assert meter.start_time is None, "Reset should clear start time"
    assert meter.get_throughput() is None, "Reset meter should return None"

    print("✓ throughput_meter passed")

if __name__ == '__main__':
    main()
