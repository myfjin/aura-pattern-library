#![forbid(unsafe_code)]
//! bloom_backed_cache — bloom filter gates cache lookups; ZERO false negatives.
//!
//! Core idea: before checking an RwLock cache, query a bloom filter. If the bloom says
//! "not present," the item is definitely absent (no false negatives). If "possibly present,"
//! check the cache. A miss when the bloom says "yes" still returns None, but we avoided
//! a lock if the bloom said "no." THE LAW: add keys, query bloom + cache, and assert
//! the bloom never says "absent" when the cache has the key.
//! When to use: negative-lookup optimization, cache miss prediction, lock avoidance.

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
use std::sync::RwLock;

struct BloomFilter {
    bits: Vec<bool>,
    num_hashes: usize,
}

impl BloomFilter {
    fn new(size: usize, num_hashes: usize) -> Self {
        BloomFilter {
            bits: vec![false; size],
            num_hashes,
        }
    }

    fn hash(&self, item: &[u8], k: usize) -> usize {
        let mut h = 0u64;
        for &byte in item {
            h = h.wrapping_mul(31).wrapping_add(byte as u64);
        }
        h = h.wrapping_add(k as u64);
        (h as usize) % self.bits.len()
    }

    fn insert(&mut self, item: &[u8]) {
        for k in 0..self.num_hashes {
            let idx = self.hash(item, k);
            self.bits[idx] = true;
        }
    }

    fn contains(&self, item: &[u8]) -> bool {
        for k in 0..self.num_hashes {
            let idx = self.hash(item, k);
            if !self.bits[idx] {
                return false;
            }
        }
        true
    }
}

struct BloomBackedCache {
    bloom: BloomFilter,
    cache: RwLock<std::collections::HashMap<Vec<u8>, Vec<u8>>>,
}

impl BloomBackedCache {
    fn new(bloom_size: usize, num_hashes: usize) -> Self {
        BloomBackedCache {
            bloom: BloomFilter::new(bloom_size, num_hashes),
            cache: RwLock::new(std::collections::HashMap::new()),
        }
    }

    fn insert(&mut self, key: &[u8], value: &[u8]) {
        self.bloom.insert(key);
        self.cache.write().unwrap().insert(key.to_vec(), value.to_vec());
    }

    fn get(&self, key: &[u8]) -> Option<Vec<u8>> {
        // If bloom says "no," return None without checking cache.
        if !self.bloom.contains(key) {
            return None;
        }

        // Bloom says "possibly yes," check cache.
        self.cache.read().unwrap().get(key).cloned()
    }
}

fn main() {
    let mut cache = BloomBackedCache::new(100, 3);

    // Test 1: insert and retrieve.
    cache.insert(b"key1", b"value1");
    cache.insert(b"key2", b"value2");
    let found = cache.get(b"key1");
    assert_eq!(found, Some(b"value1".to_vec()), "key1 found");

    // Test 2: bloom says "no" for missing key → get returns None without cache check.
    let not_found = cache.get(b"missing_key");
    assert_eq!(not_found, None, "missing key returns None");

    // Test 3: add many keys, bloom should contain all.
    for i in 0..20 {
        let key = format!("key_{}", i);
        cache.insert(key.as_bytes(), b"value");
    }

    // Every inserted key's bloom answer is "yes."
    for i in 0..20 {
        let key = format!("key_{}", i);
        assert!(cache.bloom.contains(key.as_bytes()), "key {} in bloom", i);
    }

    // Test 4: bloom false positive (possible but rare); still correct via cache check.
    // Adding a key that likely doesn't collide.
    let result = cache.get(b"key_0");
    assert_eq!(result, Some(b"value".to_vec()), "key_0 retrieves value");

    // Test 5: verify zero false negatives — if cache has it, bloom says yes.
    {
        let cache_map = cache.cache.read().unwrap();
        for key in cache_map.keys() {
            assert!(cache.bloom.contains(key), "bloom contains all cached keys — zero false negatives");
        }
    }

    println!("bloom_backed_cache: bloom gate ensures zero false negatives — PASS");
}
