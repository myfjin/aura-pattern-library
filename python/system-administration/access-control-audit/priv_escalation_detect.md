# priv escalation detect

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 18 · Access control & audit

**Signature:** `(user_privileges: dict) → ?`

## What it does

priv_escalation_detect: detect privilege escalation by comparing user privileges
across time. If a user gains a new privilege they didn't have before, flag it.
This is state-change detection, not a static read.

## Guarantee

When it runs, priv escalation detect guarantees not has_escalation; 'alice' in escalations; 'write' in escalations['alice'] (weak-grade: directional, proven by run).

**Checkable constraints:**

- `not has_escalation`
- `has_escalation`
- `'alice' in escalations`
- `'write' in escalations['alice']`
- `has_escalation`
- `'bob' in escalations`
- `'admin' in escalations['bob']`
- `has_escalation`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `class PrivilegeMonitor:`, `def __init__(self):`, `def snapshot(self, user_privileges):`, `def detect_escalation(self):`
**Valid input:** `user_privileges` is a dict mapping users to sets of privileges; at least two snapshots are needed for detection.
**Core:** State-change detector. Records privilege snapshots and compares the latest with the previous one, returning `(True, {user: new_privs})` if any user gained privileges.
**Assert:** Identical snapshots produce no escalation; adding `write` to alice, `admin` to bob, and simultaneous escalations across multiple users are all detected.
**⚠️ Defect:** Only privilege *additions* are flagged; privilege *removals* (de-escalation) are silently ignored. The snapshot is stored as a shallow copy, so if the caller mutates a nested privilege set in place, the stored history may change.

---
*△ AURA Pattern Library — © Reality Optimizer*
