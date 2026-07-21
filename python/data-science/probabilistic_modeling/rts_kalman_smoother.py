"""
RTS (Rauch-Tung-Striebel) Kalman smoother: forward-backward pass for optimal smoothing.

Core idea: forward Kalman filter, then backward pass corrects trajectory.
Smoothed RMSE < filtered RMSE < raw observations.

When to use: trajectory estimation, state inference after all data arrives.
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

def _aura_validate_kf_forward(meas_var):
    v = []
    if isinstance(meas_var, (int, float)) and meas_var < 0:
        v.append(f"AURA-E-B5: meas_var must be >= 0, got {meas_var}")
    if v:
        raise AuraInputError(v)

def kf_forward(observations: List[float], process_var: float = 0.1,
               meas_var: float = 1.0) -> Tuple[List[float], List[float], List[float], List[float]]:
    """Kalman filter forward pass: return filtered states and covariances."""
    _aura_validate_kf_forward(meas_var)
    n = len(observations)

    # Initial state
    x_filt = [observations[0]]
    P_filt = [meas_var]

    for i in range(1, n):
        # Predict
        x_pred = x_filt[i-1]
        P_pred = P_filt[i-1] + process_var

        # Update
        K = P_pred / (P_pred + meas_var)  # Kalman gain
        x_update = x_pred + K * (observations[i] - x_pred)
        P_update = (1 - K) * P_pred

        x_filt.append(x_update)
        P_filt.append(P_update)

    return x_filt, P_filt

def rts_backward_pass(x_filt: List[float], P_filt: List[float],
                      process_var: float = 0.1) -> Tuple[List[float], List[float]]:
    """RTS backward pass: return smoothed states and covariances."""
    n = len(x_filt)

    # Initialize at last state
    x_smooth = [None] * n
    P_smooth = [None] * n
    x_smooth[-1] = x_filt[-1]
    P_smooth[-1] = P_filt[-1]

    # Backward pass
    for i in range(n - 2, -1, -1):
        # Predict forward covariance
        P_pred = P_filt[i] + process_var

        # Smoothing gain
        C = P_filt[i] / P_pred

        # Smoothed estimates
        x_smooth[i] = x_filt[i] + C * (x_smooth[i+1] - x_filt[i])
        P_smooth[i] = P_filt[i] + C ** 2 * (P_smooth[i+1] - P_pred)

    return x_smooth, P_smooth

if __name__ == '__main__':
    import random
    random.seed(42)

    # Generate true trajectory (random walk) and noisy observations
    true_traj = [0.0]
    for _ in range(30):
        true_traj.append(true_traj[-1] + random.gauss(0, 0.1))

    observations = [x + random.gauss(0, 1.0) for x in true_traj]

    # Kalman filter
    x_filt, P_filt = kf_forward(observations, process_var=0.1, meas_var=1.0)

    # RTS smoother
    x_smooth, P_smooth = rts_backward_pass(x_filt, P_filt, process_var=0.1)

    assert len(x_smooth) == len(observations), f"Should have {len(observations)} smoothed states, got {len(x_smooth)}"
    assert len(P_smooth) == len(observations), f"Should have {len(observations)} smoothed covariances"

    # RMSE comparisons
    rmse_raw = math.sqrt(sum((ob - tt) ** 2 for ob, tt in zip(observations, true_traj)) / len(true_traj))
    rmse_filt = math.sqrt(sum((xf - tt) ** 2 for xf, tt in zip(x_filt, true_traj)) / len(true_traj))
    rmse_smooth = math.sqrt(sum((xs - tt) ** 2 for xs, tt in zip(x_smooth, true_traj)) / len(true_traj))

    # Smoothed should beat filtered which should beat raw
    assert rmse_smooth < rmse_filt, f"Smoothed RMSE {rmse_smooth} should beat filtered {rmse_filt}"
    assert rmse_filt < rmse_raw, f"Filtered RMSE {rmse_filt} should beat raw {rmse_raw}"

    # Covariances should be positive
    for p in P_filt:
        assert p > 0, f"Filtered covariance should be positive, got {p}"
    for p in P_smooth:
        assert p > 0, f"Smoothed covariance should be positive, got {p}"

    # Smoothed covariances should be <= filtered (less uncertainty after backward pass)
    for ps, pf in zip(P_smooth, P_filt):
        assert ps <= pf * 1.01, f"Smoothed cov {ps} should be <= filtered {pf} (accounting for numerical errors)"

    # All estimates should be in reasonable range (not wild)
    all_estimates = observations + x_filt + x_smooth
    min_val, max_val = min(all_estimates), max(all_estimates)
    range_val = max_val - min_val
    assert range_val > 0, "Estimates should have non-zero range"
    assert range_val < 20, f"Estimates should be in reasonable range, got range {range_val}"

    print("PASS")
