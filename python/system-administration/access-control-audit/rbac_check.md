# rbac check

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 18 · Access control & audit

**Signature:** `(user_role: str, resource: str, action: str, role_perms: dict) → ?`

## What it does

rbac_check: enforce role-based access control. Verify that a user with role X can perform
allowed action A, but cannot perform forbidden action B. Failure simulated: allowing a
forbidden action. The checker must DENY the forbidden action AND ALLOW the permitted one.

## Guarantee

When it runs, rbac check guarantees rbac_enforce('admin', 'files', 'delete', role_perms); rbac_enforce('user', 'files', 'write', role_perms); rbac_enforce('guest', 'files', 'read', role_perms) (weak-grade: directional, proven by run).

**Checkable constraints:**

- `rbac_enforce('admin', 'files', 'delete', role_perms)`
- `rbac_enforce('user', 'files', 'write', role_perms)`
- `rbac_enforce('guest', 'files', 'read', role_perms)`
- `'not permitted' in str(e) and 'delete' in str(e)`
- `'not permitted' in str(e) and 'write' in str(e)`
- `'not permitted' in str(e) and 'delete' in str(e)`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `def rbac_enforce(user_role, resource, action, role_perms):`
**Valid input:** `user_role` exists in `role_perms`; `role_perms` maps roles to resources to lists of permitted actions.
**Core:** Role-based access-control enforcer. Raises `ValueError` for unknown roles, unknown resources for a role, or actions not listed for the role-resource pair.
**Assert:** Admin `delete files`, user `write files`, and guest `read files` pass; user `delete files`, guest `write files`, and user `delete users` are denied.
**⚠️ Defect:** Role permissions are passed in on every call rather than being encapsulated, so policy drift between calls is possible. There is no support for dynamic role hierarchy or deny-rules; every permission must be explicitly listed.

---
*△ AURA Pattern Library — © Reality Optimizer*
