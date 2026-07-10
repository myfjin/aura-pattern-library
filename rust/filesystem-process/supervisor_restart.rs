#![forbid(unsafe_code)]
//! supervisor_restart — restart backoff state machine; crash loop backs off, stable resets.
//!
//! Core idea: track restart attempts; increase backoff on consecutive crashes, reset on stability.
//! THE ONE LAW: plant a crash sequence and a stability window, simulate restarts, assert
//! backoff increases and resets correctly.
//! When to use: process supervision, daemon restarts, circuit breakers.

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
struct RestartBackoff {
    attempt: u32,
    backoff_ms: u32,
    last_crash_time: u32,
    stable_window: u32, // If stable for this many ms, reset backoff.
}

impl RestartBackoff {
    fn new() -> Self {
        RestartBackoff {
            attempt: 0,
            backoff_ms: 100,
            last_crash_time: 0,
            stable_window: 5000,
        }
    }

    fn on_crash(&mut self, time: u32) {
        self.attempt += 1;
        self.last_crash_time = time;
        // Exponential backoff: double each time, capped at 30000ms.
        self.backoff_ms = (self.backoff_ms * 2).min(30000);
    }

    fn on_check(&mut self, time: u32) {
        // If stable for stable_window, reset.
        if time - self.last_crash_time > self.stable_window {
            self.attempt = 0;
            self.backoff_ms = 100;
        }
    }

    fn next_restart_time(&self, current_time: u32) -> u32 {
        current_time + self.backoff_ms
    }
}

fn main() {
    // Planted case 1: crash loop (backoff increases).
    let mut backoff = RestartBackoff::new();

    // Crash at t=0.
    backoff.on_crash(0);
    assert_eq!(backoff.backoff_ms, 200, "first crash backoff should be 200ms");
    assert_eq!(backoff.attempt, 1);

    // Crash again at t=250 (before stable_window).
    backoff.on_crash(250);
    assert_eq!(backoff.backoff_ms, 400, "second crash backoff should be 400ms");
    assert_eq!(backoff.attempt, 2);

    // THE ONE LAW: exponential backoff continues.
    backoff.on_crash(800);
    assert_eq!(backoff.backoff_ms, 800, "third crash backoff should be 800ms");

    backoff.on_crash(1800);
    assert_eq!(backoff.backoff_ms, 1600, "fourth crash backoff should be 1600ms");

    backoff.on_crash(3600);
    assert_eq!(backoff.backoff_ms, 3200, "fifth crash backoff should be 3200ms");

    // Planted case 2: stability resets backoff.
    let mut backoff2 = RestartBackoff::new();
    backoff2.on_crash(0);
    backoff2.on_crash(200);
    backoff2.on_crash(600);

    assert_eq!(backoff2.attempt, 3);
    assert_eq!(backoff2.backoff_ms, 800);

    // Now check at a much later time (stable for 5000ms since last crash at t=600).
    backoff2.on_check(6000);

    // Should reset.
    assert_eq!(backoff2.attempt, 0, "attempt should reset after stability");
    assert_eq!(backoff2.backoff_ms, 100, "backoff should reset after stability");

    // Planted case 3: verify next restart times.
    let mut backoff3 = RestartBackoff::new();
    backoff3.on_crash(100);
    let next_1 = backoff3.next_restart_time(100);
    assert_eq!(next_1, 100 + 200, "next restart at 100+200");

    backoff3.on_crash(350);
    let next_2 = backoff3.next_restart_time(350);
    assert_eq!(next_2, 350 + 400, "next restart at 350+400");

    // Planted case 4: cap at max backoff.
    let mut backoff4 = RestartBackoff::new();
    for _ in 0..20 {
        backoff4.on_crash(0);
    }
    assert_eq!(backoff4.backoff_ms, 30000, "backoff should be capped at 30000ms");

    println!("supervisor_restart: exponential backoff, stability reset verified — PASS");
}
