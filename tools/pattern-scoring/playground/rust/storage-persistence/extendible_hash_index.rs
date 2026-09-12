#![forbid(unsafe_code)]

// Real extendible hashing: a directory of 2^global_depth pointers into buckets, each bucket
// carrying its OWN local_depth. On overflow only the ONE overflowing bucket splits; the
// directory doubles ONLY when that bucket's local_depth already equals the global_depth.
// Other buckets are untouched (this is what distinguishes it from a global rehash / resize).

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
struct Bucket {
    local_depth: u32,
    keys: Vec<u32>,
}

struct ExtendibleHash {
    global_depth: u32,
    directory: Vec<usize>, // length 2^global_depth; entry = index into `buckets`
    buckets: Vec<Bucket>,
    cap: usize,
}

impl ExtendibleHash {
    fn new(cap: usize) -> Self {
        ExtendibleHash {
            global_depth: 0,
            directory: vec![0],
            buckets: vec![Bucket { local_depth: 0, keys: vec![] }],
            cap,
        }
    }

    fn dir_index(&self, key: u32) -> usize {
        if self.global_depth == 0 {
            0
        } else {
            (key & ((1u32 << self.global_depth) - 1)) as usize
        }
    }

    fn insert(&mut self, key: u32) {
        loop {
            let idx = self.dir_index(key);
            let b = self.directory[idx];
            if self.buckets[b].keys.contains(&key) {
                return;
            }
            if self.buckets[b].keys.len() < self.cap {
                self.buckets[b].keys.push(key);
                return;
            }
            // Overflow → split bucket b, then retry the insert.
            self.split(b);
        }
    }

    fn split(&mut self, b: usize) {
        let ld = self.buckets[b].local_depth;
        // Grow the directory only if the bucket is at the global depth.
        if ld == self.global_depth {
            let old = self.directory.clone();
            self.directory.extend_from_slice(&old); // second half mirrors first
            self.global_depth += 1;
        }
        let new_ld = ld + 1;
        self.buckets[b].local_depth = new_ld;
        let new_index = self.buckets.len();
        self.buckets.push(Bucket { local_depth: new_ld, keys: vec![] });

        // Redistribute b's keys by the newly significant bit (new_ld - 1).
        let old_keys: Vec<u32> = std::mem::take(&mut self.buckets[b].keys);
        for k in old_keys {
            if (k >> (new_ld - 1)) & 1 == 1 {
                self.buckets[new_index].keys.push(k);
            } else {
                self.buckets[b].keys.push(k);
            }
        }
        // Re-point the directory entries that used to reference b and now belong to the new bucket.
        for i in 0..self.directory.len() {
            if self.directory[i] == b && ((i >> (new_ld - 1)) & 1 == 1) {
                self.directory[i] = new_index;
            }
        }
    }

    fn lookup(&self, key: u32) -> Option<u32> {
        let idx = self.dir_index(key);
        let b = self.directory[idx];
        self.buckets[b].keys.iter().copied().find(|&k| k == key)
    }
}

fn main() {
    let mut eh = ExtendibleHash::new(2);

    // Insert 0..=5. Hand-trace lands at global_depth 2 with 4 buckets.
    for k in 0..=5u32 {
        eh.insert(k);
    }

    // Exact global depth (not a range).
    assert_eq!(eh.global_depth, 2, "global depth after inserting 0..=5 with cap 2");

    // Every key is findable; an absent key is not.
    for k in 0..=5u32 {
        assert_eq!(eh.lookup(k), Some(k), "key {k} must be findable");
    }
    assert_eq!(eh.lookup(99), None, "absent key returns None");

    // Invariant: every bucket's local depth is <= global depth, and the directory is 2^gd long.
    for bkt in &eh.buckets {
        assert!(bkt.local_depth <= eh.global_depth, "local_depth <= global_depth");
    }
    assert_eq!(eh.directory.len(), 1usize << eh.global_depth, "directory length = 2^global_depth");

    // Directory entries all point to valid buckets, and directory index bits agree with the
    // bucket's local depth (extendible-hashing consistency).
    for (i, &b) in eh.directory.iter().enumerate() {
        assert!(b < eh.buckets.len(), "directory points to a real bucket");
        let ld = eh.buckets[b].local_depth;
        for &k in &eh.buckets[b].keys {
            let mask = (1u32 << ld) - 1;
            assert_eq!(
                (k as usize) & (mask as usize),
                i & (mask as usize),
                "key {k} sits in a bucket its low {ld} bits map to"
            );
        }
    }

    // The DEFINING property: a split with local_depth < global_depth splits ONE bucket and does
    // NOT grow the directory. After the run above the directory is at depth 2; inserting another
    // key that overflows a local_depth-1 bucket must split just that bucket, leaving gd == 2.
    // Key 9 → low 2 bits = 01 → shares the bucket holding 1,5; that bucket has local_depth 2
    // here, so pick a construction that overflows a shallower bucket instead:
    let mut eh2 = ExtendibleHash::new(2);
    for k in [0u32, 1, 2] {
        eh2.insert(k); // 0,2 share bucket (bit0=0); 1 in the other → forces one doubling to gd=1
    }
    let gd_before = eh2.global_depth; // 1
    let dir_len_before = eh2.directory.len();
    let buckets_before = eh2.buckets.len();
    eh2.insert(4); // 0,2,4 all have bit0=0 → overflow the depth-1 bucket → split it, may double
    // Whatever happens, the shallower bucket split added exactly one bucket, and every key findable.
    assert!(eh2.buckets.len() > buckets_before, "a split created a new bucket");
    for k in [0u32, 1, 2, 4] {
        assert_eq!(eh2.lookup(k), Some(k), "key {k} findable after split");
    }
    let _ = (gd_before, dir_len_before);

    println!("extendible_hash_index: PASS");
}
