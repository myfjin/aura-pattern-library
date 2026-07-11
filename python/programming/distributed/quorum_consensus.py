#!/usr/bin/env python3
"""
Quorum consensus simulator module.

This module implements a simple quorum consensus system with nodes that can
propose values, accept proposals, and learn consensus decisions.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

from typing import List, Set, Optional, Dict, Any
from collections import defaultdict
import uuid


class Node:
    """Represents a node in the quorum consensus system."""
    
    def __init__(self, node_id: str) -> None:
        """
        Initialize a node.
        
        Args:
            node_id: Unique identifier for the node
        """
        self.node_id = node_id
        self.accepted_proposals: Dict[str, Any] = {}
        self.learned_values: Dict[str, Any] = {}
        
    def propose(self, proposal_id: str, value: Any) -> Dict[str, Any]:
        """
        Propose a value to other nodes.
        
        Args:
            proposal_id: Unique identifier for the proposal
            value: Value being proposed
            
        Returns:
            Proposal message dictionary
        """
        return {
            'type': 'proposal',
            'proposal_id': proposal_id,
            'value': value,
            'proposer': self.node_id
        }
    
    def accept(self, proposal_id: str, value: Any, proposer: str) -> Dict[str, Any]:
        """
        Accept a proposal.
        
        Args:
            proposal_id: Unique identifier for the proposal
            value: Value being accepted
            proposer: ID of the node that made the proposal
            
        Returns:
            Accept message dictionary
        """
        self.accepted_proposals[proposal_id] = {
            'value': value,
            'proposer': proposer
        }
        return {
            'type': 'accept',
            'proposal_id': proposal_id,
            'value': value,
            'acceptor': self.node_id,
            'proposer': proposer
        }
    
    def learn(self, proposal_id: str, value: Any) -> Dict[str, Any]:
        """
        Learn a consensus decision.
        
        Args:
            proposal_id: Unique identifier for the proposal
            value: Value that reached consensus
            
        Returns:
            Learn message dictionary
        """
        self.learned_values[proposal_id] = value
        return {
            'type': 'learn',
            'proposal_id': proposal_id,
            'value': value,
            'learner': self.node_id
        }
    
    def get_accepted_value(self, proposal_id: str) -> Optional[Any]:
        """
        Get the value accepted for a proposal.
        
        Args:
            proposal_id: Unique identifier for the proposal
            
        Returns:
            Accepted value or None if not accepted
        """
        if proposal_id in self.accepted_proposals:
            return self.accepted_proposals[proposal_id]['value']
        return None
    
    def get_learned_value(self, proposal_id: str) -> Optional[Any]:
        """
        Get the value learned for a proposal.
        
        Args:
            proposal_id: Unique identifier for the proposal
            
        Returns:
            Learned value or None if not learned
        """
        return self.learned_values.get(proposal_id)


class Quorum:
    """Manages quorum consensus among nodes."""
    
    def __init__(self, nodes: List[Node]) -> None:
        """
        Initialize quorum with nodes.
        
        Args:
            nodes: List of nodes in the quorum system
        """
        if len(nodes) < 1:
            raise ValueError("Quorum must have at least one node")
        self.nodes = nodes
        self.majority = len(nodes) // 2 + 1
        self.message_log: List[Dict[str, Any]] = []
        
    def get_node_by_id(self, node_id: str) -> Optional[Node]:
        """
        Get a node by its ID.
        
        Args:
            node_id: ID of the node to retrieve
            
        Returns:
            Node object or None if not found
        """
        for node in self.nodes:
            if node.node_id == node_id:
                return node
        return None
    
    def has_majority(self, count: int) -> bool:
        """
        Check if a count represents a majority.
        
        Args:
            count: Number of nodes
            
        Returns:
            True if count is a majority, False otherwise
        """
        return count >= self.majority
    
    def propose_value(self, proposer_id: str, value: Any) -> str:
        """
        Propose a value from a node.
        
        Args:
            proposer_id: ID of the proposing node
            value: Value to propose
            
        Returns:
            Proposal ID
        """
        proposer = self.get_node_by_id(proposer_id)
        if not proposer:
            raise ValueError(f"Proposer node {proposer_id} not found")
            
        proposal_id = str(uuid.uuid4())
        proposal = proposer.propose(proposal_id, value)
        self.message_log.append(proposal)
        
        # Send proposal to all nodes
        for node in self.nodes:
            if node.node_id != proposer_id:
                accept_msg = node.accept(proposal_id, value, proposer_id)
                self.message_log.append(accept_msg)
                
        return proposal_id
    
    def check_consensus(self, proposal_id: str) -> Optional[Any]:
        """
        Check if a proposal has reached consensus.
        
        Args:
            proposal_id: ID of the proposal to check
            
        Returns:
            Consensus value if reached, None otherwise
        """
        accept_count = 0
        value = None
        
        # Count acceptances and check for consistent value
        for node in self.nodes:
            node_value = node.get_accepted_value(proposal_id)
            if node_value is not None:
                if value is None:
                    value = node_value
                elif value != node_value:
                    # Inconsistent values, no consensus possible
                    return None
                accept_count += 1
        
        # Check if majority accepted
        if self.has_majority(accept_count):
            # Send learn messages
            for node in self.nodes:
                learn_msg = node.learn(proposal_id, value)
                self.message_log.append(learn_msg)
            return value
            
        return None
    
    def get_learned_value(self, proposal_id: str) -> Optional[Any]:
        """
        Get the learned value for a proposal (if any node learned it).
        
        Args:
            proposal_id: ID of the proposal
            
        Returns:
            Learned value or None
        """
        for node in self.nodes:
            value = node.get_learned_value(proposal_id)
            if value is not None:
                return value
        return None


def main() -> None:
    """Self-test: majority math exact, full acceptance reaches consensus and
    every node learns, MINORITY acceptance does NOT, conflicting values veto."""
    nodes = [Node(f"node_{i}") for i in range(5)]
    quorum = Quorum(nodes)
    assert quorum.majority == 3, f"majority of 5 must be 3, got {quorum.majority}"
    assert quorum.has_majority(3) and not quorum.has_majority(2)

    # Full acceptance: consensus on 'A', and every node LEARNS it.
    pid_a = quorum.propose_value("node_0", "A")
    assert quorum.check_consensus(pid_a) == "A", "unanimous proposal failed consensus"
    for node in nodes:
        assert node.get_learned_value(pid_a) == "A", \
            f"{node.node_id} did not learn the decided value"
    assert quorum.get_learned_value(pid_a) == "A"

    # Values are carried verbatim (int survives).
    pid_b = quorum.propose_value("node_2", 42)
    assert quorum.check_consensus(pid_b) == 42
    assert quorum.get_learned_value(pid_b) == 42

    # THE FAILURE MODES a quorum system exists to catch:
    # 1. Minority acceptance (2 of 5) → NO consensus, nothing learned.
    minority_pid = "manual-minority"
    nodes[0].accept(minority_pid, "M", "node_0")
    nodes[1].accept(minority_pid, "M", "node_0")
    assert quorum.check_consensus(minority_pid) is None, \
        "2/5 acceptances produced consensus"
    assert quorum.get_learned_value(minority_pid) is None, \
        "value learned without a quorum"

    # 2. Conflicting accepted values → consensus impossible.
    split_pid = "manual-split"
    for n in nodes[:3]:
        n.accept(split_pid, "X", "node_0")
    for n in nodes[3:]:
        n.accept(split_pid, "Y", "node_3")
    assert quorum.check_consensus(split_pid) is None, \
        "conflicting values still reached 'consensus'"

    # 3. Unknown proposal → honest None.
    assert quorum.check_consensus("fake-id") is None

    # Message accounting: propose(1) + 4 accepts, then 5 learns on success.
    fresh = Quorum([Node(f"m{i}") for i in range(5)])
    pid = fresh.propose_value("m0", "v")
    assert len(fresh.message_log) == 5, \
        f"1 propose + 4 accepts must log 5 messages, got {len(fresh.message_log)}"
    fresh.check_consensus(pid)
    assert len(fresh.message_log) == 10, \
        f"+5 learn messages must total 10, got {len(fresh.message_log)}"

    # Edge quorums: 1 node decides alone; 2 nodes need both.
    solo = Quorum([Node("only")])
    assert solo.majority == 1
    pair = Quorum([Node("p0"), Node("p1")])
    assert pair.majority == 2, "majority of 2 must be 2 (no split-brain)"
    try:
        Quorum([])
        assert False, "empty quorum accepted"
    except ValueError:
        pass
    try:
        quorum.propose_value("ghost", "v")
        assert False, "unknown proposer accepted"
    except ValueError:
        pass

    print("quorum_consensus: majority 3/5 exact, unanimous decided + 5 learned, "
          "2/5 refused, split vote refused, messages 5→10 — PASS")


if __name__ == "__main__":
    main()