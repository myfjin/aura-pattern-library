#!/usr/bin/env python3
"""
Distributed Lock with Lease Pattern
Lock expires after lease_ttl (logical time, not wall-clock).
Assert: lock is reacquirable after expiry, holder can renew.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"


class Lease:
    def __init__(self, holder_id, grant_time, lease_ttl):
        self.holder_id = holder_id
        self.grant_time = grant_time
        self.lease_ttl = lease_ttl

    def is_expired(self, current_time):
        """Check if lease expired."""
        return current_time > self.grant_time + self.lease_ttl


class DistributedLock:
    def __init__(self, lease_ttl=10):
        self.lease_ttl = lease_ttl
        self.lease = None
        self.current_time = 0

    def tick(self):
        """Advance logical time."""
        self.current_time += 1

    def acquire(self, holder_id):
        """
        Try to acquire lock.
        Success if no lease or lease expired.
        """
        if self.lease is None:
            self.lease = Lease(holder_id, self.current_time, self.lease_ttl)
            return True

        if self.lease.is_expired(self.current_time):
            self.lease = Lease(holder_id, self.current_time, self.lease_ttl)
            return True

        return False

    def renew(self, holder_id):
        """
        Holder renews lease.
        Success if current holder.
        """
        if self.lease and self.lease.holder_id == holder_id:
            if not self.lease.is_expired(self.current_time):
                self.lease = Lease(holder_id, self.current_time, self.lease_ttl)
                return True

        return False

    def holder(self):
        """Get current lock holder, or None."""
        if self.lease and not self.lease.is_expired(self.current_time):
            return self.lease.holder_id
        return None


def test_lease_acquire():
    """
    Lock holder A acquires lock.
    Assert: A has lock.
    """
    lock = DistributedLock(lease_ttl=10)

    assert lock.acquire('A'), "A should acquire lock"
    assert lock.holder() == 'A', "A should be holder"

    # B tries to acquire while A has lease
    assert not lock.acquire('B'), "B should not acquire while A holds"
    assert lock.holder() == 'A', "A still holds"


def test_lease_expiry():
    """
    A acquires lock (ttl=10).
    Wait ttl time units, lease expires.
    B can then acquire.
    """
    lock = DistributedLock(lease_ttl=10)

    assert lock.acquire('A'), "A acquires"
    assert lock.holder() == 'A'

    # Advance time to grant_time + ttl
    for _ in range(10):
        lock.tick()

    assert lock.holder() == 'A', "A still holds at grant_time + ttl"

    # One more tick
    lock.tick()

    assert lock.holder() is None, "Lease expired"
    assert lock.acquire('B'), "B can acquire after expiry"
    assert lock.holder() == 'B'


def test_lease_renew():
    """
    A acquires, renews before expiry.
    Assert: A keeps lock after renewal.
    """
    lock = DistributedLock(lease_ttl=10)

    assert lock.acquire('A'), "A acquires"
    grant_time_1 = lock.current_time

    # A waits 5 time units
    for _ in range(5):
        lock.tick()

    # A renews before expiry
    assert lock.renew('A'), "A renews successfully"
    grant_time_2 = lock.current_time

    # A should now have lease until grant_time_2 + ttl
    for _ in range(10):
        lock.tick()

    # At grant_time_2 + ttl, lease still valid
    assert lock.holder() == 'A'

    # One more tick: expires
    lock.tick()
    assert lock.holder() is None


def test_lease_renew_as_non_holder():
    """
    A holds lock, B tries to renew.
    Assert: B cannot renew.
    """
    lock = DistributedLock(lease_ttl=10)

    assert lock.acquire('A'), "A acquires"
    assert not lock.renew('B'), "B cannot renew (not holder)"
    assert lock.holder() == 'A'


def test_lease_multiple_holders_sequence():
    """
    A -> expires -> B -> expires -> C.
    Assert: exactly one holder at each time.
    """
    lock = DistributedLock(lease_ttl=5)

    # A acquires, holds for 5 time units
    assert lock.acquire('A')
    assert lock.holder() == 'A'

    for _ in range(5):
        lock.tick()
        assert lock.holder() == 'A'

    # One more tick: A's lease expires
    lock.tick()
    assert lock.holder() is None

    # B acquires
    assert lock.acquire('B')
    assert lock.holder() == 'B'

    for _ in range(5):
        lock.tick()
        assert lock.holder() == 'B'

    lock.tick()
    assert lock.holder() is None

    # C acquires
    assert lock.acquire('C')
    assert lock.holder() == 'C'


def test_failure_no_lease_expiry():
    """
    Counter-example: lock without expiry.
    """
    class BuggyLock:
        def __init__(self):
            self.holder = None

        def acquire(self, holder_id):
            if self.holder is None:
                self.holder = holder_id
                return True
            return False

    lock = BuggyLock()
    assert lock.acquire('A')

    # A dies, but lock never expires
    # B can never acquire
    assert not lock.acquire('B')
    assert lock.holder == 'A'  # Stuck!


if __name__ == '__main__':
    test_lease_acquire()
    test_lease_expiry()
    test_lease_renew()
    test_lease_renew_as_non_holder()
    test_lease_multiple_holders_sequence()
    test_failure_no_lease_expiry()
    print("✓ lease_distributed_lock passed")
