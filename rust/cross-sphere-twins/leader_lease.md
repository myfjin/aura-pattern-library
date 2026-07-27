# leader lease

**Language:** Rust · **Sphere:** rust · **Category:** cross-sphere-twins

## What it does

leader_lease — lease + logical clock; exactly ONE leader, lease expiry triggers re-election.

Core idea: a leader holds a lease (time-limited). Followers check the lease epoch.
If expired, a new election happens (epoch increments, new leader chosen). THE LAW:
simulate lease expiry, trigger re-election, and assert only one leader at a time.
When to use: master election, consensus leadership, Zookeeper-like systems.

## Guarantee

When it runs, leader lease guarantees assert_eq!(election.current_leader_id(), Some(leader_id)); assert_eq!(election.current_leader_id(), None, "expired leader is invalid"); assert_ne!(new_leader, leader_id, "new leader differs (in simple cycling)") (weak-grade: proven by rustc-run).

**Checkable constraints:**

- `assert!(election.current_leader_id().is_some(), "leader elected")`
- `assert_eq!(election.current_leader_id(), Some(leader_id))`
- `assert_eq!(election.current_leader_id(), None, "expired leader is invalid")`
- `assert!(election.current_leader_id().is_some(), "re-election succeeds")`
- `assert_ne!(new_leader, leader_id, "new leader differs (in simple cycling)")`
- `assert!(epoch_after > epoch_before, "epoch incremented on re-election")`
- `assert!(only_one <= 1, "at most one valid leader")`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
