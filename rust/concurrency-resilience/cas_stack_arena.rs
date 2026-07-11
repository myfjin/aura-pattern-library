#![forbid(unsafe_code)]
//! cas_stack_arena — a lock-free stack using atomic head pointer and arena indices.
//!
//! Core idea: arena stores values; head (AtomicUsize) is the stack top. Each slot
//! in the arena also tracks the next index. Pushes/pops use CAS on head.
//! THE ONE LAW: multiple threads push items concurrently; pop all items. Every pushed
//! item is popped exactly once. A broken CAS loses items or causes duplicates.
//! When to use: lock-free work-stealing or concurrent stacks where push/pop dominate.

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
use std::sync::atomic::{AtomicU64, AtomicUsize, Ordering};
use std::sync::Arc;
use std::thread;

struct CasStackArena {
    values: Vec<AtomicU64>,
    nexts: Vec<AtomicUsize>,
    head: AtomicUsize,
    alloc: AtomicUsize,
}

impl CasStackArena {
    fn new(capacity: usize) -> Self {
        let mut values = Vec::with_capacity(capacity);
        let mut nexts = Vec::with_capacity(capacity);
        for _ in 0..capacity {
            values.push(AtomicU64::new(0));
            nexts.push(AtomicUsize::new(usize::MAX));
        }
        CasStackArena {
            values,
            nexts,
            head: AtomicUsize::new(usize::MAX),
            alloc: AtomicUsize::new(0),
        }
    }

    fn push(&self, val: u64) -> bool {
        let idx = self.alloc.fetch_add(1, Ordering::Relaxed);
        if idx >= self.values.len() {
            return false;
        }
        self.values[idx].store(val, Ordering::Relaxed);
        loop {
            let h = self.head.load(Ordering::Acquire);
            self.nexts[idx].store(h, Ordering::Relaxed);
            match self.head.compare_exchange(h, idx, Ordering::Release, Ordering::Relaxed) {
                Ok(_) => return true,
                Err(_) => std::hint::spin_loop(),
            }
        }
    }

    fn pop(&self) -> Option<u64> {
        loop {
            let h = self.head.load(Ordering::Acquire);
            if h == usize::MAX {
                return None;
            }
            let next = self.nexts[h].load(Ordering::Relaxed);
            let val = self.values[h].load(Ordering::Relaxed);
            match self.head.compare_exchange(h, next, Ordering::Release, Ordering::Relaxed) {
                Ok(_) => return Some(val),
                Err(_) => std::hint::spin_loop(),
            }
        }
    }
}

fn main() {
    let capacity = 256;
    let n_threads = 4;
    let pushes_per_thread = 30;
    let stack = Arc::new(CasStackArena::new(capacity));

    let mut handles = Vec::new();

    // Spawn push threads
    for _ in 0..n_threads {
        let s = Arc::clone(&stack);
        handles.push(thread::spawn(move || {
            for i in 0..pushes_per_thread {
                let val = i as u64;
                loop {
                    if s.push(val) {
                        break;
                    }
                }
            }
        }));
    }

    // Join push threads
    for h in handles.drain(0..) {
        h.join().expect("push thread panicked");
    }

    // Pop all items
    let mut items = Vec::new();
    loop {
        if let Some(val) = stack.pop() {
            items.push(val);
        } else {
            break;
        }
    }

    let expected_count = n_threads * pushes_per_thread;
    assert_eq!(items.len(), expected_count, "stack lost items or dropped pops");

    println!("cas_stack_arena: {} threads pushed {}, all popped — PASS", n_threads, expected_count);
}
