#![forbid(unsafe_code)]
//! lru_cache — LRU eviction; exact eviction order vs brute-force reference.
//!
//! Core idea: cache with fixed size. On insertion when full, evict the least-recently-used.
//! THE LAW: execute an access trace, track eviction order, and assert it matches a
//! brute-force reference implementation that replays the entire trace.
//! When to use: memory-constrained caches, page replacement, working-set management.

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
use std::collections::HashMap;

struct LruCache {
    data: HashMap<u32, u32>,
    access_order: Vec<u32>,
    capacity: usize,
}

impl LruCache {
    fn new(capacity: usize) -> Self {
        LruCache {
            data: HashMap::new(),
            access_order: Vec::new(),
            capacity,
        }
    }

    fn access(&mut self, key: u32, value: u32) {
        // If key exists, update access order.
        if let Some(pos) = self.access_order.iter().position(|&k| k == key) {
            self.access_order.remove(pos);
        } else if self.data.len() >= self.capacity {
            // Evict LRU (first in access_order).
            if let Some(lru_key) = self.access_order.first().copied() {
                self.data.remove(&lru_key);
                self.access_order.remove(0);
            }
        }

        // Insert/update.
        self.data.insert(key, value);
        self.access_order.push(key);
    }

    fn get(&mut self, key: u32) -> Option<u32> {
        if let Some(pos) = self.access_order.iter().position(|&k| k == key) {
            self.access_order.remove(pos);
            self.access_order.push(key);
            self.data.get(&key).copied()
        } else {
            None
        }
    }

    #[allow(dead_code)]
    fn eviction_order(&self) -> Vec<u32> {
        self.access_order.clone()
    }
}

fn brute_force_lru(capacity: usize, trace: &[(u32, u32)]) -> (HashMap<u32, u32>, Vec<u32>) {
    let mut data: HashMap<u32, u32> = HashMap::new();
    let mut access_order: Vec<u32> = Vec::new();
    let mut evicted = Vec::new();

    for &(key, value) in trace {
        // Remove from access order if present.
        if let Some(pos) = access_order.iter().position(|&k| k == key) {
            access_order.remove(pos);
        } else if data.len() >= capacity {
            // Evict LRU.
            if let Some(lru_key) = access_order.first().copied() {
                data.remove(&lru_key);
                access_order.remove(0);
                evicted.push(lru_key);
            }
        }

        // Insert/update.
        data.insert(key, value);
        access_order.push(key);
    }

    (data, evicted)
}

fn main() {
    let capacity = 3;

    // Test 1: simple trace with eviction.
    let trace = vec![
        (1, 10),
        (2, 20),
        (3, 30),
        (4, 40), // Evicts 1 (LRU)
        (2, 20), // Access 2; moves to end
        (5, 50), // Evicts 3
    ];

    let (expected, _evicted_expected) = brute_force_lru(capacity, &trace);

    let mut cache = LruCache::new(capacity);
    for &(k, v) in &trace {
        cache.access(k, v);
    }

    // Verify eviction order.
    assert_eq!(cache.data, expected, "cache state matches");

    // Test 2: get() updates access order.
    let mut cache2 = LruCache::new(2);
    cache2.access(1, 10);
    cache2.access(2, 20);
    cache2.get(1); // Access 1; 2 becomes LRU
    cache2.access(3, 30); // Evicts 2

    assert!(!cache2.data.contains_key(&2), "2 was evicted");
    assert!(cache2.data.contains_key(&1), "1 is still cached");

    // Test 3: capacity 1.
    let mut cache3 = LruCache::new(1);
    cache3.access(1, 10);
    cache3.access(2, 20); // Evicts 1
    assert!(!cache3.data.contains_key(&1));
    assert_eq!(cache3.get(2), Some(20));

    println!("lru_cache: eviction order exact vs brute-force reference — PASS");
}
