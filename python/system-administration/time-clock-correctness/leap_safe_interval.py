"""Compute time intervals correctly across leap second insertions."""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"


class LeapSafeInterval:
    """Track intervals while handling leap seconds."""

    def __init__(self):
        self.last_time = None
        self.leap_seconds_seen = []  # List of leap second times

    def record_leap_second(self, leap_time):
        """Record that a leap second occurred at this Unix timestamp."""
        self.leap_seconds_seen.append(leap_time)

    def interval_between(self, time_a, time_b):
        """
        Compute elapsed time between two Unix timestamps.
        Ignore leap seconds (they don't contribute to real elapsed time).

        Return: actual_elapsed (excluding leap seconds)
        """
        if time_b < time_a:
            time_a, time_b = time_b, time_a

        # Count leap seconds in range
        leap_count = sum(1 for ls in self.leap_seconds_seen if time_a < ls <= time_b)

        # Actual elapsed = raw difference - leap seconds
        raw_diff = time_b - time_a
        actual_elapsed = raw_diff - leap_count

        return actual_elapsed


def test_interval_without_leap_second():
    """Test: normal interval (no leap seconds)."""
    calc = LeapSafeInterval()

    # 100 seconds between two timestamps
    elapsed = calc.interval_between(1000.0, 1100.0)

    assert elapsed == 100.0


def test_interval_with_one_leap_second():
    """Test: leap second in the range is excluded."""
    calc = LeapSafeInterval()

    # Record leap second at timestamp 1050
    calc.record_leap_second(1050.0)

    # Between 1000 and 1100 there's one leap second
    # Raw diff = 100, but 1 leap second occurred
    # Actual elapsed = 100 - 1 = 99 seconds
    elapsed = calc.interval_between(1000.0, 1100.0)

    assert elapsed == 99.0, f"Expected 99.0, got {elapsed}"


def test_interval_with_multiple_leap_seconds():
    """Test: multiple leap seconds in range."""
    calc = LeapSafeInterval()

    # Record two leap seconds
    calc.record_leap_second(1030.0)
    calc.record_leap_second(1070.0)

    # Between 1000 and 1100, two leap seconds occurred
    # Raw diff = 100, actual = 100 - 2 = 98
    elapsed = calc.interval_between(1000.0, 1100.0)

    assert elapsed == 98.0, f"Expected 98.0, got {elapsed}"


def test_leap_second_at_boundary_excluded():
    """Test: leap second exactly at end is included; at start is excluded."""
    calc = LeapSafeInterval()

    # Leap second at boundary
    calc.record_leap_second(1100.0)

    # If leap second is at time_b (1100), it's included in the range
    # (time_a < ls <= time_b)
    elapsed = calc.interval_between(1000.0, 1100.0)

    assert elapsed == 99.0, "Leap at end should be counted"

    # Leap at start should not be counted
    calc2 = LeapSafeInterval()
    calc2.record_leap_second(1000.0)

    elapsed2 = calc2.interval_between(1000.0, 1100.0)
    assert elapsed2 == 100.0, "Leap at start should not be counted"


def test_reverse_interval():
    """Test: interval works regardless of argument order."""
    calc = LeapSafeInterval()
    calc.record_leap_second(1050.0)

    # Both orders should give same result
    elapsed1 = calc.interval_between(1000.0, 1100.0)
    elapsed2 = calc.interval_between(1100.0, 1000.0)

    assert elapsed1 == elapsed2 == 99.0


def test_simulation_wrong_if_leap_not_excluded():
    """
    SIMULATE FAILURE: if leap seconds are NOT excluded, measurements are wrong.
    This proves the leap-second compensation is necessary.
    """
    calc = LeapSafeInterval()

    # Suppose 3 leap seconds occurred between 1100 and 1200
    # time_a < leap_time <= time_b: 1100 < ls <= 1200
    calc.record_leap_second(1110.0)  # Within range
    calc.record_leap_second(1150.0)  # Within range
    calc.record_leap_second(1190.0)  # Within range

    # True elapsed: 100 - 3 = 97 seconds
    # Raw timestamp difference: 1200 - 1100 = 100
    # But 3 leap seconds were inserted, so actual = 100 - 3 = 97

    elapsed = calc.interval_between(1100.0, 1200.0)

    assert elapsed == 97.0, f"Expected 97.0, got {elapsed}"

    # If we naively used raw diff, we'd get 100 (wrong)
    raw_diff = 1200.0 - 1100.0
    assert raw_diff == 100.0
    assert raw_diff != elapsed  # They differ (bug caught)


if __name__ == "__main__":
    test_interval_without_leap_second()
    test_interval_with_one_leap_second()
    test_interval_with_multiple_leap_seconds()
    test_leap_second_at_boundary_excluded()
    test_reverse_interval()
    test_simulation_wrong_if_leap_not_excluded()
    print("✓ leap_safe_interval passed")
