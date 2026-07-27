# sharded kv rehash router

**Language:** Rust · **Sphere:** rust · **Category:** composed-systems

**Signature:** `(key: &str, shard: u64) → u64`

## What it does

composes: rendezvous(HRW)-hash-to-shard + route + add-shard + MINIMAL-movement-rehash + verify

Naive `key % n` reshuffles almost every key when n changes — so it cannot claim "minimal
movement". This composes RENDEZVOUS (highest-random-weight) hashing: each key goes to the shard
with the highest weight(key, shard). Adding a shard only moves the keys the new shard now wins;
every other key stays put. We assert that minimality exactly.

## Guarantee

When it runs, sharded kv rehash router guarantees assert_eq!(s_after, 3, "key {k} only moved because the new shard 3 won it") (proven by rustc-run).

**Checkable constraints:**

- `assert!(s < 3)`
- `assert_eq!(assign(k, 4), s_after, "key {k} deterministically routes to its new shard")`
- `assert_eq!(s_after, 3, "key {k} only moved because the new shard 3 won it")`
- `assert!(moved >= 1, "adding a shard should capture some keys")`
- `assert!(moved < keys.len(), "minimal movement: most keys stay put ({moved} of {} moved)", keys.len())`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
