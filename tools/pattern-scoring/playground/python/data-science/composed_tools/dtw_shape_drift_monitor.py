"""
DTW Shape-Drift Monitor — catching "the day looks wrong" when every point
statistic looks fine.

COMPOSED PATTERN: dtw_dynamic_time_warping (Optimization & Distances) x
ewma_streaming_metrics (Applied DS Practice) — embedding bridge 0.501, found
2026-07-06. Point monitors (mean/variance z-scores) are blind to SHAPE: a
daily profile whose peak moved six hours has the same mean and variance as a
normal day. This monitor DTW-matches each day against a reference profile and
EWMA-smooths the distances; drift = smoothed distance crossing a calibrated
MAD fence. Shape becomes a monitored quantity.

Use when: monitoring periodic profiles (traffic, load, sales) where timing
and shape matter, not just level.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import math
import random
from typing import List


def dtw_distance(a: List[float], b: List[float]) -> float:
    n, m = len(a), len(b)
    INF = float("inf")
    D = [[INF] * (m + 1) for _ in range(n + 1)]
    D[0][0] = 0.0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            cost = abs(a[i - 1] - b[j - 1])
            D[i][j] = cost + min(D[i - 1][j], D[i][j - 1], D[i - 1][j - 1])
    return D[n][m]


def daily_profile(shift_hours: int, noise: float) -> List[float]:
    """24-point diurnal shape: quiet night, midday peak. Circular shift moves
    the peak WITHOUT changing the multiset of values much (mean/var stable)."""
    base = [1.0 + 4.0 * math.exp(-((h - 13) % 24 - 0) ** 2 / 8.0) +
            2.0 * math.sin(2 * math.pi * h / 24) for h in range(24)]
    shifted = [base[(h - shift_hours) % 24] for h in range(24)]
    return [v + random.gauss(0, noise) for v in shifted]


def mean(v: List[float]) -> float:
    return sum(v) / len(v)


def std(v: List[float]) -> float:
    m = mean(v)
    return math.sqrt(sum((x - m) ** 2 for x in v) / len(v))


if __name__ == "__main__":
    random.seed(42)

    reference = daily_profile(shift_hours=0, noise=0.0)

    # 20 calibration days (normal shape), then 10 drifted days: peak moved 6h.
    normal_days = [daily_profile(0, 0.25) for _ in range(20)]
    drifted_days = [daily_profile(6, 0.25) for _ in range(10)]
    days = normal_days + drifted_days
    change_at = len(normal_days)

    # POINT MONITOR (the blind baseline): z-score of each day's mean and std
    # against the calibration days.
    cal_means = [mean(d) for d in normal_days]
    cal_stds = [std(d) for d in normal_days]
    mu_m, sd_m = mean(cal_means), std(cal_means) or 1e-9
    mu_s, sd_s = mean(cal_stds), std(cal_stds) or 1e-9
    point_alarms = [i for i, d in enumerate(days)
                    if abs(mean(d) - mu_m) / sd_m > 3 or abs(std(d) - mu_s) / sd_s > 3]

    # SHAPE MONITOR: DTW to reference, EWMA-smoothed, MAD fence from calibration.
    dists = [dtw_distance(d, reference) for d in days]
    cal = dists[:change_at]
    med = sorted(cal)[len(cal) // 2]
    mad = sorted(abs(x - med) for x in cal)[len(cal) // 2] or 1e-9
    fence = med + 6 * 1.4826 * mad

    alpha, ewma = 0.4, dists[0]
    shape_alarms: List[int] = []
    for i, x in enumerate(dists):
        ewma = alpha * x + (1 - alpha) * ewma
        if ewma > fence:
            shape_alarms.append(i)

    first_alarm = shape_alarms[0] if shape_alarms else -1
    print(f"point-statistic alarms on shape-drift days: "
          f"{[i for i in point_alarms if i >= change_at]}")
    print(f"shape alarms: first at day {first_alarm} "
          f"(change at day {change_at}) · fence {fence:.1f} · "
          f"calib DTW ~{med:.1f} · drift DTW ~{sorted(dists[change_at:])[5]:.1f}")

    # The composed claim, measured:
    # 1. the point monitor is BLIND to the shape change (that's the whole point)
    assert not any(i >= change_at for i in point_alarms), \
        "point monitor should NOT flag a pure shape change (mean/var preserved)"
    # 2. the shape monitor catches it, promptly
    assert shape_alarms and change_at <= first_alarm <= change_at + 2, \
        f"shape monitor must fire within 3 days of the change: {first_alarm}"
    # 3. zero false alarms during calibration
    assert not any(i < change_at for i in shape_alarms), \
        "no false alarms on normal days"
    print("dtw_shape_drift_monitor.py PASS")
