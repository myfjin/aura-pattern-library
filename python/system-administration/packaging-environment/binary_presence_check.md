# binary presence check

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 17 · Packaging & environment

**Signature:** `(binary_paths: List[str]) → ?`

## What it does

binary_presence_check: verify that required binaries are installed and executable.
Failure simulated: a required binary is missing or not executable. The checker must
detect both conditions.

## Guarantee

When it runs, binary presence check guarantees check_binaries_exist([bin1, bin2, bin3]); 'binary not found' in str(e) and bin1 in str(e); 'not executable' in str(e) and bin1 in str(e) (weak-grade: directional, proven by run).

**Checkable constraints:**

- `check_binaries_exist([bin1, bin2, bin3])`
- `'binary not found' in str(e) and bin1 in str(e)`
- `'not executable' in str(e) and bin1 in str(e)`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
