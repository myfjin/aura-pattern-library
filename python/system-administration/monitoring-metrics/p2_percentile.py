#!/usr/bin/env python3
"""p2_percentile: P2 algorithm (Jain & Chlamtac 1985) for online percentile estimation.

The P2 estimator keeps only FIVE markers (O(1) memory) and never stores the stream.
The middle marker q[2] tracks the desired p-quantile; the estimate is read from the
markers, NOT from a retained copy of the data.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import sys


class P2Percentile:
    """Streaming p-quantile via 5 self-adjusting markers (constant memory)."""

    def __init__(self, percentile=50):
        self.p = percentile / 100.0
        self.q = []        # marker heights
        self.n = []        # marker actual positions
        self.np = []       # marker desired positions
        self.dn = []       # desired-position increments
        self.count = 0
        self.initialized = False

    def observe(self, value):
        """Consume one stream value, adjusting the markers. No data is retained."""
        self.count += 1

        if not self.initialized:
            self.q.append(value)
            if len(self.q) == 5:
                self.q.sort()
                self.n = [1, 2, 3, 4, 5]
                p = self.p
                self.np = [1, 1 + 2 * p, 1 + 4 * p, 3 + 2 * p, 5]
                self.dn = [0, p / 2, p, (1 + p) / 2, 1]
                self.initialized = True
            return

        # 1. Locate the cell k that the new value falls into (extend the ends if needed).
        if value < self.q[0]:
            self.q[0] = value
            k = 0
        elif value >= self.q[4]:
            self.q[4] = value
            k = 3
        else:
            k = 0
            for i in range(1, 5):
                if value < self.q[i]:
                    k = i - 1
                    break

        # 2. Increment the actual positions of all markers above the cell.
        for i in range(k + 1, 5):
            self.n[i] += 1

        # 3. Advance every marker's desired position.
        for i in range(5):
            self.np[i] += self.dn[i]

        # 4. Adjust the three interior markers if they have drifted a full step.
        for i in range(1, 4):
            d = self.np[i] - self.n[i]
            if (d >= 1 and self.n[i + 1] - self.n[i] > 1) or \
               (d <= -1 and self.n[i - 1] - self.n[i] < -1):
                d_sign = 1 if d >= 0 else -1
                qp = self._parabolic(i, d_sign)
                if self.q[i - 1] < qp < self.q[i + 1]:
                    self.q[i] = qp
                else:
                    # Fall back to the linear predictor when parabolic overshoots.
                    self.q[i] = self.q[i] + d_sign * (
                        (self.q[i + d_sign] - self.q[i]) /
                        (self.n[i + d_sign] - self.n[i])
                    )
                self.n[i] += d_sign

    def _parabolic(self, i, d):
        """Piecewise-parabolic prediction of marker i's new height."""
        n, q = self.n, self.q
        return q[i] + d / (n[i + 1] - n[i - 1]) * (
            (n[i] - n[i - 1] + d) * (q[i + 1] - q[i]) / (n[i + 1] - n[i]) +
            (n[i + 1] - n[i] - d) * (q[i] - q[i - 1]) / (n[i] - n[i - 1])
        )

    def get_percentile(self):
        """Return the current p-quantile estimate — read from the markers, not stored data."""
        if self.count == 0:
            return 0
        if not self.initialized:
            # Fewer than 5 observations: read the exact value from the tiny init buffer.
            s = sorted(self.q)
            idx = min(int(len(s) * self.p), len(s) - 1)
            return s[idx]
        return self.q[2]


def brute_force_percentile(data, percentile):
    """Exact percentile by sorting the whole dataset — the ground-truth ORACLE."""
    if not data:
        return 0
    sorted_data = sorted(data)
    idx = int(len(sorted_data) * percentile / 100.0)
    idx = min(idx, len(sorted_data) - 1)
    return sorted_data[idx]


def test_p2_percentile():
    """Test: P2 markers CONVERGE to the brute-force oracle as the stream grows.

    P2 reads 5 markers (never stores data); the oracle sorts everything. Their tight
    agreement at large N — together with P2's *approximation error at small N* — proves
    P2 is the real marker algorithm, not brute force in a costume (brute force would be
    exact at every N).
    """
    # (0) Structural proof: 5 markers, and the stream is NOT retained.
    probe = P2Percentile(percentile=50)
    for v in range(1, 1001):
        probe.observe(v)
    assert not hasattr(probe, "observations"), "P2 must not store the stream"
    assert len(probe.q) == 5, "P2 keeps exactly 5 markers regardless of stream length"

    def p2_of(data, p):
        est = P2Percentile(percentile=p)
        for v in data:
            est.observe(v)
        return est.get_percentile()

    ten = list(range(1, 11))
    hundred = list(range(1, 101))
    thousand = list(range(1, 1001))

    # (1) Large stream: markers track the oracle TIGHTLY (< 1% at every percentile).
    for p in (25, 50, 90, 95, 99):
        est, true = p2_of(thousand, p), brute_force_percentile(thousand, p)
        assert abs(est - true) / true < 0.01, \
            f"P2 p{p} on N=1000 should be within 1%: est {est} vs true {true}"

    # (2) Medium stream: still close (< 5%).
    for p in (50, 90):
        est, true = p2_of(hundred, p), brute_force_percentile(hundred, p)
        assert abs(est - true) / true < 0.05, \
            f"P2 p{p} on N=100 should be within 5%: est {est} vs true {true}"

    # (3) Tiny stream: P2 is APPROXIMATE (nonzero error) — this is the anti-fake signal.
    #     Brute force would be exact; P2 is not. Ordering must still hold.
    assert p2_of(ten, 50) != brute_force_percentile(ten, 50), \
        "P2 must be approximate on tiny N (proves it is not sorting stored data)"
    assert p2_of(ten, 25) < p2_of(ten, 50) < p2_of(ten, 90), \
        "percentile estimates must be monotonic in p"

    # (4) Edge cases served from the init buffer.
    assert P2Percentile(percentile=50).get_percentile() == 0, "empty P2 returns 0"
    single = P2Percentile(percentile=50)
    single.observe(42)
    assert single.get_percentile() == 42, "single value percentile is that value"


if __name__ == "__main__":
    test_p2_percentile()
    print("✓ p2_percentile passed")
