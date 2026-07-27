# crdt gcounter

**Language:** Rust · **Sphere:** rust · **Category:** cross-sphere-twins

**Signature:** `(replica_id: usize) → ?`

## What it does

crdt_gcounter — grow-only counter; merge is commutative, idempotent, convergent.

Core idea: each replica has a per-replica counter. Merge combines max of each.
Merge is commutative (A ⊔ B = B ⊔ A), idempotent (A ⊔ A = A), and convergent
(A ⊔ B ⊔ C = A ⊔ (B ⊔ C)). THE LAW: perform merges in different orders and
assert the same final state is reached.
When to use: conflict-free replicated counters, CRDT sync.

## Guarantee

When it runs, crdt gcounter guarantees assert_eq!(a.value() + b.value() + c.value(), 6, "expected total increments"); assert_eq!(abc_left.value(), 6, "merged counter has correct total") (proven by rustc-run).

**Checkable constraints:**

- `assert_eq!(a_merge_b, b_merge_a, "A ⊔ B = B ⊔ A")`
- `assert_eq!(a_merge_a, a, "A ⊔ A = A")`
- `assert_eq!(abc_left, abc_right, "(A ⊔ B) ⊔ C = A ⊔ (B ⊔ C)")`
- `assert_eq!(a.value() + b.value() + c.value(), 6, "expected total increments")`
- `assert_eq!(abc_left.value(), 6, "merged counter has correct total")`
- `assert_eq!(final_123, final_231)`
- `assert_eq!(final_231, final_312)`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
