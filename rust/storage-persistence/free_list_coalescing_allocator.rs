#![forbid(unsafe_code)]

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
// Free-list allocator with adjacent-block coalescing. allocate() first-fits a block
// and splits off the remainder; free() returns a block and immediately merges it with
// any physically adjacent free blocks (sort by offset, join where end == next start).
// Use it to manage fixed-region space (page/heap offsets) while resisting fragmentation.
// Guarantees: total free bytes are conserved across alloc/free, and freeing the pieces
// of a contiguous region coalesces them back into a single block of the exact merged size.
fn main() {
    // Free-list allocator with coalescing.
    // Adjacent free blocks merge; exact merged block size.

    #[derive(Clone, Debug, PartialEq, Eq)]
    struct FreeBlock {
        offset: u32,
        size: u32,
    }

    struct FreeListAllocator {
        free_list: Vec<FreeBlock>,
    }

    impl FreeListAllocator {
        fn new() -> Self {
            FreeListAllocator { free_list: vec![] }
        }

        fn allocate(&mut self, size: u32) -> Option<u32> {
            // Find first free block large enough
            for (i, block) in self.free_list.iter().enumerate() {
                if block.size >= size {
                    let allocated_offset = block.offset;
                    let remaining = block.size - size;

                    if remaining == 0 {
                        self.free_list.remove(i);
                    } else {
                        self.free_list[i] = FreeBlock {
                            offset: block.offset + size,
                            size: remaining,
                        };
                    }

                    return Some(allocated_offset);
                }
            }

            None
        }

        fn free(&mut self, offset: u32, size: u32) {
            self.free_list.push(FreeBlock { offset, size });
            self.coalesce();
        }

        fn coalesce(&mut self) {
            // Sort by offset and merge adjacent blocks
            self.free_list.sort_by_key(|b| b.offset);

            let mut i = 0;
            while i + 1 < self.free_list.len() {
                let current_end = self.free_list[i].offset + self.free_list[i].size;
                let next_start = self.free_list[i + 1].offset;

                if current_end == next_start {
                    // Adjacent blocks: merge
                    let merged_size = self.free_list[i].size + self.free_list[i + 1].size;
                    self.free_list[i].size = merged_size;
                    self.free_list.remove(i + 1);
                } else {
                    i += 1;
                }
            }
        }

        fn total_free(&self) -> u32 {
            self.free_list.iter().map(|b| b.size).sum()
        }
    }

    // Scenario 1: Alloc and free, coalesce
    let mut alloc = FreeListAllocator::new();
    alloc.free(0, 100);

    assert_eq!(alloc.total_free(), 100);

    // Allocate 30 bytes from [0, 100)
    let addr1 = alloc.allocate(30).unwrap();
    assert_eq!(addr1, 0);

    // Free list now has [30, 70)
    assert_eq!(alloc.total_free(), 70);

    // Allocate another 20 bytes
    let addr2 = alloc.allocate(20).unwrap();
    assert_eq!(addr2, 30);

    // Free list now has [50, 50)
    assert_eq!(alloc.total_free(), 50);

    // Scenario 2: Adjacent free blocks coalesce
    let mut alloc2 = FreeListAllocator::new();
    alloc2.free(0, 100);

    let a = alloc2.allocate(30).unwrap();  // [0, 30)
    let b = alloc2.allocate(20).unwrap();  // [30, 50)
    let c = alloc2.allocate(50).unwrap();  // [50, 100)

    // Free list is empty (all allocated)
    assert_eq!(alloc2.total_free(), 0);

    // Free first and last
    alloc2.free(a, 30);  // Free [0, 30)
    alloc2.free(c, 50);  // Free [50, 100)

    // After coalesce: two free blocks [0, 30) and [50, 100)
    // Total = 80
    assert_eq!(alloc2.total_free(), 80);

    // Now free the middle [30, 20)
    alloc2.free(b, 20);

    // Should coalesce all into [0, 100) = 100
    assert_eq!(alloc2.total_free(), 100);

    // Scenario 3: Exact merged block size
    let mut alloc3 = FreeListAllocator::new();

    alloc3.free(0, 50);
    alloc3.free(50, 50);

    // After coalesce, should be one block of size 100
    assert_eq!(alloc3.free_list.len(), 1);
    assert_eq!(alloc3.free_list[0].size, 100);
    assert_eq!(alloc3.free_list[0].offset, 0);

    // Scenario 4: No double-free fragmentation
    let mut alloc4 = FreeListAllocator::new();
    alloc4.free(0, 30);
    alloc4.free(30, 30);
    alloc4.free(60, 40);

    // After coalesce: single block [0, 100)
    assert_eq!(alloc4.free_list.len(), 1);
    assert_eq!(alloc4.free_list[0].size, 100);

    println!("free_list_coalescing_allocator: PASS");
}
