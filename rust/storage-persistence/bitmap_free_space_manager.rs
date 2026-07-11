#![forbid(unsafe_code)]

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
fn main() {
    // Bitmap free-space manager: alloc/free via bitmap.
    // No double-allocate, exact free count.

    struct BitmapAllocator {
        bitmap: Vec<bool>, // true = allocated, false = free
        free_count: usize,
    }

    impl BitmapAllocator {
        fn new(capacity: usize) -> Self {
            BitmapAllocator {
                bitmap: vec![false; capacity],
                free_count: capacity,
            }
        }

        fn allocate(&mut self) -> Option<usize> {
            for (i, &allocated) in self.bitmap.iter().enumerate() {
                if !allocated {
                    self.bitmap[i] = true;
                    self.free_count -= 1;
                    return Some(i);
                }
            }
            None
        }

        fn free(&mut self, addr: usize) -> bool {
            if addr < self.bitmap.len() && self.bitmap[addr] {
                self.bitmap[addr] = false;
                self.free_count += 1;
                true
            } else {
                false
            }
        }

        fn free_blocks(&self) -> usize {
            self.free_count
        }

        fn is_allocated(&self, addr: usize) -> bool {
            addr < self.bitmap.len() && self.bitmap[addr]
        }
    }

    // Scenario 1: Alloc and free, no double-allocate
    let mut alloc = BitmapAllocator::new(10);

    let addr1 = alloc.allocate().unwrap();
    let addr2 = alloc.allocate().unwrap();
    let addr3 = alloc.allocate().unwrap();

    assert_eq!(addr1, 0);
    assert_eq!(addr2, 1);
    assert_eq!(addr3, 2);
    assert_eq!(alloc.free_blocks(), 7);

    // No double-allocate: addr1 is already allocated
    assert!(alloc.is_allocated(addr1));
    assert!(alloc.is_allocated(addr2));

    // Free and reallocate
    assert!(alloc.free(addr1));
    assert_eq!(alloc.free_blocks(), 8);

    let realloc = alloc.allocate().unwrap();
    assert_eq!(realloc, 0); // Should reuse addr1
    assert_eq!(alloc.free_blocks(), 7);

    // Scenario 2: Exact free count
    let mut alloc2 = BitmapAllocator::new(5);
    assert_eq!(alloc2.free_blocks(), 5);

    alloc2.allocate();
    assert_eq!(alloc2.free_blocks(), 4);

    alloc2.allocate();
    assert_eq!(alloc2.free_blocks(), 3);

    alloc2.allocate();
    assert_eq!(alloc2.free_blocks(), 2);

    alloc2.free(0);
    assert_eq!(alloc2.free_blocks(), 3);

    // Scenario 3: Planted sequence, exact recovery
    let mut alloc3 = BitmapAllocator::new(8);

    let _a = alloc3.allocate().unwrap(); // 0
    let b = alloc3.allocate().unwrap(); // 1
    let _c = alloc3.allocate().unwrap(); // 2

    alloc3.free(b); // Free middle block
    let b_new = alloc3.allocate().unwrap(); // Should reuse 1

    assert_eq!(b_new, 1);
    assert_eq!(alloc3.free_blocks(), 5); // 8 - 3 allocated

    // Scenario 4: No over-free
    let mut alloc4 = BitmapAllocator::new(4);

    let x = alloc4.allocate().unwrap();
    let y = alloc4.allocate().unwrap();

    assert!(alloc4.free(x));
    assert!(alloc4.free(y));

    // Double-free should fail
    assert!(!alloc4.free(x)); // Already free
    assert_eq!(alloc4.free_blocks(), 4);

    println!("bitmap_free_space_manager: PASS");
}
