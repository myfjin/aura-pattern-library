# top n by resource

**Language:** Python · **Sphere:** system-administration · **Category:** Wave 15 · Process/system introspection

**Signature:** `(process_lines: str, n: int) → ?`

## What it does

top_n_by_resource: Rank processes by a resource metric (RSS, CPU, etc.).
THE ONE LAW: Sort and rank, assert exact ordering; simulate unsorted input.

## Guarantee

When it runs, top n by resource guarantees top_3[0][2] == 524288; top_3[1][2] == 262144; top_3[2][2] == 2048 (proven by run).

**Checkable constraints:**

- `len(top_3) == 3`
- `top_3[0][1] == 'chrome'`
- `top_3[0][2] == 524288`
- `top_3[1][1] == 'python'`
- `top_3[1][2] == 262144`
- `top_3[2][1] == 'bash'`
- `top_3[2][2] == 2048`
- `top_3[i][2] >= top_3[i + 1][2]`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
