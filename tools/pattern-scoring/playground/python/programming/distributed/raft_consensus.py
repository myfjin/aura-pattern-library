"""
Raft Consensus Algorithm Implementation

This module implements the Raft consensus algorithm with leader election,
log replication, and heartbeat mechanisms.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import time
import random
import threading
from enum import Enum
from typing import List, Optional, Dict, Any
from dataclasses import dataclass, field
import json


class NodeState(Enum):
    """Represents the state of a Raft node."""
    FOLLOWER = "follower"
    CANDIDATE = "candidate"
    LEADER = "leader"


@dataclass
class LogEntry:
    """Represents a log entry in the Raft log."""
    term: int
    command: Any
    index: int = field(default=0)


class RaftNode:
    """A Raft consensus node implementation."""
    
    def __init__(self, node_id: int, cluster_nodes: List[int]):
        """
        Initialize a Raft node.
        
        Args:
            node_id: Unique identifier for this node
            cluster_nodes: List of all node IDs in the cluster
        """
        self.node_id = node_id
        self.cluster_nodes = cluster_nodes
        self.state = NodeState.FOLLOWER
        self.current_term = 0
        self.voted_for: Optional[int] = None
        self.log: List[LogEntry] = []
        self.commit_index = 0
        self.last_applied = 0
        self.next_index: Dict[int, int] = {}
        self.match_index: Dict[int, int] = {}
        
        # Leader-specific attributes
        self.leader_id: Optional[int] = None
        
        # Election-related attributes
        self.election_timeout = random.uniform(1.0, 2.0)  # 1-2 seconds
        self.last_heartbeat = time.time()
        self.election_timer = None
        
        # Threading
        self.lock = threading.RLock()
        self.stop_event = threading.Event()
        
        self._initialize_node()
    
    def _initialize_node(self) -> None:
        """Initialize node state and start background threads."""
        self.reset_election_timer()
        self.background_thread = threading.Thread(target=self._run_background, daemon=True)
        self.background_thread.start()
    
    def _run_background(self) -> None:
        """Run background tasks like election timeouts and heartbeats."""
        while not self.stop_event.is_set():
            with self.lock:
                if self.state == NodeState.LEADER:
                    self._send_heartbeats()
                elif self.state == NodeState.CANDIDATE:
                    pass  # Candidate waits for election timeout or votes
                else:  # Follower
                    if time.time() - self.last_heartbeat > self.election_timeout:
                        self._start_election()
            
            time.sleep(0.1)  # Check every 100ms
    
    def reset_election_timer(self) -> None:
        """Reset the election timer with a random timeout."""
        self.election_timeout = random.uniform(1.0, 2.0)
        self.last_heartbeat = time.time()
    
    def _start_election(self) -> None:
        """Start a new election by becoming a candidate."""
        self.state = NodeState.CANDIDATE
        self.current_term += 1
        self.voted_for = self.node_id
        self.leader_id = None
        
        votes_received = 1  # Vote for self
        print(f"Node {self.node_id} starting election for term {self.current_term}")
        
        # Request votes from other nodes
        for node_id in self.cluster_nodes:
            if node_id != self.node_id:
                if self._request_vote(node_id):
                    votes_received += 1
        
        # Check if we won the election
        if votes_received > len(self.cluster_nodes) // 2:
            self._become_leader()
        else:
            # If we didn't win, become a follower
            self.state = NodeState.FOLLOWER
            self.voted_for = None
        
        self.reset_election_timer()
    
    def _become_leader(self) -> None:
        """Transition to leader state."""
        self.state = NodeState.LEADER
        self.leader_id = self.node_id
        
        # Initialize next_index and match_index for each follower
        last_log_index = len(self.log)
        for node_id in self.cluster_nodes:
            if node_id != self.node_id:
                self.next_index[node_id] = last_log_index + 1
                self.match_index[node_id] = 0
        
        print(f"Node {self.node_id} became leader for term {self.current_term}")
    
    def _send_heartbeats(self) -> None:
        """Send heartbeats to all followers."""
        for node_id in self.cluster_nodes:
            if node_id != self.node_id:
                self._send_heartbeat(node_id)
    
    def _send_heartbeat(self, node_id: int) -> None:
        """Send a heartbeat to a specific node."""
        # In a real implementation, this would send an actual network message
        # For this demo, we'll simulate it by directly calling the receiver
        pass
    
    def _request_vote(self, node_id: int) -> bool:
        """
        Request a vote from another node.
        
        Args:
            node_id: ID of the node to request vote from
            
        Returns:
            True if vote was granted, False otherwise
        """
        # In a real implementation, this would send a network request
        # For this demo, we'll simulate it by directly calling the receiver
        return False  # Simulated failure for demo purposes
    
    def receive_heartbeat(self, leader_id: int, term: int) -> None:
        """
        Receive a heartbeat from a leader.
        
        Args:
            leader_id: ID of the leader sending the heartbeat
            term: Leader's current term
        """
        with self.lock:
            if term < self.current_term:
                return
            
            if term > self.current_term:
                self.current_term = term
                self.state = NodeState.FOLLOWER
                self.voted_for = None
            
            self.leader_id = leader_id
            self.reset_election_timer()
    
    def receive_vote_request(self, candidate_id: int, term: int, 
                           last_log_index: int, last_log_term: int) -> bool:
        """
        Handle a request for vote from a candidate.
        
        Args:
            candidate_id: ID of the candidate requesting vote
            term: Candidate's term
            last_log_index: Index of candidate's last log entry
            last_log_term: Term of candidate's last log entry
            
        Returns:
            True if vote is granted, False otherwise
        """
        with self.lock:
            if term < self.current_term:
                return False
            
            if term > self.current_term:
                self.current_term = term
                self.state = NodeState.FOLLOWER
                self.voted_for = None
            
            # Check if we've already voted in this term
            if self.voted_for is not None and self.voted_for != candidate_id:
                return False
            
            # Check if candidate's log is at least as up-to-date as ours
            last_log_idx = len(self.log) - 1
            last_log_term_val = self.log[last_log_idx].term if last_log_idx >= 0 else 0
            
            if last_log_term < last_log_term_val or \
               (last_log_term == last_log_term_val and last_log_index < last_log_idx):
                return False
            
            self.voted_for = candidate_id
            self.reset_election_timer()
            return True
    
    def append_entries(self, term: int, leader_id: int, prev_log_index: int,
                      prev_log_term: int, entries: List[LogEntry],
                      leader_commit: int) -> bool:
        """
        Handle AppendEntries RPC from leader.
        
        Args:
            term: Leader's term
            leader_id: Leader's ID
            prev_log_index: Index of log entry immediately preceding new ones
            prev_log_term: Term of prev_log_index entry
            entries: Log entries to store (empty for heartbeat)
            leader_commit: Leader's commit_index
            
        Returns:
            True if successfully appended, False otherwise
        """
        with self.lock:
            if term < self.current_term:
                return False
            
            if term > self.current_term:
                self.current_term = term
                self.state = NodeState.FOLLOWER
                self.voted_for = None
            
            self.leader_id = leader_id
            self.reset_election_timer()
            
            # Check if we have the previous log entry
            if prev_log_index >= len(self.log):
                return False
            
            if prev_log_index >= 0 and self.log[prev_log_index].term != prev_log_term:
                # Log inconsistency, remove conflicting entries
                self.log = self.log[:prev_log_index + 1]
                return False
            
            # Append new entries
            for entry in entries:
                # If entry already exists at this index, check for consistency
                if entry.index < len(self.log):
                    if self.log[entry.index].term != entry.term:
                        # Remove conflicting entries
                        self.log = self.log[:entry.index]
                        self.log.append(entry)
                else:
                    # Append new entry
                    self.log.append(entry)
            
            # Update commit index
            if leader_commit > self.commit_index:
                self.commit_index = min(leader_commit, len(self.log) - 1)
            
            return True
    
    def submit_command(self, command: Any) -> bool:
        """
        Submit a command to be replicated (only valid if node is leader).
        
        Args:
            command: Command to be replicated
            
        Returns:
            True if command was accepted, False otherwise
        """
        with self.lock:
            if self.state != NodeState.LEADER:
                return False
            
            entry = LogEntry(
                term=self.current_term,
                command=command,
                index=len(self.log)
            )
            self.log.append(entry)
            return True
    
    def get_state_info(self) -> Dict[str, Any]:
        """Get current state information for debugging."""
        with self.lock:
            return {
                "node_id": self.node_id,
                "state": self.state.value,
                "term": self.current_term,
                "leader_id": self.leader_id,
                "log_length": len(self.log),
                "commit_index": self.commit_index
            }
    
    def stop(self) -> None:
        """Stop the node's background operations."""
        self.stop_event.set()
        if hasattr(self, 'background_thread'):
            self.background_thread.join(timeout=1.0)


