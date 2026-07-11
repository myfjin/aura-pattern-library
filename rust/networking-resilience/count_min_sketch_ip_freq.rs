#![forbid(unsafe_code)]

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
struct CountMinSketch {
    width: usize,
    table: Vec<Vec<u32>>,
    seeds: Vec<u64>,
}

impl CountMinSketch {
    fn new(width: usize, depth: usize) -> Self {
        let seeds = (0..depth as u64).collect::<Vec<_>>();
        let table = vec![vec![0; width]; depth];
        Self {
            width,
            table,
            seeds,
        }
    }

    fn hash(&self, item: u32, seed: u64) -> usize {
        let h = item.wrapping_mul((seed.wrapping_add(1) & 0xFFFFFFFF) as u32);
        (h as usize) % self.width
    }

    fn increment(&mut self, item: u32) {
        for (d, &seed) in self.seeds.iter().enumerate() {
            let idx = self.hash(item, seed);
            self.table[d][idx] = self.table[d][idx].saturating_add(1);
        }
    }

    fn query(&self, item: u32) -> u32 {
        let mut min_val = u32::MAX;
        for (d, &seed) in self.seeds.iter().enumerate() {
            let idx = self.hash(item, seed);
            min_val = min_val.min(self.table[d][idx]);
        }
        min_val
    }
}

fn main() {
    // Test 1: Single item
    let mut cms = CountMinSketch::new(128, 4);
    cms.increment(10);
    assert_eq!(cms.query(10), 1, "Single increment");

    // Test 2: Multiple increments same item
    cms.increment(10);
    cms.increment(10);
    assert_eq!(cms.query(10), 3, "Multiple increments");

    // Test 3: Different items
    cms.increment(20);
    cms.increment(30);
    assert_eq!(cms.query(10), 3, "Item 10 still has 3");
    assert_eq!(cms.query(20), 1, "Item 20 has 1");
    assert_eq!(cms.query(30), 1, "Item 30 has 1");

    // Test 4: Non-existent item
    assert_eq!(cms.query(999), 0, "Non-existent item has 0 (or collision)");

    // Test 5: Planted stream with known counts
    let mut cms2 = CountMinSketch::new(256, 3);
    let stream = vec![1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 4, 4];
    let mut true_counts = std::collections::HashMap::new();

    for ip in &stream {
        cms2.increment(*ip);
        *true_counts.entry(*ip).or_insert(0) += 1;
    }

    // Query and verify: estimate >= true count
    for (ip, &true_count) in &true_counts {
        let estimate = cms2.query(*ip);
        assert!(estimate >= true_count as u32, "Estimate {} >= true count {} for IP {}", estimate, true_count, ip);
        // Estimate should not be wildly off (with CMS, bounded error)
        assert!(estimate <= true_count as u32 + 5, "Estimate {} reasonably close to true count {} for IP {}", estimate, true_count, ip);
    }

    // Test 6: Exact counts for small dataset
    let mut cms3 = CountMinSketch::new(512, 4);
    let exact_counts = vec![(100, 5), (200, 3), (300, 7)];
    for (ip, count) in &exact_counts {
        for _ in 0..*count {
            cms3.increment(*ip);
        }
    }

    for (ip, count) in exact_counts {
        let estimate = cms3.query(ip);
        assert_eq!(estimate, count as u32, "Exact count for IP {} with large sketch", ip);
    }

    println!("count_min_sketch_ip_freq: PASS");
}
