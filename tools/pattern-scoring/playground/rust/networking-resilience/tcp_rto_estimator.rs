#![forbid(unsafe_code)]

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
// TCP retransmission-timeout estimator via the Jacobson/Karels algorithm in integer arithmetic.
// First sample seeds srtt = sample and rttvar = sample/2; later samples update
// rttvar = 3/4*rttvar + 1/4*|sample-srtt| and srtt = 7/8*srtt + 1/8*sample, then RTO = srtt + 4*rttvar.
// Use to derive an adaptive retransmit timer from RTT measurements without floating point.
// Guarantees (the oracle): exact integer-truncated results for known sample sequences, and
// convergence of srtt to a constant sample value with rttvar shrinking toward 0.
struct TcpRtoEstimator {
    srtt: i32,      // Smoothed RTT, in units
    rttvar: i32,    // RTT variance, in units
    rto: i32,       // RTO estimate
}

impl TcpRtoEstimator {
    fn new() -> Self {
        Self {
            srtt: 0,
            rttvar: 0,
            rto: 0,
        }
    }

    fn update(&mut self, rtt_sample: i32) {
        if self.srtt == 0 {
            // First sample
            self.srtt = rtt_sample;
            self.rttvar = rtt_sample / 2;
        } else {
            // Jacobson/Karels algorithm
            let delta = (rtt_sample - self.srtt).abs();
            self.rttvar = (self.rttvar * 3 / 4) + (delta / 4);
            self.srtt = (self.srtt * 7 / 8) + (rtt_sample / 8);
        }

        // RTO = SRTT + 4 * RTTVAR
        self.rto = self.srtt + (4 * self.rttvar);
    }

    fn get_rto(&self) -> i32 {
        self.rto
    }
}

fn main() {
    // Test 1: Single sample
    let mut est = TcpRtoEstimator::new();
    est.update(100);
    assert_eq!(est.srtt, 100, "SRTT initialized to first sample");
    assert_eq!(est.rttvar, 50, "RTTVAR = sample/2");
    assert_eq!(est.get_rto(), 100 + 200, "RTO = SRTT + 4*RTTVAR = 100+200=300");

    // Test 2: Second sample (different)
    est.update(120);
    // delta = |120 - 100| = 20
    // rttvar = (50 * 3 / 4) + (20 / 4) = 37 + 5 = 42
    // srtt = (100 * 7 / 8) + (120 / 8) = 87 + 15 = 102
    // rto = 102 + 4*42 = 102 + 168 = 270
    assert_eq!(est.srtt, 102, "SRTT after second sample");
    assert_eq!(est.rttvar, 42, "RTTVAR after second sample");
    assert_eq!(est.get_rto(), 270, "RTO correctly computed");

    // Test 3: Known sequence — exact hand-computed result (integer truncation is the oracle).
    // [100]:        srtt=100, rttvar=50
    // [110]: d=10 → rttvar=50*3/4+10/4=39, srtt=100*7/8+110/8=100
    // [105]: d=5  → rttvar=39*3/4+5/4=30,  srtt=100*7/8+105/8=100
    // [115]: d=15 → rttvar=30*3/4+15/4=25, srtt=100*7/8+115/8=101 → rto=101+4*25=201
    let mut est2 = TcpRtoEstimator::new();
    for s in vec![100, 110, 105, 115] {
        est2.update(s);
    }
    assert_eq!(est2.srtt, 101, "SRTT exact after known sequence");
    assert_eq!(est2.rttvar, 25, "RTTVAR exact after known sequence");
    assert_eq!(est2.get_rto(), 201, "RTO exact after known sequence");

    // Test 4: Convergence test
    let mut est3 = TcpRtoEstimator::new();
    for _ in 0..100 {
        est3.update(100); // All samples = 100
    }
    // SRTT should converge to 100, RTTVAR to near 0
    assert!(est3.srtt >= 95 && est3.srtt <= 105, "SRTT converges to sample value");
    assert!(est3.rttvar < 10, "RTTVAR converges to 0 for constant samples");

    println!("tcp_rto_estimator: PASS");
}
