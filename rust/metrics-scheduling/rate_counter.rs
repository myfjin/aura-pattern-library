#![forbid(unsafe_code)]
//! rate_counter — reset-safe counter rate; planted resets not read as spikes.
//!
//! Core idea: track event count and compute rate per time unit. When the counter
//! resets, the rate should remain stable (not spike). THE ONE LAW: plant a reset,
//! assert that the rate across the reset boundary is computed correctly and doesn't
//! produce a spurious spike. A naive delta (current - prev) would see the reset as a
//! negative spike; a correct impl handles it.
//! When to use: traffic rate, request counters, monotonic metric rates.

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
struct RateCounter {
    last_count: u64,
    last_time: u32,
    rate: f64,
}

impl RateCounter {
    fn new() -> Self {
        RateCounter {
            last_count: 0,
            last_time: 0,
            rate: 0.0,
        }
    }

    fn update(&mut self, count: u64, time: u32) -> f64 {
        let time_delta = time.wrapping_sub(self.last_time);
        if time_delta == 0 {
            return self.rate;
        }

        // Handle counter reset: count < last_count signals a reset.
        let count_delta = if count >= self.last_count {
            count - self.last_count
        } else {
            // Counter wrapped/reset. Assume the new count is valid and we lost the tail.
            count
        };

        self.rate = count_delta as f64 / time_delta as f64;
        self.last_count = count;
        self.last_time = time;

        self.rate
    }
}

fn main() {
    // Planted case 1: steady rate without reset.
    let mut counter = RateCounter::new();

    counter.update(100, 10); // 0->100 over time 0->10 = 10 events/time
    let rate1 = counter.update(200, 20); // 100->200 over time 10->20 = 10 events/time
    assert!((rate1 - 10.0).abs() < 1e-6, "rate should be 10 events/time");

    // Planted case 2: counter reset.
    let mut counter2 = RateCounter::new();
    counter2.update(5000, 100); // 0->5000 over 100 time units
    counter2.update(10000, 200); // 5000->10000 over 100 time units = 50 events/time

    // Reset: counter drops to 0.
    let rate_after_reset = counter2.update(100, 300); // Reset happened; count is now 100.
    // Over time 200->300 = 100 time units, we see 100 events = 1 event/time.
    // (The reset means we lost the history, but we can't create a spike.)
    assert!(rate_after_reset >= 0.0, "rate after reset must be non-negative");
    assert!(
        rate_after_reset < 1.5,
        "rate after reset (100 in 100 units) should be around 1.0, not a spike"
    );

    // Planted case 3: verify rate is monotonically updated.
    let mut counter3 = RateCounter::new();
    counter3.update(0, 0);
    let rate1 = counter3.update(100, 10); // 100 events in 10 time = 10 events/time
    let rate2 = counter3.update(200, 20); // 100 events in 10 time = 10 events/time
    let rate3 = counter3.update(300, 30); // 100 events in 10 time = 10 events/time

    // THE ONE LAW: rates should all be equal (constant rate).
    assert!((rate1 - 10.0).abs() < 1e-6);
    assert!((rate2 - 10.0).abs() < 1e-6);
    assert!((rate3 - 10.0).abs() < 1e-6);

    // Planted case 4: zero-duration update (should not divide by zero).
    let mut counter4 = RateCounter::new();
    let rate_zero = counter4.update(50, 0);
    assert_eq!(rate_zero, 0.0, "rate should initialize to 0");
    let rate_same = counter4.update(100, 0); // Same time, shouldn't update.
    assert_eq!(rate_same, 0.0, "rate at zero time-delta should not change");

    println!("rate_counter: reset-safe, steady rate verified, no spurious spikes — PASS");
}
