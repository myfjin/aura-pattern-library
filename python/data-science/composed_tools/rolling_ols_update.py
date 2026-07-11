"""
Rolling OLS Update — a running balance instead of a recount.

FUSED-BRIDGE COMPOSED PATTERN: online_covariance (Streaming & Sketches) x
sliding_window_regression (Time Series) — proposed by BOTH signals 2026-07-10:
structural edge `matrix` (an incremental covariance feeds the slope formula) +
semantic 0.408. sliding_window_regression REFITS OLS from scratch every step —
O(window) work per sample. Since the OLS slope is just cov(x,y)/var(x), the
composition maintains the window's covariance INCREMENTALLY (subtract the
departing point, add the arriving point, Welford-style) and reads the slope off
it: identical coefficients, O(1) per step instead of O(window).

Human logic of the name: a bank teller adjusts the balance per transaction
rather than recounting all the money each time a customer arrives.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import random
from collections import deque
from typing import Deque, List, Tuple

OPS = {"refit": 0, "rolling": 0}


def naive_windowed_slope(xs: List[float], ys: List[float], w: int) -> List[Tuple[float, float]]:
    """Parent: recompute OLS (intercept, slope) over each window from scratch."""
    out = []
    for end in range(w, len(xs) + 1):
        wx, wy = xs[end - w:end], ys[end - w:end]
        n = w
        mx = sum(wx) / n
        my = sum(wy) / n
        OPS["refit"] += n                      # the full re-pass over the window
        sxy = sum((wx[i] - mx) * (wy[i] - my) for i in range(n))
        sxx = sum((wx[i] - mx) ** 2 for i in range(n))
        slope = sxy / sxx if sxx > 0 else 0.0
        out.append((my - slope * mx, slope))
    return out


class RollingCovariance:
    """Child mechanism: window covariance maintained by add/remove (rolling
    Welford). add() folds in the arriving point; remove() folds out the
    departing one — the incremental covariance online_covariance produces,
    made two-sided so it works over a sliding window."""

    def __init__(self) -> None:
        self.n = 0
        self.mx = self.my = 0.0
        self.cxy = 0.0     # sum (x-mx)(y-my)
        self.cxx = 0.0     # sum (x-mx)^2

    def add(self, x: float, y: float) -> None:
        self.n += 1
        dx, dy = x - self.mx, y - self.my
        self.mx += dx / self.n
        self.my += dy / self.n
        self.cxy += dx * (y - self.my)
        self.cxx += dx * (x - self.mx)
        OPS["rolling"] += 1

    def remove(self, x: float, y: float) -> None:
        # exact inverse of add (Welford downdate)
        dx_old, dy_old = x - self.mx, y - self.my
        self.n -= 1
        if self.n == 0:
            self.mx = self.my = self.cxy = self.cxx = 0.0
            OPS["rolling"] += 1
            return
        self.mx -= dx_old / self.n
        self.my -= dy_old / self.n
        self.cxy -= dx_old * (y - self.my)
        self.cxx -= dx_old * (x - self.mx)
        OPS["rolling"] += 1

    def slope_intercept(self) -> Tuple[float, float]:
        slope = self.cxy / self.cxx if self.cxx > 1e-12 else 0.0
        return (self.my - slope * self.mx, slope)


def rolling_windowed_slope(xs: List[float], ys: List[float], w: int) -> List[Tuple[float, float]]:
    """Child: same time-varying slope via rolling covariance, O(1) per step."""
    rc = RollingCovariance()
    buf: Deque[Tuple[float, float]] = deque()
    out = []
    for x, y in zip(xs, ys):
        rc.add(x, y)
        buf.append((x, y))
        if len(buf) > w:
            ox, oy = buf.popleft()
            rc.remove(ox, oy)
        if len(buf) == w:
            out.append(rc.slope_intercept())
    return out


if __name__ == "__main__":
    random.seed(42)

    # Stream with a PLANTED time-varying slope: 0.5 for the first half, 2.5
    # after — both methods must track the change.
    n, w = 400, 40
    xs, ys = [], []
    for t in range(n):
        slope = 0.5 if t < n // 2 else 2.5
        x = random.uniform(0, 10)
        xs.append(x)
        ys.append(slope * x + random.gauss(0, 0.5))

    naive = naive_windowed_slope(xs, ys, w)
    rolling = rolling_windowed_slope(xs, ys, w)

    max_dev = max(abs(a[1] - b[1]) for a, b in zip(naive, rolling))
    # slope well before and well after the change (window fully in each regime)
    early = rolling[w // 2][1]
    late = rolling[-1][1]
    ratio = OPS["rolling"] / OPS["refit"]
    print(f"windows: {len(rolling)} · max slope deviation naive-vs-rolling: {max_dev:.2e}")
    print(f"tracked slope: early {early:.2f} (true 0.5) · late {late:.2f} (true 2.5)")
    print(f"per-step work: rolling {OPS['rolling']} vs refit {OPS['refit']} ({ratio:.1%})")

    # The composed claim, both halves measured (equivalence + efficiency):
    assert max_dev < 1e-8, f"rolling must equal naive refit to machine precision: {max_dev:.2e}"
    assert abs(early - 0.5) < 0.3 and abs(late - 2.5) < 0.3, \
        f"must track the planted slope change: {early:.2f} -> {late:.2f}"
    assert ratio < 0.10, \
        f"rolling should do <10% of refit's work (O(1) vs O(w)): {ratio:.1%}"
    print("rolling_ols_update.py PASS")
