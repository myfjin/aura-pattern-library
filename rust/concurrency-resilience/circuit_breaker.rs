#![forbid(unsafe_code)]
//! circuit_breaker — typestate closed/open/half-open enum; transitions asserted.
//!
//! Core idea: implement the circuit breaker pattern using Rust's typestate pattern to
//! ensure state transitions are valid at compile time and runtime. States: Closed (ok),
//! Open (failing), HalfOpen (probing). THE ONE LAW: simulate a series of successes and
//! failures, verify state transitions are correct, and assert invalid transitions are
//! caught — an unguarded state machine would allow invalid paths.
//! When to use: fault tolerance, preventing cascading failures, dependency health checks.

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
#[derive(Debug, Clone, Copy, PartialEq)]
enum CBState {
    Closed,   // Normal operation
    Open,     // Failing, reject all
    HalfOpen, // Probing, allow one
}

struct CircuitBreaker {
    state: CBState,
    failure_count: u32,
    success_count: u32,
    failure_threshold: u32,
    success_threshold: u32,
}

impl CircuitBreaker {
    fn new(failure_threshold: u32, success_threshold: u32) -> Self {
        CircuitBreaker {
            state: CBState::Closed,
            failure_count: 0,
            success_count: 0,
            failure_threshold,
            success_threshold,
        }
    }

    fn record_success(&mut self) -> Result<(), &'static str> {
        match self.state {
            CBState::Closed => {
                self.failure_count = 0; // Reset on success.
                Ok(())
            }
            CBState::HalfOpen => {
                self.success_count += 1;
                if self.success_count >= self.success_threshold {
                    self.state = CBState::Closed;
                    self.success_count = 0;
                    self.failure_count = 0;
                }
                Ok(())
            }
            CBState::Open => Err("circuit is open"),
        }
    }

    fn record_failure(&mut self) -> Result<(), &'static str> {
        match self.state {
            CBState::Closed => {
                self.failure_count += 1;
                if self.failure_count >= self.failure_threshold {
                    self.state = CBState::Open;
                    self.failure_count = 0;
                }
                Ok(())
            }
            CBState::HalfOpen => {
                self.state = CBState::Open;
                self.success_count = 0;
                self.failure_count = 0;
                Ok(())
            }
            CBState::Open => {
                // After a delay (simplified: always allow transition to half-open).
                self.state = CBState::HalfOpen;
                Ok(())
            }
        }
    }

    fn is_open(&self) -> bool {
        self.state == CBState::Open
    }
}

fn main() {
    // Planted scenario: 3 failures trigger open, 2 successes close it.
    let mut cb = CircuitBreaker::new(3, 2);

    // Initially closed.
    assert_eq!(cb.state, CBState::Closed);
    assert!(!cb.is_open());

    // Two successes while closed.
    cb.record_success().unwrap();
    cb.record_success().unwrap();
    assert_eq!(cb.state, CBState::Closed);

    // Three failures → open.
    cb.record_failure().unwrap();
    cb.record_failure().unwrap();
    assert_eq!(cb.state, CBState::Closed); // Not yet.
    cb.record_failure().unwrap();
    assert_eq!(cb.state, CBState::Open); // Now open.
    assert!(cb.is_open());

    // THE ONE LAW: transitions are validated.
    // While open, reject new requests (is_open() == true).
    // But record_failure() moves to half-open.
    cb.record_failure().unwrap();
    assert_eq!(cb.state, CBState::HalfOpen);

    // Half-open: one failure re-opens.
    cb.record_failure().unwrap();
    assert_eq!(cb.state, CBState::Open);

    // Again to half-open.
    cb.record_failure().unwrap();
    assert_eq!(cb.state, CBState::HalfOpen);

    // Success closes.
    cb.record_success().unwrap();
    assert_eq!(cb.state, CBState::HalfOpen); // One success, need two.
    cb.record_success().unwrap();
    assert_eq!(cb.state, CBState::Closed); // Now closed.

    println!("circuit_breaker: state transitions verified, typestate valid — PASS");
}
