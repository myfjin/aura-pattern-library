# idempotent request dedup

**Language:** Rust · **Sphere:** rust · **Category:** composed-systems

## What it does

composes: hash-request-id + dedup-cache + apply-once + replay-returns-cached-result

## Guarantee

When it runs, idempotent request dedup guarantees assert_eq!(applied_count, 3, "Exactly 3 unique requests applied"); assert_eq!(dedup_cache.len(), 3, "Cache has 3 unique request IDs"); assert_eq!(account_balance, 900, "Correct final balance") (proven by rustc-run).

**Checkable constraints:**

- `assert_eq!(applied_count, 3, "Exactly 3 unique requests applied")`
- `assert_eq!(dedup_cache.len(), 3, "Cache has 3 unique request IDs")`
- `assert_eq!(account_balance, 900, "Correct final balance")`
- `assert_eq!(cached_count, 2, "Exactly 2 replays from cache")`
- `assert_eq!(applied_per_id, 3, "Exactly 3 apply operations")`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
