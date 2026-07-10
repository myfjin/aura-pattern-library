#![forbid(unsafe_code)]
//! Leaky-bucket rate shaper — a level that FILLS on admit and LEAKS at a constant rate.
//! Core idea: unlike a token bucket (tokens accrue, bursts allowed to capacity), a leaky
//! bucket models a fixed-size queue that drains at `leak_per_sec`; each admitted unit ADDS to
//! the level, and admits that would OVERFLOW the capacity are DROPPED. It shapes bursty input
//! into a steady drip. THE ONE LAW: fill the bucket with a burst, assert the overflow is
//! dropped, then let it leak and assert exactly the freed room is re-admittable — a token
//! bucket (level falling on admit) would fail these. When to use: traffic shaping, DDoS damp.

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
struct LeakyBucket {
    capacity: u32,
    leak_per_sec: u32,
    level: u32, // current amount of "water" queued
    last: u64,
}

impl LeakyBucket {
    fn new(capacity: u32, leak_per_sec: u32) -> Self {
        LeakyBucket { capacity, leak_per_sec, level: 0, last: 0 }
    }

    fn leak(&mut self, now: u64) {
        let elapsed = now.saturating_sub(self.last) as u32;
        let leaked = elapsed.saturating_mul(self.leak_per_sec);
        self.level = self.level.saturating_sub(leaked); // drains toward empty
        self.last = now;
    }

    /// Try to admit `amount` units. Accept iff it fits under capacity AFTER leaking; else DROP.
    fn admit(&mut self, now: u64, amount: u32) -> bool {
        self.leak(now);
        if self.level + amount <= self.capacity {
            self.level += amount; // water goes IN (opposite of a token bucket)
            true
        } else {
            false // overflow → dropped, level unchanged
        }
    }
}

fn main() {
    let mut b = LeakyBucket::new(10, 2); // capacity 10, leaks 2 units/sec

    // Starts EMPTY (a token bucket would start full — this alone distinguishes them).
    assert_eq!(b.level, 0, "leaky bucket starts empty");

    // Burst: fill to the brim.
    assert!(b.admit(0, 10), "10 fits into an empty capacity-10 bucket");
    assert_eq!(b.level, 10);

    // Full → overflow is DROPPED, level unchanged.
    assert!(!b.admit(0, 1), "bucket full → admit dropped");
    assert_eq!(b.level, 10, "a dropped admit must not change the level");

    // Leak: by t=3, 3s × 2/s = 6 units have drained → level 4.
    assert!(b.admit(3, 0), "advance clock; 0 always fits");
    assert_eq!(b.level, 4, "10 - 6 leaked = 4");

    // The freed room (6) is exactly re-admittable, back to full.
    assert!(b.admit(3, 6), "4 + 6 == capacity fits");
    assert_eq!(b.level, 10);

    // A too-large admit that would overflow is dropped WHOLE (no partial fill).
    assert!(!b.admit(3, 1), "10 + 1 > 10 → dropped");
    assert_eq!(b.level, 10);

    // By t=8 (5s later), 10 units leaked → fully drained.
    assert!(b.admit(8, 0), "advance clock");
    assert_eq!(b.level, 0, "fully drained after leaking ≥ capacity");

    // Partial-fill then overflow-whole: 7 fits, then 5 more would overflow → dropped, level stays 7.
    assert!(b.admit(8, 7));
    assert_eq!(b.level, 7);
    assert!(!b.admit(8, 5), "7 + 5 > 10 → dropped whole");
    assert_eq!(b.level, 7, "no partial admission");

    // Steady state: admitting exactly the leak rate each second sustains forever, never overflows.
    let mut c = LeakyBucket::new(10, 2);
    for t in 1..=100u64 {
        assert!(c.admit(t, 2), "input at the leak rate always fits");
        assert!(c.level <= c.capacity, "level never exceeds capacity");
    }

    println!("leaky_bucket_shaper ... PASS");
}
