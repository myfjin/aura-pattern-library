#![forbid(unsafe_code)]

// GCRA: Generic Cell Rate Algorithm (virtual scheduling).
// Two parameters make it a real GCRA rather than a bare min-interval limiter:
//   T   = emission interval (time units per cell) — the sustained rate.
//   tau = limit / burst tolerance — how far ahead of the Theoretical Arrival Time (TAT)
//         a burst may run. tau = 0 collapses to a fixed-interval limiter; tau > 0 admits
//         a burst of floor(tau/T)+1 cells before throttling to the sustained rate.
// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
struct GcraRateLimiter {
    t: u64,
    tau: u64,
    tat: u64, // Theoretical Arrival Time
}

impl GcraRateLimiter {
    fn new(t: u64, tau: u64) -> Self {
        Self { t, tau, tat: 0 }
    }

    fn allow(&mut self, now: u64) -> bool {
        // Nonconforming if the arrival is earlier than TAT - tau (bucket too full).
        if now < self.tat.saturating_sub(self.tau) {
            false
        } else {
            // Conforming: advance TAT by T from max(now, TAT) (reset if the bucket drained).
            self.tat = self.tat.max(now) + self.t;
            true
        }
    }
}

fn main() {
    // Test 1: tau = 0 → pure fixed-interval (no burst). T = 10.
    let mut gcra = GcraRateLimiter::new(10, 0);
    let mut admitted = 0;
    for _ in 0..5 {
        if gcra.allow(0) {
            admitted += 1;
        }
    }
    assert_eq!(admitted, 1, "tau=0: only 1 cell admitted at t=0");
    assert!(gcra.allow(10), "cell at t=10 admitted");
    assert!(!gcra.allow(11), "cell at t=11 denied (TAT=20)");
    assert!(gcra.allow(20), "cell at t=20 admitted");

    // Test 2: burst tolerance. T=2, tau=4 → burst of floor(4/2)+1 = 3 cells.
    let mut burst = GcraRateLimiter::new(2, 4);
    let mut burst_admitted = 0;
    for _ in 0..5 {
        if burst.allow(0) {
            burst_admitted += 1;
        }
    }
    assert_eq!(burst_admitted, 3, "tau=4,T=2: burst of exactly 3 at t=0");

    // Test 3: exact admit/deny vector with burst then sustained rate. T=2, tau=4.
    let mut gcra2 = GcraRateLimiter::new(2, 4);
    let arrivals = vec![0, 0, 0, 0, 2, 4, 6];
    let expected = vec![true, true, true, false, true, true, true];
    let results: Vec<bool> = arrivals.iter().map(|&t| gcra2.allow(t)).collect();
    assert_eq!(results, expected, "exact GCRA admit/deny sequence with burst tolerance");

    println!("gcra_rate_limiter: PASS");
}
