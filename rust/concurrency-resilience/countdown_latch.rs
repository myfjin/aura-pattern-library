#![forbid(unsafe_code)]
//! countdown_latch — a latch that releases all waiters only when count reaches zero.
//!
//! Core idea: a shared counter and Condvar. Tasks decrement the counter via count_down();
//! waiters call wait() and block until the counter hits 0. THE ONE LAW: spawn N workers
//! that count down on staggered delays; spawn M waiters. The instant a waiter unblocks it
//! asserts remaining() == 0 — proving no waiter is released before the count is fully spent.
//! A no-op (broken) latch releases a waiter while remaining() is still > 0, failing the
//! assertion. When to use: coordinating completion of a fixed number of tasks.

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
use std::sync::{Arc, Condvar, Mutex};
use std::thread;

struct CountdownLatch {
    count: Mutex<usize>,
    cond: Condvar,
}

impl CountdownLatch {
    fn new(count: usize) -> Self {
        CountdownLatch {
            count: Mutex::new(count),
            cond: Condvar::new(),
        }
    }

    fn count_down(&self) {
        let mut c = self.count.lock().expect("lock poisoned");
        if *c > 0 {
            *c -= 1;
            if *c == 0 {
                self.cond.notify_all();
            }
        }
    }

    fn wait(&self) {
        let mut c = self.count.lock().expect("lock poisoned");
        while *c > 0 {
            c = self.cond.wait(c).expect("wait failed");
        }
    }

    fn remaining(&self) -> usize {
        *self.count.lock().expect("lock poisoned")
    }
}

fn main() {
    let n_workers = 5;
    let n_waiters = 3;
    let latch = Arc::new(CountdownLatch::new(n_workers));

    let wait_complete = Arc::new(Mutex::new(0usize));

    // Workers count down on staggered delays.
    let mut worker_handles = Vec::new();
    for i in 0..n_workers {
        let l = Arc::clone(&latch);
        worker_handles.push(thread::spawn(move || {
            std::thread::sleep(std::time::Duration::from_millis(10 * (i as u64 + 1)));
            l.count_down();
        }));
    }

    // Waiters: the moment wait() returns, the count MUST already be 0.
    let mut waiter_handles = Vec::new();
    for _ in 0..n_waiters {
        let l = Arc::clone(&latch);
        let wc = Arc::clone(&wait_complete);
        waiter_handles.push(thread::spawn(move || {
            l.wait();
            let remaining = l.remaining();
            assert_eq!(remaining, 0, "waiter released while {remaining} count remained");
            *wc.lock().expect("lock poisoned") += 1;
        }));
    }

    for h in worker_handles {
        h.join().expect("worker panicked");
    }
    for h in waiter_handles {
        h.join().expect("waiter panicked");
    }

    let completed = *wait_complete.lock().expect("lock poisoned");
    assert_eq!(completed, n_waiters, "not all waiters unblocked");

    println!("countdown_latch: {n_workers} workers, {completed} waiters released only at count 0 — PASS");
}
