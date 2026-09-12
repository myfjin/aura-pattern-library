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

        # Build tree level by level. An odd count can appear at ANY level
        # (5 leaves → 6 after dup → 3 parents), so duplicate per level —
        # the former leaf-only duplication crashed on 5+ odd shapes.
        while len(nodes) > 1:
            if len(nodes) % 2 == 1:
                nodes.append(nodes[-1])
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

        target_index = index

        while len(nodes) > 1:
            # Mirror build(): odd levels duplicate their last node.
            if len(nodes) % 2 == 1:
                nodes.append(nodes[-1])
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
    """Self-test: root independently re-derived, all proofs verify, and — the
    point of a Merkle tree — every tampering attempt is DETECTED."""
    h = MerkleTree._hash

    # 8 leaves; fold the root by hand as an independent oracle.
    leaves = [f"data{i}" for i in range(8)]
    tree = MerkleTree()
    for leaf in leaves:
        tree.add_leaf(leaf)
    tree.build()
    level = [h(x) for x in leaves]
    while len(level) > 1:
        level = [h(level[i] + level[i + 1]) for i in range(0, len(level), 2)]
    assert tree.get_root() == level[0], "root differs from independent fold"

    # Every leaf's proof verifies, and each proof has exactly log2(8)=3 steps.
    total_steps = 0
    for i, leaf in enumerate(leaves):
        proof = tree.get_proof(i)
        total_steps += len(proof)
        assert tree.verify_proof(leaf, i, proof) is True, f"honest proof {i} rejected"
    assert total_steps == 24, f"8 proofs x log2(8)=3 steps must total 24, got {total_steps}"

    # THE DISASTER, three ways — all must be caught:
    proof = tree.get_proof(3)
    #  a) a forged leaf value
    assert tree.verify_proof("evil_data", 3, proof) is False, "forged leaf accepted"
    #  b) a tampered proof step
    bad = [(("0" * 64) if k == 1 else s, side) for k, (s, side) in enumerate(proof)]
    assert tree.verify_proof(leaves[3], 3, bad) is False, "tampered proof accepted"
    #  c) a truncated proof
    assert tree.verify_proof(leaves[3], 3, proof[:-1]) is False, "truncated proof accepted"

    # Changing any single leaf changes the root (tamper-evidence of the tree).
    old_root = tree.get_root()
    t2 = MerkleTree()
    for i, leaf in enumerate(leaves):
        t2.add_leaf("TAMPERED" if i == 5 else leaf)
    t2.build()
    assert t2.get_root() != old_root, "root identical despite a modified leaf"

    # Odd leaf count (5): last leaf duplicated; every proof still verifies.
    odd = MerkleTree()
    for x in ("a", "b", "c", "d", "e"):
        odd.add_leaf(x)
    odd.build()
    for i, x in enumerate("abcde"):
        assert odd.verify_proof(x, i, odd.get_proof(i)) is True, \
            f"odd-count proof {i} rejected"

    # Empty tree and refusals.
    empty = MerkleTree()
    assert empty.get_root() is None
    try:
        empty.get_proof(0)
        assert False, "proof from an empty tree accepted"
    except RuntimeError:
        pass
    for call in (lambda: tree.get_proof(100), lambda: tree.get_proof(-1)):
        try:
            call()
            assert False, "out-of-range proof index accepted"
        except ValueError:
            pass
    try:
        tree.add_leaf(42)  # type: ignore[arg-type]
        assert False, "non-string leaf accepted"
    except TypeError:
        pass

    print("merkle_tree: root == independent fold, 8/8 + 5/5 proofs verify, "
          "forged/tampered/truncated all caught, leaf-change moves root — PASS")


if __name__ == "__main__":
    main()