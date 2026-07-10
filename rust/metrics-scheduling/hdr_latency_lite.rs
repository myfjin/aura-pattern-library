#![forbid(unsafe_code)]
//! hdr_latency_lite — HDR-style latency histogram; percentiles within a BOUNDED relative error.
//!
//! Core idea: a High-Dynamic-Range histogram keeps `SUB` linear sub-buckets inside every
//! power-of-two octave, so it covers 1µs..1s cheaply while bounding the relative error of any
//! recorded value to ~1/SUB — the whole point of HDR (an order-of-magnitude bucketer cannot).
//! THE ONE LAW: record a Pareto-ish latency distribution, then assert the bucketed p50/p99 are
//! within a TIGHT relative error of the exact sorted percentiles — a coarse or off-by-one bucket
//! mapping would blow past the bound. When to use: SLO tail-latency tracking, p99 dashboards.

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
const SUB: u64 = 16; // sub-buckets per octave → worst-case relative error ≈ 1/SUB ≈ 6.25%
const MAG: u64 = 21; // octaves covered (2^0 .. 2^21 µs ≈ 2.1s)

struct HdrHistogram {
    counts: Vec<u64>,
}

impl HdrHistogram {
    fn new() -> Self {
        HdrHistogram {
            counts: vec![0; (MAG * SUB) as usize + 1],
        }
    }

    fn bucket_index(v: u64) -> usize {
        let v = v.max(1);
        let mag = 63 - v.leading_zeros() as u64; // floor(log2(v))
        if mag >= MAG {
            return (MAG * SUB) as usize; // overflow bucket
        }
        let base = 1u64 << mag; // 2^mag
        let within = ((v - base) * SUB) / base; // 0..SUB-1 (linear inside the octave)
        (mag * SUB + within) as usize
    }

    /// Representative value of a bucket = the MIDPOINT of its [lo, hi) sub-range.
    fn bucket_value(idx: usize) -> u64 {
        let idx = idx as u64;
        if idx >= MAG * SUB {
            return 1u64 << MAG;
        }
        let mag = idx / SUB;
        let within = idx % SUB;
        let base = 1u64 << mag;
        let step = (base / SUB).max(1);
        base + within * step + step / 2 // lower bound + half a sub-bucket
    }

    fn record(&mut self, micros: u64) {
        let i = Self::bucket_index(micros);
        self.counts[i] += 1;
    }

    fn count(&self) -> u64 {
        self.counts.iter().sum()
    }

    fn percentile(&self, p: f64) -> u64 {
        let target = (self.count() as f64 * p / 100.0).ceil() as u64;
        let mut cumsum = 0u64;
        for (i, &c) in self.counts.iter().enumerate() {
            cumsum += c;
            if cumsum >= target && target > 0 {
                return Self::bucket_value(i);
            }
        }
        Self::bucket_value(self.counts.len() - 1)
    }
}

fn exact_percentile(mut values: Vec<u64>, p: f64) -> u64 {
    if values.is_empty() {
        return 0;
    }
    values.sort_unstable();
    let idx = (((values.len() as f64 - 1.0) * p / 100.0).ceil() as usize).min(values.len() - 1);
    values[idx]
}

fn main() {
    let mut hist = HdrHistogram::new();
    let mut samples = Vec::new();

    // Seeded Pareto-ish distribution: 80% fast (<1ms), 20% spread across 1..1000ms.
    let mut seed = 54321u64;
    for _ in 0..10_000 {
        seed = seed.wrapping_mul(2654435761).wrapping_add(2246822519);
        let uniform = ((seed >> 32) as f64) / (u32::MAX as f64);
        let micros = if uniform < 0.8 {
            (uniform * 1000.0) as u64
        } else {
            ((uniform - 0.8) / 0.2 * 999_000.0 + 1000.0) as u64
        };
        hist.record(micros);
        samples.push(micros);
    }

    // THE ONE LAW: HDR p50 and p99 are within a TIGHT relative error (≤ 12%) of exact — far
    // better than the ~half-decade error of an order-of-magnitude bucketer.
    for &p in &[50.0f64, 99.0] {
        let exact = exact_percentile(samples.clone(), p);
        let got = hist.percentile(p);
        let err = (got as f64 - exact as f64).abs() / (exact.max(1) as f64);
        assert!(
            err < 0.12,
            "p{p} error {:.1}% exceeds 12% (exact={exact}µs, hdr={got}µs)",
            err * 100.0
        );
    }

    let p50 = hist.percentile(50.0);
    let p99 = hist.percentile(99.0);
    assert!(p50 < p99, "p50 must be below p99");
    assert_eq!(hist.count(), 10_000, "every sample must be recorded once");

    let exact99 = exact_percentile(samples.clone(), 99.0);
    let err99 = (p99 as f64 - exact99 as f64).abs() / exact99 as f64 * 100.0;
    println!("hdr_latency_lite: p99 {p99}µs (exact {exact99}µs, err {err99:.1}%) within 12% — PASS");
}
