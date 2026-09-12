"""heartbeat_gossip: gossip protocol where nodes exchange heartbeats to detect failures.
Failure simulated: node_1 sends heartbeats; node_2 stops sending; node_1 should detect node_2 as down.
Recovery asserted: node_2 marked down after missing heartbeats; node_1 correctly tracks node_2 status.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import time
import sys
import json

class GossipMember:
    """Represents a cluster member with last-seen heartbeat timestamp."""
    def __init__(self, node_id, heartbeat_interval_sec=0.05, failure_threshold=0.2):
        self.node_id = node_id
        self.last_heartbeat = time.time()
        self.heartbeat_interval = heartbeat_interval_sec
        self.failure_threshold = failure_threshold  # If no heartbeat for this long, mark down
        self.is_alive = True

    def send_heartbeat(self):
        """Record a heartbeat at current time."""
        self.last_heartbeat = time.time()

    def receive_heartbeat(self):
        """Receive a heartbeat from this member (update last_heartbeat)."""
        self.last_heartbeat = time.time()
        self.is_alive = True

    def check_alive(self, current_time=None):
        """
        Check if this member is still alive based on last heartbeat.
        If no heartbeat received for failure_threshold seconds, mark as down.
        """
        if current_time is None:
            current_time = time.time()

        elapsed = current_time - self.last_heartbeat

        if elapsed > self.failure_threshold:
            self.is_alive = False
            return False
        else:
            self.is_alive = True
            return True

class GossipCluster:
    """Manages gossip-based membership and failure detection."""
    def __init__(self, heartbeat_interval_sec=0.05, failure_threshold=0.2):
        self.members = {}
        self.heartbeat_interval = heartbeat_interval_sec
        self.failure_threshold = failure_threshold

    def add_member(self, node_id):
        """Add a member to the cluster."""
        self.members[node_id] = GossipMember(
            node_id,
            heartbeat_interval_sec=self.heartbeat_interval,
            failure_threshold=self.failure_threshold
        )

    def receive_heartbeat(self, node_id):
        """Record that we received a heartbeat from node_id."""
        if node_id in self.members:
            self.members[node_id].receive_heartbeat()

    def detect_failures(self):
        """
        Check all members; return list of dead node IDs.
        """
        dead_nodes = []
        for node_id, member in self.members.items():
            if not member.check_alive():
                dead_nodes.append(node_id)
        return dead_nodes

    def alive_count(self):
        """Count how many members are currently alive."""
        return sum(1 for m in self.members.values() if m.is_alive)

if __name__ == "__main__":
    # Create a 3-node cluster
    cluster = GossipCluster(heartbeat_interval_sec=0.01, failure_threshold=0.10)
    cluster.add_member("node_1")
    cluster.add_member("node_2")
    cluster.add_member("node_3")

    # Simulate all nodes sending heartbeats
    for node_id in ["node_1", "node_2", "node_3"]:
        cluster.receive_heartbeat(node_id)

    # Check: all should be alive
    alive_count_initial = cluster.alive_count()
    assert alive_count_initial == 3, f"All 3 nodes should be alive initially; got {alive_count_initial}"

    # Simulate: node_2 stops sending heartbeats (trigger failure)
    # Keep node_1 and node_3 sending heartbeats while waiting
    # Don't call receive_heartbeat for node_2 anymore
    time.sleep(0.08)
    cluster.receive_heartbeat("node_1")  # node_1 keeps sending
    cluster.receive_heartbeat("node_3")  # node_3 keeps sending
    time.sleep(0.08)  # Total wait is 0.16s (>> failure_threshold of 0.10s — robust margin)
    cluster.receive_heartbeat("node_1")  # Send one more to ensure node_1 stays alive
    cluster.receive_heartbeat("node_3")

    # Check again: node_2 should now be marked as dead
    dead_nodes = cluster.detect_failures()
    assert "node_2" in dead_nodes, "node_2 should be detected as dead after missing heartbeats"
    assert "node_1" not in dead_nodes and "node_3" not in dead_nodes, \
        "node_1 and node_3 should still be alive (they're sending heartbeats)"

    # Check alive count
    alive_count_after = cluster.alive_count()
    assert alive_count_after == 2, f"After node_2 fails, 2 should be alive; got {alive_count_after}"

    # Assert state change: all alive (3) → one dead (2 alive)
    assert alive_count_initial == 3 and alive_count_after == 2, \
        f"Alive count must change from 3→2 when node_2 fails; got {alive_count_initial}→{alive_count_after}"

    # Additional verify: node_1 and node_3 still alive
    node_1_alive = cluster.members["node_1"].is_alive
    node_3_alive = cluster.members["node_3"].is_alive
    assert node_1_alive is True and node_3_alive is True, \
        f"node_1 and node_3 should remain alive"

    print(f"heartbeat_gossip: alive={alive_count_initial}→{alive_count_after} dead={dead_nodes} PASS")
    sys.exit(0)
