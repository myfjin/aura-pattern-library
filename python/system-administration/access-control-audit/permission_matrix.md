# permission matrix

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 18 · Access control & audit

**Signature:** `(user: str, resource: str, action: str) → ?`

## What it does

permission_matrix: manage a permission matrix (users × resources × actions).
Verify that a permission grants access. Tamper the matrix (flip a permission bit)
and verify the tamper is detected.

## Guarantee

When it runs, permission matrix guarantees matrix.verify_integrity(expected); matrix.check('alice', 'files', 'read'); 'action mismatch' in str(e) and 'bob' in str(e) (weak-grade: directional, proven by run).

**Checkable constraints:**

- `matrix.verify_integrity(expected)`
- `matrix.check('alice', 'files', 'read')`
- `'action mismatch' in str(e) and 'bob' in str(e)`
- `'action mismatch' in str(e)`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `class PermissionMatrix:`, `def __init__(self):`, `def grant(self, user, resource, action):`, `def check(self, user, resource, action):`, `def verify_integrity(self, expected):`
**Valid input:** `user`, `resource`, `action` are hashable identifiers; `expected` has the same nested dict-of-sets shape as the internal matrix.
**Core:** User × resource × action matrix. `grant` adds an action; `check` raises `ValueError` on missing user, resource, or action; `verify_integrity` compares the entire matrix against an expected structure.
**Assert:** Granted permissions pass `check`; adding an unauthorized action or removing a legitimate one is caught by `verify_integrity` with "action mismatch".
**⚠️ Defect:** Direct mutation of `matrix.perms` (as the tests do) is required to simulate tampering, exposing the internal dict to callers. The integrity check compares only the current snapshot and does not protect the matrix between grant/check operations.

---
*△ AURA Pattern Library — © Reality Optimizer*
