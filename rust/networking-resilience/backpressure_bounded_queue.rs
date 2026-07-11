#![forbid(unsafe_code)]

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
#[derive(Debug, Clone, Copy, PartialEq)]
enum BackpressureState {
    Go,
    Stop,
}

struct BackpressureBoundedQueue {
    high_watermark: usize,
    low_watermark: usize,
    queue: Vec<u64>,
    state: BackpressureState,
}

impl BackpressureBoundedQueue {
    fn new(high_watermark: usize, low_watermark: usize) -> Self {
        assert!(low_watermark < high_watermark);
        Self {
            high_watermark,
            low_watermark,
            queue: Vec::new(),
            state: BackpressureState::Go,
        }
    }

    fn push(&mut self, item: u64) -> BackpressureState {
        self.queue.push(item);
        if self.queue.len() >= self.high_watermark {
            self.state = BackpressureState::Stop;
        }
        self.state
    }

    fn pop(&mut self) -> Option<u64> {
        if self.queue.is_empty() {
            return None;
        }
        let item = self.queue.remove(0);
        if self.queue.len() < self.low_watermark {
            self.state = BackpressureState::Go;
        }
        Some(item)
    }

    fn size(&self) -> usize {
        self.queue.len()
    }

    fn state(&self) -> BackpressureState {
        self.state
    }
}

fn main() {
    // Test 1: Basic transitions
    let mut bq = BackpressureBoundedQueue::new(5, 2);
    assert_eq!(bq.state(), BackpressureState::Go, "Initial state is Go");

    // Push to high watermark
    for i in 0..5 {
        let state = bq.push(i);
        if i < 4 {
            assert_eq!(state, BackpressureState::Go, "State Go until high watermark");
        } else {
            assert_eq!(state, BackpressureState::Stop, "State Stop at high watermark");
        }
    }
    assert_eq!(bq.size(), 5, "Queue has 5 items");

    // Pop below low watermark
    while bq.size() > 2 {
        bq.pop();
    }
    assert_eq!(bq.size(), 2, "Queue at low watermark");
    assert_eq!(bq.state(), BackpressureState::Stop, "Still Stop at low watermark");

    // Pop one more to go below low watermark
    bq.pop();
    assert_eq!(bq.size(), 1, "Queue has 1");
    assert_eq!(bq.state(), BackpressureState::Go, "State transitions to Go below low watermark");

    // Test 2: Exact transition sequence
    let mut bq2 = BackpressureBoundedQueue::new(3, 1);
    let mut states = Vec::new();
    states.push(bq2.state());

    for i in 0..4 {
        states.push(bq2.push(i));
    }
    // State at [0, 1, 2, 3] should be [Go, Go, Go, Stop]
    assert_eq!(states[0], BackpressureState::Go, "t=0");
    assert_eq!(states[1], BackpressureState::Go, "t=1");
    assert_eq!(states[2], BackpressureState::Go, "t=2");
    assert_eq!(states[3], BackpressureState::Stop, "t=3");

    // Pop down: size=4 → 3 → 2 → 1 → 0
    bq2.pop(); // size=3, not < 1, still Stop
    assert_eq!(bq2.state(), BackpressureState::Stop, "Still Stop at size=3");
    bq2.pop(); // size=2, not < 1, still Stop
    assert_eq!(bq2.state(), BackpressureState::Stop, "Still Stop at size=2");
    bq2.pop(); // size=1, not < 1, still Stop
    assert_eq!(bq2.state(), BackpressureState::Stop, "Still Stop at size=1");
    bq2.pop(); // size=0, is < 1, now Go
    assert_eq!(bq2.state(), BackpressureState::Go, "Back to Go when size < low");

    println!("backpressure_bounded_queue: PASS");
}
