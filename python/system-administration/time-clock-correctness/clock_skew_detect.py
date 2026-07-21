"""Detect backward wall-clock jumps from a stream of time samples.

SkewDetector records successive wall-clock readings and flags any sample that
is earlier than the previous one (a backward jump), accumulating the count and
total magnitude of skew seen. Use it to catch NTP step-backs or manual clock
resets that would break time-based logic. Guarantees (self-test oracle): a
backward step is detected with its exact magnitude, multiple skews accumulate
correctly, and purely forward progression never raises a false positive.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"


class SkewDetector:
    """Track wall-clock samples and detect backward jumps."""
    def __init__(self):
        self.last_wall = None
        self.skew_samples = []

    def sample(self, wall_time):
        """Record a wall-clock sample. Return True if skew detected."""
        if self.last_wall is None:
            self.last_wall = wall_time
            return False

        skew_amount = self.last_wall - wall_time  # Positive if backward jump
        has_skew = skew_amount > 0

        if has_skew:
            self.skew_samples.append(skew_amount)

        self.last_wall = wall_time
        return has_skew

    def get_skew_count(self):
        return len(self.skew_samples)

    def get_total_skew(self):
        return sum(self.skew_samples)


def test_detect_backward_jump():
    """Test: detect wall-clock backward jump."""
    detector = SkewDetector()

    # Normal forward progression
    assert detector.sample(1000.0) is False
    assert detector.sample(1001.0) is False
    assert detector.sample(1002.0) is False

    # SIMULATE FAILURE: backward jump by 5 seconds
    skew_detected = detector.sample(1997.0)  # Jumped from 1002 to 1997 is forward
    assert skew_detected is False

    # Now jump backward
    skew_detected = detector.sample(1990.0)
    assert skew_detected is True, "Should detect backward jump"
    assert detector.get_skew_count() == 1
    assert detector.get_total_skew() == 7.0, f"Skew should be 7.0, got {detector.get_total_skew()}"


def test_multiple_skews():
    """Test: accumulate multiple skew events."""
    detector = SkewDetector()

    detector.sample(1000.0)
    detector.sample(1010.0)

    # First backward jump
    detector.sample(1005.0)
    assert detector.get_skew_count() == 1
    assert detector.get_total_skew() == 5.0

    # Second backward jump
    detector.sample(1002.0)
    assert detector.get_skew_count() == 2
    assert detector.get_total_skew() == 8.0, f"Expected 8.0, got {detector.get_total_skew()}"


def test_no_false_positive():
    """Test: forward movement does not trigger skew."""
    detector = SkewDetector()

    for i in range(10):
        assert detector.sample(1000.0 + i) is False

    assert detector.get_skew_count() == 0


if __name__ == "__main__":
    test_detect_backward_jump()
    test_multiple_skews()
    test_no_false_positive()
    print("✓ clock_skew_detect passed")
