#![forbid(unsafe_code)]
// composes: cache-get + miss-load-from-backing + cache-fill + hit-skips-store + eviction

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
use std::collections::HashMap;

struct CacheStore {
    cache: HashMap<String, String>,
    backing: HashMap<String, String>,
    capacity: usize,
    load_count: usize,
}

impl CacheStore {
    fn new(capacity: usize) -> Self {
        let mut backing = HashMap::new();
        backing.insert("a".to_string(), "val-a".to_string());
        backing.insert("b".to_string(), "val-b".to_string());
        backing.insert("c".to_string(), "val-c".to_string());
        backing.insert("d".to_string(), "val-d".to_string());
        CacheStore {
            cache: HashMap::new(),
            backing,
            capacity,
            load_count: 0,
        }
    }

    fn get(&mut self, key: &str) -> Option<String> {
        // Stage 1: Check cache
        if let Some(val) = self.cache.get(key) {
            return Some(val.clone());
        }

        // Stage 2: Cache miss - load from backing store
        if let Some(val) = self.backing.get(key) {
            let val_clone = val.clone();

            // Stage 3: Fill cache (with eviction if over capacity)
            if self.cache.len() >= self.capacity {
                if let Some(first_key) = self.cache.keys().next().cloned() {
                    self.cache.remove(&first_key);
                }
            }

            self.cache.insert(key.to_string(), val_clone.clone());
            self.load_count += 1;
            return Some(val_clone);
        }

        None
    }
}

fn main() {
    // Stage 1: Create cache with limited capacity
    let mut store = CacheStore::new(2);

    // Stage 2: First access - miss
    let val_a = store.get("a");
    assert_eq!(val_a, Some("val-a".to_string()), "Get a succeeded");
    assert_eq!(store.load_count, 1, "One load from backing");
    let cache_size_1 = store.cache.len();
    assert_eq!(cache_size_1, 1, "Cache has 1 item");

    // Stage 3: Second access - miss
    let val_b = store.get("b");
    assert_eq!(val_b, Some("val-b".to_string()), "Get b succeeded");
    assert_eq!(store.load_count, 2, "Two loads from backing");
    let cache_size_2 = store.cache.len();
    assert_eq!(cache_size_2, 2, "Cache at capacity");

    // Stage 4: Hit (a should be in cache)
    let val_a_hit = store.get("a");
    assert_eq!(val_a_hit, Some("val-a".to_string()), "Hit on a");
    assert_eq!(store.load_count, 2, "No new load (cache hit)");

    // Stage 5: Third access - miss, triggers eviction (cache at capacity)
    let val_c = store.get("c");
    assert_eq!(val_c, Some("val-c".to_string()), "Get c succeeded");
    assert_eq!(store.load_count, 3, "Three loads total");
    let cache_size_3 = store.cache.len();
    assert_eq!(cache_size_3, 2, "Cache still at capacity after eviction");

    // Verify backing store still has all data
    let val_d = store.get("d");
    assert_eq!(val_d, Some("val-d".to_string()), "d still retrievable from backing");
    assert_eq!(store.load_count, 4, "Four loads total");

    println!("read_through_cache_store: PASS");
}
