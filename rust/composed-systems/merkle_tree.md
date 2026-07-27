# merkle tree

**Language:** Rust · **Sphere:** rust · **Category:** composed-systems

**Signature:** `(data: &[u8]) → [u8`

## What it does

merkle_tree — SHA-256 tree; tampering any leaf changes root; inclusion proof verifies.

Core idea: a binary tree where each node is the SHA-256 hash of its children.
Tampering any leaf propagates up to change the root. An inclusion proof constructs
a path from leaf to root and verifies membership. THE LAW: build a tree, tamper
one leaf, and assert the root changes; then prove an inclusion proof catches the tamper.
When to use: Merkle trees, Git objects, blockchain leaves, data integrity proofs.

## Guarantee

When it runs, merkle tree guarantees assert_ne!(tampered_root, root, "tampering leaf changes root"); assert_eq!(single_tree.root(), leaves[0], "single leaf root is the leaf") (weak-grade: proven by rustc-run).

**Checkable constraints:**

- `assert!(MerkleTree::verify_proof(*leaf, &proof, root), "leaf {i} proof verifies")`
- `assert_ne!(tampered_root, root, "tampering leaf changes root")`
- `assert!(!MerkleTree::verify_proof(leaves[0], &proof_leaf0, tampered_root), "original proof fails on tampered root")`
- `assert_eq!(single_tree.root(), leaves[0], "single leaf root is the leaf")`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
