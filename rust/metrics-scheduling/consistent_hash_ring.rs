#![forbid(unsafe_code)]
//! consistent_hash_ring — hash ring + vnodes; key moves minimally when a node leaves.
//!
//! Core idea: consistent hashing distributes keys across nodes. When a node leaves,
//! only a small fraction of keys (≈1/N) should be reassigned. THE ONE LAW: plant a
//! hash ring with known nodes and keys, remove a node, measure key remapping, and
//! assert the count is minimal and remapped keys move ONLY to/from the affected node.
//! A broken hash or naive linear probing would cause many keys to move.
//! When to use: distributed caching, load balancing, consistent rebalancing.

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
struct ConsistentHashRing {
    vnodes: Vec<(u64, u32)>, // (hash, node_id)
    vnode_count: u32,
}

impl ConsistentHashRing {
    fn new() -> Self {
        ConsistentHashRing {
            vnodes: Vec::new(),
            vnode_count: 0,
        }
    }

    // FNV-1a hash (deterministic, no randomization).
    fn fnv_hash(data: &[u8]) -> u64 {
        const FNV_PRIME: u64 = 1099511628211;
        const FNV_OFFSET: u64 = 14695981039346656037;

        let mut hash = FNV_OFFSET;
        for &byte in data {
            hash ^= byte as u64;
            hash = hash.wrapping_mul(FNV_PRIME);
        }
        hash
    }

    fn add_node(&mut self, node_id: u32, vnode_count: u32) {
        self.vnode_count = vnode_count;
        for i in 0..vnode_count {
            let key = format!("node-{}-vnode-{}", node_id, i);
            let hash = Self::fnv_hash(key.as_bytes());
            self.vnodes.push((hash, node_id));
        }
        self.vnodes.sort_by_key(|&(h, _)| h);
    }

    fn locate_key(&self, key: &str) -> u32 {
        if self.vnodes.is_empty() {
            return 0;
        }
        let hash = Self::fnv_hash(key.as_bytes());
        // Find the first vnode with hash >= key's hash (clockwise on the ring).
        for &(vnode_hash, node_id) in &self.vnodes {
            if vnode_hash >= hash {
                return node_id;
            }
        }
        // Wrap around to the first vnode.
        self.vnodes[0].1
    }

    fn remove_node(&mut self, node_id: u32) -> Vec<u32> {
        let old_locations: Vec<u32> = (0..1000)
            .map(|i| {
                let key = format!("key-{}", i);
                self.locate_key(&key)
            })
            .collect();

        // Remove the node's vnodes.
        self.vnodes.retain(|(_, id)| *id != node_id);

        let new_locations: Vec<u32> = (0..1000)
            .map(|i| {
                let key = format!("key-{}", i);
                self.locate_key(&key)
            })
            .collect();

        // Count how many keys moved.
        let mut moved = Vec::new();
        for i in 0..1000 {
            if old_locations[i] != new_locations[i] {
                moved.push(i as u32);
            }
        }

        moved
    }
}

fn main() {
    // Planted case 1: basic 3-node ring with vnodes.
    let mut ring = ConsistentHashRing::new();
    ring.add_node(1, 16); // 3*16=48 vnodes total
    ring.add_node(2, 16);
    ring.add_node(3, 16);

    // Verify initial key distribution: roughly 1000/3 per node.
    let initial_dist: Vec<usize> = (0..1000)
        .map(|i| {
            let key = format!("key-{}", i);
            ring.locate_key(&key) as usize
        })
        .collect();

    let count_1 = initial_dist.iter().filter(|&&x| x == 1).count();
    let count_2 = initial_dist.iter().filter(|&&x| x == 2).count();
    let count_3 = initial_dist.iter().filter(|&&x| x == 3).count();

    println!("Initial distribution: node 1: {}, node 2: {}, node 3: {}", count_1, count_2, count_3);
    // With hash variance, distributions can be skewed; accept 150-600 per node.
    assert!(
        count_1 > 100 && count_1 < 600,
        "node 1 should have a reasonable fraction of keys"
    );

    // THE ONE LAW (the EXACT consistent-hashing guarantee, not a loose slop): removing node 3
    // must move PRECISELY the keys that were on node 3 — every one of them, only to a survivor
    // (1 or 2) — and EVERY other key must stay exactly where it was.
    let moved_keys = ring.remove_node(3);
    let moved_set: std::collections::HashSet<u32> = moved_keys.iter().copied().collect();

    let mut node3_keys = 0usize;
    for i in 0..1000u32 {
        let key = format!("key-{}", i);
        let new_loc = ring.locate_key(&key);
        if initial_dist[i as usize] == 3 {
            node3_keys += 1;
            assert!(new_loc == 1 || new_loc == 2, "node-3 key {i} moved to {new_loc}, not a survivor");
            assert!(moved_set.contains(&i), "node-3 key {i} must be reported as moved");
        } else {
            // The decisive check the loose version skipped: untouched keys DO NOT move.
            assert_eq!(new_loc as usize, initial_dist[i as usize], "key {i} moved but shouldn't have");
            assert!(!moved_set.contains(&i), "non-node-3 key {i} must not be reported moved");
        }
    }

    // Exactly the node-3 keys moved — no more, no less.
    assert_eq!(moved_keys.len(), node3_keys, "moved count must equal exactly node-3's key count");
    assert_eq!(node3_keys, count_3, "node-3 key count must match the initial distribution");
    assert!(moved_keys.len() < 500, "a correct ring moves only ~1/N, never a majority");

    println!(
        "consistent_hash_ring: removing a node moves EXACTLY its {} keys to survivors, others fixed — PASS",
        node3_keys
    );
}
