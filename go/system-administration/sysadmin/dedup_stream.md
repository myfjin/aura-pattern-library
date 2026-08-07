# dedup stream

**Language:** Go · **Oracle sphere:** system-administration (this file is the Go twin) · **Category:** Wave 16 · Text/stream processing for ops

## What it does

dedup_stream: remove duplicate lines while preserving order.

## Guarantee

When it runs, dedup stream guarantees deduped == expected; len(deduped) == 3; len(broken) == 6 (proven by run on the SYS original).

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
- **Independent oracle:** — established on the SYS original and shared by this Go twin (twin agreement is the evidence: consensus, xlang); the original oracle was not executed against this file
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
