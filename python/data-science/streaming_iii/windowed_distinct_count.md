# windowed distinct count

**Language:** Python · **Sphere:** data-science · **Category:** Streaming III

**Signature:** `(stream: List, window_size: int) → int`

## What it does

Windowed distinct count: exact count of unique elements in a sliding window.
Core idea: maintain window buffer; return len(set(buffer)) at query time.
When: count distinct elements over fixed-size sliding window on streams.

## Guarantee

When it runs, windowed distinct count guarantees final_distinct == true_distinct (proven by run).

**Checkable constraints:**

- `final_distinct == true_distinct`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
