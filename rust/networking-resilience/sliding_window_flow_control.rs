#![forbid(unsafe_code)]

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
// Sliding-window flow control that caps outstanding (in-flight) bytes at a fixed window.
// try_send admits a send only when in_flight + bytes <= window_size, adding to the count;
// ack frees bytes with saturating_sub so a duplicate/over-sized ACK can never underflow.
// Use to bound how much unacknowledged data a sender may have on the wire (TCP-style window).
// Guarantees: in_flight never exceeds window_size, and a send that would overflow is refused
// (returns false) leaving the counter unchanged.
struct SlidingWindowFlowControl {
    window_size: u64,
    in_flight: u64,
}

impl SlidingWindowFlowControl {
    fn new(window_size: u64) -> Self {
        Self {
            window_size,
            in_flight: 0,
        }
    }

    fn try_send(&mut self, bytes: u64) -> bool {
        if self.in_flight + bytes <= self.window_size {
            self.in_flight += bytes;
            true
        } else {
            false
        }
    }

    fn ack(&mut self, bytes: u64) {
        self.in_flight = self.in_flight.saturating_sub(bytes);
    }

    fn in_flight_bytes(&self) -> u64 {
        self.in_flight
    }
}

fn main() {
    // Test 1: Send within window
    let mut flow = SlidingWindowFlowControl::new(100);
    assert!(flow.try_send(50), "Send 50 within 100 window");
    assert_eq!(flow.in_flight_bytes(), 50, "In-flight is 50");

    // Test 2: Send more, hit limit
    assert!(flow.try_send(50), "Send another 50");
    assert_eq!(flow.in_flight_bytes(), 100, "In-flight is 100");
    assert!(!flow.try_send(1), "Send 1 more is refused");

    // Test 3: ACK and send again
    flow.ack(30);
    assert_eq!(flow.in_flight_bytes(), 70, "After ACK 30, in-flight is 70");
    assert!(flow.try_send(30), "Can send 30 more");
    assert_eq!(flow.in_flight_bytes(), 100, "Back to 100");

    // Test 4: Exact trace
    let mut flow2 = SlidingWindowFlowControl::new(100);

    assert!(flow2.try_send(40), "First send 40 succeeds");
    assert_eq!(flow2.in_flight_bytes(), 40, "In-flight 40");

    assert!(flow2.try_send(40), "Second send 40 succeeds");
    assert_eq!(flow2.in_flight_bytes(), 80, "In-flight 80");

    assert!(!flow2.try_send(40), "Third send 40 fails (would exceed window)");
    assert_eq!(flow2.in_flight_bytes(), 80, "In-flight unchanged");

    flow2.ack(20);
    assert_eq!(flow2.in_flight_bytes(), 60, "After ACK 20, in-flight 60");

    assert!(flow2.try_send(20), "Send 20 succeeds");
    assert_eq!(flow2.in_flight_bytes(), 80, "Back to 80");

    println!("sliding_window_flow_control: PASS");
}
