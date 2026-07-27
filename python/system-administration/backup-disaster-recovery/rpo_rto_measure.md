# rpo rto measure

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 13 · Backup & disaster recovery

**Signature:** `(backup_dir: Path, restore_dir: Path, clock: InjectedClock, seconds_per_file: int) → ?`

## What it does

rpo_rto_measure: measure recovery point objective and recovery time objective.

## Guarantee

When it runs, rpo rto measure guarantees b2_time == 3600; rpo == 3600; rto == 2 (proven by run).

**Checkable constraints:**

- `b1_time == 0`
- `b2_time == 3600`
- `rpo == 3600`
- `n_restored == 1`
- `rto == n_restored * 2`
- `rto == 2`
- `restored_data == 'modified_payload_v2'`
- `rpo_b2_b3 == 1800`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `class InjectedClock:`, `def __init__(self, start_time=0):`, `def advance(self, seconds):`, `def now(self):`, `def backup_with_timestamp(src_dir, backup_dir, clock):`, `def restore_with_timer(backup_dir, restore_dir, clock, seconds_per_file=2):`, `def measure_rpo_rto():`
**Valid input:** Source directory exists; `seconds_per_file` is non-negative; separate clock instances are used for backup and restore timelines.
**Core:** Measures recovery-point objective (time between backups) and recovery-time objective (restore duration) using injected clocks. Each restored file advances the restore clock by `seconds_per_file`, making RTO a measured function of work rather than a constant.
**Assert:** Backups at time 0 and 3600 give RPO = 3600; restoring one file with `seconds_per_file=2` yields RTO = 2; restored content matches the latest backup.
**⚠️ Defect:** `backup_with_timestamp` names the backup directory with the current clock value, but if two backups occur at the same clock tick they collide. The restore-time model is linear per file and ignores directory traversal, metadata operations, or parallelism.

---
*△ AURA Pattern Library — © Reality Optimizer*
