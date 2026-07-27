# retention policy

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 13 · Backup & disaster recovery

**Signature:** `(backup_dir: Path, policy_config: dict, clock: InjectedClock) → ?`

## What it does

retention_policy: implement backup retention rules (age-based, count-based).

## Guarantee

When it runs, retention policy guarantees 'backup_5' in kept; 'backup_4' in kept; 'backup_3' in kept (weak-grade: directional, proven by run).

**Checkable constraints:**

- `'backup_5' in kept`
- `'backup_4' in kept`
- `'backup_3' in kept`
- `len(kept) >= 2`
- `len(kept) == 3`
- `'backup_1' in deleted`
- `backup_path.exists()`
- `len(kept2) == 3`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `class InjectedClock:`, `def __init__(self, start_time=0):`, `def advance(self, seconds):`, `def now(self):`, `def create_backup(backup_dir, backup_id, clock):`, `def apply_retention_policy(backup_dir, policy_config, clock):`, `def test_retention_policy():`
**Valid input:** `policy_config` contains `max_age_seconds` (int or `inf`) and `min_count` (int); backups are directories named `backup_*` containing `timestamp.txt`.
**Core:** Age- and count-based backup retention. Sorts backups newest-first, keeps the newest `min_count`, and additionally keeps any backup whose age is within `max_age_seconds`.
**Assert:** With five hourly backups, a 2-hour age policy plus `min_count=2` keeps the three newest backups and deletes the oldest; a count-only policy keeps exactly the newest three.
**⚠️ Defect:** The policy does not handle ties or equal timestamps; when `max_age` is infinite, only `min_count` matters, but the code still computes ages unnecessarily. There is no guard against `min_count=0`, which would delete every backup.

---
*△ AURA Pattern Library — © Reality Optimizer*
