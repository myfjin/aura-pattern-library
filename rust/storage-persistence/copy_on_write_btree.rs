#![forbid(unsafe_code)]

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
use std::sync::Arc;

// Copy-on-write tree with STRUCTURAL SHARING — the point of COW, not eager whole-tree cloning.
// An update copies ONLY the nodes on the path from the root to the changed key; every subtree
// off that path is SHARED with the old version (same Arc allocation). The old root remains a
// valid, immutable snapshot. We prove the sharing with Arc::ptr_eq, and immutability by reading
// the old root after the update.

#[derive(Debug)]
struct Node {
    key: u32,
    val: String,
    left: Option<Arc<Node>>,
    right: Option<Arc<Node>>,
}

fn leaf(key: u32, val: &str) -> Arc<Node> {
    Arc::new(Node { key, val: val.into(), left: None, right: None })
}

fn branch(key: u32, val: &str, left: Option<Arc<Node>>, right: Option<Arc<Node>>) -> Arc<Node> {
    Arc::new(Node { key, val: val.into(), left, right })
}

// Return a new tree with `key`'s value replaced. Nodes NOT on the root→key path are shared
// (their Arc is cloned = same allocation, not deep-copied).
fn cow_update(node: &Arc<Node>, key: u32, new_val: &str) -> Arc<Node> {
    if key == node.key {
        // Copy this node; its children are unchanged → share them.
        Arc::new(Node {
            key: node.key,
            val: new_val.into(),
            left: node.left.clone(),
            right: node.right.clone(),
        })
    } else if key < node.key {
        // Recurse left; the RIGHT subtree is untouched → shared.
        let new_left = node.left.as_ref().map(|l| cow_update(l, key, new_val));
        Arc::new(Node {
            key: node.key,
            val: node.val.clone(),
            left: new_left,
            right: node.right.clone(),
        })
    } else {
        // Recurse right; the LEFT subtree is untouched → shared.
        let new_right = node.right.as_ref().map(|r| cow_update(r, key, new_val));
        Arc::new(Node {
            key: node.key,
            val: node.val.clone(),
            left: node.left.clone(),
            right: new_right,
        })
    }
}

fn lookup(node: &Arc<Node>, key: u32) -> Option<&str> {
    if key == node.key {
        Some(&node.val)
    } else if key < node.key {
        node.left.as_ref().and_then(|l| lookup(l, key))
    } else {
        node.right.as_ref().and_then(|r| lookup(r, key))
    }
}

fn main() {
    //        20:"r"
    //       /      \
    //   10:"a"    30:"c"
    let old_root = branch(20, "r", Some(leaf(10, "a")), Some(leaf(30, "c")));

    // COW-update the LEFT leaf (key 10). Only the root and the left leaf are copied; the RIGHT
    // subtree (key 30) must be SHARED with the old root.
    let new_root = cow_update(&old_root, 10, "a2");

    // 1. Old snapshot is immutable: it still reads the old value.
    assert_eq!(lookup(&old_root, 10), Some("a"), "old root unchanged");
    assert_eq!(lookup(&old_root, 30), Some("c"));
    // 2. New snapshot reflects the update.
    assert_eq!(lookup(&new_root, 10), Some("a2"), "new root has the update");
    assert_eq!(lookup(&new_root, 30), Some("c"));

    // 3. STRUCTURAL SHARING: the untouched right subtree is the SAME allocation in both trees.
    let old_right = old_root.right.as_ref().unwrap();
    let new_right = new_root.right.as_ref().unwrap();
    assert!(Arc::ptr_eq(old_right, new_right), "right subtree must be shared, not copied");

    // 4. The changed path is NOT shared: the left leaf and the root are distinct allocations.
    let old_left = old_root.left.as_ref().unwrap();
    let new_left = new_root.left.as_ref().unwrap();
    assert!(!Arc::ptr_eq(old_left, new_left), "left leaf on the update path must be a fresh copy");
    assert!(!Arc::ptr_eq(&old_root, &new_root), "root on the update path must be a fresh copy");

    // 5. Reference counting confirms sharing: the shared right node is held by BOTH roots.
    assert_eq!(Arc::strong_count(old_right), 2, "shared subtree is referenced by both versions");

    // 6. A second COW update on the right side shares the (now unchanged) left subtree instead.
    let newer_root = cow_update(&new_root, 30, "c2");
    assert_eq!(lookup(&newer_root, 30), Some("c2"));
    assert_eq!(lookup(&new_root, 30), Some("c"), "prior snapshot still immutable");
    assert!(
        Arc::ptr_eq(new_root.left.as_ref().unwrap(), newer_root.left.as_ref().unwrap()),
        "left subtree shared across the right-side update"
    );

    println!("copy_on_write_btree: PASS");
}
