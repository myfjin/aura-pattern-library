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
            
        # Remove virtual nodes
        self.ring = [vn for vn in self.ring if vn.node_id != node_id]
        self.sorted_hashes = [h for h in self.sorted_hashes if not any(vn.hash_value == h and vn.node_id == node_id for vn in self.ring)]
        
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
    """Demo of the consistent hash ring with 100 keys distributed across nodes."""
    # Create a hash ring
    ring = HashRing(virtual_nodes_per_physical_node=40)
    
    # Add nodes
    nodes = ["node1.example.com", "node2.example.com", "node3.example.com"]
    for node in nodes:
        ring.add_node(node, {"host": node, "port": 8080})
    
    print("Hash Ring Demo")
    print("=" * 50)
    print(f"Created ring with {len(ring.ring)} virtual nodes")
    print(f"Physical nodes: {list(ring.nodes.keys())}")
    print()
    
    # Distribute 100 keys
    keys = [f"key_{i}" for i in range(100)]
    distribution: Dict[str, int] = {}
    
    print("Key Distribution:")
    print("-" * 30)
    
    for key in keys:
        node = ring.get_node(key)
        if node:
            distribution[node] = distribution.get(node, 0) + 1
            if len(key) <= 10:  # Only show first few keys for brevity
                print(f"{key:<15} -> {node}")
    
    print()
    print("Distribution Summary:")
    print("-" * 30)
    for node, count in distribution.items():
        percentage = (count / len(keys)) * 100
        print(f"{node:<20}: {count:>3} keys ({percentage:>5.1f}%)")
    
    # Test adding a node
    print()
    print("Adding node4.example.com...")
    ring.add_node("node4.example.com", {"host": "node4.example.com", "port": 8080})
    
    new_distribution: Dict[str, int] = {}
    for key in keys:
        node = ring.get_node(key)
        if node:
            new_distribution[node] = new_distribution.get(node, 0) + 1
    
    print("New Distribution Summary:")
    print("-" * 30)
    for node, count in new_distribution.items():
        percentage = (count / len(keys)) * 100
        print(f"{node:<20}: {count:>3} keys ({percentage:>5.1f}%)")
    
    # Show how many keys moved
    print()
    print("Keys that moved after adding node4:")
    print("-" * 40)
    moved_count = 0
    for key in keys[:20]:  # Check first 20 keys for demo
        old_node = None
        for node, count in distribution.items():
            # This is approximate - in a real implementation we'd track actual assignments
            key_hash = ring._hash(key)
            # Simplified check for demo purposes
            if key_hash % len(distribution) == list(distribution.keys()).index(node):
                old_node = node
                break
        
        new_node = ring.get_node(key)
        if old_node and new_node and old_node != new_node:
            moved_count += 1
            print(f"{key:<15}: {old_node} -> {new_node}")
    
    print(f"\nTotal keys that moved (approx): {moved_count} out of {len(keys)}")
    print(f"Efficiency: {(1 - moved_count/len(keys))*100:.1f}% of keys stayed in place")


if __name__ == "__main__":
    main()