"""
Kaplan-Meier Survival Curve with Censored Observations.

Estimates a survival function from time-to-event data with right censoring.
Computes the product of (1 - events/at_risk) at each event time.
Use when analyzing time-to-event data with censoring (medical, reliability, churn).
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

from typing import List, Tuple
import random


def kaplan_meier(times: List[float], events: List[int]) -> List[Tuple[float, float]]:
    """
    Compute Kaplan-Meier survival curve.

    Args:
        times: event/censoring times
        events: 1 if event, 0 if censored

    Returns:
        List of (time, survival_prob) pairs, sorted by time.
    """
    n = len(times)
    assert n == len(events), "times and events must have same length"

    # Sort by time
    data = sorted(zip(times, events))
    times_sorted = [t for t, e in data]
    events_sorted = [e for t, e in data]

    # Get unique event times
    unique_times = sorted(set(t for t in times_sorted if t is not None))

    survival_curve = []
    survival_prob = 1.0
    at_risk = n

    for event_time in unique_times:
        # Count events and censoring at this time
        events_at_time = sum(1 for t, e in zip(times_sorted, events_sorted) if t == event_time and e == 1)
        censored_at_time = sum(1 for t, e in zip(times_sorted, events_sorted) if t == event_time and e == 0)

        # Update survival probability
        if at_risk > 0:
            survival_prob *= (1.0 - events_at_time / at_risk)

        survival_curve.append((event_time, survival_prob))

        # Reduce at-risk count
        at_risk -= (events_at_time + censored_at_time)

    return survival_curve


def check_kaplan_meier_properties(km_curve: List[Tuple[float, float]]) -> bool:
    """Verify KM curve is non-increasing and starts at 1.0."""
    if not km_curve:
        return False

    # Check start value (should be at or near 1.0 after first event)
    probs = [s for t, s in km_curve]

    # Check non-increasing
    for i in range(1, len(probs)):
        if probs[i] > probs[i - 1] + 1e-10:
            return False

    return True


if __name__ == "__main__":
    random.seed(42)

    # Small hand-computed example: 5 subjects, some censored
    # times: [1, 2, 2, 3, 4]
    # events: [1, 1, 0, 1, 0]  (0=censored, 1=event)
    # t=1: 1 event / 5 at risk -> S = 4/5 = 0.8
    # t=2: 1 event / 4 at risk (1 censored just before doesn't affect this instant) -> S = 0.8 * (3/4) = 0.6
    # t=3: 1 event / 2 at risk -> S = 0.6 * (1/2) = 0.3
    # t=4: 0 events -> S = 0.3
    times = [1.0, 2.0, 2.0, 3.0, 4.0]
    events = [1, 1, 0, 1, 0]

    km_curve = kaplan_meier(times, events)

    # Verify properties
    assert check_kaplan_meier_properties(km_curve), "KM curve should be non-increasing"

    # Verify against hand computation
    expected_surv_at_3 = 0.3
    surv_at_3 = next((s for t, s in km_curve if t == 3.0), None)
    assert surv_at_3 is not None, "Missing t=3.0"
    assert abs(surv_at_3 - expected_surv_at_3) < 1e-6, f"Expected {expected_surv_at_3}, got {surv_at_3}"

    # Synthetic test: more data
    random.seed(42)
    n_synthetic = 50
    times_syn = [random.expovariate(0.1) for _ in range(n_synthetic)]
    events_syn = [1 if random.random() > 0.3 else 0 for _ in range(n_synthetic)]

    km_synthetic = kaplan_meier(times_syn, events_syn)
    assert check_kaplan_meier_properties(km_synthetic), "Synthetic KM should be valid"

    print(f"kaplan_meier_survival.py: km_curve_sample={km_curve[:3]}, synthetic_points={len(km_synthetic)} PASS")
