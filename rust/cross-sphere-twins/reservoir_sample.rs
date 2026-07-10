#![forbid(unsafe_code)]
//! reservoir_sample — Algorithm R; UNIFORM over the stream, seeded-deterministic.
//!
//! Core idea: keep a size-k reservoir. The first k items fill it; the i-th item thereafter
//! (i = total seen) replaces a uniformly-random reservoir slot with probability k/i. The
//! defining property is UNIFORMITY: after the stream, every element is in the sample with
//! probability k/n. THE LAW: a broken sampler using a constant probability (k/(k+1) instead
//! of k/i) is NOT uniform — so we assert, over many seeds, that each element's inclusion
//! frequency converges to k/n, plus determinism and valid-subset. When to use: streaming
//! uniform samples, online data collection.

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
struct ReservoirSample {
    k: usize,
    reservoir: Vec<u32>,
    n_seen: u64,
    rng: u64,
}

impl ReservoirSample {
    fn new(k: usize, seed: u64) -> Self {
        ReservoirSample { k, reservoir: Vec::new(), n_seen: 0, rng: seed }
    }

    // splitmix64 — good-quality deterministic PRNG (a weak LCG would bias the uniformity test).
    fn next_rand(&mut self) -> u64 {
        self.rng = self.rng.wrapping_add(0x9E3779B97F4A7C15);
        let mut z = self.rng;
        z = (z ^ (z >> 30)).wrapping_mul(0xBF58476D1CE4E5B9);
        z = (z ^ (z >> 27)).wrapping_mul(0x94D049BB133111EB);
        z ^ (z >> 31)
    }

    fn process(&mut self, item: u32) {
        self.n_seen += 1;
        if self.reservoir.len() < self.k {
            self.reservoir.push(item);
        } else {
            // Replace slot with probability k/n_seen (Algorithm R).
            let j = (self.next_rand() % self.n_seen) as usize;
            if j < self.k {
                self.reservoir[j] = item;
            }
        }
    }

    fn sample(&self) -> Vec<u32> {
        self.reservoir.clone()
    }
}

fn run(stream: &[u32], k: usize, seed: u64) -> Vec<u32> {
    let mut rs = ReservoirSample::new(k, seed);
    for &x in stream {
        rs.process(x);
    }
    rs.sample()
}

fn main() {
    let stream: Vec<u32> = (1..=10).collect();
    let k = 3;

    // Determinism: same seed → same sample.
    assert_eq!(run(&stream, k, 42), run(&stream, k, 42), "same seed → same sample");

    // Valid subset of exactly k distinct stream elements.
    let s = run(&stream, k, 42);
    assert_eq!(s.len(), k, "sample size is k");
    for &x in &s {
        assert!(stream.contains(&x), "sample element {x} came from the stream");
    }

    // n < k → sample is the whole stream.
    assert_eq!(run(&[1, 2], 3, 7).len(), 2, "n<k keeps everything");

    // THE DEFINING PROPERTY — UNIFORMITY: over many seeds, each of the 10 elements is in the
    // final sample with frequency ≈ k/n = 0.30. A constant-probability (broken) sampler skews
    // this heavily toward late elements; the correct k/i does not.
    let trials = 20_000u32;
    let mut hits = [0u32; 11]; // index by element value 1..=10
    for seed in 0..trials as u64 {
        for x in run(&stream, k, seed.wrapping_mul(0x9E3779B97F4A7C15) ^ 0xDEAD) {
            hits[x as usize] += 1;
        }
    }
    let expected = trials as f64 * k as f64 / stream.len() as f64; // 20000 * 0.3 = 6000
    for x in 1..=10usize {
        let freq = hits[x] as f64;
        assert!(
            (freq - expected).abs() / expected < 0.06,
            "element {x} inclusion freq {freq} deviates >6% from uniform {expected} (non-uniform sampler)",
        );
    }

    println!("reservoir_sample: uniform k/i sampling ({:.0}±<6% per element), deterministic — PASS", expected);
}
