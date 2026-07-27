# leaky bucket shaper

**Language:** Rust · **Sphere:** rust · **Category:** security-crypto

**Signature:** `(now: u64) → ?`

## What it does

Leaky-bucket rate shaper — a level that FILLS on admit and LEAKS at a constant rate.
Core idea: unlike a token bucket (tokens accrue, bursts allowed to capacity), a leaky
bucket models a fixed-size queue that drains at `leak_per_sec`; each admitted unit ADDS to
the level, and admits that would OVERFLOW the capacity are DROPPED. It shapes bursty input
into a steady drip. THE ONE LAW: fill the bucket with a burst, assert the overflow is
dropped, then let it leak and assert exactly the freed room is re-admittable — a token
bucket (level falling on admit) would fail these. When to use: traffic shaping, DDoS damp.

## Guarantee

When it runs, leaky bucket shaper guarantees assert_eq!(b.level, 0, "leaky bucket starts empty"); assert_eq!(b.level, 10); assert_eq!(b.level, 10, "a dropped admit must not change the level") (proven by rustc-run).

**Checkable constraints:**

- `assert_eq!(b.level, 0, "leaky bucket starts empty")`
- `assert!(b.admit(0, 10), "10 fits into an empty capacity-10 bucket")`
- `assert_eq!(b.level, 10)`
- `assert!(!b.admit(0, 1), "bucket full → admit dropped")`
- `assert_eq!(b.level, 10, "a dropped admit must not change the level")`
- `assert!(b.admit(3, 0), "advance clock; 0 always fits")`
- `assert_eq!(b.level, 4, "10 - 6 leaked = 4")`
- `assert!(b.admit(3, 6), "4 + 6 == capacity fits")`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
