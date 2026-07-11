#![forbid(unsafe_code)]
//! future_lite_executor — a tiny single-threaded executor for state-machine tasks.
//!
//! Core idea: a set of tasks, each with a simple state machine (pending/ready/done).
//! The executor polls all tasks to completion in a loop. THE ONE LAW: create N tasks
//! with dependencies (task B waits on task A). Run the executor; all tasks must
//! complete, and task B must never run before task A finishes.
//! When to use: cooperative multitasking and executor patterns.

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
use std::sync::{Arc, Mutex};

#[derive(Clone, Copy, PartialEq, Eq)]
enum TaskState {
    Pending,
    Done,
}

struct Task {
    id: usize,
    state: TaskState,
    depends_on: Option<usize>,
}

struct Executor {
    tasks: Arc<Mutex<Vec<Task>>>,
}

impl Executor {
    fn new() -> Self {
        Executor {
            tasks: Arc::new(Mutex::new(Vec::new())),
        }
    }

    fn add_task(&self, id: usize, depends_on: Option<usize>) {
        let mut tasks = self.tasks.lock().expect("lock poisoned");
        tasks.push(Task {
            id,
            state: TaskState::Pending,
            depends_on,
        });
    }

    fn run(&self) -> Vec<usize> {
        let mut execution_order = Vec::new();
        loop {
            let mut tasks = self.tasks.lock().expect("lock poisoned");
            let mut progress = false;

            for i in 0..tasks.len() {
                if tasks[i].state == TaskState::Pending {
                    // Check if dependency is done
                    let can_run = if let Some(dep_id) = tasks[i].depends_on {
                        tasks
                            .iter()
                            .find(|t| t.id == dep_id)
                            .map(|t| t.state == TaskState::Done)
                            .unwrap_or(false)
                    } else {
                        true
                    };

                    if can_run {
                        tasks[i].state = TaskState::Done;
                        execution_order.push(tasks[i].id);
                        progress = true;
                    }
                }
            }

            if !progress {
                break;
            }
        }

        execution_order
    }
}

fn main() {
    let executor = Executor::new();

    // Create tasks: 0 → 1 → 2, and 0 → 3
    executor.add_task(0, None);
    executor.add_task(1, Some(0));
    executor.add_task(2, Some(1));
    executor.add_task(3, Some(0));

    let order = executor.run();

    // Verify all tasks ran
    assert_eq!(order.len(), 4, "not all tasks executed");

    // Verify dependency order: 0 before 1,3 and 1 before 2
    let pos = |id| order.iter().position(|&x| x == id).unwrap();
    assert!(pos(0) < pos(1), "task 0 should run before 1");
    assert!(pos(0) < pos(3), "task 0 should run before 3");
    assert!(pos(1) < pos(2), "task 1 should run before 2");

    println!("future_lite_executor: {} tasks executed in dependency order — PASS", order.len());
}
