# token gated priority scheduler

**Language:** Rust · **Sphere:** rust · **Category:** composed-systems

**Signature:** `(other: &Self) → std::cmp::Ordering`

## What it does

composes: enqueue-tasks-with-priorities + token-bucket-gate-admits-at-rate + dispatch-highest-priority-admitted

## Guarantee

When it runs, token gated priority scheduler guarantees assert_eq!(dispatched.len(), 4, "All 4 tasks dispatched"); assert_eq!(dispatched[0], 2, "Highest priority task (id=2, p=10) first"); assert_eq!(dispatched[1], 4, "Second highest priority (id=4, p=8)") (proven by rustc-run).

**Checkable constraints:**

- `assert_eq!(dispatched.len(), 4, "All 4 tasks dispatched")`
- `assert_eq!(dispatched[0], 2, "Highest priority task (id=2, p=10) first")`
- `assert_eq!(dispatched[1], 4, "Second highest priority (id=4, p=8)")`
- `assert_eq!(dispatched[2], 1, "Third priority (id=1, p=5)")`
- `assert_eq!(dispatched[3], 3, "Lowest priority (id=3, p=3)")`
- `assert!(available_tokens == tokens_per_interval, "Tokens refilled")`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
