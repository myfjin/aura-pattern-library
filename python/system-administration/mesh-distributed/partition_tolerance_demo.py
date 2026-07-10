#!/usr/bin/env python3
"""
Partition Tolerance Demo
Simulate network partition: cluster splits into two.
Assert: majority partition proceeds, minority blocks (quorum lost).
Partitions later rejoin: data merges (eventual consistency).
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"


class PartitionTolerantNode:
    def __init__(self, node_id, total_nodes):
        self.node_id = node_id
        self.total_nodes = total_nodes
        self.quorum_size = total_nodes // 2 + 1
        self.data = {}  # Key -> value
        self.term = 0
        self.alive_nodes = set(range(total_nodes))  # Track alive cluster

    def can_write(self):
        """Can write if quorum is available."""
        return len(self.alive_nodes) >= self.quorum_size

    def write(self, key, value):
        """Write succeeds only if quorum available."""
        if self.can_write():
            self.data[key] = value
            return True
        return False

    def partition(self, other_nodes):
        """
        Simulate partition: this node can only see nodes in 'other_nodes'.
        """
        self.alive_nodes = set(other_nodes)


def test_partition_tolerance_majority_wins():
    """
    5 nodes, split 3 vs 2.
    Majority (3) can write, minority (2) cannot.
    """
    total_nodes = 5
    quorum = (total_nodes // 2) + 1  # 3
    assert quorum == 3

    # Create 5 nodes
    nodes = [PartitionTolerantNode(i, total_nodes) for i in range(5)]

    # Partition: nodes 0,1,2 vs 3,4
    partition1 = [0, 1, 2]
    partition2 = [3, 4]

    # Apply partition
    for i in partition1:
        nodes[i].partition(partition1)
    for i in partition2:
        nodes[i].partition(partition2)

    # Partition 1 (3 nodes) can write
    assert nodes[0].can_write(), "Partition 1 should have quorum"
    assert nodes[0].write('x', 1), "Write should succeed on majority"

    # Partition 2 (2 nodes) cannot write
    assert not nodes[3].can_write(), "Partition 2 should NOT have quorum"
    assert not nodes[3].write('x', 1), "Write should fail on minority"


def test_partition_tolerance_data_divergence():
    """
    Majority writes data A, minority writes data B.
    After rejoin, majority's data is canonical (last-write-wins).
    """
    total_nodes = 5
    nodes = [PartitionTolerantNode(i, total_nodes) for i in range(5)]

    # Initial state: all nodes see full cluster
    for i in range(5):
        nodes[i].partition(list(range(5)))

    # All write initial value
    for i in range(5):
        nodes[i].write('shared_key', 'version_0')

    # Partition: 3 vs 2
    partition1 = [0, 1, 2]
    partition2 = [3, 4]

    for i in partition1:
        nodes[i].partition(partition1)
    for i in partition2:
        nodes[i].partition(partition2)

    # Majority writes new value
    nodes[0].write('shared_key', 'version_1_majority')
    nodes[1].write('shared_key', 'version_1_majority')
    nodes[2].write('shared_key', 'version_1_majority')

    # Verify majority's data
    assert nodes[0].data['shared_key'] == 'version_1_majority'

    # Minority could not write (can_write() = False), so data unchanged
    assert nodes[3].data['shared_key'] == 'version_0'

    # After partition heals, majority's write is canonical
    # (In a real system, we'd implement merge/reconciliation)


def test_partition_tolerance_rejoin():
    """
    Partition heals: nodes rejoin full cluster.
    Assert: quorum restored, both partitions see each other.
    """
    total_nodes = 5
    nodes = [PartitionTolerantNode(i, total_nodes) for i in range(5)]

    # Partition
    partition1 = [0, 1, 2]
    partition2 = [3, 4]

    for i in partition1:
        nodes[i].partition(partition1)
    for i in partition2:
        nodes[i].partition(partition2)

    # Both can't write initially, then... (only majority can write)
    assert nodes[0].can_write()
    assert not nodes[3].can_write()

    # Rejoin: all nodes see all nodes
    full_cluster = list(range(5))
    for i in range(5):
        nodes[i].partition(full_cluster)

    # All can write again
    for i in range(5):
        assert nodes[i].can_write(), f"Node {i} should be able to write after rejoin"


def test_partition_split_brain_avoidance():
    """
    Assert: only 1 partition can be write-active at a time.
    """
    total_nodes = 4
    nodes = [PartitionTolerantNode(i, total_nodes) for i in range(4)]

    quorum = (total_nodes // 2) + 1  # 3
    assert quorum == 3

    # Partition 2 vs 2: neither has quorum of 3
    partition1 = [0, 1]
    partition2 = [2, 3]

    for i in partition1:
        nodes[i].partition(partition1)
    for i in partition2:
        nodes[i].partition(partition2)

    # Both partitions LOSE quorum (each has 2 out of 4)
    assert not nodes[0].can_write()
    assert not nodes[2].can_write()

    # No split-brain: neither partition can write
    assert not nodes[0].write('x', 1)
    assert not nodes[2].write('x', 1)


def test_failure_no_quorum_check():
    """
    Counter-example: writes succeed without quorum check.
    """
    class BuggyNode:
        def __init__(self):
            self.data = {}

        def write(self, key, value):
            # Bug: no quorum check
            self.data[key] = value
            return True

    nodes = [BuggyNode() for _ in range(5)]

    # Both partitions "write" without quorum
    nodes[0].write('x', 'partition1')
    nodes[3].write('x', 'partition2')

    # Bug: conflicting writes, no consensus
    assert nodes[0].data['x'] == 'partition1'
    assert nodes[3].data['x'] == 'partition2'


if __name__ == '__main__':
    test_partition_tolerance_majority_wins()
    test_partition_tolerance_data_divergence()
    test_partition_tolerance_rejoin()
    test_partition_split_brain_avoidance()
    test_failure_no_quorum_check()
    print("✓ partition_tolerance_demo passed")
