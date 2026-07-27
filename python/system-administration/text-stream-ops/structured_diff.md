# structured diff

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 16 · Text/stream processing for ops

**Signature:** `(before_text: str, after_text: str, key_field: int) → ?`

## What it does

structured_diff: Diff two structured outputs (e.g., process lists, config states).
THE ONE LAW: Parse both versions, identify exact adds/removes/changes.

## Guarantee

When it runs, structured diff guarantees '3000' in diff['removed'][0]; '4000' in diff['added'][0]; 'python3' in diff['changed'][0] (weak-grade: directional, proven by run).

**Checkable constraints:**

- `len(diff['removed']) == 1`
- `len(diff['added']) == 1`
- `len(diff['changed']) == 1`
- `len(diff['unchanged']) == 1`
- `'3000' in diff['removed'][0]`
- `'4000' in diff['added'][0]`
- `'python3' in diff['changed'][0]`
- `'alice' in diff['unchanged'][0]`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
