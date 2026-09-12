#![forbid(unsafe_code)]
//! lsm_memtable_flush — memtable flushes to immutable sstable; merged read returns newest.
//!
//! Core idea: an in-memory sorted map (memtable) accumulates writes. When full, it flushes
//! to an immutable sorted table (sstable). A read checks memtable first (newest), then
//! sstable. THE LAW: write, read from memtable, flush, read from sstable, and assert
//! the read always returns the newest version of a key.
//! When to use: LSM trees, log-structured storage, RocksDB-like systems.

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
use std::collections::BTreeMap;

struct MemTable {
    data: BTreeMap<u32, u32>,
    max_size: usize,
}

impl MemTable {
    fn new(max_size: usize) -> Self {
        MemTable {
            data: BTreeMap::new(),
            max_size,
        }
    }

    fn insert(&mut self, key: u32, value: u32) {
        self.data.insert(key, value);
    }

    fn is_full(&self) -> bool {
        self.data.len() >= self.max_size
    }

    fn flush(&mut self) -> BTreeMap<u32, u32> {
        let mut new_data = BTreeMap::new();
        std::mem::swap(&mut self.data, &mut new_data);
        new_data
    }

    fn get(&self, key: u32) -> Option<u32> {
        self.data.get(&key).copied()
    }
}

struct LSMStore {
    memtable: MemTable,
    sstables: Vec<BTreeMap<u32, u32>>,
}

impl LSMStore {
    fn new(max_memtable_size: usize) -> Self {
        LSMStore {
            memtable: MemTable::new(max_memtable_size),
            sstables: Vec::new(),
        }
    }

    fn insert(&mut self, key: u32, value: u32) {
        self.memtable.insert(key, value);
        if self.memtable.is_full() {
            let flushed = self.memtable.flush();
            self.sstables.push(flushed);
        }
    }

    fn get(&self, key: u32) -> Option<u32> {
        // Check memtable first (newest).
        if let Some(v) = self.memtable.get(key) {
            return Some(v);
        }

        // Check sstables in reverse order (newest first).
        for sstable in self.sstables.iter().rev() {
            if let Some(v) = sstable.get(&key) {
                return Some(*v);
            }
        }

        None
    }
}

fn main() {
    // Test 1: insert, read from memtable.
    let mut store = LSMStore::new(3);
    store.insert(1, 10);
    store.insert(2, 20);
    assert_eq!(store.get(1), Some(10));
    assert_eq!(store.get(2), Some(20));

    // Test 2: flush and read from sstable.
    store.insert(3, 30); // memtable full, triggers flush
    assert_eq!(store.get(1), Some(10), "read from sstable");
    assert_eq!(store.get(2), Some(20), "read from sstable");
    assert_eq!(store.get(3), Some(30), "read from memtable");

    // Test 3: update in memtable shadows sstable.
    store.insert(1, 100); // Update 1 in memtable
    assert_eq!(store.get(1), Some(100), "memtable version shadows");

    // Test 4: flush again, read from newer sstable.
    store.insert(4, 40);
    store.insert(5, 50);
    store.insert(6, 60); // Flush 2
    assert_eq!(store.get(1), Some(100), "read from sstable");
    assert_eq!(store.get(4), Some(40), "read from sstable");

    // Test 5: key not in store.
    assert_eq!(store.get(999), None);

    println!("lsm_memtable_flush: read returns newest version — PASS");
}
