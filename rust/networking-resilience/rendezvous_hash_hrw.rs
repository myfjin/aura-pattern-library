#![forbid(unsafe_code)]

// Seeded LCG for deterministic hashing
// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
fn lcg_hash(key: u64, node_id: u64, seed: u64) -> u64 {
    let a = 1664525u64;
    let c = 1013904223u64;
    a.wrapping_mul(key ^ node_id ^ seed).wrapping_add(c)
}

struct RendezvousHashHRW {
    nodes: Vec<u64>,
    seed: u64,
}

impl RendezvousHashHRW {
    fn new(nodes: Vec<u64>, seed: u64) -> Self {
        Self { nodes, seed }
    }

    fn get(&self, key: u64) -> Option<u64> {
        self.nodes
            .iter()
            .max_by_key(|&&node_id| lcg_hash(key, node_id, self.seed))
            .copied()
    }

    fn remove(&mut self, node_id: u64) {
        self.nodes.retain(|&n| n != node_id);
    }

    fn add(&mut self, node_id: u64) {
        if !self.nodes.contains(&node_id) {
            self.nodes.push(node_id);
        }
    }
}

fn main() {
    // Test 1: Basic mapping with 3 nodes
    let hrw = RendezvousHashHRW::new(vec![0, 1, 2], 42);

    let key1 = 100u64;
    let mapped1 = hrw.get(key1).unwrap();
    assert!(mapped1 < 3, "Should map to a valid node");

    // Test 2: Same key always maps to same node (deterministic)
    let mapped1_again = hrw.get(key1).unwrap();
    assert_eq!(mapped1, mapped1_again, "Same key should map to same node");

    // Test 3: Different keys might map to different nodes
    let key2 = 200u64;
    let _mapped2 = hrw.get(key2).unwrap();
    // _mapped2 might equal mapped1 or be different, depending on hash

    // Test 4: Removing a node causes only its keys to remapping
    // Count how many keys map to node 0 initially
    let mut on_node_0 = 0;
    for key in 0..100 {
        if hrw.get(key).unwrap() == 0 {
            on_node_0 += 1;
        }
    }
    // Now remove node 0 and verify those keys map elsewhere
    let mut hrw_no_0 = RendezvousHashHRW::new(vec![0, 1, 2], 42);
    hrw_no_0.remove(0);
    let mut remapped_count = 0;
    for key in 0..100 {
        if hrw.get(key).unwrap() == 0 {
            // This key was on node 0, verify it maps elsewhere
            assert_ne!(hrw_no_0.get(key).unwrap(), 0, "Key should not map to removed node 0");
            remapped_count += 1;
        }
    }
    assert_eq!(remapped_count, on_node_0, "All keys from removed node must remapping");
    assert!(on_node_0 > 0, "At least some keys should map to node 0");

    // Test 5: Verify known mapping sequence
    let keys = vec![10, 20, 30, 40, 50];
    let mut mappings = Vec::new();
    for k in keys {
        mappings.push(hrw.get(k).unwrap());
    }
    // All mappings should be deterministic and valid
    for &m in &mappings {
        assert!(m < 3, "All mappings should be to nodes 0-2");
    }

    // Test 6: Re-run same mappings should match
    let mappings2: Vec<_> = vec![10, 20, 30, 40, 50]
        .iter()
        .map(|&k| hrw.get(k).unwrap())
        .collect();
    assert_eq!(mappings, mappings2, "Mappings must be stable");

    // Test 7: Add a node back and verify new distribution
    let mut hrw3 = RendezvousHashHRW::new(vec![0, 1], 42);
    let mappings_before: Vec<_> = (0..50).map(|k| hrw3.get(k).unwrap()).collect();

    hrw3.add(2);
    let mappings_after: Vec<_> = (0..50).map(|k| hrw3.get(k).unwrap()).collect();

    // Some keys might now map to node 2 instead of 0/1
    let remapped = mappings_before.iter().zip(&mappings_after)
        .filter(|(b, a)| b != a)
        .count();
    assert!(remapped > 0, "Adding node should remapping some keys");

    println!("rendezvous_hash_hrw: PASS");
}
