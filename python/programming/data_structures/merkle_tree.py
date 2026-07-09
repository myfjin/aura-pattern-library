"""
A simple Merkle tree implementation using SHA-256 hashing.

This module provides classes to create and work with Merkle trees,
including building trees, generating proofs, and verifying them.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import hashlib
from typing import List, Optional, Tuple, Union


class MerkleNode:
    """
    Represents a node in a Merkle tree.
    
    Attributes:
        hash_value: The hash value of this node
        left: Left child node
        right: Right child node
        is_leaf: Whether this node is a leaf
    """
    
    def __init__(self, 
                 hash_value: str, 
                 left: Optional['MerkleNode'] = None, 
                 right: Optional['MerkleNode'] = None,
                 is_leaf: bool = False):
        """
        Initialize a Merkle node.
        
        Args:
            hash_value: Hash value for this node
            left: Left child node
            right: Right child node
            is_leaf: Whether this is a leaf node
        """
        self.hash_value = hash_value
        self.left = left
        self.right = right
        self.is_leaf = is_leaf
    
    def __str__(self) -> str:
        """Return string representation of the node."""
        return f"MerkleNode({self.hash_value[:8]}...)"
    
    def __repr__(self) -> str:
        """Return detailed string representation."""
        return self.__str__()


class MerkleTree:
    """
    A Merkle tree implementation for creating and verifying Merkle proofs.
    
    Attributes:
        leaves: List of leaf values
        root: Root node of the Merkle tree
    """
    
    def __init__(self):
        """Initialize an empty Merkle tree."""
        self.leaves: List[str] = []
        self.root: Optional[MerkleNode] = None
    
    @staticmethod
    def _hash(data: str) -> str:
        """
        Hash data using SHA-256.
        
        Args:
            data: String data to hash
            
        Returns:
            Hexadecimal representation of the hash
        """
        return hashlib.sha256(data.encode('utf-8')).hexdigest()
    
    def add_leaf(self, value: str) -> None:
        """
        Add a leaf to the tree.
        
        Args:
            value: Value to add as a leaf
        """
        if not isinstance(value, str):
            raise TypeError("Leaf value must be a string")
        self.leaves.append(value)
        # Reset root since tree structure will change
        self.root = None
    
    def build(self) -> None:
        """Build the Merkle tree from the current leaves."""
        if not self.leaves:
            self.root = None
            return
            
        # Create leaf nodes
        nodes = [MerkleNode(self._hash(leaf), is_leaf=True) for leaf in self.leaves]
        
        # Handle odd number of nodes by duplicating the last one
        if len(nodes) % 2 == 1:
            nodes.append(nodes[-1])
        
        # Build tree level by level
        while len(nodes) > 1:
            next_level = []
            for i in range(0, len(nodes), 2):
                left = nodes[i]
                right = nodes[i + 1]
                # Hash of concatenated child hashes
                combined_hash = self._hash(left.hash_value + right.hash_value)
                parent = MerkleNode(combined_hash, left, right)
                next_level.append(parent)
            nodes = next_level
        
        self.root = nodes[0] if nodes else None
    
    def get_root(self) -> Optional[str]:
        """
        Get the root hash of the Merkle tree.
        
        Returns:
            Root hash as hex string, or None if tree is empty
        """
        if not self.root:
            self.build()
        return self.root.hash_value if self.root else None
    
    def get_proof(self, index: int) -> List[Tuple[str, bool]]:
        """
        Generate a Merkle proof for a leaf at the given index.
        
        Args:
            index: Index of the leaf to generate proof for
            
        Returns:
            List of tuples (hash, is_left_sibling) representing the proof path
            
        Raises:
            ValueError: If index is out of range
            RuntimeError: If tree hasn't been built
        """
        if not self.root:
            self.build()
            
        if not self.root:
            raise RuntimeError("Cannot generate proof for empty tree")
            
        if index < 0 or index >= len(self.leaves):
            raise ValueError(f"Index {index} out of range [0, {len(self.leaves)-1}]")
        
        proof: List[Tuple[str, bool]] = []
        nodes = [MerkleNode(self._hash(leaf), is_leaf=True) for leaf in self.leaves]
        
        # Handle odd number of nodes
        if len(nodes) % 2 == 1:
            nodes.append(nodes[-1])
        
        target_index = index
        
        while len(nodes) > 1:
            next_level = []
            for i in range(0, len(nodes), 2):
                left = nodes[i]
                right = nodes[i + 1]
                combined_hash = self._hash(left.hash_value + right.hash_value)
                parent = MerkleNode(combined_hash, left, right)
                
                # If target is one of the children, add the sibling to proof
                if i == target_index or i + 1 == target_index:
                    if i == target_index:
                        proof.append((right.hash_value, False))  # Right is sibling
                        target_index = len(next_level)  # Position in next level
                    else:
                        proof.append((left.hash_value, True))  # Left is sibling
                        target_index = len(next_level)  # Position in next level
                next_level.append(parent)
            nodes = next_level
            
        return proof
    
    def verify_proof(self, 
                     leaf_value: str, 
                     index: int, 
                     proof: List[Tuple[str, bool]]) -> bool:
        """
        Verify a Merkle proof for a given leaf.
        
        Args:
            leaf_value: The leaf value to verify
            index: Index of the leaf in the tree
            proof: The proof path as list of (hash, is_left_sibling)
            
        Returns:
            True if proof is valid, False otherwise
        """
        if not self.root:
            self.build()
            
        if not self.root:
            return False
            
        # Start with the leaf hash
        current_hash = self._hash(leaf_value)
        
        # Apply each step in the proof
        for sibling_hash, is_left in proof:
            if is_left:
                # Sibling is left, so it comes first in concatenation
                current_hash = self._hash(sibling_hash + current_hash)
            else:
                # Sibling is right, so current comes first
                current_hash = self._hash(current_hash + sibling_hash)
        
        # Check if we arrived at the root
        return current_hash == self.root.hash_value


def main():
    """Demo the Merkle tree with 8 leaves."""
    # Create a Merkle tree
    tree = MerkleTree()
    
    # Add 8 leaves
    leaves = [f"data{i}" for i in range(8)]
    for leaf in leaves:
        tree.add_leaf(leaf)
    
    # Build the tree
    tree.build()
    
    print("Merkle Tree Demo")
    print("================")
    print(f"Leaves: {leaves}")
    print(f"Root hash: {tree.get_root()}")
    print()
    
    # Generate and verify proofs for all leaves
    for i in range(len(leaves)):
        proof = tree.get_proof(i)
        is_valid = tree.verify_proof(leaves[i], i, proof)
        
        print(f"Leaf {i}: {leaves[i]}")
        print(f"  Proof: {proof}")
        print(f"  Valid: {is_valid}")
        
        # Test with invalid proof
        if i < len(leaves) - 1:
            # Try with wrong leaf value
            invalid_valid = tree.verify_proof("wrong_value", i, proof)
            print(f"  Valid with wrong value: {invalid_valid}")
        print()
    
    # Test error handling
    try:
        tree.get_proof(100)  # Should raise ValueError
    except ValueError as e:
        print(f"Correctly caught error: {e}")


if __name__ == "__main__":
    main()