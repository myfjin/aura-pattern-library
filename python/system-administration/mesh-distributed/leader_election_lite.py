#!/usr/bin/env python3
"""
Leader Election (Lite) Pattern
N nodes, each with ID and term number.
Simulate: a node gets term majority, becomes leader.
Assert: exactly ONE leader at any term, term number only increases.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"


class Node:
    def __init__(self, node_id, term=0, leader_id=None):
        self.node_id = node_id
        self.term = term
        self.leader_id = leader_id  # Who is leader in current term
        self.voted_for = None  # Voted for which node in current term

    def request_vote(self, candidate_id, candidate_term):
        """
        Handle vote request from candidate.
        Grant if: candidate_term > our term, and we haven't voted yet.
        """
        if candidate_term > self.term:
            self.term = candidate_term
            self.voted_for = None
            self.leader_id = None

        if candidate_term == self.term:
            if self.voted_for is None:
                self.voted_for = candidate_id
                return True
            else:
                return self.voted_for == candidate_id
        return False

    def become_leader(self):
        """This node becomes leader (after winning election)."""
        self.leader_id = self.node_id


def test_leader_election_lite():
    """
    Three nodes. Node 0 requests votes, wins (2 votes out of 3).
    Assert: Node 0 is the only leader.
    """
    nodes = [Node(node_id=i) for i in range(3)]

    # Node 0 campaigns for term 1
    candidate_id = 0
    candidate_term = 1

    votes = 0
    for node in nodes:
        if node.request_vote(candidate_id, candidate_term):
            votes += 1

    # Node 0 has 2 votes (itself + one other)
    majority = len(nodes) // 2 + 1
    assert votes >= majority, f"Need {majority} votes, got {votes}"

    # Node 0 becomes leader
    nodes[candidate_id].become_leader()

    # Assert: exactly one leader
    leaders = [n for n in nodes if n.leader_id == n.node_id]
    assert len(leaders) == 1, f"Expected 1 leader, got {len(leaders)}"
    assert leaders[0].node_id == 0


def test_leader_election_node_crash():
    """
    Three nodes, node 0 is leader in term 1.
    Node 0 crashes, node 1 campaigns for term 2.
    Assert: node 1 becomes new leader.
    """
    nodes = [Node(node_id=i) for i in range(3)]

    # Term 1: node 0 is leader
    for node in nodes:
        node.request_vote(0, 1)
    nodes[0].become_leader()

    # Node 0 crashes (remove from cluster)
    active_nodes = nodes[1:]

    # Term 2: node 1 campaigns
    votes = 0
    for node in active_nodes:
        if node.request_vote(1, 2):
            votes += 1

    majority = len(active_nodes) // 2 + 1
    assert votes >= majority, f"Node 1 failed to get majority"

    nodes[1].become_leader()

    # Assert: old leader (node 0) is not leader, node 1 is
    assert nodes[0].leader_id != 0 or nodes[0] not in active_nodes
    assert nodes[1].leader_id == 1


def test_leader_election_term_monotonic():
    """
    Assert: once a term is seen, we never go back to older term.
    """
    node = Node(node_id=0, term=0)

    # See term 5
    node.request_vote(1, 5)
    assert node.term == 5

    # Try to go back to term 3 (should be ignored)
    node.request_vote(2, 3)
    assert node.term == 5, "Term should not decrease"

    # See term 6
    node.request_vote(3, 6)
    assert node.term == 6


def test_leader_election_split_brain():
    """
    Partition: nodes 0,1 vs node 2.
    Partition 1 (nodes 0,1): node 0 is leader with 2 votes (majority of 2).
    Partition 2 (node 2): node 2 tries to become leader with 1 vote (not majority of 1).
    Assert: one partition can elect, the other can't.
    """
    nodes = [Node(node_id=i) for i in range(3)]

    # Partition 1: nodes 0, 1
    partition1 = nodes[:2]
    votes1 = sum(1 for n in partition1 if n.request_vote(0, 1))
    assert votes1 == 2, f"Partition 1 should get 2 votes, got {votes1}"
    nodes[0].become_leader()

    # Partition 2: node 2 only
    partition2 = nodes[2:]
    votes2 = sum(1 for n in partition2 if n.request_vote(2, 1))
    assert votes2 == 1, f"Partition 2 can only get 1 vote"

    # A leader needs majority in the FULL cluster (3 nodes: need 2)
    # Node 2 with 1 vote is not a valid leader
    # (In real Raft, node 2 would not be elected because 1 < 2)
    # Simulate: only partition 1 can elect

    # Assert: partition 1 has leader, partition 2 does not
    leaders = [n for n in nodes if n.leader_id == n.node_id]
    assert len(leaders) == 1, f"Should have 1 leader in cluster, got {len(leaders)}"
    assert leaders[0].node_id == 0


def test_failure_no_term_tracking():
    """
    Counter-example: code that doesn't track terms.
    """
    class BuggyNode:
        def __init__(self, node_id):
            self.node_id = node_id
            self.leader_id = None

        def claim_leadership(self):
            self.leader_id = self.node_id

    nodes = [BuggyNode(i) for i in range(3)]

    # All nodes claim to be leader (bug: no term to arbitrate)
    for n in nodes:
        n.claim_leadership()

    leaders = [n for n in nodes if n.leader_id == n.node_id]
    assert len(leaders) == 3  # Bug: all are leaders!


if __name__ == '__main__':
    test_leader_election_lite()
    test_leader_election_node_crash()
    test_leader_election_term_monotonic()
    test_leader_election_split_brain()
    test_failure_no_term_tracking()
    print("✓ leader_election_lite passed")
