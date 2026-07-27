# rate limited request pipeline

**Language:** Rust · **Sphere:** rust · **Category:** composed-systems

## What it does

composes: request-parse + sliding-window-rate-limit + status-classify + admit-deny

## Guarantee

When it runs, rate limited request pipeline guarantees assert_eq!(admitted.len(), 6, "All requests fit in sliding window"); assert_eq!(denied.len(), 0, "No requests denied with this pattern") (proven by rustc-run).

**Checkable constraints:**

- `assert_eq!(admitted.len(), 6, "All requests fit in sliding window")`
- `assert_eq!(denied.len(), 0, "No requests denied with this pattern")`
- `assert!(admitted_strict.len() < admitted.len(), "Stricter limit admits fewer requests")`
- `assert!(denied_strict.len() > 0, "Stricter limit denies some requests")`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
