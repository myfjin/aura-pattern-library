#![forbid(unsafe_code)]

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
// SSTable sparse block index. Stores one (first_key, block_offset) boundary per block over
// a sorted key space; find_block(key) returns the rightmost block whose first_key <= key.
// Use it to locate the single block a key must live in without indexing every key.
// Guarantees a correct block for both present and absent keys: an absent key routes to the
// block that would contain it, exact boundary keys map to their own block, and a key below
// the first boundary returns None (no block can hold it).
fn main() {
    // SSTable block index: sparse index over sorted keys.
    // seek(key) returns correct block for present AND absent keys.

    #[derive(Clone, Debug)]
    struct BlockIndex {
        block_boundaries: Vec<(u32, usize)>, // (first_key, block_offset)
    }

    impl BlockIndex {
        fn new() -> Self {
            BlockIndex { block_boundaries: vec![] }
        }

        fn add_block(&mut self, first_key: u32, offset: usize) {
            self.block_boundaries.push((first_key, offset));
        }

        fn find_block(&self, key: u32) -> Option<usize> {
            // Binary search for the block containing key
            // Find the rightmost block whose first_key <= key
            let mut result = None;
            for &(first_key, offset) in &self.block_boundaries {
                if first_key <= key {
                    result = Some(offset);
                } else {
                    break;
                }
            }
            result
        }
    }

    // Scenario 1: Present and absent keys
    let mut index = BlockIndex::new();

    // Block 0: keys 1-10
    index.add_block(1, 0);
    // Block 1: keys 11-20
    index.add_block(11, 1);
    // Block 2: keys 21-30
    index.add_block(21, 2);

    // Present key
    assert_eq!(index.find_block(5), Some(0));
    assert_eq!(index.find_block(15), Some(1));
    assert_eq!(index.find_block(25), Some(2));

    // Absent key (but should point to block it would be in)
    assert_eq!(index.find_block(8), Some(0));  // Between 1 and 11
    assert_eq!(index.find_block(12), Some(1)); // Between 11 and 21
    assert_eq!(index.find_block(35), Some(2)); // Beyond 21

    // Scenario 2: Keys before first block
    assert_eq!(index.find_block(0), None); // Before block 0

    // Scenario 3: Dense index with single-key blocks
    let mut index2 = BlockIndex::new();
    for i in (1..=100).step_by(10) {
        index2.add_block(i as u32, (i / 10) as usize);
    }

    assert_eq!(index2.find_block(5), Some(0));
    assert_eq!(index2.find_block(45), Some(4));
    assert_eq!(index2.find_block(99), Some(9));

    // Scenario 4: Exact boundary keys
    let mut index3 = BlockIndex::new();
    index3.add_block(10, 0);
    index3.add_block(20, 1);
    index3.add_block(30, 2);

    assert_eq!(index3.find_block(10), Some(0));
    assert_eq!(index3.find_block(20), Some(1));
    assert_eq!(index3.find_block(30), Some(2));
    assert_eq!(index3.find_block(9), None);

    println!("sstable_block_index: PASS");
}
