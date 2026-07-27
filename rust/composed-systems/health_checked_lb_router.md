# health checked lb router

**Language:** Rust · **Sphere:** rust · **Category:** composed-systems

## What it does

composes: health-probe-backends + lb-select-healthy + failover-on-drop + recovery

## Guarantee

When it runs, health checked lb router guarantees assert_eq!(routing_sequence.len(), 5, "All requests routed"); assert_eq!(failover_sequence.len(), 3, "Failover handled 3 requests"); assert_eq!(healthy_now.len(), 3, "All backends healthy after recovery") (proven by rustc-run).

**Checkable constraints:**

- `assert_eq!(routing_sequence.len(), 5, "All requests routed")`
- `assert_eq!(failover_sequence.len(), 3, "Failover handled 3 requests")`
- `assert_ne!(*backend_id, 2, "Backend 2 not selected after drop")`
- `assert_eq!(healthy_now.len(), 3, "All backends healthy after recovery")`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
