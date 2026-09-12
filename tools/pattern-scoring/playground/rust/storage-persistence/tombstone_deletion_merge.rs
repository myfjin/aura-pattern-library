#![forbid(unsafe_code)]

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
// Tombstone-based deletion for LSM/SSTable merges. A delete writes a Tombstone marker
// rather than removing data; during a merge the newer level wins, so a tombstone masks an
// older value for the same key, and past the GC horizon both are dropped. Use it when
// deletes must propagate across immutable, layered sorted files.
// Guarantees the exact surviving set after compaction: masked keys disappear, updated keys
// keep their newest value, and a newer tombstone overrides an older value during a level merge.
fn main() {
    // Tombstone deletion: a tombstone masks an older value across a merge.
    // After GC horizon both are dropped; exact surviving set.

    #[derive(Clone, Debug, PartialEq, Eq)]
    enum VersionedValue {
        Value(String),
        Tombstone,
    }

    // Scenario 1: Insert, delete, merge
    let mut ss_table: std::collections::HashMap<String, VersionedValue> =
        std::collections::HashMap::new();

    // Initial table: key a → v1
    ss_table.insert("a".into(), VersionedValue::Value("v1".into()));
    ss_table.insert("b".into(), VersionedValue::Value("v2".into()));

    // Delete key a (add tombstone)
    ss_table.insert("a".into(), VersionedValue::Tombstone);

    // Now during GC/compaction: tombstone at "a" masks the old value "v1"
    // Both should be dropped after the GC horizon

    // Compacted (GC horizon passed): only live values remain
    let mut compacted: std::collections::HashMap<String, VersionedValue> =
        std::collections::HashMap::new();

    for (key, val) in &ss_table {
        // Skip tombstones during compaction (post-GC)
        if !matches!(val, VersionedValue::Tombstone) {
            compacted.insert(key.clone(), val.clone());
        }
    }

    // After GC: only "b" remains
    assert_eq!(compacted.len(), 1);
    assert_eq!(compacted.get("a"), None);
    assert_eq!(compacted.get("b"), Some(&VersionedValue::Value("v2".into())));

    // Scenario 2: Multiple inserts, deletes, exact set preservation
    let mut sstable: std::collections::HashMap<String, VersionedValue> =
        std::collections::HashMap::new();

    // Insert multiple keys
    sstable.insert("x".into(), VersionedValue::Value("x1".into()));
    sstable.insert("y".into(), VersionedValue::Value("y1".into()));
    sstable.insert("z".into(), VersionedValue::Value("z1".into()));

    // Delete "y"
    sstable.insert("y".into(), VersionedValue::Tombstone);

    // Update "x"
    sstable.insert("x".into(), VersionedValue::Value("x2".into()));

    // After GC compaction
    let mut compacted2: std::collections::HashMap<String, VersionedValue> =
        std::collections::HashMap::new();

    for (key, val) in &sstable {
        if !matches!(val, VersionedValue::Tombstone) {
            compacted2.insert(key.clone(), val.clone());
        }
    }

    // Exact surviving set: x→x2, z→z1 (y deleted)
    assert_eq!(compacted2.len(), 2);
    assert_eq!(compacted2.get("x"), Some(&VersionedValue::Value("x2".into())));
    assert_eq!(compacted2.get("y"), None);
    assert_eq!(compacted2.get("z"), Some(&VersionedValue::Value("z1".into())));

    // Scenario 3: Old value, tombstone, new value in same compaction
    // (simulating a merge of multiple levels)
    let mut level0: std::collections::HashMap<String, VersionedValue> =
        std::collections::HashMap::new();
    let mut level1: std::collections::HashMap<String, VersionedValue> =
        std::collections::HashMap::new();

    // Level1 (older): key "k" → "old_val"
    level1.insert("k".into(), VersionedValue::Value("old_val".into()));

    // Level0 (newer): key "k" → Tombstone (delete)
    level0.insert("k".into(), VersionedValue::Tombstone);

    // Merge: newer level wins; tombstone masks old value
    let mut merged: std::collections::HashMap<String, VersionedValue> =
        std::collections::HashMap::new();

    // Copy level1 first
    for (key, val) in &level1 {
        merged.insert(key.clone(), val.clone());
    }

    // Overlay level0 (newer)
    for (key, val) in &level0 {
        if matches!(val, VersionedValue::Tombstone) {
            merged.remove(key);
        } else {
            merged.insert(key.clone(), val.clone());
        }
    }

    // After merge: key "k" is gone (tombstone won)
    assert_eq!(merged.get("k"), None);

    // Scenario 4: Compaction exactly preserves live state
    let mut sst: std::collections::HashMap<String, VersionedValue> =
        std::collections::HashMap::new();

    sst.insert("a".into(), VersionedValue::Value("v1".into()));
    sst.insert("b".into(), VersionedValue::Value("v2".into()));
    sst.insert("c".into(), VersionedValue::Value("v3".into()));
    sst.insert("a".into(), VersionedValue::Tombstone); // Delete "a"

    let mut live_set: std::collections::HashMap<String, VersionedValue> =
        std::collections::HashMap::new();

    for (key, val) in &sst {
        if !matches!(val, VersionedValue::Tombstone) {
            live_set.insert(key.clone(), val.clone());
        }
    }

    // Exact surviving keys: b, c
    let live_keys: std::collections::HashSet<_> = live_set.keys().cloned().collect();
    assert_eq!(live_keys.len(), 2);
    assert!(live_keys.contains("b"));
    assert!(live_keys.contains("c"));
    assert!(!live_keys.contains("a"));

    println!("tombstone_deletion_merge: PASS");
}
