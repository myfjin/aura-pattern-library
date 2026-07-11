#![forbid(unsafe_code)]
//! work_stealing_deque — a lock-free deque where the owner uses one end, stealers the other.
//!
//! Core idea: the Chase-Lev work-stealing deque. A single owner thread pushes and pops at
//! `bottom` (LIFO, cache-friendly); any number of stealer threads take from `top` (FIFO).
//! There is NO lock — `top` and `bottom` are atomics, the buffer holds atomics, and the
//! only synchronization is a CAS on `top`. The subtle case is a single remaining element,
//! where the owner's pop and a steal both target it: exactly one wins the CAS on `top`.
//! THE ONE LAW: the owner pushes N items, then stealers steal concurrently while the owner
//! pops. Each item is taken exactly once (owner-popped + stolen sums to the planted total,
//! and no value is counted twice). A serialized-under-a-Mutex "deque" is not this pattern;
//! the concurrency here is genuine. When to use: task schedulers and parallel work loops.

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
use std::sync::atomic::{fence, AtomicUsize, Ordering};
use std::sync::Arc;
use std::thread;

/// Result of a steal attempt: empty, a transient race (retry), or a value.
enum Steal {
    Empty,
    Retry,
    Got(u64),
}

struct WorkStealingDeque {
    buffer: Vec<AtomicUsize>, // storing u64-as-usize payloads; indices are monotonic (no wrap)
    top: AtomicUsize,         // stealers advance this (front)
    bottom: AtomicUsize,      // owner advances this (back)
}

impl WorkStealingDeque {
    fn new(capacity: usize) -> Self {
        let mut buffer = Vec::with_capacity(capacity);
        for _ in 0..capacity {
            buffer.push(AtomicUsize::new(0));
        }
        WorkStealingDeque {
            buffer,
            top: AtomicUsize::new(0),
            bottom: AtomicUsize::new(0),
        }
    }

    /// Owner only. Push at the bottom. (Called before stealers start, single-threaded.)
    fn push(&self, val: u64) {
        let b = self.bottom.load(Ordering::Relaxed);
        self.buffer[b].store(val as usize, Ordering::Relaxed);
        self.bottom.store(b + 1, Ordering::Release);
    }

    /// Owner only. Pop from the bottom (LIFO). Races a steal on the final element.
    fn pop(&self) -> Option<u64> {
        let b = self.bottom.load(Ordering::Relaxed);
        if b == 0 {
            return None;
        }
        let b = b - 1;
        self.bottom.store(b, Ordering::SeqCst); // tentatively claim; publish before reading top
        fence(Ordering::SeqCst);
        let t = self.top.load(Ordering::SeqCst);

        if t > b {
            // Deque was already empty; restore bottom and report empty.
            self.bottom.store(b + 1, Ordering::Relaxed);
            return None;
        }

        let val = self.buffer[b].load(Ordering::Relaxed) as u64;
        if t == b {
            // Single remaining element: contend with a concurrent steal for it.
            let won = self
                .top
                .compare_exchange(t, t + 1, Ordering::SeqCst, Ordering::Relaxed)
                .is_ok();
            // Either way the deque is now empty; reset bottom above top.
            self.bottom.store(b + 1, Ordering::Relaxed);
            if won {
                Some(val)
            } else {
                None // a stealer took the last element
            }
        } else {
            // t < b: more than one element remains, this slot is exclusively the owner's.
            Some(val)
        }
    }

    /// Stealer. Take from the top (front). Returns Retry on a lost CAS race.
    fn steal(&self) -> Steal {
        let t = self.top.load(Ordering::Acquire);
        fence(Ordering::SeqCst);
        let b = self.bottom.load(Ordering::Acquire);
        if t >= b {
            return Steal::Empty;
        }
        let val = self.buffer[t].load(Ordering::Relaxed) as u64;
        if self
            .top
            .compare_exchange(t, t + 1, Ordering::SeqCst, Ordering::Relaxed)
            .is_ok()
        {
            Steal::Got(val)
        } else {
            Steal::Retry
        }
    }
}

fn main() {
    let n_items = 100usize;
    let n_stealers = 3;

    let deque = Arc::new(WorkStealingDeque::new(n_items));

    // Owner pushes all items first (single-threaded push phase).
    for i in 0..n_items {
        deque.push(i as u64);
    }

    let stolen_total = Arc::new(AtomicUsize::new(0));
    let stolen_count = Arc::new(AtomicUsize::new(0));

    // Stealers drain from the top concurrently with the owner draining from the bottom.
    let mut stealer_handles = Vec::new();
    for _ in 0..n_stealers {
        let d = Arc::clone(&deque);
        let sum = Arc::clone(&stolen_total);
        let cnt = Arc::clone(&stolen_count);
        stealer_handles.push(thread::spawn(move || {
            let mut local_sum = 0u64;
            let mut local_cnt = 0usize;
            loop {
                match d.steal() {
                    Steal::Got(v) => {
                        local_sum += v;
                        local_cnt += 1;
                    }
                    Steal::Retry => std::hint::spin_loop(),
                    Steal::Empty => break,
                }
            }
            sum.fetch_add(local_sum as usize, Ordering::Relaxed);
            cnt.fetch_add(local_cnt, Ordering::Relaxed);
        }));
    }

    // Owner pops from the bottom concurrently.
    let mut owner_sum = 0u64;
    let mut owner_cnt = 0usize;
    while let Some(v) = deque.pop() {
        owner_sum += v;
        owner_cnt += 1;
    }

    for h in stealer_handles {
        h.join().expect("stealer panicked");
    }

    let stolen_sum = stolen_total.load(Ordering::Relaxed) as u64;
    let stolen_cnt = stolen_count.load(Ordering::Relaxed);

    let total_sum = owner_sum + stolen_sum;
    let total_cnt = owner_cnt + stolen_cnt;

    let expected_sum: u64 = (0..n_items as u64).sum();

    // Each item taken exactly once: both the sum AND the count must match the planted set.
    assert_eq!(total_cnt, n_items, "item count mismatch: {total_cnt} taken, expected {n_items} (lost or duplicated)");
    assert_eq!(total_sum, expected_sum, "sum mismatch: items lost or double-counted");

    println!(
        "work_stealing_deque: owner took {owner_cnt}, {n_stealers} stealers took {stolen_cnt}, {n_items} items each exactly once — PASS"
    );
}
