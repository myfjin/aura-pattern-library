#![forbid(unsafe_code)]
//! hyperloglog_lite — cardinality estimate; relative error within a COMPUTED bound.
//!
//! Core idea: hash each item to 64 bits; the low P bits pick a register (m = 2^P), the remaining
//! bits' leading-zero run + 1 (rho) is recorded as the register's max. The harmonic-mean estimate
//! α·m²/Σ2^-reg approximates the distinct count with standard error 1.04/√m. The bucket bits and
//! the rho bits must NOT overlap, and the hash must spread bits well — get either wrong and the
//! estimate blows up. THE LAW: estimate a large distinct set and assert the relative error is
//! within 3× the standard error (a real ~3σ bound, not a vacuous 10×). When to use: approximate
//! distinct counts, cardinality estimation. (`_lite`: no small/large-range bias correction.)

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
struct HyperLogLogLite {
    m: u32,
    p: u32, // log2(m)
    registers: Vec<u8>,
}

impl HyperLogLogLite {
    fn new(m: u32) -> Self {
        assert!(m.is_power_of_two(), "m must be a power of two");
        HyperLogLogLite { m, p: m.trailing_zeros(), registers: vec![0; m as usize] }
    }

    // FNV-1a + splitmix64 finalizer → well-distributed 64 bits (a weak *31 hash biases rho).
    fn hash(item: &str) -> u64 {
        let mut h = 1469598103934665603u64;
        for &b in item.as_bytes() {
            h ^= b as u64;
            h = h.wrapping_mul(1099511628211);
        }
        let mut z = h.wrapping_add(0x9E3779B97F4A7C15);
        z = (z ^ (z >> 30)).wrapping_mul(0xBF58476D1CE4E5B9);
        z = (z ^ (z >> 27)).wrapping_mul(0x94D049BB133111EB);
        z ^ (z >> 31)
    }

    fn insert(&mut self, item: &str) {
        let h = Self::hash(item);
        let j = (h & (self.m as u64 - 1)) as usize; // low P bits → register
        let w = h >> self.p; // remaining 64-P bits
        let rho = if w == 0 {
            (64 - self.p + 1) as u8
        } else {
            // leading zeros within the (64-P)-bit window, +1
            (w.leading_zeros() - self.p + 1) as u8
        };
        if rho > self.registers[j] {
            self.registers[j] = rho;
        }
    }

    fn estimate(&self) -> f64 {
        let m = self.m as f64;
        let alpha = 0.7213 / (1.0 + 1.079 / m);
        let sum: f64 = self.registers.iter().map(|&r| 2.0_f64.powi(-(r as i32))).sum();
        alpha * m * m / sum
    }

    fn relative_error(&self) -> f64 {
        1.04 / (self.m as f64).sqrt()
    }
}

fn main() {
    // n/m ≈ 49 (well above the small-range regime), so the raw estimate is accurate here.
    let m: u32 = 1024;
    let mut hll = HyperLogLogLite::new(m);
    let true_cardinality: u32 = 50_000;
    for i in 0..true_cardinality {
        hll.insert(&format!("item_{}", i));
    }

    let estimated = hll.estimate();
    let std_error = hll.relative_error(); // 1.04/√1024 ≈ 0.0325
    let actual_error = (estimated - true_cardinality as f64).abs() / true_cardinality as f64;

    // THE LAW: error within 3× the standard error (~3σ), a real COMPUTED bound.
    assert!(
        actual_error <= std_error * 3.0,
        "actual error {:.4} exceeds 3×std {:.4} (est {:.0}, true {})",
        actual_error, std_error * 3.0, estimated, true_cardinality
    );

    // `_lite` honesty: an UNCORRECTED HLL does not read ~0 when empty — the raw estimate floors
    // near α·m (this is exactly why production HLL adds small-range/linear-counting correction).
    let alpha = 0.7213 / (1.0 + 1.079 / m as f64);
    let empty = HyperLogLogLite::new(m).estimate();
    assert!((empty - alpha * m as f64).abs() < 1.0, "empty raw estimate floors near α·m ≈ {:.0}", alpha * m as f64);
    assert!(estimated > empty * 10.0, "a large distinct set estimates far above the empty floor");

    println!(
        "hyperloglog_lite: est {:.0} for {} distinct, error {:.2}% ≤ 3×std {:.2}% — PASS",
        estimated, true_cardinality, actual_error * 100.0, std_error * 300.0
    );
}
