#![forbid(unsafe_code)]
//! histogram_quantile — bucketed histogram; quantile within tolerance of exact.
//!
//! Core idea: log-scale buckets hold sample counts; approximate quantile is computed
//! by scanning buckets. THE ONE LAW: plant a known distribution into the histogram,
//! compute the quantile from exact sorted data, then assert the bucketed quantile
//! is within a tolerance (relative error). A broken bucket boundary or skipped bucket
//! would produce a quantile outside tolerance.
//! When to use: latency histograms, percentile-based SLOs, scalable quantile estimation.

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
struct Histogram {
    buckets: Vec<u64>,
}

impl Histogram {
    fn new() -> Self {
        // Finer buckets: powers of 2 plus intermediate steps.
        // [1, 1.4, 2, 2.8, 4, 5.6, 8, 11.3, 16, 22.6, 32, 45.3, 64, 90.5, 128, 181, 256, 362, 512, 1024]
        let buckets = vec![0; 20];
        Histogram { buckets }
    }

    fn add_sample(&mut self, value: f64) {
        let bounds = [
            1.0, 1.4, 2.0, 2.8, 4.0, 5.6, 8.0, 11.3, 16.0, 22.6, 32.0, 45.3, 64.0, 90.5, 128.0,
            181.0, 256.0, 362.0, 512.0, 1024.0,
        ];
        let mut idx = 19;
        for (i, &bound) in bounds.iter().enumerate() {
            if value < bound {
                idx = i;
                break;
            }
        }
        self.buckets[idx] += 1;
    }

    fn count(&self) -> u64 {
        self.buckets.iter().sum()
    }

    fn quantile(&self, q: f64) -> f64 {
        let bounds = [
            1.0, 1.4, 2.0, 2.8, 4.0, 5.6, 8.0, 11.3, 16.0, 22.6, 32.0, 45.3, 64.0, 90.5, 128.0,
            181.0, 256.0, 362.0, 512.0, 1024.0,
        ];
        let total = self.count() as f64;
        let target_rank = total * q;
        let mut cumsum = 0.0;

        for (i, &count) in self.buckets.iter().enumerate() {
            let bucket_lower = if i == 0 { 1.0 } else { bounds[i - 1] };
            let bucket_upper = bounds[i];
            let prev_cumsum = cumsum;
            cumsum += count as f64;

            if cumsum >= target_rank {
                // Linear interpolation within the bucket.
                let within_bucket = target_rank - prev_cumsum;
                let fraction = within_bucket / (count as f64).max(1.0);
                return bucket_lower + fraction * (bucket_upper - bucket_lower);
            }
        }
        1024.0
    }
}

fn exact_quantile(mut values: Vec<f64>, q: f64) -> f64 {
    values.sort_by(|a, b| a.partial_cmp(b).unwrap_or(std::cmp::Ordering::Equal));
    let idx = ((values.len() as f64 - 1.0) * q) as usize;
    values[idx]
}

fn main() {
    // Planted case: uniform distribution over [1..512].
    let mut hist = Histogram::new();
    let mut samples = Vec::new();

    // Generate seeded deterministic sequence in log space.
    let mut seed = 12345u64;
    for _ in 0..1000 {
        seed = seed.wrapping_mul(2654435761).wrapping_add(2246822519);
        let uniform = ((seed >> 32) as f64) / (u32::MAX as f64); // [0, 1]
        let value = 1.0 + uniform * 511.0; // [1, 512]
        hist.add_sample(value);
        samples.push(value);
    }

    // THE ONE LAW: the histogram's quantile must be within ±20% (relative error) of the exact.
    let exact_p50 = exact_quantile(samples.clone(), 0.5);
    let hist_p50 = hist.quantile(0.5);
    let error_p50 = (hist_p50 - exact_p50).abs() / exact_p50.max(1.0);
    assert!(
        error_p50 < 0.2,
        "p50 quantile error {:.2}% exceeds 20% tolerance (exact={}, hist={})",
        error_p50 * 100.0,
        exact_p50,
        hist_p50
    );

    let exact_p99 = exact_quantile(samples.clone(), 0.99);
    let hist_p99 = hist.quantile(0.99);
    let error_p99 = (hist_p99 - exact_p99).abs() / exact_p99.max(1.0);
    assert!(
        error_p99 < 0.2,
        "p99 quantile error {:.2}% exceeds 20% tolerance (exact={}, hist={})",
        error_p99 * 100.0,
        exact_p99,
        hist_p99
    );

    // Verify no bucket overflow: total count matches samples.
    assert_eq!(hist.count(), 1000, "histogram count must match input sample count");

    // Verify monotonicity: quantiles increase with q.
    let q1 = hist.quantile(0.25);
    let q2 = hist.quantile(0.75);
    assert!(q1 <= q2, "quantiles must be monotonic in q");

    println!(
        "histogram_quantile: p50 error {:.1}%, p99 error {:.1}%, within tolerance — PASS",
        error_p50 * 100.0,
        error_p99 * 100.0
    );
}