class RaftCluster:
    """Manages a cluster of Raft nodes for demonstration purposes."""
    
    def __init__(self, node_ids: List[int]):
        """
        Initialize a Raft cluster.
        
        Args:
            node_ids: List of node IDs to create in the cluster
        """
        self.nodes: Dict[int, RaftNode] = {}
        for node_id in node_ids:
            self.nodes[node_id] = RaftNode(node_id, node_ids)
    
    def simulate_network_message(self, sender_id: int, receiver_id: int, 
                                message_type: str, data: Dict[str, Any]) -> Any:
        """
        Simulate sending a message between nodes.
        
        Args:
            sender_id: ID of the sending node
            receiver_id: ID of the receiving node
            message_type: Type of message ('vote_request', 'vote_response', etc.)
            data: Message data
            
        Returns:
            Response from the receiver
        """
        if receiver_id not in self.nodes:
            return None
            
        receiver = self.nodes[receiver_id]
        
        if message_type == "vote_request":
            return receiver.receive_vote_request(
                data["candidate_id"],
                data["term"],
                data["last_log_index"],
                data["last_log_term"]
            )
        elif message_type == "append_entries":
            return receiver.append_entries(
                data["term"],
                data["leader_id"],
                data["prev_log_index"],
                data["prev_log_term"],
                data["entries"],
                data["leader_commit"]
            )
        elif message_type == "heartbeat":
            receiver.receive_heartbeat(data["leader_id"], data["term"])
            return True
            
        return None
    
    def get_leader(self) -> Optional[int]:
        """Get the current leader node ID."""
        for node_id, node in self.nodes.items():
            if node.state == NodeState.LEADER:
                return node_id
        return None
    
    def get_cluster_state(self) -> Dict[int, Dict[str, Any]]:
        """Get the state of all nodes in the cluster."""
        return {node_id: node.get_state_info() for node_id, node in self.nodes.items()}
    
    def stop_all_nodes(self) -> None:
        """Stop all nodes in the cluster."""
        for node in self.nodes.values():
            node.stop()


