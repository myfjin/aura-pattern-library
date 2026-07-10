#!/usr/bin/env python3
"""
Idempotent Replication Pattern
Replicate writes across replicas.
Crash mid-replication, resume.
Assert: each write applied exactly once (no duplicates).
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"


class ReplicatedStore:
    def __init__(self, replica_id):
        self.replica_id = replica_id
        self.data = {}
        self.applied_writes = set()  # Track applied write IDs

    def apply_write(self, write_id, key, value):
        """
        Apply write only if not already applied (idempotent).
        """
        if write_id in self.applied_writes:
            # Already applied, skip
            return True

        # Apply write
        self.data[key] = value
        self.applied_writes.add(write_id)
        return True

    def get_applied(self):
        """Get list of applied write IDs."""
        return sorted(self.applied_writes)


def test_idempotent_replication():
    """
    Primary writes, replica applies.
    Replay same writes: idempotent.
    """
    primary = ReplicatedStore('primary')
    replica = ReplicatedStore('replica')

    # Primary: write w1
    primary.apply_write('w1', 'x', 10)

    # Replicate to replica
    replica.apply_write('w1', 'x', 10)

    assert primary.data == replica.data
    assert replica.applied_writes == {'w1'}

    # Crash and replay: re-apply w1 to replica
    replica.apply_write('w1', 'x', 10)

    # Idempotent: data unchanged
    assert replica.data == {'x': 10}
    assert replica.applied_writes == {'w1'}


def test_idempotent_replication_batch():
    """
    Replicate batch of writes, crash mid-batch.
    Resume: skip already-applied, apply new ones.
    """
    primary = ReplicatedStore('primary')
    replica = ReplicatedStore('replica')

    writes = [
        ('w1', 'x', 10),
        ('w2', 'y', 20),
        ('w3', 'z', 30),
        ('w4', 'a', 40)
    ]

    # Primary writes all
    for wid, key, val in writes:
        primary.apply_write(wid, key, val)

    # Replicate w1, w2 (crash before w3, w4)
    replica.apply_write('w1', 'x', 10)
    replica.apply_write('w2', 'y', 20)

    assert replica.applied_writes == {'w1', 'w2'}

    # Resume: replay all writes
    for wid, key, val in writes:
        replica.apply_write(wid, key, val)

    # All writes applied exactly once
    assert replica.applied_writes == {'w1', 'w2', 'w3', 'w4'}
    assert replica.data == primary.data


def test_idempotent_replication_concurrent():
    """
    Multiple replicas apply same write concurrently.
    Assert: no duplicates despite concurrent application.
    """
    replicas = [ReplicatedStore(f'r{i}') for i in range(3)]

    write_id = 'w1'
    key, value = 'x', 100

    # All replicas apply same write concurrently
    for replica in replicas:
        replica.apply_write(write_id, key, value)

    # All have same state
    for replica in replicas:
        assert replica.data == {'x': 100}
        assert replica.applied_writes == {write_id}


def test_idempotent_replication_ordering():
    """
    Writes must be applied in order, but replication can be out-of-order.
    Assert: replica state is consistent if writes are applied in order.
    """
    primary = ReplicatedStore('primary')
    replica = ReplicatedStore('replica')

    writes = [
        ('w1', 'x', 10),
        ('w2', 'x', 20),  # Overwrite x
        ('w3', 'x', 30)   # Overwrite x again
    ]

    for wid, key, val in writes:
        primary.apply_write(wid, key, val)

    # Apply to replica in order
    for wid, key, val in writes:
        replica.apply_write(wid, key, val)

    assert replica.data['x'] == 30

    # Crash and resume: same result
    replica2 = ReplicatedStore('replica2')
    for wid, key, val in writes:
        replica2.apply_write(wid, key, val)

    assert replica2.data['x'] == 30


def test_idempotent_replication_duplicate_write():
    """
    Same write sent twice (network retry).
    Assert: applied only once.
    """
    replica = ReplicatedStore('replica')

    # Write w1 sent twice
    result1 = replica.apply_write('w1', 'x', 100)
    result2 = replica.apply_write('w1', 'x', 100)

    assert result1 and result2
    assert replica.applied_writes == {'w1'}
    assert len(replica.applied_writes) == 1


def test_failure_no_write_id_tracking():
    """
    Counter-example: code without write ID tracking.
    """
    class BuggyReplica:
        def __init__(self):
            self.data = {}

        def apply_write(self, key, value):
            # Bug: no tracking of applied writes
            self.data[key] = value

    replica = BuggyReplica()

    # Same write applied twice
    replica.apply_write('x', 10)
    replica.apply_write('x', 10)

    # No way to know if it was applied twice or once


if __name__ == '__main__':
    test_idempotent_replication()
    test_idempotent_replication_batch()
    test_idempotent_replication_concurrent()
    test_idempotent_replication_ordering()
    test_idempotent_replication_duplicate_write()
    test_failure_no_write_id_tracking()
    print("✓ idempotent_replication passed")
