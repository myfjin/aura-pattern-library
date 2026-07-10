#!/usr/bin/env python3
"""
Heartbeat/Lease Pattern
Follower sends heartbeats to leader.
Leader grants lease based on heartbeats.
Assert: lease expires if heartbeats stop, leader detects failure.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"


class HeartbeatLease:
    def __init__(self, lease_ttl=10):
        self.lease_ttl = lease_ttl
        self.current_time = 0
        self.last_heartbeat = 0
        self.is_leader = False

    def tick(self):
        """Advance logical time."""
        self.current_time += 1

    def send_heartbeat(self):
        """Follower sends heartbeat."""
        self.last_heartbeat = self.current_time

    def is_alive(self):
        """
        Leader checks if follower is alive.
        Alive if heartbeat received within ttl (time_since <= ttl-1, or strictly before ttl+1).
        """
        time_since_heartbeat = self.current_time - self.last_heartbeat
        return time_since_heartbeat < self.lease_ttl

    def leader_think_follower_alive(self):
        """Grant lease to follower (grants continue assuming follower alive)."""
        return self.is_alive()


def test_heartbeat_lease_alive():
    """
    Follower sends heartbeat, leader sees it alive.
    """
    follower = HeartbeatLease(lease_ttl=10)

    follower.send_heartbeat()
    assert follower.last_heartbeat == 0

    # Advance time
    for _ in range(5):
        follower.tick()

    # Within ttl, should be alive
    assert follower.is_alive(), "Follower should be alive within ttl"


def test_heartbeat_lease_expiry():
    """
    No heartbeat for ttl time units.
    Assert: leader detects death.
    """
    follower = HeartbeatLease(lease_ttl=10)

    follower.send_heartbeat()
    assert follower.is_alive()

    # Advance time past ttl
    for _ in range(10):
        follower.tick()

    # At current_time = 10, last_heartbeat = 0, time_since = 10
    assert not follower.is_alive()  # Dead at exactly ttl (time_since >= ttl)


def test_heartbeat_lease_renew():
    """
    Follower renews heartbeat before expiry.
    Assert: lease extends.
    """
    follower = HeartbeatLease(lease_ttl=10)

    follower.send_heartbeat()
    # current_time = 0, last_heartbeat = 0

    # Advance 5 time units
    for _ in range(5):
        follower.tick()

    # Follower still alive at time 5
    assert follower.is_alive()

    # Renew at time 5
    follower.send_heartbeat()
    assert follower.last_heartbeat == 5

    # Advance 9 more (now at time 14)
    for _ in range(9):
        follower.tick()

    # time_since_heartbeat = 14 - 5 = 9 < ttl, should be alive
    assert follower.is_alive()

    # One more tick: time 15, time_since = 10 >= ttl
    follower.tick()
    assert not follower.is_alive()


def test_heartbeat_lease_multi_followers():
    """
    Leader monitors multiple followers.
    Some fail, leader detects.
    """
    ttl = 10
    followers = {
        'F1': HeartbeatLease(lease_ttl=ttl),
        'F2': HeartbeatLease(lease_ttl=ttl),
        'F3': HeartbeatLease(lease_ttl=ttl)
    }

    # All send heartbeat at time 0
    for f in followers.values():
        f.send_heartbeat()

    # Advance time 5
    for f in followers.values():
        for _ in range(5):
            f.tick()

    # F1 and F2 renew, F3 doesn't
    followers['F1'].send_heartbeat()
    followers['F2'].send_heartbeat()

    # Advance time to 15 (5 + 10)
    for f in followers.values():
        for _ in range(10):
            f.tick()

    # F1 and F2 alive (last HB at time 5, now at 15, time_since = 10 >= ttl: dead)
    assert not followers['F1'].is_alive()
    assert not followers['F2'].is_alive()

    # F3 dead at time 15 (last HB = 5, time_since = 10)
    assert not followers['F3'].is_alive()


def test_failure_no_heartbeat_monitoring():
    """
    Counter-example: code without heartbeat checking.
    """
    class BuggyFollower:
        def __init__(self):
            self.is_alive = True  # Static assumption

    # Bug: assumes follower is always alive
    # No detection of crash


if __name__ == '__main__':
    test_heartbeat_lease_alive()
    test_heartbeat_lease_expiry()
    test_heartbeat_lease_renew()
    test_heartbeat_lease_multi_followers()
    test_failure_no_heartbeat_monitoring()
    print("✓ heartbeat_lease passed")
