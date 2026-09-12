"""Bayes factor for comparing two normal means: H1 (θ ≠ 0) vs H0 (θ = 0) — CORRECTED.

BF = p(data|H1) / p(data|H0), data ~ N(θ, 1), H1: θ ~ N(0, prior_var_h1).
Correct closed form: log BF = -0.5·log(1+n·τ²) + 0.5·τ²·(Σy)²/(1+n·τ²)
(the shipped version used y_mean²·n instead of τ²·(Σy)² — missing factor n·τ²,
verified wrong against brute-force numeric integration, 2026-07-19).
"""
import math

class AuraInputError(ValueError):
    def __init__(self, violations):
        self.violations = violations
        super().__init__("input contract violated:\n  " + "\n  ".join(violations))

def _validate(data, prior_var_h1):
    v = []
    if not isinstance(data, list) or len(data) == 0:
        v.append("AURA-E-B8: data must be a non-empty list (BF from no data is undefined here by contract)")
    else:
        for i, y in enumerate(data):
            if not isinstance(y, (int, float)) or isinstance(y, bool) or not math.isfinite(y):
                v.append(f"AURA-E008: data[{i}] non-finite/non-numeric: {y!r}")
                break
    if not (isinstance(prior_var_h1, (int, float)) and prior_var_h1 > 0):
        v.append(f"AURA-E-B5: prior_var_h1 must be > 0 (a variance), got {prior_var_h1!r}")
    if v: raise AuraInputError(v)

def bayes_factor_normal(data, prior_var_h1=1.0) -> float:
    _validate(data, prior_var_h1)
    n, S = len(data), sum(data)
    denom = 1.0 + n * prior_var_h1
    log_bf = -0.5 * math.log(denom) + 0.5 * prior_var_h1 * S * S / denom
    return math.exp(log_bf) if log_bf < 700 else float("inf")

if __name__ == "__main__":
    import random
    random.seed(42)
    data_h1 = [random.gauss(2.0, 1.0) for _ in range(30)]
    data_h0 = [random.gauss(0.0, 1.0) for _ in range(30)]
    bf_h1 = bayes_factor_normal(data_h1, 1.0)
    bf_h0 = bayes_factor_normal(data_h0, 1.0)
    assert bf_h1 > 1.0, f"BF under H1 {bf_h1} should be > 1"
    assert bf_h0 < 1.0, f"BF under H0 {bf_h0} should be < 1"
    print(f"PASS: BF(H1-data)={bf_h1:.3g}>1 · BF(H0-data)={bf_h0:.3g}<1")
    print()
    print("=== Illia's 300-identical-points case (code shipped 0.42 — sign-flipped) ===")
    print("corrected BF:", bayes_factor_normal([2.0]*300, 1.0))
    print()
    print("=== attacks ===")
    for label, args in [("empty data", ([], 1.0)),
                        ("NaN in data", ([float("nan"), 1.0, 2.0], 1.0)),
                        ("negative prior variance", ([1.0, 2.0, 3.0], -1.0))]:
        try:
            print(f"  {label}: {bayes_factor_normal(*args)} !! SILENT")
        except AuraInputError as e:
            print(f"  {label}:")
            for viol in e.violations: print(f"      {viol}")
