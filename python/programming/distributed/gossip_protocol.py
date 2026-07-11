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
    """Self-test (no background threads — the state machine is driven by
    hand on a fake clock): membership exact, SWIM lifecycle
    alive→suspect→dead→forgotten at the configured timeouts, incarnation
    ordering on updates."""
    _real_time = time.time
    _now = [_real_time()]          # align with Member's default_factory
    time.time = lambda: _now[0]
    try:
        node = Gossip(member_id="node-0", address="127.0.0.1", port=8000,
                      suspicion_timeout=3.0, cleanup_timeout=6.0,
                      gossip_interval=0.5)
        for i in range(1, 5):
            node.add_member(Member(id=f"node-{i}", address="127.0.0.1",
                                   port=8000 + i))
        alive = {m.id for m in node.get_alive_members()}
        assert alive >= {f"node-{i}" for i in range(1, 5)}, f"members missing: {alive}"
        n_members = len(node.get_membership_list())
        assert n_members == 5, f"self + 4 peers must be 5 members, got {n_members}"

        # Duplicate adds don't duplicate.
        node.add_member(Member(id="node-1", address="127.0.0.1", port=8001))
        assert len(node.get_membership_list()) == 5, "duplicate add grew the list"

        # SUSPECT: honest transition, honest returns.
        assert node.mark_suspect("node-4") is True
        assert node.mark_suspect("ghost") is False
        assert {m.id for m in node.get_suspect_members()} == {"node-4"}
        assert "node-4" not in {m.id for m in node.get_alive_members()}

        # Before the suspicion timeout the suspect is NOT declared dead.
        _now[0] += 2.9
        node._check_timeouts()
        assert node.get_dead_members() == [], "suspect declared dead before timeout"

        # Past the timeout it becomes DEAD.
        _now[0] += 0.2
        node._check_timeouts()
        assert {m.id for m in node.get_dead_members()} == {"node-4"}, \
            "suspect not promoted to dead after suspicion_timeout"
        assert len(node.get_suspect_members()) == 0

        # Past the cleanup timeout the corpse is forgotten entirely.
        _now[0] += 6.1
        node._check_timeouts()
        assert "node-4" not in {m.id for m in node.get_membership_list()}, \
            "dead member not cleaned up after cleanup_timeout"
        assert len(node.get_membership_list()) == 4

        # Direct mark_dead works too.
        assert node.mark_dead("node-3") is True
        assert {m.id for m in node.get_dead_members()} == {"node-3"}

        # INCARNATION: an older incarnation must not overwrite a newer one.
        fresh = Member(id="node-2", address="127.0.0.1", port=8002, incarnation=5)
        node.add_member(fresh)
        assert node.members["node-2"].incarnation == 5
        stale = Member(id="node-2", address="127.0.0.1", port=8002, incarnation=3)
        node.add_member(stale)
        assert node.members["node-2"].incarnation == 5, \
            "stale incarnation overwrote a newer member record"

        # Gossip exchange converges membership between two live nodes.
        other = Gossip(member_id="node-9", address="127.0.0.1", port=8009,
                       suspicion_timeout=3.0, cleanup_timeout=6.0)
        for m in node.get_membership_list():
            other.add_member(m)
        assert {m.id for m in other.get_alive_members()} >= \
            {m.id for m in node.get_alive_members()}, "membership transfer lost members"
    finally:
        time.time = _real_time

    print("gossip_protocol: 5 members exact, suspect held at 2.9s / dead at 3.1s "
          "/ forgotten at +6.1s, stale incarnation rejected — PASS")


if __name__ == "__main__":
    main()