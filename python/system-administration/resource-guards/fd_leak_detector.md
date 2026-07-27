# fd leak detector

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 6 · Resource guards & quotas

**Signature:** `(soft_cap: int) → ?`

## What it does

File descriptor leak detector: caps open fds, refuses opens past limit.
Failure simulated: open 1000 fds, assert the guard trips before exhaustion and
peak fds never reach 1000 (caps at 64), refuses > 800.

## Guarantee

When it runs, fd leak detector guarantees peak_fds <= 64; num_refused > 800; len(open_fds) == peak_fds (weak-grade: directional, proven by run).

**Checkable constraints:**

- `peak_fds <= 64`
- `num_refused > 800`
- `len(open_fds) == peak_fds`
- `len(open_fds) < 100 and num_refused > len(open_fds)`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
