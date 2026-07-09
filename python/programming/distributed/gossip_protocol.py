"""
Gossip Protocol Membership List Implementation

This module implements a gossip protocol for maintaining membership lists in distributed systems.
It includes features for member management, failure detection, and gossip-based information
dissemination using both infect and anti-entropy mechanisms.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import time
import random
import threading
from typing import Dict, List, Optional, Set, Tuple
from enum import Enum
from dataclasses import dataclass, field
from collections import defaultdict


class MemberStatus(Enum):
    """Enumeration of possible member statuses in the gossip protocol."""
    ALIVE = "alive"
    SUSPECT = "suspect"
    DEAD = "dead"


@dataclass
class Member:
    """Represents a member in the gossip network."""
    id: str
    address: str
    port: int
    status: MemberStatus = MemberStatus.ALIVE
    incarnation: int = 0
    last_update: float = field(default_factory=time.time)
    
    def __hash__(self) -> int:
        return hash(self.id)
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, Member):
            return False
        return self.id == other.id


class Gossip:
    """Implements a gossip protocol for membership management."""
    
    def __init__(
        self,
        member_id: str,
        address: str,
        port: int,
        suspicion_timeout: float = 5.0,
        cleanup_timeout: float = 10.0,
        gossip_interval: float = 1.0,
        max_gossip_targets: int = 3
    ):
        """
        Initialize a gossip node.
        
        Args:
            member_id: Unique identifier for this member
            address: IP address of this member
            port: Port number for this member
            suspicion_timeout: Time in seconds before suspecting a member is dead
            cleanup_timeout: Time in seconds before removing dead members
            gossip_interval: Interval between gossip rounds
            max_gossip_targets: Maximum number of targets to gossip with per round
        """
        self.member = Member(member_id, address, port)
        self.members: Dict[str, Member] = {member_id: self.member}
        self.suspicion_timeout = suspicion_timeout
        self.cleanup_timeout = cleanup_timeout
        self.gossip_interval = gossip_interval
        self.max_gossip_targets = max_gossip_targets
        self._lock = threading.RLock()
        self._stop_event = threading.Event()
        self._gossip_thread: Optional[threading.Thread] = None
        
    def join(self, target_address: str, target_port: int) -> bool:
        """
        Join the gossip network by contacting an existing member.
        
        Args:
            target_address: Address of existing member
            target_port: Port of existing member
            
        Returns:
            True if join was successful, False otherwise
        """
        try:
            # In a real implementation, this would send a join request
            # For this demo, we'll simulate success
            with self._lock:
                # Add the target as our first known member
                target_id = f"{target_address}:{target_port}"
                if target_id not in self.members:
                    self.members[target_id] = Member(
                        target_id, target_address, target_port
                    )
            return True
        except Exception:
            return False
    
    def add_member(self, member: Member) -> None:
        """
        Add a new member to the membership list.
        
        Args:
            member: Member to add
        """
        with self._lock:
            if member.id not in self.members:
                self.members[member.id] = member
            else:
                # Update existing member if this info is newer
                existing = self.members[member.id]
                if member.incarnation >= existing.incarnation:
                    self.members[member.id] = member
    
    def mark_suspect(self, member_id: str) -> bool:
        """
        Mark a member as suspect.
        
        Args:
            member_id: ID of member to mark as suspect
            
        Returns:
            True if member was updated, False otherwise
        """
        with self._lock:
            if member_id in self.members:
                member = self.members[member_id]
                if member.status == MemberStatus.ALIVE:
                    member.status = MemberStatus.SUSPECT
                    member.last_update = time.time()
                    member.incarnation += 1
                    return True
            return False
    
    def mark_dead(self, member_id: str) -> bool:
        """
        Mark a member as dead.
        
        Args:
            member_id: ID of member to mark as dead
            
        Returns:
            True if member was updated, False otherwise
        """
        with self._lock:
            if member_id in self.members:
                member = self.members[member_id]
                if member.status != MemberStatus.DEAD:
                    member.status = MemberStatus.DEAD
                    member.last_update = time.time()
                    member.incarnation += 1
                    return True
            return False
    
    def get_alive_members(self) -> List[Member]:
        """
        Get all alive members in the membership list.
        
        Returns:
            List of alive members
        """
        with self._lock:
            return [m for m in self.members.values() if m.status == MemberStatus.ALIVE]
    
    def get_suspect_members(self) -> List[Member]:
        """
        Get all suspect members in the membership list.
        
        Returns:
            List of suspect members
        """
        with self._lock:
            return [m for m in self.members.values() if m.status == MemberStatus.SUSPECT]
    
    def get_dead_members(self) -> List[Member]:
        """
        Get all dead members in the membership list.
        
        Returns:
            List of dead members
        """
        with self._lock:
            return [m for m in self.members.values() if m.status == MemberStatus.DEAD]
    
    def get_membership_list(self) -> List[Member]:
        """
        Get the complete membership list.
        
        Returns:
            List of all members
        """
        with self._lock:
            return list(self.members.values())
    
    def _infect_gossip(self) -> None:
        """Perform infect-style gossip by sending recent updates."""
        with self._lock:
            # Select random targets
            alive_members = [m for m in self.members.values() 
                           if m.status == MemberStatus.ALIVE and m.id != self.member.id]
            
            if not alive_members:
                return
                
            targets = random.sample(
                alive_members, 
                min(self.max_gossip_targets, len(alive_members))
            )
            
            # For demo purposes, we'll just print what would be sent
            # In a real implementation, this would send actual network messages
            for target in targets:
                # Send membership updates to target
                pass
    
    def _anti_entropy_gossip(self) -> None:
        """Perform anti-entropy gossip by exchanging full membership lists."""
        with self._lock:
            # Select random targets
            alive_members = [m for m in self.members.values() 
                           if m.status == MemberStatus.ALIVE and m.id != self.member.id]
            
            if not alive_members:
                return
                
            targets = random.sample(
                alive_members, 
                min(self.max_gossip_targets, len(alive_members))
            )
            
            # For demo purposes, we'll just print what would be sent
            # In a real implementation, this would exchange full membership lists
            for target in targets:
                # Exchange full membership lists with target
                pass
    
    def _check_timeouts(self) -> None:
        """Check for suspect timeouts and cleanup dead members."""
        current_time = time.time()
        with self._lock:
            # Check for suspect timeouts
            for member in list(self.members.values()):
                if (member.status == MemberStatus.SUSPECT and 
                    current_time - member.last_update > self.suspicion_timeout):
                    self.mark_dead(member.id)
            
            # Clean up dead members
            for member_id, member in list(self.members.items()):
                if (member.status == MemberStatus.DEAD and 
                    current_time - member.last_update > self.cleanup_timeout):
                    del self.members[member_id]
    
    def _gossip_round(self) -> None:
        """Perform one round of gossip operations."""
        # Alternate between infect and anti-entropy
        if random.random() < 0.7:  # 70% infect, 30% anti-entropy
            self._infect_gossip()
        else:
            self._anti_entropy_gossip()
        
        self._check_timeouts()
    
    def start(self) -> None:
        """Start the gossip protocol background thread."""
        if self._gossip_thread is not None:
            return
            
        self._stop_event.clear()
        
        def _run():
            while not self._stop_event.wait(self.gossip_interval):
                try:
                    self._gossip_round()
                except Exception:
                    # In production, log this error
                    pass
        
        self._gossip_thread = threading.Thread(target=_run, daemon=True)
        self._gossip_thread.start()
    
    def stop(self) -> None:
        """Stop the gossip protocol background thread."""
        if self._gossip_thread is None:
            return
            
        self._stop_event.set()
        self._gossip_thread.join()
        self._gossip_thread = None
    
    def __enter__(self):
        """Context manager entry."""
        self.start()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.stop()


def main():
    """Demo the gossip protocol with 5 peers."""
    print("Starting gossip protocol demo with 5 peers...")
    
    # Create 5 gossip nodes
    nodes: List[Gossip] = []
    for i in range(5):
        node = Gossip(
            member_id=f"node-{i}",
            address="127.0.0.1",
            port=8000 + i,
            suspicion_timeout=3.0,
            cleanup_timeout=6.0,
            gossip_interval=0.5
        )
        nodes.append(node)
    
    # Start all nodes
    for node in nodes:
        node.start()
    
    # Simulate nodes joining the network
    print("Simulating network formation...")
    for i in range(1, 5):
        # Node i joins by contacting node 0
        nodes[i].add_member(nodes[0].member)
        nodes[0].add_member(nodes[i].member)
    
    # Let the network stabilize
    time.sleep(2)
    
    # Print initial membership
    print("\nInitial membership lists:")
    for i, node in enumerate(nodes):
        alive_count = len(node.get_alive_members())
        print(f"Node {i}: {alive_count} alive members")
    
    # Simulate node failure (node 4 dies)
    print("\nSimulating node 4 failure...")
    nodes[4].stop()  # Stop the gossip thread
    
    # Manually mark node 4 as suspect in other nodes
    for i in range(4):
        nodes[i].mark_suspect("node-4")
    
    # Wait for suspicion timeout
    print("Waiting for suspicion timeout...")
    time.sleep(4)
    
    # Check membership after timeout
    print("\nMembership after suspicion timeout:")
    for i in range(4):
        alive_count = len(nodes[i].get_alive_members())
        suspect_count = len(nodes[i].get_suspect_members())
        dead_count = len(nodes[i].get_dead_members())
        print(f"Node {i}: {alive_count} alive, {suspect_count} suspect, {dead_count} dead")
    
    # Wait for cleanup timeout
    print("\nWaiting for cleanup timeout...")
    time.sleep(7)
    
    # Check membership after cleanup
    print("\nMembership after cleanup timeout:")
    for i in range(4):
        alive_count = len(nodes[i].get_alive_members())
        suspect_count = len(nodes[i].get_suspect_members())
        dead_count = len(nodes[i].get_dead_members())
        print(f"Node {i}: {alive_count} alive, {suspect_count} suspect, {dead_count} dead")
    
    # Stop all remaining nodes
    for i in range(4):
        nodes[i].stop()
    
    print("\nDemo completed successfully!")


if __name__ == "__main__":
    main()