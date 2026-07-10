#![forbid(unsafe_code)]
//! retry_with_budget — retry budget guard; amplification capped, measured over seeds.
//!
//! Core idea: retry logic with a fixed budget (max retries, max amplification). Each retry
//! costs budget. THE ONE LAW: run a series of flaky operations with retry budget, measure
//! the amplification (total attempts / initial requests), then assert amplification is
//! capped and doesn't exceed budget — an unguarded retry would amplify without bound.
//! When to use: rate limiting, preventing amplification attacks, backoff-bounded retry.

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
struct SimpleRng {
    state: u64,
}

impl SimpleRng {
    fn new(seed: u64) -> Self {
        SimpleRng { state: seed }
    }

    fn next(&mut self) -> u64 {
        self.state = self.state.wrapping_mul(6364136223846793005).wrapping_add(1442695040888963407);
        self.state
    }
}

struct RetryBudget {
    max_retries: u32,
    retries_used: u32,
}

impl RetryBudget {
    fn new(max_retries: u32) -> Self {
        RetryBudget {
            max_retries,
            retries_used: 0,
        }
    }

    fn can_retry(&mut self) -> bool {
        if self.retries_used < self.max_retries {
            self.retries_used += 1;
            true
        } else {
            false
        }
    }

    fn amplification(&self, initial_count: u32) -> f64 {
        (self.retries_used as f64 + initial_count as f64) / initial_count as f64
    }
}

fn main() {
    // Planted scenario: 100 requests, each has 30% failure rate, retry up to 5 times.
    let initial_requests = 100u32;
    let max_retries = 5u32;
    let failure_rate = 0.3; // 30% chance of failure

    let mut rng = SimpleRng::new(42);
    let mut budget = RetryBudget::new(max_retries);
    let mut total_attempts = initial_requests;

    for _ in 0..initial_requests {
        loop {
            let rand = (rng.next() as f64) / (u64::MAX as f64);
            let failed = rand < failure_rate;

            if !failed {
                break;
            }

            if budget.can_retry() {
                total_attempts += 1;
            } else {
                break; // Out of budget.
            }
        }
    }

    // THE ONE LAW: a GLOBAL retry budget caps TOTAL extra attempts at max_retries, so the
    // amplification cannot exceed 1 + max_retries/initial — a far tighter (real) bound than
    // the per-request 1+max_retries. An unbounded retry would blow past this cap.
    let amplification = budget.amplification(initial_requests);
    let tight_cap = 1.0 + (max_retries as f64) / (initial_requests as f64);
    assert!(
        amplification <= tight_cap + 1e-9,
        "amplification {:.4}x exceeded the global-budget cap {:.4}x",
        amplification,
        tight_cap
    );
    // The raw invariant the assert rests on: total attempts never exceed initial + budget.
    assert!(
        total_attempts <= initial_requests + max_retries,
        "total attempts {total_attempts} exceeded initial+budget {}",
        initial_requests + max_retries
    );

    // Budget was genuinely exercised and fully exhausted (≥5 failures over 100 requests).
    assert!(budget.retries_used > 0, "no retries used (too lucky)");
    assert_eq!(budget.retries_used, budget.max_retries, "budget should be exhausted");

    println!(
        "retry_with_budget: {} initial → {} attempts, amplification {:.4}x (cap {:.4}x) — PASS",
        initial_requests, total_attempts, amplification, tight_cap
    );
}
