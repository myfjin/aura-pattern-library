#![forbid(unsafe_code)]
//! reusable_phaser — a reusable multi-phase barrier for N threads across P phases.
//!
//! Core idea: N threads synchronize at each of P phases. Each phase requires all N to
//! arrive before any advance. THE ONE LAW: at every phase each thread increments a shared
//! per-phase witness BEFORE arriving, then AFTER the phaser returns asserts the witness
//! equals N — no thread advances past phase k until all N have reached phase k. A no-op
//! (broken) phaser lets a thread advance while the witness is still below N, failing the
//! assertion. When to use: iterative algorithms with per-iteration synchronization points.

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
use std::sync::atomic::{AtomicUsize, Ordering};
use std::sync::{Arc, Condvar, Mutex};
use std::thread;

struct Phaser {
    n_threads: usize,
    phase: Mutex<u64>,
    arrived: Mutex<usize>,
    cond: Condvar,
}

impl Phaser {
    fn new(n_threads: usize) -> Self {
        Phaser {
            n_threads,
            phase: Mutex::new(0),
            arrived: Mutex::new(0),
            cond: Condvar::new(),
        }
    }

    fn arrive_and_await_advance(&self) {
        let current_phase = *self.phase.lock().expect("lock poisoned");

        let mut arrived = self.arrived.lock().expect("lock poisoned");
        *arrived += 1;

        if *arrived < self.n_threads {
            // Wait until the phase counter advances past the one we arrived in.
            loop {
                let advanced = { *self.phase.lock().expect("lock poisoned") > current_phase };
                if advanced {
                    break;
                }
                arrived = self.cond.wait(arrived).expect("wait failed");
            }
        } else {
            // Last to arrive: advance the phase and reset arrivals for the next round.
            *self.phase.lock().expect("lock poisoned") += 1;
            *arrived = 0;
            self.cond.notify_all();
        }
    }
}

fn main() {
    let n_threads = 4;
    let n_phases = 5;
    let phaser = Arc::new(Phaser::new(n_threads));

    // Per-phase witness of how many threads have reached that phase.
    let witness: Arc<Vec<AtomicUsize>> =
        Arc::new((0..n_phases).map(|_| AtomicUsize::new(0)).collect());

    let mut handles = Vec::new();
    for _ in 0..n_threads {
        let p = Arc::clone(&phaser);
        let w = Arc::clone(&witness);

        handles.push(thread::spawn(move || {
            for phase in 0..n_phases {
                // Announce arrival at this phase BEFORE synchronizing.
                w[phase].fetch_add(1, Ordering::SeqCst);
                p.arrive_and_await_advance();
                // If the phaser held, all N threads reached this phase before we advanced.
                let seen = w[phase].load(Ordering::SeqCst);
                assert_eq!(seen, n_threads, "advanced past phase {phase} with only {seen}/{n_threads} arrived");
            }
        }));
    }

    for h in handles {
        h.join().expect("thread panicked");
    }

    for (phase, w) in witness.iter().enumerate() {
        let count = w.load(Ordering::SeqCst);
        assert_eq!(count, n_threads, "phase {phase} had {count} arrivals, expected {n_threads}");
    }

    println!("reusable_phaser: {n_threads} threads × {n_phases} phases, none advanced before all arrived — PASS");
}
