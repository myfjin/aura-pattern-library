# wal backed kv store

**Language:** Rust · **Sphere:** rust · **Category:** composed-systems

## What it does

composes: kv-put-del + wal-append + crash-simulate + replay-recover

## Guarantee

When it runs, wal backed kv store guarantees assert_eq!(state_before_crash.len(), 2, "Before crash had 2 keys"); assert_eq!(recovered_map.len(), 2, "After replay has 2 keys") (proven by rustc-run).

**Checkable constraints:**

- `assert_eq!(state_before_crash.len(), 2, "Before crash had 2 keys")`
- `assert_eq!(recovered_map.len(), 2, "After replay has 2 keys")`
- `assert_eq!(recovered_map.get("a"), Some(&"1".to_string()), "Recovered a=1")`
- `assert_eq!(recovered_map.get("b"), Some(&"2".to_string()), "Recovered b=2")`
- `assert_eq!(recovered_map.get("c"), None, "c was lost in crash")`
- `assert!(!recovered_map.is_empty(), "Replay happened")`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
