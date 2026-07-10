#![forbid(unsafe_code)]
//! crdt_gcounter — grow-only counter; merge is commutative, idempotent, convergent.
//!
//! Core idea: each replica has a per-replica counter. Merge combines max of each.
//! Merge is commutative (A ⊔ B = B ⊔ A), idempotent (A ⊔ A = A), and convergent
//! (A ⊔ B ⊔ C = A ⊔ (B ⊔ C)). THE LAW: perform merges in different orders and
//! assert the same final state is reached.
//! When to use: conflict-free replicated counters, CRDT sync.

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
use std::collections::HashMap;

#[derive(Clone, Debug, PartialEq)]
struct GCounter {
    counters: HashMap<usize, u64>,
}

impl GCounter {
    fn new() -> Self {
        GCounter {
            counters: HashMap::new(),
        }
    }

    fn increment(&mut self, replica_id: usize) {
        *self.counters.entry(replica_id).or_insert(0) += 1;
    }

    fn value(&self) -> u64 {
        self.counters.values().sum()
    }

    fn merge(&mut self, other: &GCounter) {
        for (id, count) in &other.counters {
            let current = self.counters.entry(*id).or_insert(0);
            *current = (*current).max(*count);
        }
    }

    fn clone_and_merge(&self, other: &GCounter) -> GCounter {
        let mut result = self.clone();
        result.merge(other);
        result
    }
}

fn main() {
    // Test 1: commutativity: A ⊔ B = B ⊔ A.
    let mut a = GCounter::new();
    a.increment(0);
    a.increment(0);

    let mut b = GCounter::new();
    b.increment(1);
    b.increment(1);
    b.increment(1);

    let mut a_merge_b = a.clone();
    a_merge_b.merge(&b);

    let mut b_merge_a = b.clone();
    b_merge_a.merge(&a);

    assert_eq!(a_merge_b, b_merge_a, "A ⊔ B = B ⊔ A");

    // Test 2: idempotence: A ⊔ A = A.
    let mut a_merge_a = a.clone();
    a_merge_a.merge(&a);
    assert_eq!(a_merge_a, a, "A ⊔ A = A");

    // Test 3: convergence: (A ⊔ B) ⊔ C = A ⊔ (B ⊔ C).
    let mut c = GCounter::new();
    c.increment(2);

    let abc_left = a.clone_and_merge(&b).clone_and_merge(&c);
    let abc_right = a.clone_and_merge(&b.clone_and_merge(&c));
    assert_eq!(abc_left, abc_right, "(A ⊔ B) ⊔ C = A ⊔ (B ⊔ C)");

    // Test 4: value consistency.
    assert_eq!(a.value() + b.value() + c.value(), 6, "expected total increments");
    assert_eq!(abc_left.value(), 6, "merged counter has correct total");

    // Test 5: independent branches converge.
    let mut r0 = GCounter::new();
    r0.increment(0);
    r0.increment(0);

    let mut r1 = GCounter::new();
    r1.increment(1);

    let mut r2 = GCounter::new();
    r2.increment(2);
    r2.increment(2);
    r2.increment(2);

    // Converge from different merge orders.
    let final_123 = r0.clone_and_merge(&r1).clone_and_merge(&r2);
    let final_231 = r1.clone_and_merge(&r2).clone_and_merge(&r0);
    let final_312 = r2.clone_and_merge(&r0).clone_and_merge(&r1);

    assert_eq!(final_123, final_231);
    assert_eq!(final_231, final_312);

    println!("crdt_gcounter: merge commutative, idempotent, convergent — PASS");
}
