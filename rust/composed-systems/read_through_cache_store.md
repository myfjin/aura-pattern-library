# read through cache store

**Language:** Rust · **Sphere:** rust · **Category:** composed-systems

**Signature:** `(key: &str) → Option<String>`

## What it does

composes: cache-get + miss-load-from-backing + cache-fill + hit-skips-store + eviction

## Guarantee

When it runs, read through cache store guarantees assert_eq!(store.load_count, 1, "One load from backing"); assert_eq!(cache_size_1, 1, "Cache has 1 item"); assert_eq!(store.load_count, 2, "Two loads from backing") (proven by rustc-run).

**Checkable constraints:**

- `assert_eq!(val_a, Some("val-a".to_string()), "Get a succeeded")`
- `assert_eq!(store.load_count, 1, "One load from backing")`
- `assert_eq!(cache_size_1, 1, "Cache has 1 item")`
- `assert_eq!(val_b, Some("val-b".to_string()), "Get b succeeded")`
- `assert_eq!(store.load_count, 2, "Two loads from backing")`
- `assert_eq!(cache_size_2, 2, "Cache at capacity")`
- `assert_eq!(val_a_hit, Some("val-a".to_string()), "Hit on a")`
- `assert_eq!(store.load_count, 2, "No new load (cache hit)")`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
