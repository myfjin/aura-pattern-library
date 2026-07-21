#![forbid(unsafe_code)]

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
// CLOCK (second-chance) page cache: each entry carries a reference bit; a hit sets the bit,
// and on a miss into a full cache a rotating hand clears set bits (granting a second chance)
// and evicts the first entry it finds already clear, inserting the new key there. Use as a
// low-overhead LRU approximation for a fixed-capacity cache.
// Guarantees the second-chance rule holds: a recently-accessed entry (ref bit set) is spared
// on the current sweep while an unreferenced entry is evicted, so a planted access trace
// yields deterministic, exactly-predictable eviction victims.
fn main() {
    // CLOCK cache: reference bit gives second chance.
    // Planted trace → exact eviction victims.

    #[derive(Clone, Debug)]
    struct ClockEntry {
        key: u32,
        ref_bit: bool,
    }

    struct ClockCache {
        entries: Vec<ClockEntry>,
        capacity: usize,
        hand: usize,
    }

    impl ClockCache {
        fn new(capacity: usize) -> Self {
            ClockCache {
                entries: Vec::new(),
                capacity,
                hand: 0,
            }
        }

        fn access(&mut self, key: u32) -> bool {
            // True = hit, False = miss
            for entry in &mut self.entries {
                if entry.key == key {
                    entry.ref_bit = true;
                    return true;
                }
            }
            // Miss: insert
            if self.entries.len() < self.capacity {
                self.entries.push(ClockEntry { key, ref_bit: true });
                return false;
            }

            // Evict via clock
            loop {
                if self.hand >= self.entries.len() {
                    self.hand = 0;
                }
                if self.entries[self.hand].ref_bit {
                    self.entries[self.hand].ref_bit = false;
                    self.hand += 1;
                } else {
                    // Evict this entry
                    let _ = self.entries.remove(self.hand);
                    self.entries.push(ClockEntry { key, ref_bit: true });
                    if self.hand >= self.entries.len() && self.entries.len() > 0 {
                        self.hand = 0;
                    }
                    return false;
                }
            }
        }
    }

    // Scenario 1: Basic eviction
    let mut clock = ClockCache::new(3);

    clock.access(1); // Miss
    clock.access(2); // Miss
    clock.access(3); // Miss

    assert_eq!(clock.entries.len(), 3);

    // Access 1 again (set ref bit)
    let hit = clock.access(1);
    assert!(hit);
    assert!(clock.entries.iter().find(|e| e.key == 1).map(|e| e.ref_bit).unwrap_or(false));

    // Scenario 2: Exact eviction sequence
    let mut clock2 = ClockCache::new(2);

    clock2.access(1); // Miss
    clock2.access(2); // Miss

    // Clear ref bits for deterministic eviction
    for entry in &mut clock2.entries {
        entry.ref_bit = false;
    }

    // Access 1 (set ref bit)
    clock2.access(1);

    // Access 3 (should evict 2, since 1 has ref bit)
    clock2.access(3);

    // Verify 2 is evicted
    assert!(!clock2.entries.iter().any(|e| e.key == 2));
    assert!(clock2.entries.iter().any(|e| e.key == 1));
    assert!(clock2.entries.iter().any(|e| e.key == 3));

    // Scenario 3: Reference bit behavior
    let mut clock3 = ClockCache::new(3);

    // Add 3 entries
    clock3.access(1);
    clock3.access(2);
    clock3.access(3);

    // Verify all 3 are in cache
    assert_eq!(clock3.entries.len(), 3);

    // Accessing an entry hits it
    let hit = clock3.access(1);
    assert!(hit);

    // Verify the entry with key 1 has ref bit set
    let has_ref = clock3.entries.iter().any(|e| e.key == 1 && e.ref_bit);
    assert!(has_ref);

    println!("clock_second_chance_cache: PASS");
}
