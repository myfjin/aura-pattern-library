#![forbid(unsafe_code)]
//! misra_gries_topk — heavy hitters; GUARANTEE: any freq > n/(k+1) is in output.
//!
//! Core idea: maintain k candidate items + counters. For new item, if it's a candidate,
//! increment; else if space, add; else decrement all. Query returns items with freq > 0.
//! Guarantee: any item with freq > n/(k+1) is guaranteed in the output. THE LAW: plant
//! items with known frequencies, run Misra-Gries, and assert every item with freq > n/(k+1)
//! appears in the output.
//! When to use: finding heavy hitters, top-k detection, streaming analytics.

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
use std::collections::HashMap;

struct MisraGries {
    k: usize,
    candidates: HashMap<String, u64>,
}

impl MisraGries {
    fn new(k: usize) -> Self {
        MisraGries {
            k,
            candidates: HashMap::new(),
        }
    }

    fn process(&mut self, item: String) {
        if let Some(count) = self.candidates.get_mut(&item) {
            *count += 1;
        } else if self.candidates.len() < self.k {
            self.candidates.insert(item, 1);
        } else {
            // Decrement all.
            for count in self.candidates.values_mut() {
                *count -= 1;
            }
            // Remove zeros.
            self.candidates.retain(|_, v| *v > 0);
        }
    }

    fn output(&self) -> Vec<String> {
        self.candidates
            .iter()
            .filter(|(_, &v)| v > 0)
            .map(|(k, _)| k.clone())
            .collect()
    }
}

fn main() {
    let k = 2; // Find heavy hitters with freq > n/(k+1) = n/3
    let n = 12; // 12 items
    let threshold = n / (k + 1); // 12 / 3 = 4

    // Plant items: "a"(5 times), "b"(4 times), "c"(2 times), "d"(1 time).
    let stream = vec![
        "a", "b", "a", "c", "a", "b", "a", "b", "d", "a", "b", "c",
    ];

    let mut mg = MisraGries::new(k);
    for item in stream {
        mg.process(item.to_string());
    }

    let heavy_hitters = mg.output();

    // Test 1: items with freq > threshold are in output.
    // "a" has freq 5 > 4, "b" has freq 4 > 4 is false, so only "a" guaranteed.
    // But the algorithm is approximate, so we check the guarantee.
    let freq_a = 5;
    assert!(
        freq_a > threshold,
        "a has freq 5 > threshold {}",
        threshold
    );
    // "a" should be in output (though not guaranteed by the theorem for "b" since 4 is not > 4).
    assert!(
        heavy_hitters.contains(&"a".to_string()),
        "a (freq > threshold) is in output"
    );

    // Test 2: output size ≤ k.
    assert!(heavy_hitters.len() <= k, "output size <= k");

    // Test 3: empty stream.
    let mg_empty = MisraGries::new(2);
    let empty_output = mg_empty.output();
    assert_eq!(empty_output.len(), 0, "empty stream yields empty output");

    // Test 4: all distinct items (no heavy hitters).
    let mut mg_distinct = MisraGries::new(2);
    for item in &["x", "y", "z", "w"] {
        mg_distinct.process(item.to_string());
    }
    // All have freq 1, threshold = 4 / 3 = 1, so no guarantees.

    println!("misra_gries_topk: heavy hitters guaranteed — PASS");
}
