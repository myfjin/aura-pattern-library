#![forbid(unsafe_code)]

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
fn main() {
    // Double-write buffer: write page to buffer first, then to home.
    // Crash mid-home-write → recover full page from buffer.

    // Model: double-write buffer and main storage
    let mut dwb: std::collections::HashMap<u64, Vec<u8>> = std::collections::HashMap::new();
    let mut storage: std::collections::HashMap<u64, Vec<u8>> = std::collections::HashMap::new();

    // Initial state
    storage.insert(1, b"page1_v1".to_vec());
    storage.insert(2, b"page2_v1".to_vec());

    // Scenario 1: Successful write (no crash)
    let new_page_data = b"page1_v2".to_vec();

    // Step 1: Write to DWB
    dwb.insert(1, new_page_data.clone());

    // Step 2: Write to storage (atomic in this model)
    storage.insert(1, new_page_data.clone());

    // Step 3: Clear DWB (log compaction)
    dwb.remove(&1);

    // Assert: storage has new data, DWB is empty
    assert_eq!(storage.get(&1), Some(&b"page1_v2".to_vec()));
    assert_eq!(dwb.get(&1), None);

    // Scenario 2: Crash DURING home-write (after DWB, before storage fully written)
    let mut dwb2: std::collections::HashMap<u64, Vec<u8>> = std::collections::HashMap::new();
    let mut storage2: std::collections::HashMap<u64, Vec<u8>> = std::collections::HashMap::new();
    storage2.insert(1, b"page1_v1".to_vec());

    // Write to DWB
    let new_data = b"page1_v2".to_vec();
    dwb2.insert(1, new_data.clone());

    // CRASH DURING storage write (page half-written, invalid state)
    // Do NOT update storage in this scenario
    // Simulate a half-written page
    storage2.insert(1, b"pa".to_vec()); // Corrupted

    // After crash + recovery: replay from DWB
    if let Some(valid_page) = dwb2.get(&1) {
        storage2.insert(1, valid_page.clone());
    }

    // Assert: storage is recovered to the full, valid page
    assert_eq!(storage2.get(&1), Some(&b"page1_v2".to_vec()));

    // Scenario 3: Crash AFTER storage write but before DWB clear
    let mut dwb3: std::collections::HashMap<u64, Vec<u8>> = std::collections::HashMap::new();
    let mut storage3: std::collections::HashMap<u64, Vec<u8>> = std::collections::HashMap::new();
    storage3.insert(1, b"page1_v1".to_vec());

    // Write to DWB
    let new_data3 = b"page1_v3".to_vec();
    dwb3.insert(1, new_data3.clone());

    // Write to storage succeeds
    storage3.insert(1, new_data3.clone());

    // CRASH before DWB clear
    // DWB still contains the page

    // After crash + recovery:
    // - Storage has the new data (write was complete)
    // - DWB has a copy (for safety, can be cleared on next startup)
    assert_eq!(storage3.get(&1), Some(&b"page1_v3".to_vec()));
    assert_eq!(dwb3.get(&1), Some(&b"page1_v3".to_vec()));

    // Cleanup DWB
    dwb3.remove(&1);
    assert_eq!(dwb3.get(&1), None);

    // Scenario 4: Multiple pages
    let mut dwb4: std::collections::HashMap<u64, Vec<u8>> = std::collections::HashMap::new();
    let mut storage4: std::collections::HashMap<u64, Vec<u8>> = std::collections::HashMap::new();
    storage4.insert(1, b"v1".to_vec());
    storage4.insert(2, b"v1".to_vec());

    // Update page 1 and 2
    dwb4.insert(1, b"v2".to_vec());
    dwb4.insert(2, b"v2".to_vec());

    // Crash mid-write: only page 1 written
    storage4.insert(1, b"v2".to_vec());
    storage4.insert(2, b"halfway".to_vec()); // Corrupted

    // Recovery: restore both from DWB
    for (id, data) in &dwb4 {
        storage4.insert(*id, data.clone());
    }

    assert_eq!(storage4.get(&1), Some(&b"v2".to_vec()));
    assert_eq!(storage4.get(&2), Some(&b"v2".to_vec()));

    println!("double_write_buffer: PASS");
}
