# lockfile hash integrity

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 17 · Packaging & environment

**Signature:** `(lockfile_path: str, dep_contents: dict) → ?`

## What it does

lockfile_hash_integrity: store dep checksums in a lockfile; verify them; tamper one and
detect the break. Each entry is hashed (SHA256 of the dep content). Tampering with the
content breaks the hash. A naive verifier that just reads hashes from the tampered file
would miss the breach — this one recomputes and compares.

## Guarantee

When it runs, lockfile hash integrity guarantees verify_lockfile(lockfile_path, {'flask-reqs': dep1_content, 'requests-reqs': dep2_content}); 'hash mismatch' in str(e) and 'flask-reqs' in str(e) (weak-grade: directional, proven by run).

**Checkable constraints:**

- `verify_lockfile(lockfile_path, {'flask-reqs': dep1_content, 'requests-reqs': dep2_content})`
- `'hash mismatch' in str(e) and 'flask-reqs' in str(e)`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
