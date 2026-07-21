import math
"""
Queue Capacity Planner — simulate your queue's future before you deploy it.

CROSS-SPHERE COMPOSED PATTERN: async_task_queue (programming sphere,
awesome-python-patterns) x discrete_event_simulation (DS Simulation &
Decision Science) — embedding bridge 0.479, found 2026-07-06. The programming
sphere builds task queues; the DS sphere predicts waiting lines. Composed: a
discrete-event model of the queue answers "how many workers meet the SLA at
projected load?" BEFORE the load arrives. The simulator is validated against
exact M/M/1 theory first — trust is earned where theory exists, then spent
where it doesn't.

Use when: capacity planning for worker pools, sizing before launch.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import heapq
import random
from typing import Dict, List, Tuple




class AuraInputError(ValueError):
    """All input-contract violations, reported together (accumulate-then-raise)."""
    def __init__(self, violations):
        self.violations = violations
        super().__init__("input contract violated:\n  " + "\n  ".join(violations))

def _aura_validate_plan_capacity(service_rate, sla_mean_wait):
    v = []
    if isinstance(service_rate, (int, float)) and not math.isfinite(service_rate):
        v.append(f"AURA-E008: service_rate must be finite, got {service_rate}")
    if isinstance(service_rate, (int, float)) and service_rate <= 0:
        v.append(f"AURA-E001: service_rate must be > 0, got {service_rate}")
    if isinstance(sla_mean_wait, (int, float)) and not math.isfinite(sla_mean_wait):
        v.append(f"AURA-E008: sla_mean_wait must be finite, got {sla_mean_wait}")
    if isinstance(sla_mean_wait, (int, float)) and sla_mean_wait <= 0:
        v.append(f"AURA-E009: sla_mean_wait must be > 0, got {sla_mean_wait}")
    if v:
        raise AuraInputError(v)

def _aura_validate_simulate_queue(arrival_rate, service_rate):
    v = []
    if isinstance(arrival_rate, (int, float)) and not math.isfinite(arrival_rate):
        v.append(f"AURA-E008: arrival_rate must be finite, got {arrival_rate}")
    if isinstance(arrival_rate, (int, float)) and arrival_rate <= 0:
        v.append(f"AURA-E001: arrival_rate must be > 0, got {arrival_rate}")
    if isinstance(service_rate, (int, float)) and not math.isfinite(service_rate):
        v.append(f"AURA-E008: service_rate must be finite, got {service_rate}")
    if isinstance(service_rate, (int, float)) and service_rate <= 0:
        v.append(f"AURA-E001: service_rate must be > 0, got {service_rate}")
    if v:
        raise AuraInputError(v)

def simulate_queue(arrival_rate: float, service_rate: float, workers: int,
                   n_jobs: int, seed: int) -> Dict[str, float]:
    """Discrete-event simulation: Poisson arrivals, exponential service,
    `workers` parallel servers, FIFO queue. Returns wait statistics."""
    _aura_validate_simulate_queue(arrival_rate, service_rate)
    rng = random.Random(seed)
    t, arrivals = 0.0, []
    for _ in range(n_jobs):
        t += rng.expovariate(arrival_rate)
        arrivals.append(t)

    free_at = [0.0] * workers          # heap of worker-free times
    heapq.heapify(free_at)
    waits: List[float] = []
    served = 0
    for at in arrivals:
        worker_free = heapq.heappop(free_at)
        start = max(at, worker_free)
        waits.append(start - at)
        heapq.heappush(free_at, start + rng.expovariate(service_rate))
        served += 1

    assert served == len(arrivals), "conservation: every arrival must be served"
    waits_sorted = sorted(waits)
    return {"mean_wait": sum(waits) / len(waits),
            "p90_wait": waits_sorted[int(0.9 * len(waits))]}


def plan_capacity(arrival_rate: float, service_rate: float, sla_mean_wait: float,
                  n_jobs: int = 30000) -> Tuple[int, Dict[int, float]]:
    """Smallest worker count whose simulated mean wait meets the SLA."""
    _aura_validate_plan_capacity(service_rate, sla_mean_wait)
    results: Dict[int, float] = {}
    k = max(1, int(arrival_rate / service_rate) + 1)   # start at stability
    while k < 50:
        mw = simulate_queue(arrival_rate, service_rate, k, n_jobs, seed=k)["mean_wait"]
        results[k] = mw
        if mw <= sla_mean_wait:
            return k, results
        k += 1
    raise RuntimeError("no worker count met the SLA")


if __name__ == "__main__":
    random.seed(42)

    # STEP 1 — EARN TRUST WHERE THEORY EXISTS: single worker = M/M/1, whose
    # exact mean queueing delay is Wq = rho / (mu - lambda).
    lam, mu = 6.0, 10.0
    rho = lam / mu
    wq_theory = rho / (mu - lam)
    sim = simulate_queue(lam, mu, workers=1, n_jobs=200000, seed=1)
    rel_err = abs(sim["mean_wait"] - wq_theory) / wq_theory
    print(f"M/M/1 validation: simulated Wq {sim['mean_wait']:.4f} vs "
          f"theory {wq_theory:.4f} (rel err {rel_err:.1%})")
    assert rel_err < 0.05, f"simulator must match M/M/1 theory within 5%: {rel_err:.1%}"

    # STEP 2 — SPEND TRUST WHERE THEORY IS MESSY: projected production load,
    # SLA on mean wait, find the minimal worker pool.
    lam_prod, mu_prod, sla = 40.0, 9.0, 0.010   # 40 rps, ~9/s per worker, 10ms
    k_star, curve = plan_capacity(lam_prod, mu_prod, sla)
    print(f"capacity plan: {k_star} workers "
          f"(wait curve: {', '.join(f'{k}->{w*1000:.0f}ms' for k, w in sorted(curve.items()))})")

    # The plan must be MINIMAL: k* meets the SLA, k*-1 must violate it.
    below = simulate_queue(lam_prod, mu_prod, k_star - 1, 30000, seed=k_star - 1)
    at = simulate_queue(lam_prod, mu_prod, k_star, 30000, seed=k_star)
    print(f"check: {k_star-1} workers -> {below['mean_wait']*1000:.1f}ms (violates) · "
          f"{k_star} workers -> {at['mean_wait']*1000:.1f}ms (meets)")
    assert at["mean_wait"] <= sla, "chosen pool must meet the SLA"
    assert below["mean_wait"] > sla, "one fewer worker must violate the SLA (minimality)"

    # More workers must never make waiting worse (sanity of the curve).
    ks = sorted(curve)
    assert all(curve[a] >= curve[b] - 1e-9 for a, b in zip(ks, ks[1:])), \
        "mean wait should be non-increasing in worker count"
    print("queue_capacity_planner.py PASS")
