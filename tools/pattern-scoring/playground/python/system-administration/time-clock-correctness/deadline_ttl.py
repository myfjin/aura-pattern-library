"""Deadline/TTL checker over an injectable clock.

DeadlineChecker turns a TTL into an absolute deadline via a supplied clock
function, then reports whether that deadline has passed and how much time
remains (negative once expired). Injecting the clock keeps expiry logic
deterministic and testable. Use it for cache TTLs, request deadlines, or
lease timers. Guarantees (self-test oracle): not-expired before the deadline,
expired exactly at and after it (>= boundary), remaining time is exact
including negative values, and independent deadlines are tracked separately.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"


class DeadlineChecker:
    """Track deadline and check if expired."""

    def __init__(self, clock_fn):
        """Init with clock function (returns current time)."""
        self.clock_fn = clock_fn

    def is_expired(self, deadline_time):
        """Return True if current time >= deadline."""
        current = self.clock_fn()
        return current >= deadline_time

    def remaining(self, deadline_time):
        """Return remaining time (seconds). Negative if expired."""
        current = self.clock_fn()
        return deadline_time - current

    def set_deadline(self, ttl_seconds):
        """Create a deadline N seconds from now. Return deadline time."""
        current = self.clock_fn()
        return current + ttl_seconds


def test_not_expired_before_deadline():
    """Test: returns False when not yet expired."""
    clock_value = [1000.0]

    def mock_clock():
        return clock_value[0]

    checker = DeadlineChecker(mock_clock)
    deadline = checker.set_deadline(10.0)

    # Current time: 1000, deadline: 1010
    assert checker.is_expired(deadline) is False
    assert checker.remaining(deadline) == 10.0


def test_expired_after_deadline():
    """Test: returns True when expired."""
    clock_value = [1000.0]

    def mock_clock():
        return clock_value[0]

    checker = DeadlineChecker(mock_clock)
    deadline = checker.set_deadline(10.0)

    # SIMULATE FAILURE: advance clock past deadline
    clock_value[0] = 1011.0

    assert checker.is_expired(deadline) is True, "Should be expired at 1011 (past 1010)"
    assert checker.remaining(deadline) == -1.0


def test_expired_exactly_at_deadline():
    """Test: True at exact deadline time."""
    clock_value = [1000.0]

    def mock_clock():
        return clock_value[0]

    checker = DeadlineChecker(mock_clock)
    deadline = checker.set_deadline(10.0)

    # Advance to exactly the deadline
    clock_value[0] = 1010.0

    assert checker.is_expired(deadline) is True
    assert checker.remaining(deadline) == 0.0


def test_multiple_deadlines():
    """Test: multiple independent deadlines."""
    clock_value = [1000.0]

    def mock_clock():
        return clock_value[0]

    checker = DeadlineChecker(mock_clock)

    deadline1 = checker.set_deadline(5.0)   # 1005
    deadline2 = checker.set_deadline(10.0)  # 1010

    clock_value[0] = 1006.0

    # deadline1 expired, deadline2 not
    assert checker.is_expired(deadline1) is True
    assert checker.is_expired(deadline2) is False
    assert checker.remaining(deadline1) == -1.0
    assert checker.remaining(deadline2) == 4.0


if __name__ == "__main__":
    test_not_expired_before_deadline()
    test_expired_after_deadline()
    test_expired_exactly_at_deadline()
    test_multiple_deadlines()
    print("✓ deadline_ttl passed")