def main():
    """Self-test: Raft's SAFETY rules driven by hand (no timer threads, no
    randomness) — one vote per term, term monotonicity, log up-to-dateness
    veto, append-entries consistency check, commit advancement."""
    # Disable the background election timers: the protocol itself is under
    # test, not the scheduler.
    RaftNode._initialize_node = lambda self: None

    ids = [1, 2, 3, 4, 5]
    nodes = {i: RaftNode(i, ids) for i in ids}

    # ELECTION SAFETY: candidate 2 (term 1) gathers all 4 votes...
    votes = sum(1 for i in (1, 3, 4, 5)
                if nodes[i].receive_vote_request(2, 1, -1, 0))
    assert votes == 4, f"up-to-date candidate must get 4/4 votes, got {votes}"
    # ...and a SECOND candidate in the SAME term gets none (one vote per term).
    votes3 = sum(1 for i in (1, 4, 5)
                 if nodes[i].receive_vote_request(3, 1, -1, 0))
    assert votes3 == 0, f"double voting in one term: {votes3} votes granted"

    # TERM MONOTONICITY: a higher term unseats the old vote...
    assert nodes[1].receive_vote_request(3, 2, -1, 0) is True, \
        "higher-term candidate denied"
    assert nodes[1].current_term == 2, "voter did not adopt the higher term"
    # ...and a stale term is refused outright.
    assert nodes[1].receive_vote_request(4, 1, -1, 0) is False, \
        "stale-term vote request granted"

    # LOG UP-TO-DATENESS VETO: a voter with a term-3 entry refuses a
    # candidate whose log ends in term 2.
    nodes[5].log.append(LogEntry(term=3, command="x", index=0))
    nodes[5].current_term = 3
    assert nodes[5].receive_vote_request(2, 4, -1, 0) is False, \
        "candidate with a STALE log was granted a vote"
    assert nodes[5].receive_vote_request(2, 4, 0, 3) is True, \
        "candidate with an up-to-date log was denied"

    # APPEND ENTRIES: replication, consistency check, commit advancement.
    f = nodes[4]
    e0 = LogEntry(term=1, command="set x=1", index=0)
    e1 = LogEntry(term=1, command="set y=2", index=1)
    assert f.append_entries(1, leader_id=2, prev_log_index=-1, prev_log_term=0,
                            entries=[e0, e1], leader_commit=0) is True
    assert len(f.log) == 2 and f.log[1].command == "set y=2"
    assert f.commit_index == 0, f"commit index must advance to 0, got {f.commit_index}"
    assert f.leader_id == 2

    # A GAP is refused (prev entry we don't have).
    e9 = LogEntry(term=1, command="orphan", index=9)
    assert f.append_entries(1, 2, prev_log_index=8, prev_log_term=1,
                            entries=[e9], leader_commit=0) is False, \
        "append with a log gap accepted"

    # A stale-term leader is refused.
    f.current_term = 5
    assert f.append_entries(1, 2, -1, 0, [], 0) is False, \
        "stale leader's append accepted"

    # CONFLICT: an entry with a different term at an existing index replaces
    # the tail (the Raft overwrite rule).
    g = nodes[3]
    g.append_entries(1, 2, -1, 0, [LogEntry(term=1, command="a", index=0),
                                   LogEntry(term=1, command="b", index=1)], -1)
    g.append_entries(2, 5, 0, 1, [LogEntry(term=2, command="B", index=1)], -1)
    assert len(g.log) == 2 and g.log[1].term == 2 and g.log[1].command == "B", \
        f"conflicting tail not overwritten: {[(e.term, e.command) for e in g.log]}"

    # Heartbeat: a candidate steps down to follower for an equal/higher term.
    c = nodes[2]
    c.state = NodeState.CANDIDATE
    c.current_term = 3
    c.receive_heartbeat(leader_id=5, term=4)
    assert c.state == NodeState.FOLLOWER, "candidate did not step down on heartbeat"
    assert c.current_term == 4 and c.leader_id == 5

    # Cluster wrapper: leader visibility.
    cluster = RaftCluster([])
    cluster.nodes = nodes
    assert cluster.get_leader() is None
    nodes[5].state = NodeState.LEADER
    assert cluster.get_leader() == 5
    assert cluster.simulate_network_message(5, 99, "heartbeat", {}) is None

    print("raft_consensus: 4/4 then 0/3 votes (one per term), stale terms "
          "refused, log veto held, gap refused, conflict tail overwritten, "
          "candidate stepped down — PASS")


if __name__ == "__main__":
    main()