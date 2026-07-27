# replicated log quorum

**Language:** Rust · **Sphere:** rust · **Category:** composed-systems

**Signature:** `(replicas: &[&[Entry]], quorum: usize) → Option<Entry>`

## What it does

composes: append-to-N-replicas + lag + quorum-read + majority-VALUE-consensus

A quorum read returns the (index, value) that a MAJORITY of replicas agree on — the value is
load-bearing, not just the index. An entry present on only a minority (or a divergent value on
a minority) is not returned.

## Guarantee

When it runs, replicated log quorum guarantees assert_eq!(read, Some(Entry { index: 3, value: "val3".to_string() }), "quorum read returns index 3 AND its majority-agreed value"); assert_eq!(read2.as_ref().map(|e| e.index), Some(3), "minority index 99 is not chosen; quorum stays at 3"); assert_ne!(read2.unwrap().value, "ghost", "the minority value is never returned") (weak-grade: proven by rustc-run).

**Checkable constraints:**

- `assert_eq!(read, Some(Entry { index: 3, value: "val3".to_string() }), "quorum read returns index 3 AND its majority-agreed value")`
- `assert_eq!(read2.as_ref().map(|e| e.index), Some(3), "minority index 99 is not chosen; quorum stays at 3")`
- `assert_ne!(read2.unwrap().value, "ghost", "the minority value is never returned")`
- `assert_eq!(read3.map(|e| e.index), Some(3), "split value at index 4 has no quorum → falls back to committed index 3")`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
