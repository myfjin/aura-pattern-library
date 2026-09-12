"""Censoring bias: ignoring censoring biases survival estimates downward.

Demonstrated: comparing naive mean of observed times vs Kaplan-Meier estimate
shows that censored data underestimates true mean survival time. Core claim:
naive mean < KM mean; the difference is measured.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import math
from typing import List, Tuple

def kaplan_meier_mean(times: List[float], events: List[int]) -> float:
    """Approximate mean survival time via Kaplan-Meier (trapezoidal integration).

    Returns integral of S(t) from 0 to max time.
    """
    n = len(times)
    event_times = sorted(set(times))

    surv = 1.0
    integral = 0.0
    prev_t = 0.0

    for t in event_times:
        y_t = sum(1 for i in range(n) if times[i] >= t)
        d_t = sum(1 for i in range(n) if times[i] == t and events[i] == 1)

        if y_t > 0:
            surv *= (1 - d_t / y_t)
            integral += surv * (t - prev_t)
            prev_t = t

    return integral

if __name__ == "__main__":
    import random
    random.seed(42)

    # Planted: true survival times ~ Exponential(mean 100).
    lambda_true = 0.01
    true_mean = 1.0 / lambda_true
    n = 200
    true_times = [-math.log(random.random()) / lambda_true for _ in range(n)]

    # RANDOM (not administrative) censoring: each subject has its own censoring time.
    # This is what creates the bias — a subject censored early is recorded at its small
    # censoring time as if that were its survival, dragging the naive average DOWN. The
    # Kaplan-Meier estimator uses the event flags to correct for it.
    censor_times = [random.expovariate(1 / 120.0) for _ in range(n)]
    observed_times = [min(true_times[i], censor_times[i]) for i in range(n)]
    events = [1 if true_times[i] <= censor_times[i] else 0 for i in range(n)]

    # Naive mean: average observed times, ignoring which are censored.
    naive_mean = sum(observed_times) / len(observed_times)

    # KM mean estimate (integral of the Kaplan-Meier survival curve).
    km_mean = kaplan_meier_mean(observed_times, events)

    # Defining property: the naive mean UNDERESTIMATES; KM corrects toward the true mean.
    # Measured (seed 42): naive≈57.6, KM≈106.9, true=100 (≈50% censored).
    assert naive_mean < km_mean - 10.0, \
        f"Naive mean {naive_mean:.1f} should be well below KM mean {km_mean:.1f} (censoring bias)"
    assert naive_mean < 0.75 * true_mean, \
        f"Naive mean {naive_mean:.1f} should underestimate true mean {true_mean}"
    assert abs(km_mean - true_mean) < 30.0, \
        f"KM mean {km_mean:.1f} should recover near true mean {true_mean}"

    print("PASS")
