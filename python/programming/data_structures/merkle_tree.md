# merkle tree

**Language:** Python · **Oracle sphere:** rust (this file is the Python twin) · **Category:** data structures

## What it does

A simple Merkle tree implementation using SHA-256 hashing.

This module provides classes to create and work with Merkle trees,
including building trees, generating proofs, and verifying them.

## Guarantee

When it runs, merkle tree guarantees `tree.get_root() == level[0]`; `tree.verify_proof(leaf, i, proof) is True`; `total_steps == 24` — read from this file's own self-test. The oracle behind this pattern was established on the rust original and is not claimed to have been run against this file.

**Checkable constraints:**

- `tree.get_root() == level[0]`
- `tree.verify_proof(leaf, i, proof) is True`
- `total_steps == 24`
- `tree.verify_proof('evil_data', 3, proof) is False`
- `tree.verify_proof(leaves[3], 3, bad) is False`
- `tree.verify_proof(leaves[3], 3, proof[:-1]) is False`
- `t2.get_root() != old_root`
- `odd.verify_proof(x, i, odd.get_proof(i)) is True`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — established on the RUST original and shared by this Python twin (twin agreement is the evidence: consensus, xlang); the original oracle was not executed against this file
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
