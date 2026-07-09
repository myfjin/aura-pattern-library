"""Richardson extrapolation: boost convergence order via linear combination.

If F(h) ≈ L + C·h^p + O(h^(2p)) and the step is halved, then
(2^p·F(h/2) - F(h))/(2^p - 1) ≈ L + O(h^(2p)) — the C·h^p term cancels because
F(h/2) carries it scaled by (1/2)^p. Core claim: raises O(h^p) error to O(h^(2p))
without changing the method. Planted integral; error dropped to O(h^(2p)) verified.

NOTE: the elimination factor is 2^p (the halving ratio raised to the order), NOT p.
Using p leaves a residual -C·h^p/2 and stays O(h^p) — see romberg_integration's 4^j.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
from typing import Callable

def richardson_extrapolate(
    F: Callable[[float], float],
    h: float,
    p: int
) -> float:
    """Apply Richardson extrapolation to refine estimate F(h).

    Assumes F(h) has error term C·h^p under step-halving. Returns improved estimate
    with error O(h^(2p)). Computes (2^p·F(h/2) - F(h)) / (2^p - 1).
    """
    f_h = F(h)
    f_h_half = F(h / 2.0)
    factor = 2.0 ** p  # halving ratio (2) raised to the error order p
    return (factor * f_h_half - f_h) / (factor - 1.0)

def midpoint_rule(f: Callable[[float], float], a: float, b: float, h: float) -> float:
    """Midpoint rule: ∑ f(x_i + h/2) · h, O(h²) error."""
    n = int((b - a) / h)
    if n == 0:
        return 0.0
    result = 0.0
    for i in range(n):
        x_mid = a + i * h + h / 2
        result += f(x_mid) * h
    return result

if __name__ == "__main__":
    import random
    import math
    random.seed(42)

    # Planted: ∫₀^1 x³ dx = 1/4.
    def f_planted(x: float) -> float:
        return x**3

    def make_integrator(h: float) -> float:
        return midpoint_rule(f_planted, 0.0, 1.0, h)

    # Midpoint is O(h²), so p = 2.
    h_val = 0.1
    estimate_direct = make_integrator(h_val)
    estimate_extrapolated = richardson_extrapolate(lambda h: make_integrator(h), h_val, p=2)

    exact = 0.25
    error_before = abs(estimate_direct - exact)
    error_after = abs(estimate_extrapolated - exact)

    # Defining property: the O(h²) leading term is CANCELLED, not just shrunk.
    # For a cubic integrand, correct O(h⁴) Richardson on the midpoint rule is exact
    # (error ~ machine epsilon). The broken p-instead-of-2^p form only halves the
    # error to ~6e-4 and stays O(h²) — this bound (1e-10) separates the two.
    assert error_after < error_before, \
        f"Extrapolation did not improve: before {error_before}, after {error_after}"
    assert error_after < 1e-10, \
        f"Order not raised (still O(h²)?): error_after {error_after} — expected ~machine eps"

    print("PASS")
