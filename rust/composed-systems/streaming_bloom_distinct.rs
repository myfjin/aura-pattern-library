#![forbid(unsafe_code)]
// composes: parse-stream + k-hash-bloom-membership + cardinality-estimate-from-fill
//
// A real k-hash bloom filter (not a single bit). Membership guarantees NO false negatives, and
// the DISTINCT count is ESTIMATED FROM THE BLOOM ITSELF (via the fill ratio), not read off an
// exact set — n ≈ -(m/k)·ln(1 - X/m), where X = set bits, m = size, k = hashes. We check the
// estimate against the true cardinality (computed only as the test oracle).

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
use std::collections::HashSet;

struct Bloom {
    bits: Vec<bool>,
    m: usize,
    k: usize,
}

impl Bloom {
    fn new(m: usize, k: usize) -> Self {
        Bloom { bits: vec![false; m], m, k }
    }

    // k independent-ish hashes via distinct seeds (double-hashing style).
    fn hashes(&self, item: &str) -> Vec<usize> {
        let mut h1: u64 = 1469598103934665603;
        let mut h2: u64 = 1099511628211;
        for b in item.bytes() {
            h1 = h1.wrapping_mul(31).wrapping_add(b as u64);
            h2 = h2.wrapping_mul(37).wrapping_add(b as u64).wrapping_add(1);
        }
        (0..self.k)
            .map(|i| ((h1.wrapping_add((i as u64).wrapping_mul(h2))) % self.m as u64) as usize)
            .collect()
    }

    fn insert(&mut self, item: &str) {
        for idx in self.hashes(item) {
            self.bits[idx] = true;
        }
    }

    fn contains(&self, item: &str) -> bool {
        self.hashes(item).iter().all(|&idx| self.bits[idx])
    }

    fn set_bits(&self) -> usize {
        self.bits.iter().filter(|&&b| b).count()
    }

    // Cardinality estimate from the fill ratio.
    fn estimate_cardinality(&self) -> f64 {
        let x = self.set_bits() as f64;
        let m = self.m as f64;
        let k = self.k as f64;
        if x >= m {
            return f64::INFINITY;
        }
        -(m / k) * (1.0 - x / m).ln()
    }
}

fn main() {
    let m = 1024;
    let k = 3;
    let mut bloom = Bloom::new(m, k);
    let mut exact: HashSet<u64> = HashSet::new();

    // Stage 1: parse a stream — a seeded generator yields ~100 distinct ids with repeats.
    let mut seed = 12345u64;
    let mut stream: Vec<String> = Vec::new();
    for _ in 0..300 {
        seed = seed.wrapping_mul(1664525).wrapping_add(1013904223);
        let id = seed % 100; // 100 distinct possible values
        stream.push(format!("ip-{id}"));
    }

    // Stage 2: bloom membership + exact oracle.
    for item in &stream {
        bloom.insert(item);
        let mut h = 1469598103934665603u64;
        for b in item.bytes() {
            h = h.wrapping_mul(31).wrapping_add(b as u64);
        }
        exact.insert(h);
    }
    let true_distinct = exact.len();

    // NO FALSE NEGATIVES: every item seen must test positive.
    for item in &stream {
        assert!(bloom.contains(item), "bloom must never give a false negative");
    }

    // Stage 3: estimate distinct FROM THE BLOOM and compare to the truth.
    let est = bloom.estimate_cardinality();
    let err = (est - true_distinct as f64).abs() / true_distinct as f64;
    assert!(
        err < 0.15,
        "bloom fill-ratio estimate {est:.1} within 15% of true {true_distinct} (err {err:.3})"
    );

    // A single-hash degenerate bloom would fail here: prove k-hash actually sets multiple bits.
    assert!(bloom.set_bits() > true_distinct, "k-hash bloom sets more bits than there are items");

    println!("streaming_bloom_distinct: PASS");
}
