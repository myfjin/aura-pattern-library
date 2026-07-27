# deadline guard

**Language:** Rust · **Sphere:** rust · **Category:** concurrency-resilience

**Signature:** `(child_budget: Duration) → Deadline`

## What it does

deadline_guard — Instant/Duration deadline propagation; child < parent, expiry detected.

Core idea: track deadlines using std::time::Instant + Duration. Child operations inherit
and tighten parent deadlines. THE ONE LAW: plant parent and child deadlines, verify child
≤ parent and expiry is detected on time — an unguarded deadline would allow children to
outlive parents or miss expirations.
When to use: RPC timeouts, deadline propagation in concurrent systems, request cancellation.

## Guarantee

When it runs, deadline guard guarantees assert!(child_remaining <= parent_remaining + Duration::from_millis(5), "child deadline not tightened") (weak-grade: proven by rustc-run).

**Checkable constraints:**

- `assert!(child_remaining <= parent_remaining + Duration::from_millis(5), "child deadline not tightened")`
- `assert!(immediate.is_expired(), "deadline should be expired")`
- `assert!(!future.is_expired(), "deadline should not be expired yet")`
- `assert!(!infinite.is_expired(), "infinite deadline should not expire")`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
