#![forbid(unsafe_code)]

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
// Insert-with-split for a single B-tree node: keys are kept sorted on insert, and when a
// node exceeds max_keys it splits at the median, returning (median_key, right_node) so the
// caller can promote the median into the parent. Use as the core rebalancing step when
// building a B-tree of a chosen branching factor.
// Guarantees the split invariants that make the tree valid: both halves stay sorted and
// within max_keys, every left key is < median and every right key is > median, and no key
// is lost across the split (the promoted median plus both halves account for all keys).
fn main() {
    // B-tree node split: insert until overflow, split.
    // Assert sorted-keys + fanout bounds, median promoted.

    // Simulate a B-tree node: max 4 keys (branching factor 5)
    #[derive(Clone, Debug, PartialEq, Eq)]
    struct Node {
        keys: Vec<u32>,
    }

    impl Node {
        fn new() -> Self {
            Node { keys: vec![] }
        }

        fn insert(&mut self, key: u32, max_keys: usize) -> Option<(u32, Node)> {
            // Insert into sorted position
            let pos = self.keys.iter().position(|&k| k > key).unwrap_or(self.keys.len());
            self.keys.insert(pos, key);

            // Check if split needed
            if self.keys.len() > max_keys {
                // Split at median
                let mid = self.keys.len() / 2;
                let median = self.keys[mid];
                let right_keys: Vec<u32> = self.keys.drain((mid + 1)..).collect();

                self.keys.truncate(mid);

                let right_node = Node { keys: right_keys };

                // Assert invariants
                assert!(self.keys.is_sorted());
                assert!(right_node.keys.is_sorted());
                assert!(self.keys.len() <= max_keys);
                assert!(right_node.keys.len() <= max_keys);
                assert_eq!(self.keys.iter().all(|&k| k < median), true);
                assert_eq!(right_node.keys.iter().all(|&k| k > median), true);

                Some((median, right_node))
            } else {
                assert!(self.keys.is_sorted());
                None
            }
        }
    }

    // Scenario 1: Insert until split
    let max_keys = 4;
    let mut node = Node::new();

    // Insert keys: 10, 20, 30, 40 (fills node)
    assert_eq!(node.insert(10, max_keys), None);
    assert_eq!(node.insert(20, max_keys), None);
    assert_eq!(node.insert(30, max_keys), None);
    assert_eq!(node.insert(40, max_keys), None);

    assert!(node.keys.is_sorted());
    assert_eq!(node.keys.len(), 4);

    // Insert 50 causes split
    if let Some((median, right)) = node.insert(50, max_keys) {
        assert_eq!(median, 30);
        assert_eq!(node.keys, vec![10, 20]);
        assert_eq!(right.keys, vec![40, 50]);
        assert!(node.keys.is_sorted());
        assert!(right.keys.is_sorted());
    } else {
        panic!("Expected split");
    }

    // Scenario 2: Split preserves all keys in node
    let mut node2 = Node::new();
    let keys_to_insert = vec![10, 20, 30, 40];

    for &k in &keys_to_insert {
        let _ = node2.insert(k, max_keys);
    }

    // After 4 inserts, node2 should have all 4 keys
    assert_eq!(node2.keys.len(), 4);
    assert!(node2.keys.is_sorted());

    // Insert 5th key (causes split)
    if let Some((median, right)) = node2.insert(35, max_keys) {
        // After split: node2 has left keys, right has right keys, median is promoted
        // Verify no keys lost (count median too)
        let mut all_keys = node2.keys.clone();
        all_keys.push(median);
        all_keys.extend(right.keys.clone());
        all_keys.sort();
        // Should have 5 distinct keys total
        assert_eq!(all_keys.len(), 5);
    } else {
        panic!("Expected split");
    }

    // Scenario 3: Duplicate keys
    let mut node3 = Node::new();
    node3.insert(10, max_keys);
    node3.insert(20, max_keys);
    node3.insert(10, max_keys); // Insert same key again
    node3.insert(30, max_keys);

    assert!(node3.keys.is_sorted());

    println!("btree_node_split: PASS");
}
