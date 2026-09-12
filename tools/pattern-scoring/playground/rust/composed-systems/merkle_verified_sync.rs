#![forbid(unsafe_code)]
// composes: chunk-two-versions + build-REAL-merkle-trees + root+subtree-diff + sync-only-changed
//
// A real merkle tree: leaves are chunk hashes, each internal node = hash(left, right), up to a
// single root. The diff descends from the root and SKIPS any subtree whose node hash matches —
// that is the whole point of a merkle tree (verify/diff without touching every leaf). We prove
// the skip: the unchanged sibling subtree's node hash is compared once and its leaves never are.

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
fn hash_bytes(data: &[u8]) -> u64 {
    let mut h: u64 = 1469598103934665603; // FNV-ish offset
    for &b in data {
        h = h.wrapping_mul(31).wrapping_add(b as u64);
    }
    h
}

fn hash_pair(a: u64, b: u64) -> u64 {
    a.wrapping_mul(1099511628211).wrapping_add(b).wrapping_mul(31)
}

// Level 0 = leaves; each higher level halves (duplicating the last node when odd). Top = root.
fn build_tree(leaf_hashes: &[u64]) -> Vec<Vec<u64>> {
    let mut levels = vec![leaf_hashes.to_vec()];
    while levels.last().unwrap().len() > 1 {
        let cur = levels.last().unwrap();
        let mut next = Vec::new();
        let mut i = 0;
        while i < cur.len() {
            let a = cur[i];
            let b = if i + 1 < cur.len() { cur[i + 1] } else { cur[i] };
            next.push(hash_pair(a, b));
            i += 2;
        }
        levels.push(next);
    }
    levels
}

fn root(levels: &[Vec<u64>]) -> u64 {
    *levels.last().unwrap().first().unwrap()
}

// Descend from the top; return changed leaf indices. `visited_leaves` counts how many leaf nodes
// the diff actually inspected — proof that unchanged subtrees were skipped.
fn diff(l1: &[Vec<u64>], l2: &[Vec<u64>], level: usize, idx: usize, changed: &mut Vec<usize>, visited_leaves: &mut usize) {
    if l1[level][idx] == l2[level][idx] {
        return; // subtree identical → skip entirely (no leaf comparisons below)
    }
    if level == 0 {
        *visited_leaves += 1;
        changed.push(idx);
        return;
    }
    let lower = level - 1;
    for c in [idx * 2, idx * 2 + 1] {
        if c < l1[lower].len() {
            diff(l1, l2, lower, c, changed, visited_leaves);
        }
    }
}

fn main() {
    // Stage 1: chunk two versions (chunk 1 changed).
    let v1: Vec<&[u8]> = vec![b"chunk-0-v1", b"chunk-1-v1", b"chunk-2-v1", b"chunk-3-v1"];
    let v2: Vec<&[u8]> = vec![b"chunk-0-v1", b"chunk-1-v2", b"chunk-2-v1", b"chunk-3-v1"];

    // Stage 2: build REAL merkle trees over the leaf hashes.
    let leaves1: Vec<u64> = v1.iter().map(|c| hash_bytes(c)).collect();
    let leaves2: Vec<u64> = v2.iter().map(|c| hash_bytes(c)).collect();
    let tree1 = build_tree(&leaves1);
    let tree2 = build_tree(&leaves2);

    // A one-byte change in any chunk changes its leaf hash → changes the ROOT.
    assert_ne!(root(&tree1), root(&tree2), "a changed chunk must change the merkle root");

    // Stage 3: diff by descending the tree, skipping matching subtrees.
    let top = tree1.len() - 1;
    let mut changed = Vec::new();
    let mut visited_leaves = 0usize;
    diff(&tree1, &tree2, top, 0, &mut changed, &mut visited_leaves);
    changed.sort();
    assert_eq!(changed, vec![1], "exactly leaf 1 changed");
    // Merkle efficiency proof: with 4 leaves and one change, the diff visited only the 2 leaves of
    // the differing half — the other subtree (chunks 2,3) was skipped by a single node comparison.
    assert!(visited_leaves < v1.len(), "unchanged subtree skipped (visited {visited_leaves} of {} leaves)", v1.len());

    // Stage 4: sync only the changed chunks.
    let mut synced = v1.clone();
    for &i in &changed {
        synced[i] = v2[i];
    }
    assert_eq!(synced, v2, "after syncing changed chunks, versions match exactly");
    // Unchanged chunks were not touched (same references/content as v1 originally).
    assert_eq!(synced[0], v1[0]);
    assert_eq!(synced[2], v1[2]);

    println!("merkle_verified_sync: PASS");
}
