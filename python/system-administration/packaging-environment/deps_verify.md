# deps verify

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 17 · Packaging & environment

**Signature:** `(manifest_path: str, actual_versions: dict) → ?`

## What it does

deps_verify: verify a dependency manifest exists, all versions are pinned, and checksums match.
Failure simulated: a malicious dep replaces a legitimate one with a different version under
the same name. The verifier MUST catch it (version mismatch in actual vs expected).

## Guarantee

When it runs, deps verify guarantees 'version mismatch' in str(e) and 'requests' in str(e); verify_dependencies(manifest_path, good_versions) (weak-grade: directional, proven by run).

**Checkable constraints:**

- `'version mismatch' in str(e) and 'requests' in str(e)`
- `verify_dependencies(manifest_path, good_versions)`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
