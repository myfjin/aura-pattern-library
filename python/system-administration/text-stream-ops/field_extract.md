# field extract

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 16 · Text/stream processing for ops

**Signature:** `(line: str, field_indices: List[int], delimiter: None) → ?`

## What it does

field_extract: Extract specific fields from whitespace-separated lines.
THE ONE LAW: Parse real data with varying field counts, assert exact extraction.

## Guarantee

When it runs, field extract guarantees fields is not None; user_cmd == ['root', '/bin/bash']; pid == ['5678'] (weak-grade: directional, proven by run).

**Checkable constraints:**

- `fields is not None`
- `len(fields) == 2`
- `user_cmd == ['root', '/bin/bash']`
- `pid == ['5678']`
- `fields is None`
- `multi == ['9012', 'admin', '/sbin/sshd']`
- `csv_fields == ['john', 'engineer']`
- `empty_fields is None`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
