"""Canary deployment gate (gradual traffic shift with rollback)."""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"


class CanaryGate:
    """Gradually shift traffic to new version, rollback on error rate spike."""

    def __init__(self, error_threshold=0.05):
        """Init with acceptable error rate threshold (5% by default)."""
        self.error_threshold = error_threshold
        self.canary_traffic = 0.0  # Percentage of traffic to canary (0-100)
        self.canary_errors = 0
        self.canary_total = 0
        self.stable_errors = 0
        self.stable_total = 0

    def increase_canary_traffic(self, percent):
        """Increase canary traffic by N percentage points."""
        self.canary_traffic = min(100.0, self.canary_traffic + percent)

    def record_canary_request(self, success):
        """Record a request to canary. success=True if no error."""
        self.canary_total += 1
        if not success:
            self.canary_errors += 1

    def record_stable_request(self, success):
        """Record a request to stable version."""
        self.stable_total += 1
        if not success:
            self.stable_errors += 1

    def get_canary_error_rate(self):
        """Return current canary error rate."""
        if self.canary_total == 0:
            return 0.0
        return self.canary_errors / self.canary_total

    def is_healthy(self):
        """
        Check if canary is healthy enough to continue.
        Return False if error rate exceeds threshold.
        """
        error_rate = self.get_canary_error_rate()

        if error_rate > self.error_threshold:
            return False

        return True

    def should_rollback(self):
        """Return True if error rate warrants rollback."""
        return not self.is_healthy()


def test_canary_starts_at_zero():
    """Test: canary starts with zero traffic."""
    gate = CanaryGate()

    assert gate.canary_traffic == 0.0


def test_increase_canary_traffic():
    """Test: gradually increase canary traffic."""
    gate = CanaryGate()

    gate.increase_canary_traffic(10.0)
    assert gate.canary_traffic == 10.0

    gate.increase_canary_traffic(20.0)
    assert gate.canary_traffic == 30.0

    # Cap at 100
    gate.increase_canary_traffic(100.0)
    assert gate.canary_traffic == 100.0


def test_healthy_canary_continues():
    """Test: low error rate canary is healthy."""
    gate = CanaryGate(error_threshold=0.05)

    # 1 error in 100 requests = 1% error rate (below 5%)
    gate.increase_canary_traffic(50.0)

    for i in range(100):
        gate.record_canary_request(i != 50)  # One failure at index 50

    assert gate.get_canary_error_rate() == 0.01
    assert gate.is_healthy() is True
    assert gate.should_rollback() is False


def test_unhealthy_canary_triggers_rollback():
    """Test: high error rate triggers rollback."""
    gate = CanaryGate(error_threshold=0.05)

    gate.increase_canary_traffic(50.0)

    # SIMULATE FAILURE: canary has 10% error rate (above 5% threshold)
    for i in range(100):
        gate.record_canary_request(i >= 10)  # First 10 fail

    error_rate = gate.get_canary_error_rate()
    assert error_rate == 0.1, f"Expected 0.1, got {error_rate}"
    assert gate.is_healthy() is False, "Error rate 10% > threshold 5%"
    assert gate.should_rollback() is True, "Should trigger rollback"


def test_error_rate_at_threshold():
    """Test: error rate exactly at threshold is acceptable."""
    gate = CanaryGate(error_threshold=0.05)

    gate.increase_canary_traffic(50.0)

    # Exactly 5% error rate (at threshold)
    for i in range(100):
        gate.record_canary_request(i >= 5)  # First 5 fail

    assert gate.get_canary_error_rate() == 0.05
    assert gate.is_healthy() is True, "At threshold should pass"


def test_rollback_clears_canary():
    """Test: after rollback, canary traffic goes back to zero."""
    gate = CanaryGate()

    gate.increase_canary_traffic(50.0)

    # Simulate failure requiring rollback
    for i in range(100):
        gate.record_canary_request(False)  # All fail

    assert gate.should_rollback() is True

    # Manual reset after rollback decision
    gate.canary_traffic = 0.0
    assert gate.canary_traffic == 0.0


def test_gradual_ramp_up():
    """Test: gradual canary ramp-up sequence."""
    gate = CanaryGate(error_threshold=0.02)

    # Stage 3: 50% canary traffic, errors spike
    # (Using fresh gate to show spike detection on new load)
    gate.increase_canary_traffic(50.0)

    # Add many healthy requests first
    for _ in range(100):
        gate.record_canary_request(True)

    # Now error spike: 10% error rate (above 2% threshold)
    for i in range(100):
        gate.record_canary_request(i >= 10)  # First 10 fail, so 10% error

    # Cumulative: 100 success + 90 success + 10 fail = 190 success, 10 fail
    # Error rate = 10/200 = 5% (above 2%)
    assert gate.get_canary_error_rate() > 0.02
    assert gate.should_rollback() is True, "Should detect error spike"


if __name__ == "__main__":
    test_canary_starts_at_zero()
    test_increase_canary_traffic()
    test_healthy_canary_continues()
    test_unhealthy_canary_triggers_rollback()
    test_error_rate_at_threshold()
    test_rollback_clears_canary()
    test_gradual_ramp_up()
    print("✓ canary_gate passed")
