#!/usr/bin/env python3
"""
Quorum Check Pattern
Write requires quorum (majority of nodes).
Simulate: partition that loses majority can't write.
Assert: quorum_lost() returns True when alive < majority.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"


def quorum_size(total_nodes):
    """Majority quorum: > half."""
    return total_nodes // 2 + 1


def can_write(alive_nodes, total_nodes):
    """
    Can write if alive nodes >= quorum size.
    """
    quorum = quorum_size(total_nodes)
    return alive_nodes >= quorum


def test_quorum_check():
    """
    5 nodes, 3 alive (majority).
    Assert: can write.
    """
    total = 5
    alive = 3
    quorum = quorum_size(total)

    assert quorum == 3, f"Quorum of 5 should be 3, got {quorum}"
    assert can_write(alive, total), "Should be able to write with 3 alive"


def test_quorum_lost_on_partition():
    """
    5 nodes, partition: 2 alive vs 3 alive.
    Majority (3) can write, minority (2) cannot.
    """
    total = 5
    quorum = quorum_size(total)
    assert quorum == 3

    # Partition 1: 3 alive (majority)
    alive_p1 = 3
    assert can_write(alive_p1, total), "Majority partition should write"

    # Partition 2: 2 alive (minority)
    alive_p2 = 2
    assert not can_write(alive_p2, total), "Minority partition should NOT write"


def test_quorum_check_even_nodes():
    """
    4 nodes (even), quorum = 3.
    Partition: 2 vs 2.
    Neither can write (neither has quorum of 3).
    """
    total = 4
    quorum = quorum_size(total)
    assert quorum == 3, f"Quorum of 4 should be 3, got {quorum}"

    # 2 nodes cannot reach quorum of 3
    alive = 2
    assert not can_write(alive, total), "2 nodes out of 4 should not be able to write"


def test_quorum_minimal():
    """
    Minimal cluster: 1 node.
    Quorum = 1, can write if alive.
    """
    total = 1
    quorum = quorum_size(total)
    assert quorum == 1

    alive = 1
    assert can_write(alive, total), "Single node should write"

    alive = 0
    assert not can_write(alive, total), "No nodes should not write"


def test_quorum_three_nodes():
    """
    3 nodes, quorum = 2.
    1 alive: cannot write.
    2 alive: can write.
    """
    total = 3
    quorum = quorum_size(total)
    assert quorum == 2, f"Quorum of 3 should be 2, got {quorum}"

    assert not can_write(1, total), "1 node of 3 should not write"
    assert can_write(2, total), "2 nodes of 3 should write"
    assert can_write(3, total), "3 nodes of 3 should write"


def test_failure_majority_requirement():
    """
    Counter-example: code that doesn't enforce quorum.
    """
    def buggy_can_write(alive_nodes):
        """Bug: allows write with just 1 node."""
        return alive_nodes >= 1

    total = 5
    # Bug: 1 node can "write" even without quorum
    assert buggy_can_write(1)
    assert buggy_can_write(2)  # All counts as writable


if __name__ == '__main__':
    test_quorum_check()
    test_quorum_lost_on_partition()
    test_quorum_check_even_nodes()
    test_quorum_minimal()
    test_quorum_three_nodes()
    test_failure_majority_requirement()
    print("✓ quorum_check passed")
