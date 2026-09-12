"""
P² Quantile Estimator (Jain & Chlamtac, 1985) — streaming quantiles in O(1) memory.

The REAL P² algorithm: exactly FIVE markers track (min, p/2, p, (1+p)/2, max).
Each new observation shifts marker positions; when a marker drifts from its
desired position, its height is adjusted by PIECEWISE-PARABOLIC (P²)
interpolation, falling back to linear when the parabola would break marker
ordering. No buffer, no window — five numbers summarize the whole stream.

Use when: streaming percentiles (latency p50/p90/p99) with hard memory bounds.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import random
from typing import List


class P2Quantile:
    """Five-marker P² estimator for a single quantile p."""

    def __init__(self, p: float):
        self.p = p
        self._init: List[float] = []   # first five observations
        self.q: List[float] = []       # marker heights
        self.n: List[int] = []         # actual marker positions
        self.d: List[float] = []       # desired marker positions

    def process(self, x: float) -> None:
        if len(self._init) < 5:
            self._init.append(x)
            if len(self._init) == 5:
                self._init.sort()
                self.q = self._init[:]
                self.n = [1, 2, 3, 4, 5]
                self.d = [1.0, 1 + 2 * self.p, 1 + 4 * self.p, 3 + 2 * self.p, 5.0]
            return

        # locate the cell containing x (adjusting extremes)
        if x < self.q[0]:
            self.q[0] = x
            k = 0
        elif x >= self.q[4]:
            self.q[4] = x
            k = 3
        else:
            k = next(i - 1 for i in range(1, 5) if x < self.q[i])

        for i in range(k + 1, 5):
            self.n[i] += 1
        incr = [0.0, self.p / 2, self.p, (1 + self.p) / 2, 1.0]
        for i in range(5):
            self.d[i] += incr[i]

        # adjust the three interior markers toward their desired positions
        for i in range(1, 4):
            gap = self.d[i] - self.n[i]
            if (gap >= 1 and self.n[i + 1] - self.n[i] > 1) or \
               (gap <= -1 and self.n[i - 1] - self.n[i] < -1):
                s = 1 if gap >= 0 else -1
                qp = self._parabolic(i, s)
                if not (self.q[i - 1] < qp < self.q[i + 1]):
                    qp = self._linear(i, s)
                self.q[i] = qp
                self.n[i] += s

    def _parabolic(self, i: int, s: int) -> float:
        return self.q[i] + s / (self.n[i + 1] - self.n[i - 1]) * (
            (self.n[i] - self.n[i - 1] + s) * (self.q[i + 1] - self.q[i])
            / (self.n[i + 1] - self.n[i])
            + (self.n[i + 1] - self.n[i] - s) * (self.q[i] - self.q[i - 1])
            / (self.n[i] - self.n[i - 1]))

    def _linear(self, i: int, s: int) -> float:
        return self.q[i] + s * (self.q[i + s] - self.q[i]) / (self.n[i + s] - self.n[i])

    def query(self) -> float:
        if len(self._init) < 5:
            srt = sorted(self._init)
            return srt[len(srt) // 2] if srt else 0.0
        return self.q[2]

    @property
    def memory_markers(self) -> int:
        return len(self.q)


if __name__ == "__main__":
    random.seed(42)
    data = [random.gauss(100, 15) for _ in range(5000)]

    est_med, est_p90 = P2Quantile(0.5), P2Quantile(0.9)
    for x in data:
        est_med.process(x)
        est_p90.process(x)

    srt = sorted(data)
    exact_med = srt[len(srt) // 2]
    exact_p90 = srt[int(len(srt) * 0.9)]
    err_med = abs(est_med.query() - exact_med)
    err_p90 = abs(est_p90.query() - exact_p90)

    print(f"median: exact {exact_med:.2f} · P² {est_med.query():.2f} · err {err_med:.3f}")
    print(f"p90:    exact {exact_p90:.2f} · P² {est_p90.query():.2f} · err {err_p90:.3f}")
    print(f"memory: {est_med.memory_markers} markers (σ of data = 15)")

    # The claim, measured honestly: five numbers track the stream's quantiles
    # to a small fraction of σ — not "within 2σ", which would accept garbage.
    assert est_med.memory_markers == 5 and not hasattr(est_med, "buffer"), \
        "P² must hold exactly five markers — no buffer"
    assert err_med < 1.5, f"median error should be a small fraction of σ=15: {err_med:.3f}"
    assert err_p90 < 2.5, f"p90 error should be a small fraction of σ=15: {err_p90:.3f}"
    print("p2_quantile_estimator.py PASS")
