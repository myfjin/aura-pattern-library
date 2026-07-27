# extendible hash index

**Language:** Rust · **Sphere:** rust · **Category:** storage-persistence

**Signature:** `(key: u32) → usize`

## What it does

Real extendible hashing: a directory of 2^global_depth pointers into buckets, each bucket
carrying its OWN local_depth. On overflow only the ONE overflowing bucket splits; the
directory doubles ONLY when that bucket's local_depth already equals the global_depth.
Other buckets are untouched (this is what distinguishes it from a global rehash / resize).

## Guarantee

When it runs, extendible hash index guarantees assert_eq!(eh.global_depth, 2, "global depth after inserting 0..=5 with cap 2"); assert_eq!(eh.directory.len(), 1usize << eh.global_depth, "directory length = 2^global_depth") (proven by rustc-run).

**Checkable constraints:**

- `assert_eq!(eh.global_depth, 2, "global depth after inserting 0..=5 with cap 2")`
- `assert_eq!(eh.lookup(k), Some(k), "key {k} must be findable")`
- `assert_eq!(eh.lookup(99), None, "absent key returns None")`
- `assert!(bkt.local_depth <= eh.global_depth, "local_depth <= global_depth")`
- `assert_eq!(eh.directory.len(), 1usize << eh.global_depth, "directory length = 2^global_depth")`
- `assert!(b < eh.buckets.len(), "directory points to a real bucket")`
- `assert_eq!((k as usize) & (mask as usize), i & (mask as usize), "key {k} sits in a bucket its low {ld} bits map to")`
- `assert!(eh2.buckets.len() > buckets_before, "a split created a new bucket")`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
