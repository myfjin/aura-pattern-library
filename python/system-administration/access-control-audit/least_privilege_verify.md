# least privilege verify

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 18 · Access control & audit

**Signature:** `(user: str, privilege: str) → ?`

## What it does

least_privilege_verify: grant only the minimum permissions needed for a task,
then verify that unauthorized escalations are blocked.

## Guarantee

When it runs, least privilege verify guarantees checker.check('alice', 'read_files'); checker.check('bob', 'read_files'); checker.check('bob', 'write_files') (weak-grade: directional, proven by run).

**Checkable constraints:**

- `checker.check('alice', 'read_files')`
- `checker.check('bob', 'read_files')`
- `checker.check('bob', 'write_files')`
- `'not permitted' in str(e) and 'write_files' in str(e)`
- `'not permitted' in str(e) and 'delete_files' in str(e)`
- `'not permitted' in str(e)`
- `checker.check('alice', 'write_files')`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `class PrivilegeChecker:`, `def __init__(self):`, `def grant(self, user, privilege):`, `def revoke(self, user, privilege):`, `def check(self, user, required_priv):`
**Valid input:** `user` and `privilege` are hashable identifiers; a user must exist and hold `required_priv` for `check` to succeed.
**Core:** Minimal-privilege enforcer. Maintains `user -> set(privilege)`; `check` raises `ValueError` for missing users, missing privileges, or attempts to use a revoked privilege.
**Assert:** Alice with only `read_files` passes `read_files` but is blocked from `write_files`, `delete_files`, and `admin`; after granting and then revoking `write_files`, the privilege is denied again.
**⚠️ Defect:** `check` leaks the user's full privilege set in the error message, which is a minor information-disclosure side channel. There is no concept of roles or inheritance, so real least-privilege policies must be flattened manually.

---
*△ AURA Pattern Library — © Reality Optimizer*
