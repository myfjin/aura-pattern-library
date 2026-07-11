#!/usr/bin/env python3
"""
Consistent Hash Ring Implementation

This module provides a consistent hash ring implementation that distributes
keys across nodes in a way that minimizes redistribution when nodes are
added or removed.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import hashlib
import bisect
from typing import Dict, List, Optional, Tuple, Any


class VirtualNode:
    """
    Represents a virtual node in the hash ring.
    
    Each physical node is represented by multiple virtual nodes to ensure
    better distribution across the ring.
    """
    
    def __init__(self, node_id: str, index: int, hash_value: int):
        """
        Initialize a virtual node.
        
        Args:
            node_id: Identifier of the physical node
            index: Index of this virtual node for the physical node
            hash_value: Hash value position on the ring
        """
        self.node_id = node_id
        self.index = index
        self.hash_value = hash_value
    
    def __repr__(self) -> str:
        return f"VirtualNode(node_id='{self.node_id}', index={self.index}, hash_value={self.hash_value})"
    
    def __lt__(self, other) -> bool:
        if isinstance(other, VirtualNode):
            return self.hash_value < other.hash_value
        return NotImplemented


class HashRing:
    """
    Consistent Hash Ring implementation.
    
    Distributes keys across nodes with minimal redistribution when nodes
    are added or removed. Uses virtual nodes to ensure even distribution.
    """
    
    def __init__(self, virtual_nodes_per_physical_node: int = 100):
        """
        Initialize the hash ring.
        
        Args:
            virtual_nodes_per_physical_node: Number of virtual nodes per physical node
            
        Raises:
            ValueError: If virtual_nodes_per_physical_node is less than 1
        """
        if virtual_nodes_per_physical_node < 1:
            raise ValueError("virtual_nodes_per_physical_node must be at least 1")
            
        self.virtual_nodes_per_physical_node = virtual_nodes_per_physical_node
        self.ring: List[VirtualNode] = []
        self.nodes: Dict[str, Any] = {}
        self.sorted_hashes: List[int] = []
    
    def _hash(self, key: str) -> int:
        """
        Generate a hash value for a key.
        
        Args:
            key: String to hash
            
        Returns:
            Integer hash value
        """
        return int(hashlib.md5(key.encode('utf-8')).hexdigest(), 16)
    
    def add_node(self, node_id: str, node_data: Any = None) -> None:
        """
        Add a node to the hash ring.
        
        Args:
            node_id: Unique identifier for the node
            node_data: Optional data to associate with the node
        """
        if node_id in self.nodes:
            return
            
        self.nodes[node_id] = node_data
        
        # Create virtual nodes for this physical node
        for i in range(self.virtual_nodes_per_physical_node):
            virtual_node_key = f"{node_id}:{i}"
            hash_value = self._hash(virtual_node_key)
            virtual_node = VirtualNode(node_id, i, hash_value)
            
            # Insert into sorted positions
            bisect.insort(self.ring, virtual_node)
            bisect.insort(self.sorted_hashes, hash_value)
    
    def remove_node(self, node_id: str) -> None:
        """
        Remove a node from the hash ring.
        
        Args:
            node_id: Identifier of the node to remove
            
        Raises:
            KeyError: If node_id is not in the ring
        """
        if node_id not in self.nodes:
            raise KeyError(f"Node '{node_id}' not found in ring")
            
        # Remove virtual nodes, then rebuild the hash index from what
        # remains. (The former code filtered the ring FIRST and then looked
        # for the removed node in the filtered ring — never true, so stale
        # hashes stayed behind and keys landing on them resolved to None.)
        self.ring = [vn for vn in self.ring if vn.node_id != node_id]
        self.sorted_hashes = sorted(vn.hash_value for vn in self.ring)
        
        # Remove from nodes dict
        del self.nodes[node_id]
    
    def get_node(self, key: str) -> Optional[str]:
        """
        Get the node responsible for a key.
        
        Args:
            key: Key to find node for
            
        Returns:
            Node ID responsible for the key, or None if no nodes exist
        """
        if not self.ring:
            return None
            
        if len(self.ring) == 1:
            return self.ring[0].node_id
            
        key_hash = self._hash(key)
        
        # Find the first virtual node >= key_hash
        idx = bisect.bisect_left(self.sorted_hashes, key_hash)
        
        # If we're past the end, wrap around to the beginning
        if idx == len(self.sorted_hashes):
            idx = 0
            
        target_hash = self.sorted_hashes[idx]
        
        # Find the virtual node with this hash
        for virtual_node in self.ring:
            if virtual_node.hash_value == target_hash:
                return virtual_node.node_id
                
        return None
    
    def rebalance(self) -> Dict[str, List[str]]:
        """
        Rebalance keys across nodes.
        
        Returns:
            Dictionary mapping node IDs to lists of keys they should own
        """
        # This is a simplified rebalance - in a real implementation,
        # you would have a data store to move actual data
        return {}


def main():
    """Self-test: THE consistent-hashing claims, measured — stable mapping,
    bounded movement on add (only keys moving TO the new node), total
    redistribution of a removed node's keys, rough balance."""
    ring = HashRing(virtual_nodes_per_physical_node=40)
    nodes = ["node1", "node2", "node3"]
    for node in nodes:
        ring.add_node(node, {"host": node})
    assert len(ring.ring) == 120, f"3 nodes x 40 vnodes must be 120, got {len(ring.ring)}"

    keys = [f"key_{i}" for i in range(1000)]

    # Deterministic, total, stable mapping.
    before = {k: ring.get_node(k) for k in keys}
    assert all(v in nodes for v in before.values()), "key mapped to a ghost node"
    assert before == {k: ring.get_node(k) for k in keys}, "mapping not stable"

    # Rough balance: with 40 vnodes each, every node holds a sane share.
    counts = {n: sum(1 for v in before.values() if v == n) for n in nodes}
    assert sum(counts.values()) == 1000
    assert all(150 <= c <= 550 for c in counts.values()), \
        f"distribution badly skewed: {counts}"

    # THE CONSISTENCY CLAIM: adding a node moves keys ONLY onto the new
    # node — no key may move between two old nodes — and the moved share
    # is near 1/4 (bounded well below a full reshuffle).
    ring.add_node("node4", {"host": "node4"})
    after = {k: ring.get_node(k) for k in keys}
    moved = {k for k in keys if before[k] != after[k]}
    illegal = [k for k in moved if after[k] != "node4"]
    assert illegal == [], \
        f"{len(illegal)} keys moved between OLD nodes (consistency broken)"
    assert 0 < len(moved) < 500, \
        f"adding 1 of 4 nodes should move ~250/1000 keys, moved {len(moved)}"

    # Removing the node hands its keys back — and ONLY its keys move.
    ring.remove_node("node4")
    restored = {k: ring.get_node(k) for k in keys}
    assert restored == before, \
        "remove(add(ring)) must restore the exact original mapping"

    # Removing an original node: its keys redistribute, others stay put.
    ring.remove_node("node2")
    final = {k: ring.get_node(k) for k in keys}
    for k in keys:
        if before[k] != "node2":
            assert final[k] == before[k], \
                f"key {k} moved although its node was not removed"
        else:
            assert final[k] in ("node1", "node3"), f"orphaned key {k} -> {final[k]}"
    assert counts["node2"] == sum(1 for k in keys if before[k] == "node2")

    # Empty ring answers honestly.
    empty = HashRing()
    assert empty.get_node("anything") is None, "empty ring invented a node"

    print(f"consistent_hash_ring: 1000 keys stable, balance {sorted(counts.values())}, "
          f"add moved {len(moved)} (all to node4), remove restored exactly — PASS")


if __name__ == "__main__":
    main()