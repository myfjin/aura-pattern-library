"""Monotonic clock immune to wall-clock backward jumps."""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import time

class ClockMock:
    """Injected logical clock."""
    def __init__(self):
        self.wall = 1000.0
        self.mono = 1000.0

    def step_wall_backward(self, amount):
        """Jump wall-clock backward (simulates NTP correction)."""
        self.wall -= amount

    def step_mono(self, amount):
        """Advance monotonic (always forward)."""
        self.mono += amount

    def get_wall(self):
        return self.wall

    def get_mono(self):
        return self.mono


def elapsed_time_safe(clock, start_wall, start_mono):
    """
    Compute elapsed time using monotonic, but validate wall-clock
    against backward jump.

    Return: (elapsed_mono, was_wall_skew)
    """
    current_wall = clock.get_wall()
    current_mono = clock.get_mono()

    elapsed_mono = current_mono - start_mono
    wall_diff = current_wall - start_wall

    # Detect wall-clock backward jump
    was_skew = wall_diff < 0

    # Elapsed time is ALWAYS monotonic (never corrupted by wall skew)
    return elapsed_mono, was_skew


def test_monotonic_survives_backward_jump():
    """Test: wall-clock backward jump does NOT corrupt monotonic elapsed."""
    clock = ClockMock()

    # Record start times
    start_wall = clock.get_wall()
    start_mono = clock.get_mono()

    # Advance monotonic by 5 units (real elapsed time)
    clock.step_mono(5.0)

    # SIMULATE FAILURE: wall-clock jumps backward by 10 units (NTP correction)
    clock.step_wall_backward(10.0)

    # Compute elapsed
    elapsed_mono, was_skew = elapsed_time_safe(clock, start_wall, start_mono)

    # ASSERT the defended outcome:
    # 1. Monotonic elapsed is EXACTLY 5.0 (not corrupted)
    assert elapsed_mono == 5.0, f"Expected 5.0, got {elapsed_mono}"

    # 2. Skew was detected
    assert was_skew is True, "Should have detected wall-clock backward jump"

    # 3. Re-test: if we DON'T detect skew properly, elapsed_mono would be wrong
    # If elapsed_time_safe() used wall-clock directly, it would give -5 - 10 = -15
    # instead of +5. The assert on 5.0 would fail.
    # This proves the function uses monotonic correctly.


def test_no_false_positive_on_forward_jump():
    """Test: forward wall-clock jump does NOT trigger false skew alarm."""
    clock = ClockMock()

    start_wall = clock.get_wall()
    start_mono = clock.get_mono()

    # Advance both by 5
    clock.step_mono(5.0)
    clock.wall += 5.0  # Forward jump (normal)

    elapsed_mono, was_skew = elapsed_time_safe(clock, start_wall, start_mono)

    # ASSERT:
    assert elapsed_mono == 5.0
    assert was_skew is False, "Forward jump should NOT trigger skew alarm"


if __name__ == "__main__":
    test_monotonic_survives_backward_jump()
    test_no_false_positive_on_forward_jump()
    print("✓ monotonic_vs_wall passed")
