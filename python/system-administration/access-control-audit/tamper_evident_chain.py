"""
tamper_evident_chain: build a Merkle tree where each node's hash depends on its children.
Any tampering with a leaf changes the root hash. Flip a byte in a leaf and verify the
root hash validation fails.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import hashlib
import json
import tempfile
import os
import sys


def sha256(data):
    """Compute SHA256 of data (bytes or str)."""
    if isinstance(data, str):
        data = data.encode()
    return hashlib.sha256(data).hexdigest()


class MerkleTree:
    """Simple Merkle tree for tamper detection."""

    def __init__(self):
        self.leaves = []
        self.root = None

    def add_leaf(self, data):
        """Add a leaf to the tree."""
        leaf_hash = sha256(data)
        self.leaves.append((data, leaf_hash))

    def build_tree(self):
        """Build the Merkle tree and compute root hash."""
        if not self.leaves:
            self.root = "0" * 64
            return

        hashes = [h for _, h in self.leaves]

        # Build tree level by level until one hash remains.
        while len(hashes) > 1:
            new_level = []
            for i in range(0, len(hashes), 2):
                if i + 1 < len(hashes):
                    combined = hashes[i] + hashes[i + 1]
                else:
                    combined = hashes[i]
                new_level.append(sha256(combined))
            hashes = new_level

        self.root = hashes[0]

    def verify_leaf(self, leaf_index, expected_leaf_data):
        """Verify a leaf hasn't been tampered."""
        if leaf_index >= len(self.leaves):
            raise ValueError(f"leaf index {leaf_index} out of range")
        original_data, _ = self.leaves[leaf_index]
        if sha256(expected_leaf_data) != sha256(original_data):
            raise ValueError(f"leaf {leaf_index} has been tampered")
        return True

    def verify_root(self, tampered_leaves=None):
        """Verify root hash matches current tree. If tampered_leaves provided, check those."""
        if tampered_leaves is None:
            tampered_leaves = {}

        # Rebuild tree with potential tampering.
        hashes = []
        for idx, (original_data, _) in enumerate(self.leaves):
            if idx in tampered_leaves:
                leaf_hash = sha256(tampered_leaves[idx])
            else:
                leaf_hash = sha256(original_data)
            hashes.append(leaf_hash)

        while len(hashes) > 1:
            new_level = []
            for i in range(0, len(hashes), 2):
                if i + 1 < len(hashes):
                    combined = hashes[i] + hashes[i + 1]
                else:
                    combined = hashes[i]
                new_level.append(sha256(combined))
            hashes = new_level

        rebuilt_root = hashes[0] if hashes else "0" * 64

        if rebuilt_root != self.root:
            raise ValueError(
                f"root mismatch: expected {self.root}, got {rebuilt_root}"
            )
        return True


if __name__ == "__main__":
    tree = MerkleTree()

    # Add leaves (events).
    tree.add_leaf("event: user alice logged in")
    tree.add_leaf("event: file /etc/passwd accessed")
    tree.add_leaf("event: user bob created directory")

    # Build tree.
    tree.build_tree()
    original_root = tree.root

    # Clean case: verify root with no tampering.
    assert tree.verify_root()

    # THE FAILURE: tamper with a leaf.
    tampered_leaves = {
        0: b"event: user alice HACKED"  # tampered leaf 0
    }

    # ASSERT: root verification catches the tampering.
    try:
        tree.verify_root(tampered_leaves)
        assert False, "should have detected tampering"
    except ValueError as e:
        assert "root mismatch" in str(e)

    # THE FAILURE 2: tamper with a middle leaf.
    tampered_leaves2 = {
        1: b"event: file /etc/passwd DELETED"  # tampered leaf 1
    }

    try:
        tree.verify_root(tampered_leaves2)
        assert False, "should have detected tampering"
    except ValueError as e:
        assert "root mismatch" in str(e)

    import shutil
    print("✓ tamper_evident_chain passed")
    sys.exit(0)
