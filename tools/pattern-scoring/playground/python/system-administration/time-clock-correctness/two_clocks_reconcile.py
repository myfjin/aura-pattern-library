"""Reconcile two independent clock sources (e.g., system + hardware)."""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"


class DualClockReconciler:
    """Compare two clocks, use the sane one."""

    def __init__(self, max_skew_allowed=1.0):
        """Init with max allowed difference between clocks."""
        self.max_skew_allowed = max_skew_allowed
        self.last_clock1 = None
        self.last_clock2 = None

    def reconcile(self, clock1_time, clock2_time):
        """
        Compare two clock readings.
        Return: (selected_time, is_consistent)

        If clocks agree: return their value and True.
        If one jumped backward: return the one that didn't jump, False.
        If both jumped backward: return max (most forward), False.
        """
        diff = abs(clock1_time - clock2_time)

        if diff <= self.max_skew_allowed:
            # Clocks agree
            self.last_clock1 = clock1_time
            self.last_clock2 = clock2_time
            return clock1_time, True

        # Detect which clock jumped backward
        clock1_backward = (
            self.last_clock1 is not None and clock1_time < self.last_clock1
        )
        clock2_backward = (
            self.last_clock2 is not None and clock2_time < self.last_clock2
        )

        # Prefer the one that did NOT jump backward
        if clock1_backward and not clock2_backward:
            selected = clock2_time
        elif clock2_backward and not clock1_backward:
            selected = clock1_time
        else:
            # No history yet (both None): use min (conservative)
            if self.last_clock1 is None and self.last_clock2 is None:
                selected = min(clock1_time, clock2_time)
            else:
                # Both jumped: use max (most forward)
                selected = max(clock1_time, clock2_time)

        self.last_clock1 = clock1_time
        self.last_clock2 = clock2_time

        return selected, False


def test_clocks_agree():
    """Test: when both clocks agree, return their value."""
    reconciler = DualClockReconciler(max_skew_allowed=0.5)

    selected, is_consistent = reconciler.reconcile(1000.0, 1000.0)

    assert selected == 1000.0
    assert is_consistent is True


def test_clocks_within_tolerance():
    """Test: small disagreement is acceptable."""
    reconciler = DualClockReconciler(max_skew_allowed=1.0)

    selected, is_consistent = reconciler.reconcile(1000.0, 1000.5)

    assert selected == 1000.0  # Returns clock1 (arbitrary choice)
    assert is_consistent is True


def test_one_clock_jumps_backward():
    """Test: detect backward jump, use the forward-moving clock."""
    reconciler = DualClockReconciler(max_skew_allowed=0.5)

    # Establish history
    reconciler.reconcile(1000.0, 1000.0)

    # Advance normally
    reconciler.reconcile(1010.0, 1010.0)

    # SIMULATE FAILURE: clock1 jumps backward
    selected, is_consistent = reconciler.reconcile(1005.0, 1015.0)

    # Should use clock2 (1015.0) which didn't jump
    assert selected == 1015.0, f"Should select 1015.0 (forward), got {selected}"
    assert is_consistent is False


def test_both_clocks_jump_backward():
    """Test: both jump backward, use maximum (most forward)."""
    reconciler = DualClockReconciler(max_skew_allowed=0.5)

    # Establish history
    reconciler.reconcile(1000.0, 1000.0)
    reconciler.reconcile(1010.0, 1010.0)

    # SIMULATE FAILURE: both jump backward
    selected, is_consistent = reconciler.reconcile(1008.0, 1009.0)

    # Both jumped, so use max (most forward, safest for monotonic time)
    assert selected == 1009.0, f"Should select max 1009.0, got {selected}"
    assert is_consistent is False


def test_large_disagreement_no_history():
    """Test: large disagreement, no jump history, use minimum."""
    reconciler = DualClockReconciler(max_skew_allowed=0.5)

    # No history yet, large disagreement
    selected, is_consistent = reconciler.reconcile(1000.0, 1100.0)

    # Use minimum (safest)
    assert selected == 1000.0
    assert is_consistent is False


if __name__ == "__main__":
    test_clocks_agree()
    test_clocks_within_tolerance()
    test_one_clock_jumps_backward()
    test_both_clocks_jump_backward()
    test_large_disagreement_no_history()
    print("✓ two_clocks_reconcile passed")
