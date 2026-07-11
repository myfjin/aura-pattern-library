#![forbid(unsafe_code)]
//! seqlock_snapshot — a seqlock ensuring readers never observe torn (partial) updates.
//!
//! Core idea: a sequence number guards reads — there is NO lock on the data itself, so a
//! reader genuinely can catch the writer mid-update. The writer bumps seq to odd, writes
//! the two fields (as independent atomics, so field-by-field visibility is real), then
//! bumps seq to even. A reader samples seq (must be even), reads both fields lock-free,
//! then re-samples seq; if it changed, the writer intervened and the reader retries.
//! THE ONE LAW: a writer updates a 2-field value (y == 2·x) concurrently with lock-free
//! readers. Because the fields are separate atomics, a reader with a broken/absent seq
//! protocol WOULD see x from the new value and y from the old (y != 2·x). The seq protocol
//! must catch every such torn read. When to use: multi-field snapshots under high
//! concurrent read pressure with a single writer.

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
use std::sync::atomic::{fence, AtomicU64, Ordering};
use std::sync::Arc;
use std::thread;

struct SeqLock {
    seq: AtomicU64,
    x: AtomicU64,
    y: AtomicU64,
}

impl SeqLock {
    fn new(x: u64, y: u64) -> Self {
        SeqLock {
            seq: AtomicU64::new(0),
            x: AtomicU64::new(x),
            y: AtomicU64::new(y),
        }
    }

    // Single writer. No lock on the data — only the seq protocol.
    fn write(&self, new_x: u64, new_y: u64) {
        let s = self.seq.load(Ordering::Relaxed);
        self.seq.store(s + 1, Ordering::Release); // seq becomes odd: "write in progress"
        fence(Ordering::Release);
        self.x.store(new_x, Ordering::Relaxed);
        self.y.store(new_y, Ordering::Relaxed);
        self.seq.store(s + 2, Ordering::Release); // seq becomes even: "write complete"
    }

    // Lock-free reader: optimistic read with seq validation and retry.
    fn read(&self) -> (u64, u64) {
        loop {
            let before = self.seq.load(Ordering::Acquire);
            if before & 1 != 0 {
                // Writer is mid-update; spin and retry.
                std::hint::spin_loop();
                continue;
            }
            let x = self.x.load(Ordering::Relaxed);
            let y = self.y.load(Ordering::Relaxed);
            fence(Ordering::Acquire);
            let after = self.seq.load(Ordering::Acquire);
            if before == after {
                return (x, y); // stable snapshot
            }
            // Torn read: a write raced us. Retry.
            std::hint::spin_loop();
        }
    }
}

fn main() {
    let n_threads = 4;
    let n_writes = 2000;
    let n_reads_per_thread = 5000;

    let lock = Arc::new(SeqLock::new(0, 0));
    let mut reader_handles = Vec::new();

    // Single writer maintaining the invariant y == 2·x.
    let l = Arc::clone(&lock);
    let writer_handle = thread::spawn(move || {
        for i in 1..=n_writes {
            l.write(i, i * 2);
        }
    });

    // Lock-free readers: every snapshot returned by read() must satisfy y == 2·x.
    for _ in 0..n_threads {
        let l = Arc::clone(&lock);
        reader_handles.push(thread::spawn(move || {
            let mut torn = 0u64;
            for _ in 0..n_reads_per_thread {
                let (x, y) = l.read();
                if y != x * 2 {
                    torn += 1;
                }
            }
            torn
        }));
    }

    writer_handle.join().expect("writer thread panicked");

    let mut total_torn = 0;
    for h in reader_handles {
        total_torn += h.join().expect("reader thread panicked");
    }

    assert_eq!(total_torn, 0, "seqlock failed: {total_torn} torn reads observed");

    println!("seqlock_snapshot: {n_threads} lock-free readers vs 1 writer, zero torn reads — PASS");
}
