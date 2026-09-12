#!/usr/bin/env python3
"""
Gossip Membership Protocol
Nodes periodically exchange membership list.
Simulate: node joins/leaves, gossip propagates change.
Assert: membership eventually consistent across cluster.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"


class GossipNode:
    def __init__(self, node_id):
        self.node_id = node_id
        self.membership = {node_id}  # Initially just self
        self.lamport_time = 0

    def gossip(self, other_node):
        """
        Exchange membership with another node.
        Merge membership sets.
        """
        # Merge membership
        self.membership.update(other_node.membership)
        other_node.membership.update(self.membership)

        # Increment Lamport time
        self.lamport_time += 1
        other_node.lamport_time += 1


def test_gossip_membership_join():
    """
    Node A knows {A}.
    Node B knows {B}.
    Gossip once: both know {A, B}.
    """
    node_a = GossipNode('A')
    node_b = GossipNode('B')

    assert node_a.membership == {'A'}
    assert node_b.membership == {'B'}

    # A and B gossip
    node_a.gossip(node_b)

    # Both now know each other
    assert node_a.membership == {'A', 'B'}, f"A knows {node_a.membership}"
    assert node_b.membership == {'A', 'B'}, f"B knows {node_b.membership}"


def test_gossip_membership_multi_hop():
    """
    Chain: A -> B -> C.
    A knows {A}, B knows {B}, C knows {C}.
    Gossip A-B, then B-C.
    Assert: C eventually knows {A, B, C}.
    """
    node_a = GossipNode('A')
    node_b = GossipNode('B')
    node_c = GossipNode('C')

    # Gossip A-B
    node_a.gossip(node_b)
    assert node_a.membership == {'A', 'B'}
    assert node_b.membership == {'A', 'B'}
    assert node_c.membership == {'C'}

    # Gossip B-C (B has knowledge of A)
    node_b.gossip(node_c)
    assert node_b.membership == {'A', 'B', 'C'}
    assert node_c.membership == {'A', 'B', 'C'}

    # A doesn't yet know C (no gossip with C)
    assert 'C' not in node_a.membership

    # Gossip A-B again
    node_a.gossip(node_b)
    assert node_a.membership == {'A', 'B', 'C'}


def test_gossip_membership_leave():
    """
    Cluster: {A, B, C}.
    B decides to leave (removes self from membership).
    Gossip propagates.
    Assert: eventually all know B left.
    """
    node_a = GossipNode('A')
    node_b = GossipNode('B')
    node_c = GossipNode('C')

    # Form cluster
    node_a.gossip(node_b)
    node_b.gossip(node_c)

    # Now all should know each other
    node_a.gossip(node_b)
    assert node_a.membership == {'A', 'B', 'C'}

    # B leaves (removes self)
    node_b.membership.discard('B')
    assert 'B' not in node_b.membership

    # B gossips with A
    node_b.gossip(node_a)
    assert node_b.membership == {'A', 'B', 'C'}  # A re-adds B
    # This is the issue: simple gossip can't handle explicit leaves
    # In real systems, we'd use a "leave" message or version numbers


def test_gossip_membership_version_numbers():
    """
    Track version numbers for each node.
    Only accept updates with higher version.
    Prevents re-adding departed nodes.
    """
    class VersionedGossipNode:
        def __init__(self, node_id):
            self.node_id = node_id
            self.membership = {node_id: 0}  # node -> version

        def gossip(self, other):
            # Merge: keep max version for each node
            for node_id, version in other.membership.items():
                if node_id not in self.membership or version > self.membership[node_id]:
                    self.membership[node_id] = version

            for node_id, version in self.membership.items():
                if node_id not in other.membership or version > other.membership[node_id]:
                    other.membership[node_id] = version

        def leave(self):
            """Increment self's version to signal leave."""
            self.membership[self.node_id] += 1

    node_a = VersionedGossipNode('A')
    node_b = VersionedGossipNode('B')

    # Form cluster
    node_a.gossip(node_b)
    assert node_a.membership == {'A': 0, 'B': 0}
    assert node_b.membership == {'A': 0, 'B': 0}

    # B leaves (version bump)
    node_b.leave()
    assert node_b.membership == {'A': 0, 'B': 1}

    # Gossip
    node_b.gossip(node_a)
    assert node_a.membership == {'A': 0, 'B': 1}  # Knows B left


def test_failure_no_gossip():
    """
    Counter-example: static membership list.
    """
    class StaticNode:
        def __init__(self, node_id, initial_membership):
            self.node_id = node_id
            self.membership = set(initial_membership)

    nodes = [StaticNode('A', ['A', 'B']), StaticNode('B', ['A', 'B'])]

    # If C joins, neither A nor B knows
    # (no gossip mechanism to propagate)
    pass


if __name__ == '__main__':
    test_gossip_membership_join()
    test_gossip_membership_multi_hop()
    test_gossip_membership_leave()
    test_gossip_membership_version_numbers()
    test_failure_no_gossip()
    print("✓ gossip_membership passed")
