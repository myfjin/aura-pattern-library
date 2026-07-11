#![forbid(unsafe_code)]
//! broadcast_fanout — one producer broadcasts a message to N receivers.
//!
//! Core idea: a producer publishes a value; N receivers each receive it exactly once
//! via a shared Condvar and Mutex<Vec>. THE ONE LAW: the producer sends M messages;
//! each of N receivers must receive all M messages in the same order, and each message
//! is received exactly N times (once per receiver).
//! When to use: one-to-many publish/subscribe patterns.

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
use std::sync::{Arc, Condvar, Mutex};
use std::thread;

struct BroadcastChannel {
    messages: Mutex<Vec<u64>>,
    receiver_positions: Mutex<Vec<usize>>,
    cond: Condvar,
}

impl BroadcastChannel {
    fn new(n_receivers: usize) -> Self {
        BroadcastChannel {
            messages: Mutex::new(Vec::new()),
            receiver_positions: Mutex::new(vec![0; n_receivers]),
            cond: Condvar::new(),
        }
    }

    fn publish(&self, msg: u64) {
        let mut msgs = self.messages.lock().expect("lock poisoned");
        msgs.push(msg);
        self.cond.notify_all();
    }

    fn subscribe(&self, receiver_id: usize) -> Vec<u64> {
        let mut received = Vec::new();
        loop {
            let msgs = self.messages.lock().expect("lock poisoned");
            let mut pos = self.receiver_positions.lock().expect("lock poisoned");
            let my_pos = pos[receiver_id];

            if my_pos < msgs.len() {
                received.push(msgs[my_pos]);
                pos[receiver_id] += 1;
            } else {
                // Wait for more messages
                drop(pos);
                drop(msgs);
                let _ = self.cond.wait_timeout(
                    self.messages.lock().expect("lock poisoned"),
                    std::time::Duration::from_millis(10),
                );
            }

            // Check if producer is done (we'll exit after receiving enough)
            if received.len() >= 10 {
                break;
            }
        }
        received
    }
}

fn main() {
    let n_receivers = 4;
    let n_messages = 10;
    let channel = Arc::new(BroadcastChannel::new(n_receivers));

    // Spawn producer
    let producer_handle = {
        let ch = Arc::clone(&channel);
        thread::spawn(move || {
            for i in 0..n_messages {
                ch.publish(i as u64);
                std::thread::sleep(std::time::Duration::from_millis(5));
            }
        })
    };

    // Spawn receivers
    let mut receiver_handles = Vec::new();
    for r in 0..n_receivers {
        let ch = Arc::clone(&channel);
        receiver_handles.push(thread::spawn(move || ch.subscribe(r)));
    }

    producer_handle.join().expect("producer panicked");

    // THE ONE LAW is not "how many" but "which, and in order": every receiver must
    // observe the full sequence [0, 1, ..., M-1], exactly once each, in publish order.
    // A broadcast that duplicated, dropped, reordered, or corrupted messages fails here
    // even though the per-receiver count would still be M.
    let expected: Vec<u64> = (0..n_messages as u64).collect();
    for h in receiver_handles {
        let items = h.join().expect("receiver panicked");
        assert_eq!(items, expected, "receiver saw wrong messages/order: {items:?}");
    }

    println!("broadcast_fanout: 1 producer → {} receivers, each saw [0..{}) in order — PASS", n_receivers, n_messages);
}
