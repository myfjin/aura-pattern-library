#!/usr/bin/env python3
"""
Last-Write-Wins (LWW) Conflict Resolution Pattern
When replicas diverge (partition), use Lamport clock to resolve.
Higher timestamp wins, lower is discarded.
Assert: both replicas converge to same value after merge.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"


class VersionedValue:
    def __init__(self, value, timestamp):
        self.value = value
        self.timestamp = timestamp

    def __repr__(self):
        return f"V({self.value}, ts={self.timestamp})"


class LWWStore:
    def __init__(self, node_id):
        self.node_id = node_id
        self.data = {}  # Key -> VersionedValue
        self.lamport_clock = 0

    def tick(self):
        """Advance logical clock."""
        self.lamport_clock += 1

    def write(self, key, value):
        """Write with current Lamport timestamp."""
        self.lamport_clock += 1
        self.data[key] = VersionedValue(value, self.lamport_clock)

    def merge(self, other_store):
        """
        Merge another store's data using LWW.
        Keep higher timestamp, discard lower.
        """
        for key, other_version in other_store.data.items():
            if key not in self.data:
                # New key: adopt other's version
                self.data[key] = other_version
            else:
                # Conflict: keep higher timestamp
                if other_version.timestamp > self.data[key].timestamp:
                    self.data[key] = other_version
                # else: keep self's version (higher or equal timestamp)

    def see_write(self, key, value, timestamp):
        """
        Receive write from another node with timestamp.
        LWW: keep if timestamp > current timestamp for that key.
        """
        self.lamport_clock = max(self.lamport_clock, timestamp) + 1

        if key not in self.data:
            self.data[key] = VersionedValue(value, timestamp)
        else:
            if timestamp > self.data[key].timestamp:
                self.data[key] = VersionedValue(value, timestamp)


def test_lww_conflict_resolution():
    """
    Two replicas partition.
    A writes x=10 at ts=1.
    B writes x=20 at ts=2.
    Merge: B's write wins (higher ts).
    """
    store_a = LWWStore('A')
    store_b = LWWStore('B')

    # A: write x=10
    store_a.lamport_clock = 1
    store_a.data['x'] = VersionedValue(10, 1)

    # B: write x=20 at ts=2 (later)
    store_b.lamport_clock = 2
    store_b.data['x'] = VersionedValue(20, 2)

    # Merge A into B
    store_a.merge(store_b)

    # A now has x=20 (B's write won)
    assert store_a.data['x'].value == 20
    assert store_a.data['x'].timestamp == 2


def test_lww_partition_heal():
    """
    Initial sync: both have x=10 at ts=1.
    Partition: A writes x=20 (ts=2), B writes x=30 (ts=3).
    Partition heals: merge.
    B's write wins (higher ts).
    """
    store_a = LWWStore('A')
    store_b = LWWStore('B')

    # Initial: both write x=10
    store_a.write('x', 10)
    store_b.write('x', 10)

    # Partition
    # A writes x=20
    store_a.write('x', 20)
    ts_a = store_a.data['x'].timestamp

    # B advances clock then writes x=30 (to guarantee higher ts)
    store_b.tick()
    store_b.write('x', 30)
    ts_b = store_b.data['x'].timestamp

    # Verify: ts_b > ts_a
    assert ts_b > ts_a, f"B's timestamp {ts_b} should be > A's {ts_a}"

    # Merge A into B
    store_a.merge(store_b)

    # A converges to B's value
    assert store_a.data['x'].value == 30
    assert store_a.data['x'].timestamp == ts_b

    # Merge B into A
    store_b.merge(store_a)

    # Both have same state
    assert store_a.data['x'].value == store_b.data['x'].value


def test_lww_causality_preserved():
    """
    Write sequence: w1 at ts=1, w2 at ts=2, w3 at ts=3.
    Receive out-of-order: w3, w1, w2.
    Assert: final value is from w3 (highest ts).
    """
    store = LWWStore('A')

    # Receive w3
    store.see_write('x', 'value3', 3)
    assert store.data['x'].value == 'value3'

    # Receive w1 (lower ts: ignored)
    store.see_write('x', 'value1', 1)
    assert store.data['x'].value == 'value3'

    # Receive w2 (lower ts: ignored)
    store.see_write('x', 'value2', 2)
    assert store.data['x'].value == 'value3'


def test_lww_multiple_keys():
    """
    Multiple keys with divergent histories.
    Merge resolves each by LWW.
    """
    store_a = LWWStore('A')
    store_b = LWWStore('B')

    # A: x=1 (ts=1), y=2 (ts=3)
    store_a.data['x'] = VersionedValue(1, 1)
    store_a.data['y'] = VersionedValue(2, 3)

    # B: x=10 (ts=2), y=20 (ts=2), z=30 (ts=1)
    store_b.data['x'] = VersionedValue(10, 2)
    store_b.data['y'] = VersionedValue(20, 2)
    store_b.data['z'] = VersionedValue(30, 1)

    # Merge
    store_a.merge(store_b)

    # After merge:
    # x: B's (ts=2) > A's (ts=1) -> value=10
    assert store_a.data['x'].value == 10

    # y: A's (ts=3) > B's (ts=2) -> value=2
    assert store_a.data['y'].value == 2

    # z: new key from B -> value=30
    assert store_a.data['z'].value == 30


def test_lww_tie_breaking():
    """
    Same timestamp from two sources (tie).
    LWW: arbitrary tie-break (we choose lower node ID or deterministic rule).
    """
    store_a = LWWStore('A')
    store_b = LWWStore('B')

    # Both have x at same timestamp
    store_a.data['x'] = VersionedValue(10, 5)
    store_b.data['x'] = VersionedValue(20, 5)

    # Merge (tie: keep self's value by convention)
    store_a.merge(store_b)

    # A's value unchanged (equal timestamp = no update)
    assert store_a.data['x'].value == 10


def test_failure_no_timestamp_tracking():
    """
    Counter-example: last-write-wins without timestamp.
    """
    class BuggyStore:
        def __init__(self):
            self.data = {}

        def write(self, key, value):
            self.data[key] = value

        def merge(self, other):
            # Bug: just overwrite with other's values (no LWW)
            for key, value in other.data.items():
                self.data[key] = value

    store_a = BuggyStore()
    store_b = BuggyStore()

    # A writes first
    store_a.write('x', 'from_a')

    # B writes later
    store_b.write('x', 'from_b')

    # Merge A into B
    store_a.merge(store_b)

    # Bug: A's value is now from_b (merge order matters, not time)
    assert store_a.data['x'] == 'from_b'

    # If we merge in reverse order, result changes
    store_c = BuggyStore()
    store_c.write('x', 'from_a')
    store_d = BuggyStore()
    store_d.write('x', 'from_b')
    store_d.merge(store_c)

    # Bug: result depends on merge order, not causality
    assert store_d.data['x'] == 'from_a'


if __name__ == '__main__':
    test_lww_conflict_resolution()
    test_lww_partition_heal()
    test_lww_causality_preserved()
    test_lww_multiple_keys()
    test_lww_tie_breaking()
    test_failure_no_timestamp_tracking()
    print("✓ lww_conflict_resolve passed")
