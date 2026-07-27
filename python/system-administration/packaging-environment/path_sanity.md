# path sanity

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 17 · Packaging & environment

**Signature:** `(path_str: str, required: dict) → ?`

## What it does

path_sanity: verify that required binaries exist in PATH and are at expected locations.
Failure simulated: a binary is moved/deleted, or a malicious binary is injected earlier
in PATH. The checker must detect the absence or unexpected location.

## Guarantee

When it runs, path sanity guarantees verify_binary_locations(path_str, required); 'binary not found' in str(e) and 'python' in str(e); 'wrong directory' in str(e) and 'python' in str(e) (weak-grade: directional, proven by run).

**Checkable constraints:**

- `verify_binary_locations(path_str, required)`
- `'binary not found' in str(e) and 'python' in str(e)`
- `'wrong directory' in str(e) and 'python' in str(e)`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
