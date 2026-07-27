# misra gries topk

**Language:** Rust · **Sphere:** rust · **Category:** cross-sphere-twins

**Signature:** `(item: String) → ?`

## What it does

misra_gries_topk — heavy hitters; GUARANTEE: any freq > n/(k+1) is in output.

Core idea: maintain k candidate items + counters. For new item, if it's a candidate,
increment; else if space, add; else decrement all. Query returns items with freq > 0.
Guarantee: any item with freq > n/(k+1) is guaranteed in the output. THE LAW: plant
items with known frequencies, run Misra-Gries, and assert every item with freq > n/(k+1)
appears in the output.
When to use: finding heavy hitters, top-k detection, streaming analytics.

## Guarantee

When it runs, misra gries topk guarantees assert_eq!(empty_output.len(), 0, "empty stream yields empty output") (proven by rustc-run).

**Checkable constraints:**

- `assert!(freq_a > threshold, "a has freq 5 > threshold {}", threshold)`
- `assert!(heavy_hitters.contains(&"a".to_string()), "a (freq > threshold) is in output")`
- `assert!(heavy_hitters.len() <= k, "output size <= k")`
- `assert_eq!(empty_output.len(), 0, "empty stream yields empty output")`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
