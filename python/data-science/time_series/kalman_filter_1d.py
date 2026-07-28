"""
1D Kalman Filter

Recursively estimate the state of a 1D system (constant velocity model).
State: x = [position, velocity]. Observations are noisy position measurements.
The filter balances prediction (prior) and observation (likelihood) using
Gaussian uncertainties (variances). Reduces observation noise.
Use for smoothing GPS, sensor readings, or tracking slow-moving targets.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import math
from typing import List, Tuple




class AuraInputError(ValueError):
    """All input-contract violations, reported together (accumulate-then-raise)."""
    def __init__(self, violations):
        self.violations = violations
        super().__init__("input contract violated:\n  " + "\n  ".join(violations))

def _aura_validate_kalman_filter_1d(process_variance, measurement_variance, initial_state, initial_estimate_error):
    v = []
    if isinstance(process_variance, (int, float)) and process_variance <= 0:
        v.append(f"AURA-E009: process_variance must be > 0, got {process_variance}")
    if isinstance(measurement_variance, (int, float)) and not math.isfinite(measurement_variance):
        v.append(f"AURA-E008: measurement_variance must be finite, got {measurement_variance}")
    if isinstance(measurement_variance, (int, float)) and measurement_variance <= 0:
        v.append(f"AURA-E009: measurement_variance must be > 0, got {measurement_variance}")
    if isinstance(initial_state, (int, float)) and initial_state <= 0:
        v.append(f"AURA-E009: initial_state must be > 0, got {initial_state}")
    if isinstance(initial_estimate_error, (int, float)) and initial_estimate_error <= 0:
        v.append(f"AURA-E009: initial_estimate_error must be > 0, got {initial_estimate_error}")
    if v:
        raise AuraInputError(v)

def kalman_filter_1d(
    observations: List[float],
    process_variance: float,
    measurement_variance: float,
    initial_state: float,
    initial_estimate_error: float,
) -> Tuple[List[float], List[float]]:
    """
    1D Kalman filter for constant-value model.
    state: the true (unknown) value
    observation = state + measurement_noise
    process_variance: how much state can change between steps
    measurement_variance: sensor noise
    initial_state: prior on state
    initial_estimate_error: uncertainty in prior
    Returns (filtered_states, kalman_gains)
    """
    _aura_validate_kalman_filter_1d(process_variance, measurement_variance, initial_state, initial_estimate_error)
    filtered_states = [initial_state]
    kalman_gains = []
    estimate_error = initial_estimate_error
    state = initial_state

    for obs in observations:
        # Prediction step: state stays same (constant model), error grows
        predicted_state = state
        predicted_error = estimate_error + process_variance

        # Update step: Kalman gain
        kalman_gain = predicted_error / (predicted_error + measurement_variance)
        kalman_gains.append(kalman_gain)

        # Update state and error
        innovation = obs - predicted_state
        state = predicted_state + kalman_gain * innovation
        estimate_error = (1 - kalman_gain) * predicted_error

        filtered_states.append(state)

    return filtered_states[1:], kalman_gains  # Skip initial state


def compute_mse(actual: List[float], estimated: List[float]) -> float:
    """Mean squared error."""
    if len(actual) != len(estimated):
        raise ValueError("Length mismatch")
    return sum((a - e) ** 2 for a, e in zip(actual, estimated)) / len(actual)


if __name__ == "__main__":
    import random
    random.seed(42)

    # Generate true constant signal (position = 10)
    true_value = 10.0
    true_series = [true_value] * 100

    # Add measurement noise
    measurement_noise = [random.gauss(0, 2) for _ in range(100)]
    observations = [true_series[i] + measurement_noise[i] for i in range(100)]

    # Raw observation MSE
    raw_mse = compute_mse(true_series, observations)

    # Apply Kalman filter
    filtered, gains = kalman_filter_1d(
        observations,
        process_variance=0.01,  # Low: expect constant
        measurement_variance=4.0,  # Sensor noise variance
        initial_state=10.0,
        initial_estimate_error=1.0,
    )

    # Filtered MSE should be lower than raw observations
    filtered_mse = compute_mse(true_series, filtered)
    assert filtered_mse < raw_mse, f"Filtered MSE should be lower: {filtered_mse} vs {raw_mse}"

    # Kalman gains should be positive and less than 1
    assert all(0 < g < 1 for g in gains), "Kalman gains should be in (0, 1)"

    # After convergence, gain should stabilize
    gains_early = sum(gains[:10]) / 10
    gains_late = sum(gains[-10:]) / 10
    assert abs(gains_early - gains_late) < 0.1, "Kalman gains should converge"

    # Filtered estimates should be close to true value
    filtered_mean = sum(filtered) / len(filtered)
    assert abs(filtered_mean - true_value) < 0.5, f"Filtered mean should be close to {true_value}, got {filtered_mean}"

    print("kalman_filter_1d.py PASS")
