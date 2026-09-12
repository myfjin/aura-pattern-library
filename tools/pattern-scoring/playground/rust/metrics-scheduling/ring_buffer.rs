#![forbid(unsafe_code)]
//! ring_buffer — fixed-capacity ring buffer; windowed stats (sum/mean) match brute force.
//!
//! Core idea: ring buffer holds the last N samples in a circular buffer; sum and mean
//! are computed incrementally as items are pushed. THE ONE LAW: plant a known sequence
//! into the ring, compare windowed sum and mean to brute-force computation on the same
//! window, and assert they match exactly. A broken circular index or stale sum would fail.
//! When to use: sliding-window aggregates, online metrics, memory-bounded statistics.

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
use std::collections::VecDeque;

struct RingBuffer {
    capacity: usize,
    data: VecDeque<f64>,
    sum: f64,
}

impl RingBuffer {
    fn new(capacity: usize) -> Self {
        RingBuffer {
            capacity,
            data: VecDeque::with_capacity(capacity),
            sum: 0.0,
        }
    }

    fn push(&mut self, value: f64) {
        if self.data.len() >= self.capacity {
            if let Some(evicted) = self.data.pop_front() {
                self.sum -= evicted;
            }
        }
        self.data.push_back(value);
        self.sum += value;
    }

    fn mean(&self) -> f64 {
        if self.data.is_empty() {
            0.0
        } else {
            self.sum / self.data.len() as f64
        }
    }

    fn sum(&self) -> f64 {
        self.sum
    }

    fn len(&self) -> usize {
        self.data.len()
    }
}

fn brute_force_mean(samples: &[f64]) -> f64 {
    if samples.is_empty() {
        0.0
    } else {
        samples.iter().sum::<f64>() / samples.len() as f64
    }
}

fn brute_force_sum(samples: &[f64]) -> f64 {
    samples.iter().sum()
}

fn main() {
    // Planted scenario: push 50 samples into a ring of capacity 20.
    let mut ring = RingBuffer::new(20);

    // Generate deterministic sequence: 2..52
    for i in 2..52 {
        ring.push(i as f64);
    }

    // After 50 pushes into capacity 20, the ring holds samples 32..51 (the last 20).
    let expected_window: Vec<f64> = (32..52).map(|i| i as f64).collect();

    assert_eq!(
        ring.len(),
        20,
        "ring should hold exactly capacity items"
    );

    // THE ONE LAW: the ring's incremental sum and mean must match brute-force computation.
    let expected_sum = brute_force_sum(&expected_window);
    let expected_mean = brute_force_mean(&expected_window);

    assert!(
        (ring.sum() - expected_sum).abs() < 1e-9,
        "ring sum {} does not match expected sum {}",
        ring.sum(),
        expected_sum
    );
    assert!(
        (ring.mean() - expected_mean).abs() < 1e-9,
        "ring mean {} does not match expected mean {}",
        ring.mean(),
        expected_mean
    );

    // Verify the window contents: ring holds 32..51 (ascending).
    let window_vec: Vec<f64> = ring.data.iter().copied().collect();
    assert_eq!(window_vec, expected_window, "ring contents must match expected window");

    // Test that pushing beyond capacity evicts: push one more (52).
    ring.push(52.0);
    let expected_after_evict: Vec<f64> = (33..53).map(|i| i as f64).collect();
    let expected_sum_after = brute_force_sum(&expected_after_evict);
    let expected_mean_after = brute_force_mean(&expected_after_evict);

    assert!(
        (ring.sum() - expected_sum_after).abs() < 1e-9,
        "after eviction, ring sum must match"
    );
    assert!(
        (ring.mean() - expected_mean_after).abs() < 1e-9,
        "after eviction, ring mean must match"
    );

    println!("ring_buffer: windowed sum/mean match brute force over 50→20 samples — PASS");
}
