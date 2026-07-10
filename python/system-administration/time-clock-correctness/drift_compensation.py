"""Compensate for clock drift (clock running fast or slow)."""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"


class DriftCompensator:
    """Track and correct for clock drift."""

    def __init__(self, drift_rate):
        """
        Init with drift rate (e.g., 1.01 = clock runs 1% fast).
        drift_rate < 1.0: clock slow
        drift_rate > 1.0: clock fast
        """
        self.drift_rate = drift_rate
        self.reference_time = 0.0
        self.reference_real = 0.0

    def calibrate(self, real_time, clock_time):
        """Set calibration point (what real time should be at clock time)."""
        self.reference_time = clock_time
        self.reference_real = real_time

    def correct(self, clock_time):
        """
        Given a clock reading, return corrected (real) time.
        Accounts for drift from calibration point.
        """
        # Time elapsed on the drifting clock since calibration
        clock_elapsed = clock_time - self.reference_time

        # Real time elapsed (accounting for drift)
        real_elapsed = clock_elapsed / self.drift_rate

        # Corrected absolute time
        return self.reference_real + real_elapsed

    def error_at(self, clock_time):
        """Return error (uncorrected - corrected) at this clock time."""
        uncorrected = clock_time
        corrected = self.correct(clock_time)
        return uncorrected - corrected


def test_fast_clock_compensation():
    """Test: compensate for clock running 10% fast."""
    comp = DriftCompensator(drift_rate=1.10)

    # Calibrate: at clock-time 1000, real time is 1000
    comp.calibrate(real_time=1000.0, clock_time=1000.0)

    # Clock advances by 110 units (real time should be 100)
    corrected = comp.correct(1110.0)
    expected = 1100.0  # 1000 + (110 / 1.10)

    assert corrected == expected, f"Expected {expected}, got {corrected}"


def test_slow_clock_compensation():
    """Test: compensate for clock running 10% slow (drift_rate=0.90)."""
    comp = DriftCompensator(drift_rate=0.90)

    comp.calibrate(real_time=1000.0, clock_time=1000.0)

    # Clock advances by 90 units (real time should be 100)
    corrected = comp.correct(1090.0)
    expected = 1100.0  # 1000 + (90 / 0.90)

    assert corrected == expected, f"Expected {expected}, got {corrected}"


def test_error_calculation():
    """Test: compute error between uncorrected and corrected."""
    # Clock runs 20% fast (1.20)
    comp = DriftCompensator(drift_rate=1.20)
    comp.calibrate(real_time=1000.0, clock_time=1000.0)

    # At clock-time 1120 (120 units elapsed)
    # Real time is 1000 + (120/1.20) = 1100
    # Error = 1120 - 1100 = 20
    error = comp.error_at(1120.0)
    assert error == 20.0, f"Expected error 20.0, got {error}"


def test_simulation_fast_clock_causes_wrong_measure():
    """
    SIMULATE FAILURE: if we don't correct for drift, measurements are wrong.
    This proves the correction function is necessary.
    """
    comp = DriftCompensator(drift_rate=1.15)  # 15% fast
    comp.calibrate(real_time=2000.0, clock_time=2000.0)

    # Real elapsed time should be 100 seconds
    # But on a 15% fast clock, it looks like 115 seconds have passed
    clock_reading = 2115.0

    # UNCORRECTED: would say 115 seconds elapsed
    # CORRECTED: says 100 seconds elapsed
    corrected = comp.correct(clock_reading)
    real_elapsed = corrected - 2000.0

    assert real_elapsed == 100.0, f"Real elapsed should be 100, got {real_elapsed}"
    # If we used uncorrected, we'd get 115 (wrong)
    uncorrected_elapsed = clock_reading - 2000.0
    assert uncorrected_elapsed == 115.0
    assert uncorrected_elapsed != real_elapsed  # They differ (bug caught)


if __name__ == "__main__":
    test_fast_clock_compensation()
    test_slow_clock_compensation()
    test_error_calculation()
    test_simulation_fast_clock_causes_wrong_measure()
    print("✓ drift_compensation passed")
