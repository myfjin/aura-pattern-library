#!/usr/bin/env python3
"""
Lamport Clock Pattern
Logical clock for causality ordering in distributed systems.
Not wall-clock time. Step manually, track total order.
Assert: clock is monotonic, happens-before ordering is preserved.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import json
import tempfile
import os
from dataclasses import dataclass


@dataclass
class LamportClock:
    """Lamport logical clock."""
    value: int

    def increment(self):
        """Local event: increment."""
        self.value += 1
        return self.value

    def see(self, other_ts):
        """Receive message with other_ts: max(local, other) + 1."""
        self.value = max(self.value, other_ts) + 1
        return self.value

    def read(self):
        """Read current value without incrementing."""
        return self.value


def test_lamport_clock():
    """
    Two processes: A and B.
    A sends to B, B increments.
    Assert: B's clock > A's clock (happened after).
    """
    clock_a = LamportClock(value=0)
    clock_b = LamportClock(value=0)

    # A: local event
    ts_a1 = clock_a.increment()
    assert ts_a1 == 1, f"A should be at 1, got {ts_a1}"

    # A sends message with ts=1 to B
    # B receives message
    ts_b1 = clock_b.see(ts_a1)
    assert ts_b1 == 2, f"B should be at 2 (max(0,1)+1), got {ts_b1}"
    assert ts_b1 > ts_a1, "B's clock must be > A's when B receives A's message"

    # B: another local event
    ts_b2 = clock_b.increment()
    assert ts_b2 == 3, f"B should be at 3, got {ts_b2}"

    # B sends to A
    ts_a2 = clock_a.see(ts_b2)
    assert ts_a2 == 4, f"A should be at 4 (max(1,3)+1), got {ts_a2}"
    assert ts_a2 > ts_b2, "A's clock must be > B's when A receives B's message"


def test_lamport_monotonic():
    """
    Assert: clock never decreases, always increases or stays same.
    """
    clock = LamportClock(value=5)

    # Local increment
    ts1 = clock.increment()
    assert ts1 == 6

    # Receive message with older timestamp
    ts2 = clock.see(2)  # max(6, 2) + 1 = 7
    assert ts2 == 7
    assert ts2 >= ts1, "Clock should be monotonic"

    # Another local event
    ts3 = clock.increment()
    assert ts3 == 8
    assert ts3 >= ts2


def test_lamport_causality():
    """
    Three processes forming a chain: A -> B -> C.
    Assert: C's clock > B's clock > A's clock (causal order preserved).
    """
    clocks = {
        'A': LamportClock(value=0),
        'B': LamportClock(value=0),
        'C': LamportClock(value=0)
    }

    # A sends to B
    ts_a = clocks['A'].increment()  # A: 1
    ts_b1 = clocks['B'].see(ts_a)   # B: max(0,1)+1 = 2

    # B sends to C
    ts_c1 = clocks['C'].see(ts_b1)  # C: max(0,2)+1 = 3

    # Verify causal chain
    assert ts_c1 > ts_b1 > ts_a, \
        f"Causal order broken: A={ts_a}, B={ts_b1}, C={ts_c1}"


def test_lamport_concurrent_events():
    """
    Two processes A and B run independently (no communication).
    Timestamps increase but don't reflect ordering.
    Assert: both clocks increment.
    """
    clock_a = LamportClock(value=0)
    clock_b = LamportClock(value=0)

    # Concurrent local events
    ts_a1 = clock_a.increment()  # A: 1
    ts_b1 = clock_b.increment()  # B: 1

    ts_a2 = clock_a.increment()  # A: 2
    ts_b2 = clock_b.increment()  # B: 2

    # No communication, so clocks don't sync
    assert ts_a2 == 2
    assert ts_b2 == 2
    # Both can have same timestamp for concurrent events


def test_failure_wall_clock():
    """
    Counter-example: using wall-clock time instead of Lamport clock.
    """
    import time

    # Bug: using time.time() as timestamp
    ts_a1 = time.time()
    ts_b1 = time.time()  # May be before or after ts_a1 depending on system

    # Can't rely on wall-clock ordering for causality
    # (time skew, system clock adjustments)
    pass


if __name__ == '__main__':
    test_lamport_clock()
    test_lamport_monotonic()
    test_lamport_causality()
    test_lamport_concurrent_events()
    test_failure_wall_clock()
    print("✓ lamport_clock passed")
