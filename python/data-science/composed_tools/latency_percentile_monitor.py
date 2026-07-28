"""
Latency Percentile Monitor — p99 tracking in five floats per quantile.

CROSS-SPHERE COMPOSED PATTERN: metric_aggregator (programming sphere,
awesome-python-patterns) x p2_quantile_estimator (DS Streaming & Sketches) —
embedding bridge 0.470, found 2026-07-06. Observability aggregators track
means and counts; means are BLIND to tail regressions. Welding the P²
five-marker estimator into the aggregator gives per-service p50/p99 in O(1)
memory — and the demo plants exactly the failure means cannot see: a
tail-only regression, invisible at p50, screaming at p99.

Use when: service latency monitoring where the tail IS the product.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import math
import random
from typing import Dict, List


class P2Quantile:
    """Compact Jain-Chlamtac P² (five markers, parabolic adjustment)."""

    def __init__(self, p: float):
        self.p = p
        self._init: List[float] = []
        self.q: List[float] = []
        self.n: List[int] = []
        self.d: List[float] = []

    def process(self, x: float) -> None:
        if len(self._init) < 5:
            self._init.append(x)
            if len(self._init) == 5:
                self._init.sort()
                self.q = self._init[:]
                self.n = [1, 2, 3, 4, 5]
                self.d = [1.0, 1 + 2 * self.p, 1 + 4 * self.p, 3 + 2 * self.p, 5.0]
            return
        if x < self.q[0]:
            self.q[0] = x; k = 0
        elif x >= self.q[4]:
            self.q[4] = x; k = 3
        else:
            k = next(i - 1 for i in range(1, 5) if x < self.q[i])
        for i in range(k + 1, 5):
            self.n[i] += 1
        incr = [0.0, self.p / 2, self.p, (1 + self.p) / 2, 1.0]
        for i in range(5):
            self.d[i] += incr[i]
        for i in range(1, 4):
            gap = self.d[i] - self.n[i]
            if (gap >= 1 and self.n[i + 1] - self.n[i] > 1) or \
               (gap <= -1 and self.n[i - 1] - self.n[i] < -1):
                s = 1 if gap >= 0 else -1
                qp = self.q[i] + s / (self.n[i + 1] - self.n[i - 1]) * (
                    (self.n[i] - self.n[i - 1] + s) * (self.q[i + 1] - self.q[i])
                    / (self.n[i + 1] - self.n[i])
                    + (self.n[i + 1] - self.n[i] - s) * (self.q[i] - self.q[i - 1])
                    / (self.n[i] - self.n[i - 1]))
                if not (self.q[i - 1] < qp < self.q[i + 1]):
                    qp = self.q[i] + s * (self.q[i + s] - self.q[i]) / (self.n[i + s] - self.n[i])
                self.q[i] = qp
                self.n[i] += s

    def query(self) -> float:
        if len(self._init) < 5:
            srt = sorted(self._init)
            return srt[len(srt) // 2] if srt else 0.0
        return self.q[2]


class LatencyMonitor:
    """Per-service aggregator: count/mean plus streaming p50 and p99."""

    def __init__(self):
        self.services: Dict[str, Dict] = {}

    def record(self, service: str, latency_ms: float) -> None:
        s = self.services.setdefault(
            service, {"count": 0, "total": 0.0,
                      "p50": P2Quantile(0.5), "p99": P2Quantile(0.99)})
        s["count"] += 1
        s["total"] += latency_ms
        s["p50"].process(latency_ms)
        s["p99"].process(latency_ms)

    def snapshot(self, service: str) -> Dict[str, float]:
        s = self.services[service]
        return {"count": s["count"], "mean": s["total"] / s["count"],
                "p50": s["p50"].query(), "p99": s["p99"].query()}




class AuraInputError(ValueError):
    """All input-contract violations, reported together (accumulate-then-raise)."""
    def __init__(self, violations):
        self.violations = violations
        super().__init__("input contract violated:\n  " + "\n  ".join(violations))

def _aura_validate_lognormalish(tail):
    v = []
    if isinstance(tail, (int, float)) and not math.isfinite(tail):
        v.append(f"AURA-E008: tail must be finite, got {tail}")
    if v:
        raise AuraInputError(v)

def lognormalish(base: float, tail: float) -> float:
    _aura_validate_lognormalish(tail)
    v = random.lognormvariate(0, 0.4) * base
    if random.random() < 0.01:
        v += tail * random.random()
    return v


if __name__ == "__main__":
    random.seed(42)
    mon = LatencyMonitor()

    # Phase 1: healthy service. Phase 2: TAIL-ONLY regression — 5% of requests
    # slow 10x, median traffic untouched (the failure a mean/median can't see).
    phase1 = [lognormalish(50, 300) for _ in range(6000)]
    phase2 = []
    for _ in range(6000):
        v = lognormalish(50, 300)
        if random.random() < 0.05:
            v = 500 + 300 * random.random()
        phase2.append(v)

    for v in phase1:
        mon.record("api", v)
    snap1 = mon.snapshot("api")

    mon2 = LatencyMonitor()
    for v in phase2:
        mon2.record("api", v)
    snap2 = mon2.snapshot("api")

    exact_p99_1 = sorted(phase1)[int(len(phase1) * 0.99)]
    exact_p99_2 = sorted(phase2)[int(len(phase2) * 0.99)]

    print(f"phase1: p50 {snap1['p50']:.0f} · p99 {snap1['p99']:.0f} "
          f"(exact {exact_p99_1:.0f}) · mean {snap1['mean']:.0f}")
    print(f"phase2: p50 {snap2['p50']:.0f} · p99 {snap2['p99']:.0f} "
          f"(exact {exact_p99_2:.0f}) · mean {snap2['mean']:.0f}")

    # The composed claims, measured:
    # 1. streaming p99 tracks exact p99 (relative error), both phases
    assert abs(snap1["p99"] - exact_p99_1) / exact_p99_1 < 0.15, "p99 estimate off (phase1)"
    assert abs(snap2["p99"] - exact_p99_2) / exact_p99_2 < 0.15, "p99 estimate off (phase2)"
    # 2. the tail regression is INVISIBLE at p50 (<25% shift) but LOUD at p99 (>2x)
    assert abs(snap2["p50"] - snap1["p50"]) / snap1["p50"] < 0.25, \
        "median should barely move on a tail-only regression"
    assert snap2["p99"] > 2.0 * snap1["p99"], \
        f"p99 must scream on the tail regression: {snap1['p99']:.0f} -> {snap2['p99']:.0f}"
    # 3. O(1) memory: five markers per quantile, no stored stream
    assert len(mon2.services["api"]["p99"].q) == 5
    print("latency_percentile_monitor.py PASS")
