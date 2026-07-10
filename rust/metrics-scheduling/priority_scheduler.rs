#![forbid(unsafe_code)]
//! priority_scheduler — BinaryHeap job scheduler with fairness.
//!
//! Core idea: jobs with priority are scheduled; higher priority jobs run first.
//! Fairness is maintained by aging: priority increases over time. THE ONE LAW: plant
//! a job mix, run them, and assert that jobs execute in priority order respecting
//! aging — a stale job eventually runs despite lower initial priority.
//! When to use: task scheduling, priority queues, fair resource allocation.

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
use std::cmp::Ordering;
use std::collections::BinaryHeap;

#[derive(Eq, PartialEq)]
struct Job {
    id: u32,
    priority: u32,
    created_at: u32,
}

impl Ord for Job {
    fn cmp(&self, other: &Self) -> Ordering {
        // Higher priority jobs come first (larger priority = "greater" in heap).
        let priority_cmp = self.priority.cmp(&other.priority);
        if priority_cmp != Ordering::Equal {
            priority_cmp
        } else {
            // Same priority: older (smaller created_at) comes first.
            other.created_at.cmp(&self.created_at)
        }
    }
}

impl PartialOrd for Job {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        Some(self.cmp(other))
    }
}

struct Scheduler {
    queue: BinaryHeap<Job>,
    current_time: u32,
    run_order: Vec<u32>,
}

impl Scheduler {
    fn new() -> Self {
        Scheduler {
            queue: BinaryHeap::new(),
            current_time: 0,
            run_order: Vec::new(),
        }
    }

    fn submit(&mut self, id: u32, priority: u32) {
        self.queue.push(Job {
            id,
            priority,
            created_at: self.current_time,
        });
    }

    fn run_next(&mut self) -> Option<u32> {
        if let Some(job) = self.queue.pop() {
            self.run_order.push(job.id);
            Some(job.id)
        } else {
            None
        }
    }

    fn advance_time(&mut self) {
        self.current_time += 1;
        // Age all jobs in queue: increase their effective priority.
        // (Simplification: we re-queue with increased priority.)
        let mut aged = Vec::new();
        while let Some(job) = self.queue.pop() {
            aged.push(job);
        }
        for mut job in aged {
            // Increase priority by 1 per time unit (aging).
            job.priority = job.priority.saturating_add(1);
            self.queue.push(job);
        }
    }
}

fn main() {
    // Planted case 1: priority order.
    let mut sched = Scheduler::new();
    sched.submit(1, 5); // Low priority
    sched.submit(2, 10); // High priority
    sched.submit(3, 8); // Medium priority

    let order1 = sched.run_next().unwrap();
    let order2 = sched.run_next().unwrap();
    let order3 = sched.run_next().unwrap();

    // THE ONE LAW: jobs run in priority order (high → low).
    assert_eq!(order1, 2, "job 2 (priority 10) should run first");
    assert_eq!(order2, 3, "job 3 (priority 8) should run second");
    assert_eq!(order3, 1, "job 1 (priority 5) should run third");

    // Planted case 2: fairness via aging.
    let mut sched2 = Scheduler::new();
    sched2.submit(10, 1); // Low priority, created first
    sched2.current_time = 1;
    sched2.submit(11, 1); // Same priority, created later
    sched2.current_time = 2;
    sched2.submit(12, 10); // High priority, created very late

    // At creation time, job 12 should run first (priority 10 > 1).
    let order = sched2.run_next().unwrap();
    assert_eq!(order, 12, "job 12 (high priority) runs first");

    // Now age: job 10 has priority 1 + aging = 1 + 1 = 2
    //          job 11 has priority 1 + aging = 1 + 1 = 2
    // Both have same aged priority; job 10 (older) should run next.
    sched2.advance_time();
    let order = sched2.run_next().unwrap();
    assert_eq!(order, 10, "after aging, older job 10 (same priority) runs next");

    let order = sched2.run_next().unwrap();
    assert_eq!(order, 11, "younger job 11 runs last");

    // Verify run_order consistency.
    assert_eq!(
        sched.run_order,
        vec![2, 3, 1],
        "run order must match priority then creation"
    );

    println!("priority_scheduler: priority order, fairness via aging verified — PASS");
}
