#![forbid(unsafe_code)]
//! token_bucket — real token bucket with virtual clock; burst shaped to rate.
//!
//! Core idea: token bucket rate limiter using a virtual clock. Tokens accumulate over time
//! at a fixed rate; consumers take tokens to perform work. Bursts are bounded by bucket
//! capacity. THE ONE LAW: advance the virtual clock, request tokens, and assert the burst
//! pattern matches the expected shape — an unguarded bucket would allow unlimited bursts,
//! failing the capacity assert. When to use: API rate limiting, traffic shaping.

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
struct TokenBucket {
    capacity: f64,
    rate: f64,           // tokens per time unit
    tokens: f64,
    last_time: i64,
}

impl TokenBucket {
    fn new(capacity: f64, rate: f64) -> Self {
        TokenBucket {
            capacity,
            rate,
            tokens: capacity,
            last_time: 0,
        }
    }

    fn refill(&mut self, now: i64) {
        let elapsed = (now - self.last_time) as f64;
        let tokens_generated = elapsed * self.rate;
        self.tokens = (self.tokens + tokens_generated).min(self.capacity);
        self.last_time = now;
    }

    fn try_consume(&mut self, now: i64, amount: f64) -> bool {
        self.refill(now);
        if self.tokens >= amount {
            self.tokens -= amount;
            true
        } else {
            false
        }
    }

    fn available(&mut self, now: i64) -> f64 {
        self.refill(now);
        self.tokens
    }
}

fn main() {
    // Planted scenario: capacity 10, rate 1 token per time unit.
    let mut bucket = TokenBucket::new(10.0, 1.0);

    // At time 0, bucket is full (10 tokens).
    assert!(bucket.try_consume(0, 10.0), "should consume full capacity");
    assert!(!bucket.try_consume(0, 1.0), "should be empty after consuming all");

    // Advance time by 5 units → 5 tokens generated.
    let available_at_5 = bucket.available(5);
    assert!(available_at_5 >= 4.9 && available_at_5 <= 5.1, "should have ~5 tokens at t=5");

    // Consume 5 tokens.
    assert!(bucket.try_consume(5, 5.0), "should consume 5 at t=5");

    // Advance time by 10 units → another 10 tokens, but capped at capacity.
    let available_at_15 = bucket.available(15);
    assert!(available_at_15 >= 9.9 && available_at_15 <= 10.1, "should be capped at capacity");

    // THE ONE LAW: burst is bounded by capacity.
    let mut bucket2 = TokenBucket::new(5.0, 0.1); // capacity 5, rate 0.1/time.
    bucket2.try_consume(0, 5.0); // Consume all.

    // Rapidly request tokens at the same time (burst).
    let mut burst_count = 0;
    for _ in 0..50 {
        if bucket2.try_consume(0, 1.0) {
            burst_count += 1;
        }
    }
    // Only the initial capacity (5) should be consumable in a burst at the same time.
    assert_eq!(burst_count, 0, "burst should be fully depleted");

    println!("token_bucket: rate limiting verified, burst bounded — PASS");
}
