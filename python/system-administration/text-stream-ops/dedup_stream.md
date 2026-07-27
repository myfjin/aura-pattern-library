# dedup stream

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 16 · Text/stream processing for ops

**Signature:** `(lines: List[str], keep_first: bool) → ?`

## What it does

dedup_stream: Remove duplicate lines while preserving order.
THE ONE LAW: Deduplicate stream, assert exact count and order preservation.

## Guarantee

When it runs, dedup stream guarantees deduped == expected; len(deduped) == 3; len(broken) == 6 (proven by run).

**Checkable constraints:**

- `len(deduped) == 3`
- `deduped == expected`
- `len(broken) == 6`
- `len(broken) != len(deduped)`
- `len(deduped_last) == 3`
- `deduped_last == ['User: charlie', 'User: bob', 'User: alice']`
- `len(deduped_ident) == 1`
- `deduped_ident == ['Line X']`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
