# rollback on failure

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 12 · Deployment & rollback

**Signature:** `(version: str) → ?`

## What it does

Automatic rollback when deployment fails or becomes unhealthy.

## Guarantee

When it runs, rollback on failure guarantees rollback.get_current_version() == 'v1.0'; rollback.should_rollback() is False; rollback.should_rollback() is True (weak-grade: directional, proven by run).

**Checkable constraints:**

- `rollback.get_current_version() == 'v1.0'`
- `rollback.should_rollback() is False`
- `rollback.should_rollback() is True`
- `rollback.failure_reason == 'database connection failed'`
- `rollback.get_current_version() == 'v1.0'`
- `rollback.get_current_version() == 'v2.0'`
- `rollback.should_rollback() is True`
- `rollback.get_current_version() == 'v1.0'`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `class RollbackOnFailure:`, `def __init__(self):`, `def deploy(self, version):`, `def mark_unhealthy(self, reason):`, `def rollback(self):`, `def should_rollback(self):`, `def get_current_version(self):`
**Valid input:** `version` is a string; `reason` is a string describing the failure.
**Core:** Tracks `current_version` and `previous_version`; when the current version is marked unhealthy, `should_rollback()` returns `True`; `rollback()` restores `current_version` to `previous_version` and clears the unhealthy flag.
**Assert:** Healthy deployment does not rollback; marking unhealthy triggers rollback recommendation; rollback restores previous version; rollback without previous version raises `RuntimeError`; multi-version chain rolls back one step at a time.
**⚠️ Defect:** There is no automatic rollback trigger; the caller must poll `should_rollback()` and call `rollback()`. Only one previous version is remembered, so rolling back twice in a row just toggles between the last two versions. Health state is a single boolean with no time-based decay.

---
*△ AURA Pattern Library — © Reality Optimizer*
