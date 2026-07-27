# tail follow stream

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 16 · Text/stream processing for ops

**Signature:** `(file_path: str) → ?`

## What it does

tail_follow_stream: Simulate tail -f behavior (read from file position, follow new lines).
THE ONE LAW: Track file position, read only new lines, handle file rotation edge case.

## Guarantee

When it runs, tail follow stream guarantees lines == ['Line 1']; lines == []; lines == ['Line 2', 'Line 3'] (weak-grade: directional, proven by run).

**Checkable constraints:**

- `lines == ['Line 1']`
- `lines == []`
- `lines == ['Line 2', 'Line 3']`
- `lines == []`
- `lines == ['Rotated line 1']`
- `len(all_new) == 100`
- `all_new[0].startswith('Line 2')`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
