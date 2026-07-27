# tamper evident chain

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 18 · Access control & audit

**Signature:** `(data: str) → ?`

## What it does

tamper_evident_chain: build a Merkle tree where each node's hash depends on its children.
Any tampering with a leaf changes the root hash. Flip a byte in a leaf and verify the
root hash validation fails.

## Guarantee

When it runs, tamper evident chain guarantees tree.verify_root(); 'root mismatch' in str(e); 'root mismatch' in str(e) (weak-grade: directional, proven by run).

**Checkable constraints:**

- `tree.verify_root()`
- `'root mismatch' in str(e)`
- `'root mismatch' in str(e)`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `def sha256(data):`, `class MerkleTree:`, `def __init__(self):`, `def add_leaf(self, data):`, `def build_tree(self):`, `def verify_leaf(self, leaf_index, expected_leaf_data):`, `def verify_root(self, tampered_leaves=None):`
**Valid input:** Leaves are bytes-like or string data; `leaf_index` is in range; `tampered_leaves` is a dict of index → replacement data.
**Core:** Simple Merkle tree. Pairwise SHA-256 hashes are combined level by level to produce a root; `verify_root` rebuilds the tree with optional tampered leaves and compares the resulting root.
**Assert:** Clean tree verifies; replacing leaf 0 with `b"event: user alice HACKED"` or leaf 1 with tampered data raises "root mismatch".
**⚠️ Defect:** `verify_leaf` compares hashes rather than raw data (`sha256(expected) != sha256(original)`), so it never validates the caller's expected data against the stored leaf content. The tree does not store internal node hashes, so it cannot produce or verify a real Merkle proof path.

---

## Category: backup-disaster-recovery

---
*△ AURA Pattern Library — © Reality Optimizer*
