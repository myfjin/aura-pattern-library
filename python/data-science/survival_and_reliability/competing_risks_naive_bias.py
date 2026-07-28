"""Competing risks: the naive 1−KM overestimates incidence; Aalen-Johansen is correct.

With competing events, a common MISTAKE is to estimate the cumulative incidence of
cause 1 as 1 − KM, where the cause-specific Kaplan-Meier treats every competing event
(and censoring) as if it were independent right-censoring. That double-counts the people
removed by the competing risk and OVERSTATES the incidence. The correct Aalen-Johansen
CIF weights each cause-1 hazard increment by the overall survival S(t⁻):
    F₁(t) = Σ_{s≤t} [d₁(s)/Y(s)] · S(s⁻),  S(s) = ∏ (1 − d_any(s)/Y(s)).
Core claim: with censoring present, naive (1−KM) > correct (Aalen-Johansen); bias shown.
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

def _aura_validate_aalen_johansen_cif(event_type):
    v = []
    if isinstance(event_type, (int, float)) and event_type <= 0:
        v.append(f"AURA-E009: event_type must be > 0, got {event_type}")
    if v:
        raise AuraInputError(v)

def _aura_validate_naive_km_cif(event_type):
    v = []
    if isinstance(event_type, (int, float)) and event_type <= 0:
        v.append(f"AURA-E009: event_type must be > 0, got {event_type}")
    if v:
        raise AuraInputError(v)

def naive_km_cif(times: List[float], events: List[int], event_type: int) -> Tuple[List[float], List[float]]:
    """NAIVE cumulative incidence = 1 − (cause-specific Kaplan-Meier).

    Treats competing events and censoring alike as independent censoring — the classic
    error that overestimates incidence.
    """
    _aura_validate_naive_km_cif(event_type)
    n = len(times)
    event_times = sorted(set(times))
    surv = 1.0
    cif = [0.0]
    times_out = [0.0]
    for t in event_times:
        d_type = sum(1 for i in range(n) if times[i] == t and events[i] == event_type)
        y_t = sum(1 for i in range(n) if times[i] >= t)
        if y_t > 0:
            surv *= (1 - d_type / y_t)
        cif.append(1 - surv)
        times_out.append(t)
    return times_out, cif

def aalen_johansen_cif(times: List[float], events: List[int], event_type: int) -> Tuple[List[float], List[float]]:
    """CORRECT cumulative incidence (Aalen-Johansen): cause-1 hazard weighted by S(t⁻)."""
    _aura_validate_aalen_johansen_cif(event_type)
    n = len(times)
    event_times = sorted(set(times))
    cif = [0.0]
    times_out = [0.0]
    surv = 1.0  # overall survival S(t⁻), all causes
    for t in event_times:
        d_type = sum(1 for i in range(n) if times[i] == t and events[i] == event_type)
        d_any = sum(1 for i in range(n) if times[i] == t and events[i] != 0)  # any-cause EVENTS (not censoring)
        y_t = sum(1 for i in range(n) if times[i] >= t)
        if y_t > 0:
            cif.append(cif[-1] + (d_type / y_t) * surv)
            surv *= (1 - d_any / y_t)
        else:
            cif.append(cif[-1])
        times_out.append(t)
    return times_out, cif

if __name__ == "__main__":
    import random
    random.seed(42)

    # Planted: two competing failure causes + independent right-censoring.
    # Censoring is essential — it is what makes the naive 1−KM overestimate.
    times = []
    events = []  # 0 = censored, 1 = cause 1, 2 = cause 2
    for _ in range(300):
        t1 = random.expovariate(0.5)
        t2 = random.expovariate(0.3)
        c = random.expovariate(0.15)
        t = min(t1, t2, c)
        times.append(t)
        events.append(0 if t == c else (1 if t1 < t2 else 2))

    _, cif_naive = naive_km_cif(times, events, event_type=1)
    _, cif_correct = aalen_johansen_cif(times, events, event_type=1)

    final_naive = cif_naive[-1]
    final_correct = cif_correct[-1]

    # Defining property: naive (1−KM) OVERSTATES incidence vs Aalen-Johansen.
    # Measured (seed 42): naive≈0.917, correct≈0.571, gap≈0.35 (with ~53 censored).
    assert final_naive > final_correct + 0.1, \
        f"Naive 1−KM {final_naive:.3f} should overstate correct AJ CIF {final_correct:.3f}"
    # Aalen-Johansen CIF is a valid probability (competing risk keeps it below 1).
    assert 0.0 < final_correct < 1.0, f"AJ CIF out of range: {final_correct}"
    assert final_naive <= 1.0 + 1e-9, f"1−KM should not exceed 1: {final_naive}"

    print("PASS")
