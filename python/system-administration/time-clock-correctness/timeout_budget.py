"""Budget timeouts across multiple sequential operations."""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"


class TimeoutBudget:
    """Track remaining time across operations."""

    def __init__(self, clock_fn, total_seconds):
        """Init with clock and total budget."""
        self.clock_fn = clock_fn
        self.total_seconds = total_seconds
        self.start_time = None

    def start(self):
        """Mark the start of budget tracking."""
        self.start_time = self.clock_fn()

    def remaining(self):
        """Return remaining seconds. Raises if budget exhausted."""
        if self.start_time is None:
            raise RuntimeError("Budget not started")

        current = self.clock_fn()
        elapsed = current - self.start_time

        if elapsed > self.total_seconds:
            raise TimeoutError(
                f"Budget exhausted: {elapsed:.2f}s > {self.total_seconds}s"
            )

        return self.total_seconds - elapsed

    def consume(self, operation_duration):
        """Check if operation duration fits in remaining budget."""
        remaining = self.remaining()

        if operation_duration > remaining:
            raise TimeoutError(
                f"Operation {operation_duration}s exceeds remaining {remaining:.2f}s"
            )

        return remaining - operation_duration


def test_operations_within_budget():
    """Test: operations fit within budget."""
    clock_value = [1000.0]

    def mock_clock():
        return clock_value[0]

    budget = TimeoutBudget(mock_clock, total_seconds=10.0)
    budget.start()

    # Operation 1: 3 seconds
    remaining = budget.consume(3.0)
    assert remaining == 7.0, f"Expected 7.0, got {remaining}"

    # Advance clock by 3 seconds
    clock_value[0] = 1003.0

    # Operation 2: 5 seconds (fits in 7 remaining)
    remaining = budget.consume(5.0)
    assert remaining == 2.0

    # Advance by 5 seconds
    clock_value[0] = 1008.0

    # Operation 3: 2 seconds (fits exactly)
    remaining = budget.consume(2.0)
    assert remaining == 0.0


def test_operation_exceeds_remaining_budget():
    """Test: reject operation that exceeds remaining time."""
    clock_value = [1000.0]

    def mock_clock():
        return clock_value[0]

    budget = TimeoutBudget(mock_clock, total_seconds=10.0)
    budget.start()

    # Consume 8 seconds
    budget.consume(8.0)
    clock_value[0] = 1008.0

    # SIMULATE FAILURE: try to consume 3 seconds (only 2 left)
    try:
        budget.consume(3.0)
        assert False, "Should raise TimeoutError"
    except TimeoutError as e:
        assert "exceeds remaining" in str(e)


def test_total_budget_exhausted():
    """Test: detect when total budget time has passed."""
    clock_value = [1000.0]

    def mock_clock():
        return clock_value[0]

    budget = TimeoutBudget(mock_clock, total_seconds=10.0)
    budget.start()

    # Advance time past the budget
    clock_value[0] = 1012.0

    # SIMULATE FAILURE: check remaining after exhaustion
    try:
        budget.remaining()
        assert False, "Should raise TimeoutError"
    except TimeoutError as e:
        assert "Budget exhausted" in str(e)
        assert "12" in str(e)  # 12 > 10


def test_not_started_raises():
    """Test: raise error if checking budget before start()."""
    def mock_clock():
        return 1000.0

    budget = TimeoutBudget(mock_clock, total_seconds=10.0)

    # Don't call start()
    try:
        budget.remaining()
        assert False, "Should raise RuntimeError"
    except RuntimeError as e:
        assert "not started" in str(e)


def test_multiple_operations():
    """Test: track budget across many operations."""
    clock_value = [1000.0]

    def mock_clock():
        return clock_value[0]

    budget = TimeoutBudget(mock_clock, total_seconds=20.0)
    budget.start()

    operations = [
        (2.0, 2.0),   # op_duration, real_time_to_advance
        (3.0, 3.0),
        (5.0, 5.0),
        (4.0, 4.0),
        (6.0, 6.0),   # Total: 20 seconds
    ]

    for op_duration, advance_time in operations:
        budget.consume(op_duration)
        clock_value[0] += advance_time

    # At boundary, should succeed
    assert budget.remaining() == 0.0

    # One more operation should fail
    try:
        budget.consume(0.1)
        assert False, "Should fail at boundary"
    except TimeoutError:
        pass


if __name__ == "__main__":
    test_operations_within_budget()
    test_operation_exceeds_remaining_budget()
    test_total_budget_exhausted()
    test_not_started_raises()
    test_multiple_operations()
    print("✓ timeout_budget passed")
