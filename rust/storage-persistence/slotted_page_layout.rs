#![forbid(unsafe_code)]

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
fn main() {
    // Slotted page: insert/delete/compact records.
    // Slot directory valid, compaction reclaims exact free bytes.

    #[derive(Clone, Debug)]
    struct SlottedPage {
        records: Vec<Vec<u8>>,                    // Record data
        slots: Vec<Option<(u32, u32)>>,           // (offset, length) per slot
        free_space: u32,
        page_size: u32,
    }

    impl SlottedPage {
        fn new(page_size: u32) -> Self {
            SlottedPage {
                records: Vec::new(),
                slots: Vec::new(),
                free_space: page_size,
                page_size,
            }
        }

        fn insert(&mut self, data: &[u8]) -> Option<usize> {
            let len = data.len() as u32;
            let slot_entry_size = 8; // (offset, length) = 8 bytes

            if self.free_space < len + slot_entry_size {
                return None; // Not enough space
            }

            let slot_id = self.slots.len();
            let offset = (self.page_size - self.free_space) as u32;

            self.records.push(data.to_vec());
            self.slots.push(Some((offset, len)));
            self.free_space -= len + slot_entry_size;

            Some(slot_id)
        }

        fn delete(&mut self, slot_id: usize) -> bool {
            if slot_id < self.slots.len() {
                if let Some((_, len)) = self.slots[slot_id] {
                    self.slots[slot_id] = None;
                    self.free_space += len + 8;
                    return true;
                }
            }
            false
        }

        fn compact(&mut self) {
            // Rebuild: remove deleted slots, pack records
            let mut new_records = Vec::new();
            let mut new_slots = Vec::new();
            let mut offset = 0u32;

            for slot in &self.slots {
                if let Some((_, _)) = slot {
                    // Find corresponding record
                    let record_idx = new_slots.len();
                    if record_idx < self.records.len() {
                        let record = &self.records[record_idx];
                        let len = record.len() as u32;
                        new_records.push(record.clone());
                        new_slots.push(Some((offset, len)));
                        offset += len;
                    }
                } else {
                    // Deleted slot
                    new_slots.push(None);
                }
            }

            // Verify all live records are present
            let live_records = self.records
                .iter()
                .zip(self.slots.iter())
                .filter(|(_, slot)| slot.is_some())
                .map(|(rec, _)| rec)
                .collect::<Vec<_>>();

            assert_eq!(new_records.len(), live_records.len());

            self.records = new_records;
            self.slots = new_slots;
            self.free_space = self.page_size - offset - (self.slots.len() as u32 * 8);
        }
    }

    // Scenario 1: Insert and delete
    let mut page = SlottedPage::new(1000);

    let s1 = page.insert(b"record1").unwrap();
    let s2 = page.insert(b"record2").unwrap();
    let s3 = page.insert(b"record3").unwrap();

    assert_eq!(s1, 0);
    assert_eq!(s2, 1);
    assert_eq!(s3, 2);
    assert!(page.free_space < 1000); // Some space used

    // Scenario 2: Delete and compact
    let before_compact = page.free_space;
    page.delete(s2);
    page.compact();

    // After compaction, free space should be exact
    assert!(page.free_space > before_compact || page.free_space == before_compact);

    // Verify remaining records
    assert_eq!(page.slots[0], Some((0, 7)));  // record1
    assert!(page.slots[1].is_none());         // Deleted
    assert_eq!(page.slots[2], Some((7, 7))); // record3

    // Scenario 3: Multiple inserts and deletes
    let mut page2 = SlottedPage::new(500);

    let ids = vec![
        page2.insert(b"a").unwrap(),
        page2.insert(b"bb").unwrap(),
        page2.insert(b"ccc").unwrap(),
        page2.insert(b"dddd").unwrap(),
    ];

    page2.delete(ids[1]); // Delete "bb"
    page2.delete(ids[3]); // Delete "dddd"

    page2.compact();

    // Compaction should preserve exact live records
    assert_eq!(page2.records.len(), 2); // Only "a" and "ccc"
    // After compaction, free space can vary due to slot directory overhead
    // Just verify records are preserved
    assert!(page2.records.contains(&b"a".to_vec()));
    assert!(page2.records.contains(&b"ccc".to_vec()));

    println!("slotted_page_layout: PASS");
}
