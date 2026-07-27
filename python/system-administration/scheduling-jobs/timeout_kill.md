# timeout kill

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 7 · Scheduling & jobs

**Signature:** `(cmd: List[str], timeout_seconds: float, stdin_data: None) → ?`

## What it does

Timeout kill: terminate a subprocess if it exceeds timeout.
Failure simulated: spawn a hanging child; assert it's killed within timeout, not before.

## Guarantee

When it runs, timeout kill guarantees success_count == 5; returncode == -1; elapsed < 2 (proven by run).

**Checkable constraints:**

- `returncode == -1`
- `elapsed < 2`
- `duration < 1.0`
- `returncode == 0`
- `'done' in stdout`
- `duration < 1`
- `returncode == 0`
- `duration < 0.3`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
