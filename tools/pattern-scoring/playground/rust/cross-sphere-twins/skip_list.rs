#![forbid(unsafe_code)]
//! skip_list — a real probabilistic skip list (index-arena, safe); levels drive search.
//!
//! Core idea: each node has a random height; higher levels are "express lanes" that skip ahead,
//! giving O(log n) expected search. Nodes live in a Vec (index links, no unsafe). Search starts
//! at the top level and drops down — the levels are LOAD-BEARING, not decoration. THE LAW: insert
//! a set, and assert (1) sorted iteration and (2) search results match a BTreeSet reference, AND
//! (3) the structure actually built multiple levels (a sorted-Vec impostor never would). When to
//! use: ordered sets, Redis sorted-sets, probabilistic ordered indices.

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
use std::collections::BTreeSet;

const MAX_LEVEL: usize = 12;

struct Node {
    key: u32,
    forward: Vec<Option<usize>>, // forward[l] = index of next node on level l
}

struct SkipList {
    nodes: Vec<Node>, // nodes[0] is the head sentinel
    level: usize,     // number of levels currently in use (≥1)
    rng: u64,
}

impl SkipList {
    fn new(seed: u64) -> Self {
        SkipList {
            nodes: vec![Node { key: 0, forward: vec![None; MAX_LEVEL] }],
            level: 1,
            rng: seed,
        }
    }

    fn random_level(&mut self) -> usize {
        let mut lvl = 1;
        loop {
            self.rng = self.rng.wrapping_mul(6364136223846793005).wrapping_add(1442695040888963407);
            if (self.rng >> 33) & 1 == 1 && lvl < MAX_LEVEL {
                lvl += 1;
            } else {
                break;
            }
        }
        lvl
    }

    fn insert(&mut self, key: u32) {
        let mut update = [0usize; MAX_LEVEL]; // predecessor at each level
        let mut x = 0usize;
        for lvl in (0..self.level).rev() {
            while let Some(nxt) = self.nodes[x].forward[lvl] {
                if self.nodes[nxt].key < key {
                    x = nxt;
                } else {
                    break;
                }
            }
            update[lvl] = x;
        }
        // Already present?
        if let Some(nxt) = self.nodes[x].forward[0] {
            if self.nodes[nxt].key == key {
                return;
            }
        }

        let new_level = self.random_level();
        if new_level > self.level {
            for u in update.iter_mut().take(new_level).skip(self.level) {
                *u = 0; // head is predecessor on brand-new levels
            }
            self.level = new_level;
        }

        let new_idx = self.nodes.len();
        let mut forward = vec![None; MAX_LEVEL];
        for l in 0..new_level {
            forward[l] = self.nodes[update[l]].forward[l];
            self.nodes[update[l]].forward[l] = Some(new_idx);
        }
        self.nodes.push(Node { key, forward });
    }

    /// Search traversing levels top-down (the defining O(log n) skip-list walk).
    fn search(&self, key: u32) -> bool {
        let mut x = 0usize;
        for lvl in (0..self.level).rev() {
            while let Some(nxt) = self.nodes[x].forward[lvl] {
                if self.nodes[nxt].key < key {
                    x = nxt;
                } else {
                    break;
                }
            }
        }
        match self.nodes[x].forward[0] {
            Some(nxt) => self.nodes[nxt].key == key,
            None => false,
        }
    }

    fn iter_sorted(&self) -> Vec<u32> {
        let mut out = Vec::new();
        let mut x = self.nodes[0].forward[0];
        while let Some(idx) = x {
            out.push(self.nodes[idx].key);
            x = self.nodes[idx].forward[0];
        }
        out
    }

    fn max_level_used(&self) -> usize {
        self.level
    }
}

fn main() {
    let mut sl = SkipList::new(0xC0FFEE);
    let mut reference: BTreeSet<u32> = BTreeSet::new();

    // Insert a decent set in scrambled order.
    let vals = [50u32, 3, 17, 99, 42, 8, 71, 25, 60, 1, 88, 33, 5, 77, 12, 64, 29, 90, 46, 20];
    for &v in &vals {
        sl.insert(v);
        reference.insert(v);
    }

    // (1) sorted iteration matches the BTreeSet reference exactly.
    let sorted: Vec<u32> = reference.iter().copied().collect();
    assert_eq!(sl.iter_sorted(), sorted, "skip-list iteration must match BTreeSet order");

    // (2) search agrees with the reference for members AND non-members.
    for v in 0..100u32 {
        assert_eq!(sl.search(v), reference.contains(&v), "search({v}) must match reference");
    }

    // (3) it is REALLY a skip list — multiple express-lane levels got built (a sorted Vec has 1).
    assert!(sl.max_level_used() > 1, "a real skip list builds >1 level, got {}", sl.max_level_used());
    // Some node must have a forward pointer above level 0 (an actual express link).
    let has_express = sl.nodes.iter().any(|n| n.forward.iter().skip(1).any(|f| f.is_some()));
    assert!(has_express, "at least one node must have an express-lane link above level 0");

    // Duplicates ignored; empty/single sane.
    sl.insert(50);
    assert_eq!(sl.iter_sorted().len(), vals.len(), "duplicate insert does not grow the set");
    assert_eq!(SkipList::new(1).iter_sorted().len(), 0, "empty skip list");

    println!("skip_list: {} levels, express-lane search matches BTreeSet exactly — PASS", sl.max_level_used());
}
