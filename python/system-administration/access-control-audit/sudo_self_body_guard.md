# sudo self body guard

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 18 · Access control & audit

**Signature:** `(cmd: str) → ?`

## What it does

sudo_self_body_guard: detect and block self-destructive sudo commands.
Examples: rm -rf /, pkill -9 -u <self>, etc.
The guard must allow safe sudo commands and block dangerous ones.

## Guarantee

When it runs, sudo self body guard guarantees guard.check_command('sudo apt-get install vim'); guard.check_command('sudo systemctl restart nginx'); guard.check_command('sudo usermod -aG docker alice') (weak-grade: directional, proven by run).

**Checkable constraints:**

- `guard.check_command('sudo apt-get install vim')`
- `guard.check_command('sudo systemctl restart nginx')`
- `guard.check_command('sudo usermod -aG docker alice')`
- `guard.check_command('sudo touch /etc/file.conf')`
- `'rm' in str(e).lower() or 'dangerous' in str(e).lower()`
- `'dd' in str(e).lower() or 'dangerous' in str(e).lower()`
- `'chmod' in str(e).lower() or 'dangerous' in str(e).lower()`
- `'mkfs' in str(e).lower() or 'dangerous' in str(e).lower()`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `class SudoGuard:`, `def check_command(self, cmd):`
**Valid input:** `cmd` is a string representing a command that may be run under sudo.
**Core:** Regex-based guard against self-destructive sudo commands. Raises `ValueError` when `cmd` matches dangerous patterns (`rm -rf /`, `dd if=/dev/zero of=/`, `mkfs`, etc.).
**Assert:** Safe commands (`apt-get install`, `systemctl restart`, `usermod`) pass; `rm -rf /etc/important`, `dd if=/dev/zero of=/dev/sda`, `chmod -r /`, and `mkfs.ext4 /dev/sda1` are blocked.
**⚠️ Defect:** Pattern `rm\s+-rf\s+/` only matches literal `/` at the end, missing variants like `rm -rf --no-preserve-root /` or `rm -rf /*`. The check is purely syntactic and can be bypassed by aliases, encoded spaces, or shell expansion.

---
*△ AURA Pattern Library — © Reality Optimizer*
