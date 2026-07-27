# command allowlist

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 18 · Access control & audit

**Signature:** `(cmd: str, args: str) → ?`

## What it does

command_allowlist: enforce a whitelist of allowed commands.
Only commands in the allowlist can be executed. Anything else is blocked.

## Guarantee

When it runs, command allowlist guarantees allowlist.check('ls', '-la'); allowlist.check('ls', '/tmp'); allowlist.check('cat', '/etc/passwd') (weak-grade: directional, proven by run).

**Checkable constraints:**

- `allowlist.check('ls', '-la')`
- `allowlist.check('ls', '/tmp')`
- `allowlist.check('cat', '/etc/passwd')`
- `allowlist.check('echo', 'hello world')`
- `allowlist.check('grep', '-i')`
- `'not in allowlist' in str(e)`
- `'not allowed' in str(e) and 'shadow' in str(e)`
- `'not allowed' in str(e) and '-r' in str(e)`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** unreviewed

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `class CommandAllowlist:`, `def __init__(self, allowed_commands):`, `def check(self, cmd, args):`
**Valid input:** `allowed_commands` is a dict mapping command names to lists of allowed argument strings (or `"*"` for any args); `cmd` is a string; `args` is a string.
**Core:** Whitelist guard. Returns `True` if `cmd` is present and `args` matches one of the allowed patterns; raises `ValueError` for unknown commands or disallowed arguments.
**Assert:** `ls /tmp`, `cat /etc/passwd`, `echo hello world`, and `grep -i` pass; `rm -rf`, `cat /etc/shadow`, and `grep -r` are rejected with `ValueError`.
**⚠️ Defect:** Argument matching is exact-string equality, so patterns like `/etc/passwd` are brittle (a path containing a trailing slash or `..` bypasses the allowlist). The wildcard `"*"` is all-or-nothing per command, offering no granular control.

---
*△ AURA Pattern Library — © Reality Optimizer*
