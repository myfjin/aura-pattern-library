#![forbid(unsafe_code)]

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
use std::collections::VecDeque;

// ARC (Megiddo & Modha) — a REAL adaptive replacement cache, not a two-queue lookalike.
// The defining feature is the target `p` that adapts between recency (T1) and frequency (T2)
// driven by hits in the ghost lists B1/B2. We prove two things a plain LRU cannot do:
//   (1) `p` actually adapts (moves off 0) in response to ghost hits;
//   (2) scan resistance — a frequently-used key survives a flood of one-time keys, where an
//       LRU of the same capacity evicts it.
// Lists are front = LRU, back = MRU.

struct Arc2Q {
    c: usize,
    p: usize,
    t1: VecDeque<u32>,
    t2: VecDeque<u32>,
    b1: VecDeque<u32>,
    b2: VecDeque<u32>,
}

fn remove(q: &mut VecDeque<u32>, x: u32) -> bool {
    if let Some(i) = q.iter().position(|&k| k == x) {
        q.remove(i);
        true
    } else {
        false
    }
}

impl Arc2Q {
    fn new(c: usize) -> Self {
        Arc2Q { c, p: 0, t1: VecDeque::new(), t2: VecDeque::new(), b1: VecDeque::new(), b2: VecDeque::new() }
    }

    // Move the LRU of T1→B1 or T2→B2 per the ARC REPLACE rule.
    fn replace(&mut self, in_b2: bool) {
        if !self.t1.is_empty() && (self.t1.len() > self.p || (in_b2 && self.t1.len() == self.p)) {
            if let Some(v) = self.t1.pop_front() {
                self.b1.push_back(v);
            }
        } else if let Some(v) = self.t2.pop_front() {
            self.b2.push_back(v);
        }
    }

    fn access(&mut self, x: u32) -> bool {
        // Case I: hit in the cache (T1 or T2) → promote to MRU of T2.
        if self.t1.contains(&x) || self.t2.contains(&x) {
            remove(&mut self.t1, x);
            remove(&mut self.t2, x);
            self.t2.push_back(x);
            return true;
        }
        // Case II: ghost hit in B1 → increase p toward recency, then fetch into T2.
        if self.b1.contains(&x) {
            let delta = (self.b2.len() / self.b1.len().max(1)).max(1);
            self.p = (self.p + delta).min(self.c);
            self.replace(false);
            remove(&mut self.b1, x);
            self.t2.push_back(x);
            return false;
        }
        // Case III: ghost hit in B2 → decrease p toward frequency, then fetch into T2.
        if self.b2.contains(&x) {
            let delta = (self.b1.len() / self.b2.len().max(1)).max(1);
            self.p = self.p.saturating_sub(delta);
            self.replace(true);
            remove(&mut self.b2, x);
            self.t2.push_back(x);
            return false;
        }
        // Case IV: total miss.
        if self.t1.len() + self.b1.len() == self.c {
            if self.t1.len() < self.c {
                self.b1.pop_front();
                self.replace(false);
            } else {
                self.t1.pop_front();
            }
        } else {
            let total = self.t1.len() + self.t2.len() + self.b1.len() + self.b2.len();
            if total >= self.c {
                if total == 2 * self.c {
                    self.b2.pop_front();
                }
                self.replace(false);
            }
        }
        self.t1.push_back(x);
        false
    }
}

// Minimal LRU of the same capacity, for the scan-resistance comparison.
struct Lru {
    c: usize,
    q: VecDeque<u32>,
}
impl Lru {
    fn new(c: usize) -> Self {
        Lru { c, q: VecDeque::new() }
    }
    fn access(&mut self, x: u32) -> bool {
        if remove(&mut self.q, x) {
            self.q.push_back(x);
            return true;
        }
        if self.q.len() == self.c {
            self.q.pop_front();
        }
        self.q.push_back(x);
        false
    }
}

fn main() {
    let c = 4;

    // --- Property 1: p adapts off 0 in response to a B1 ghost hit. ---
    let mut a = Arc2Q::new(c);
    // Prime one frequency entry into T2 (touch twice) so the cache isn't 100% T1 — this makes
    // eviction go through REPLACE (T1→B1), which is what records recency ghosts. (When T1 owns
    // the whole cache, ARC evicts with no ghost, so p can never move — that's by design.)
    a.access(9);
    a.access(9);
    // A short scan of distinct keys now pushes evicted T1 pages into the B1 ghost list.
    for k in 0..6u32 {
        a.access(k);
    }
    assert_eq!(a.p, 0, "no ghost hits yet → p unchanged");
    // Re-touch whatever the scan parked in B1: a genuine B1 ghost hit must raise p.
    let ghost = *a.b1.front().expect("the scan must have produced a B1 ghost (proves REPLACE ran)");
    let was_miss = !a.access(ghost);
    assert!(was_miss, "the ghost key is not resident → miss");
    assert!(a.p > 0, "a B1 ghost hit must push p above 0 (adaptation LRU cannot do)");

    // --- Property 2: scan resistance vs LRU. ---
    let mut arc = Arc2Q::new(c);
    let mut lru = Lru::new(c);
    // Prime two HOT keys with repeated use → ARC promotes them to the frequency list T2.
    for _ in 0..3 {
        arc.access(100);
        arc.access(200);
        lru.access(100);
        lru.access(200);
    }
    // Now flood with one-time scan keys (more than capacity).
    for k in 0..20u32 {
        arc.access(k);
        lru.access(k);
    }
    // ARC's frequency list protects the hot keys through the scan; LRU does not.
    assert!(arc.access(100), "ARC keeps the hot key through a scan (frequency protection)");
    assert!(arc.access(200), "ARC keeps the second hot key too");
    assert!(!lru.access(100), "LRU evicts the hot key during the scan");
    assert!(!lru.access(200), "LRU evicts the second hot key too");

    // Cache invariant: resident set never exceeds capacity.
    assert!(arc.t1.len() + arc.t2.len() <= c, "T1+T2 within capacity");

    println!("arc_adaptive_cache: PASS");
}
