#![forbid(unsafe_code)]

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
// Integer-only EWMA latency tracker with a companion EWMV (mean-absolute-deviation)
// estimate. The first sample seeds the mean; each later sample nudges the mean and
// deviation by delta/alpha, where alpha is the inverse smoothing factor (alpha=10 ≈
// weight 1/10). Use for lightweight, allocation-free latency/jitter monitoring on
// fixed-point platforms. Guarantees: deterministic integer arithmetic (no floats),
// mean converges toward a constant stream and variance decays to ~0; asserts pin
// exact values for the seeded update sequences.
struct EwmaLatencyTracker {
    ewma: i32,     // Exponentially Weighted Moving Average
    ewmv: i32,     // Exponentially Weighted Moving Variance
    alpha: i32,    // Smoothing factor (e.g., 10 = 1/10)
    initialized: bool,
}

impl EwmaLatencyTracker {
    fn new(alpha: i32) -> Self {
        Self {
            ewma: 0,
            ewmv: 0,
            alpha,
            initialized: false,
        }
    }

    fn update(&mut self, sample: i32) {
        if !self.initialized {
            self.ewma = sample;
            self.ewmv = 0;
            self.initialized = true;
        } else {
            // EWMA update: ewma = ewma + alpha * (sample - ewma)
            let delta = sample - self.ewma;
            self.ewma = self.ewma + (delta / self.alpha);

            // EWMV update: ewmv = ewmv + alpha * (|delta| - ewmv)
            let abs_delta = delta.abs();
            self.ewmv = self.ewmv + ((abs_delta - self.ewmv) / self.alpha);
        }
    }

    fn mean(&self) -> i32 {
        self.ewma
    }

    fn variance(&self) -> i32 {
        self.ewmv
    }
}

fn main() {
    // Test 1: Single sample
    let mut tracker = EwmaLatencyTracker::new(10);
    tracker.update(100);
    assert_eq!(tracker.mean(), 100, "Mean after first sample");
    assert_eq!(tracker.variance(), 0, "Variance after first sample");

    // Test 2: Second sample (different)
    tracker.update(120);
    // delta = 120 - 100 = 20
    // ewma = 100 + 20/10 = 100 + 2 = 102
    // ewmv = 0 + (20 - 0)/10 = 0 + 2 = 2
    assert_eq!(tracker.mean(), 102, "Mean after second sample");
    assert_eq!(tracker.variance(), 2, "Variance after second sample");

    // Test 3: Convergence to constant samples
    let mut tracker2 = EwmaLatencyTracker::new(10);
    for _ in 0..100 {
        tracker2.update(100);
    }
    // After many samples of 100, EWMA should converge to 100
    assert!(tracker2.mean() >= 99 && tracker2.mean() <= 101, "Mean converges to constant sample");
    assert!(tracker2.variance() < 2, "Variance approaches 0 for constant samples");

    // Test 4: Variance with oscillating samples
    let mut tracker3 = EwmaLatencyTracker::new(4);
    tracker3.update(100);
    tracker3.update(110);
    // delta = 110 - 100 = 10
    // ewma = 100 + 10/4 = 100 + 2 = 102
    // ewmv = 0 + (10 - 0)/4 = 0 + 2 = 2
    tracker3.update(90);
    // delta = 90 - 102 = -12
    // ewma = 102 + (-12)/4 = 102 - 3 = 99
    // ewmv = 2 + (12 - 2)/4 = 2 + 10/4 = 2 + 2 = 4
    assert_eq!(tracker3.mean(), 99, "Mean exact after oscillation");
    assert_eq!(tracker3.variance(), 4, "Variance exact after oscillation");

    // Test 5: Exact sequence
    let mut tracker4 = EwmaLatencyTracker::new(2);
    tracker4.update(50);
    assert_eq!(tracker4.mean(), 50);

    tracker4.update(100);
    // delta = 100 - 50 = 50
    // ewma = 50 + 50/2 = 50 + 25 = 75
    assert_eq!(tracker4.mean(), 75, "Exact mean after update");

    println!("ewma_latency_tracker: PASS");
}
