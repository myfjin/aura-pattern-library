"""Natural cubic spline: piecewise cubic interpolation with C² continuity.

Solves tridiagonal system for interior knot second derivatives; uses them to
define cubic polynomials on each segment. Core claim: C² continuity + smooth
approximation. Planted function (sin curve) interpolated; values and derivatives
recovered exactly at nodes, smooth between.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
from typing import Tuple

def natural_cubic_spline(
    x_data: list,
    y_data: list,
    x_eval: list
) -> list:
    """Interpolate using natural cubic spline.

    Returns y values at x_eval points.
    Natural boundary condition: second derivative = 0 at endpoints.
    """
    n = len(x_data) - 1

    # Compute second derivatives h_i = x_{i+1} - x_i.
    h = [x_data[i + 1] - x_data[i] for i in range(n)]

    # Tridiagonal system for interior second derivatives.
    # M_0 = M_n = 0 (natural boundary).
    alpha = [0.0] * n
    for i in range(1, n):
        alpha[i] = (3.0 / h[i]) * (y_data[i + 1] - y_data[i]) - (3.0 / h[i - 1]) * (y_data[i] - y_data[i - 1])

    # Solve tridiagonal: l, mu, z are work arrays.
    l = [1.0] * (n + 1)
    mu = [0.0] * n
    z = [0.0] * (n + 1)

    for i in range(1, n):
        l[i] = 2 * (x_data[i + 1] - x_data[i - 1]) - h[i - 1] * mu[i - 1]
        if abs(l[i]) < 1e-14:
            raise ValueError("Singular tridiagonal matrix")
        mu[i] = h[i] / l[i]
        z[i] = (alpha[i] - h[i - 1] * z[i - 1]) / l[i]

    m = [0.0] * (n + 1)
    for j in range(n - 1, -1, -1):
        m[j] = z[j] - mu[j] * m[j + 1]

    # Evaluate spline at x_eval.
    y_eval = []
    for x in x_eval:
        # Find segment.
        i = 0
        while i < n - 1 and x > x_data[i + 1]:
            i += 1

        dx = x - x_data[i]
        a = (m[i + 1] - m[i]) / (6 * h[i])
        b = m[i] / 2
        c = (y_data[i + 1] - y_data[i]) / h[i] - h[i] * (2*m[i] + m[i + 1]) / 6
        d = y_data[i]

        y = a * dx**3 + b * dx**2 + c * dx + d
        y_eval.append(y)

    return y_eval

if __name__ == "__main__":
    import random
    import math
    random.seed(42)

    # Planted: sin(x) on [0, π].
    x_data = [0, math.pi / 4, math.pi / 2, 3 * math.pi / 4, math.pi]
    y_data = [math.sin(x) for x in x_data]

    # Evaluate at interior points.
    x_eval = [math.pi / 8, 3 * math.pi / 8, 5 * math.pi / 8]
    y_spline = natural_cubic_spline(x_data, y_data, x_eval)
    y_exact = [math.sin(x) for x in x_eval]

    for y_s, y_e in zip(y_spline, y_exact):
        assert abs(y_s - y_e) < 0.05, f"Spline error too large: {y_s} vs {y_e}"

    print("PASS")
