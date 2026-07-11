#![forbid(unsafe_code)]
//! double_buffer — atomic front/back buffer swap ensuring readers always see consistent state.
//!
//! Core idea: two buffers (front and back). A writer updates the back buffer, then
//! swaps it to front (atomically). Readers always see a complete front buffer, never
//! catching a half-written update. THE ONE LAW: readers must never observe a torn
//! buffer (partial write). Concurrent writers/readers with an atomic swap ensure readers
//! always see a fully-consistent snapshot. When to use: publishing large updated state
//! (configs, metrics snapshots) without blocking readers.

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
use std::sync::atomic::{AtomicUsize, Ordering};
use std::sync::{Arc, Mutex};
use std::thread;

struct Buffer {
    data: Vec<u64>,
}

impl Buffer {
    fn new(size: usize) -> Self {
        Buffer { data: vec![0; size] }
    }

    fn checksum(&self) -> u64 {
        self.data.iter().sum()
    }
}

struct DoubleBuffer {
    buffers: [Mutex<Buffer>; 2],
    front: AtomicUsize, // index of the front buffer
}

impl DoubleBuffer {
    fn new(size: usize) -> Self {
        DoubleBuffer {
            buffers: [Mutex::new(Buffer::new(size)), Mutex::new(Buffer::new(size))],
            front: AtomicUsize::new(0),
        }
    }

    fn write(&self, updates: Vec<u64>) {
        let front_idx = self.front.load(Ordering::Acquire);
        let back_idx = 1 - front_idx;

        let mut back = self.buffers[back_idx].lock().expect("lock poisoned");
        back.data = updates;
        drop(back);

        // Swap front to back
        self.front.store(back_idx, Ordering::Release);
    }

    fn read(&self) -> (Vec<u64>, u64) {
        let front_idx = self.front.load(Ordering::Acquire);
        let front = self.buffers[front_idx].lock().expect("lock poisoned");
        let data = front.data.clone();
        let cs = front.checksum();
        (data, cs)
    }
}

fn main() {
    let buffer_size = 100;
    let db = Arc::new(DoubleBuffer::new(buffer_size));

    // Writer thread
    let d = Arc::clone(&db);
    let writer_handle = thread::spawn(move || {
        for gen in 0..20 {
            let mut data = vec![gen as u64; buffer_size];
            data[0] = gen as u64 * 1000;
            d.write(data);
            std::thread::sleep(std::time::Duration::from_micros(50));
        }
    });

    // Reader threads
    let mut reader_handles = Vec::new();
    for _ in 0..4 {
        let d = Arc::clone(&db);
        reader_handles.push(thread::spawn(move || {
            let mut torn_reads = 0;
            for _ in 0..200 {
                let (data, checksum) = d.read();
                let actual_cs: u64 = data.iter().sum();
                if checksum != actual_cs {
                    torn_reads += 1;
                }
                if !data.is_empty() {
                    let marker = data[0];
                    for i in 1..buffer_size {
                        if i < data.len() && data[i] != marker / 1000 {
                            torn_reads += 1;
                            break;
                        }
                    }
                }
                std::hint::spin_loop();
            }
            torn_reads
        }));
    }

    writer_handle.join().expect("writer panicked");

    let mut total_torn = 0;
    for h in reader_handles {
        let torn = h.join().expect("reader panicked");
        total_torn += torn;
    }

    assert_eq!(total_torn, 0, "double_buffer failed: {} inconsistencies detected", total_torn);

    println!("double_buffer: concurrent writer/readers, zero torn updates — PASS");
}
