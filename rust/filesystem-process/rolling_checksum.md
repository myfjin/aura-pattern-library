# rolling checksum

**Language:** Rust · **Sphere:** rust · **Category:** filesystem-process

**Signature:** `(data: &[u8], w: usize) → Vec<u64>`

## What it does

rolling_checksum — polynomial rolling checksum for delta sync; O(1) window updates.

Core idea: as the window slides one byte, the hash is updated INCREMENTALLY — subtract the
outgoing byte's contribution, shift, add the incoming byte — in O(1), not by re-hashing the
whole window. THE ONE LAW: compute the rolled hashes, then assert each equals a from-scratch
recompute of the same window. If the roll math were wrong, rolled ≠ recompute would catch it
(a naive impl that just recomputes would make this test vacuous — so we roll for real).
When to use: rsync-like delta detection, content-defined chunking, dedup across chunks.

## Guarantee

When it runs, rolling checksum guarantees assert_eq!(rolled.len(), 8) (proven by rustc-run).

**Checkable constraints:**

- `assert_eq!(rolled.len(), data.len() - w + 1)`
- `assert_eq!(rolled.len(), 8)`
- `assert_eq!(rh, recomputed, "rolled hash at {i} disagrees with recompute")`
- `assert_eq!(r2[0], h_abc)`
- `assert_eq!(r2[3], h_abc)`
- `assert_eq!(r2[6], h_abc)`
- `assert_ne!(r2[1], r2[0], "\"bca\" must differ from \"abc\"")`
- `assert_eq!(distinct, r3.len(), "distinct windows must hash distinctly here")`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
