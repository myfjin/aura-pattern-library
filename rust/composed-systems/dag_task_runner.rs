#![forbid(unsafe_code)]
//! dag_task_runner — topological readiness + a real thread worker-pool executing a DAG.
//!
//! Core idea: composes W2's topological ordering with W1's shared-queue worker pool. Tasks with
//! satisfied dependencies land on a shared ready-queue; N worker threads pull and run them, and
//! on completion release dependents (decrement in-degree, enqueue newly-ready) under a Condvar.
//! Because a task is enqueued ONLY after every dependency has committed, deps always run first —
//! even under parallel scheduling. THE LAW: run a DAG on multiple threads and assert (1) every
//! task ran exactly once, (2) each task ran AFTER all its deps (checked against the real exec log),
//! (3) the aggregate is exact, and (4) a cycle is rejected. When to use: build systems, workflows.

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
use std::collections::VecDeque;
use std::sync::{Arc, Condvar, Mutex};
use std::thread;

struct Task {
    deps: Vec<usize>,
    value: usize,
}

struct Shared {
    ready: VecDeque<usize>,
    in_degree: Vec<usize>,
    dependents: Vec<Vec<usize>>,
    values: Vec<usize>,
    results: Vec<Option<usize>>,
    exec_order: Vec<usize>, // real completion order under threads
    completed: usize,
    total: usize,
}

fn execute_parallel(tasks: &[Task], workers: usize) -> Result<(Vec<Option<usize>>, Vec<usize>), String> {
    let n = tasks.len();
    let mut in_degree = vec![0usize; n];
    let mut dependents = vec![Vec::new(); n];
    for (i, t) in tasks.iter().enumerate() {
        for &d in &t.deps {
            if d >= n {
                return Err(format!("invalid dep {d}"));
            }
            dependents[d].push(i);
            in_degree[i] += 1;
        }
    }
    // Cycle check up-front (Kahn count) so the pool can never deadlock on a cyclic graph.
    {
        let mut deg = in_degree.clone();
        let mut q: VecDeque<usize> = (0..n).filter(|&i| deg[i] == 0).collect();
        let mut seen = 0;
        while let Some(u) = q.pop_front() {
            seen += 1;
            for &v in &dependents[u] {
                deg[v] -= 1;
                if deg[v] == 0 {
                    q.push_back(v);
                }
            }
        }
        if seen != n {
            return Err("cycle detected".to_string());
        }
    }

    let ready: VecDeque<usize> = (0..n).filter(|&i| in_degree[i] == 0).collect();
    let shared = Arc::new((
        Mutex::new(Shared {
            ready,
            in_degree,
            dependents,
            values: tasks.iter().map(|t| t.value).collect(),
            results: vec![None; n],
            exec_order: Vec::new(),
            completed: 0,
            total: n,
        }),
        Condvar::new(),
    ));

    let mut handles = Vec::new();
    for _ in 0..workers.max(1) {
        let shared = Arc::clone(&shared);
        handles.push(thread::spawn(move || {
            let (lock, cv) = &*shared;
            loop {
                // Wait for a ready task, or exit when all are done.
                let task_id = {
                    let mut st = lock.lock().expect("poisoned");
                    loop {
                        if let Some(id) = st.ready.pop_front() {
                            break id;
                        }
                        if st.completed >= st.total {
                            return; // all work finished
                        }
                        st = cv.wait(st).expect("wait");
                    }
                };
                // Do the "work" OUTSIDE the lock.
                let result = {
                    let st = lock.lock().expect("poisoned");
                    st.values[task_id] * 2
                };
                // Commit: record result, release dependents, wake others.
                {
                    let mut st = lock.lock().expect("poisoned");
                    st.results[task_id] = Some(result);
                    st.exec_order.push(task_id);
                    st.completed += 1;
                    let deps_of: Vec<usize> = st.dependents[task_id].clone();
                    for v in deps_of {
                        st.in_degree[v] -= 1;
                        if st.in_degree[v] == 0 {
                            st.ready.push_back(v);
                        }
                    }
                    cv.notify_all();
                }
            }
        }));
    }
    for h in handles {
        h.join().expect("worker panicked");
    }

    let st = Arc::try_unwrap(shared).ok().unwrap().0.into_inner().unwrap();
    Ok((st.results, st.exec_order))
}

fn main() {
    // DAG: 0 → 1 → 2, and 0 → 3.
    let tasks = vec![
        Task { deps: vec![], value: 10 },
        Task { deps: vec![0], value: 20 },
        Task { deps: vec![1], value: 30 },
        Task { deps: vec![0], value: 40 },
    ];

    let (results, exec_order) = execute_parallel(&tasks, 3).expect("should execute");

    // (1) every task ran exactly once.
    assert_eq!(exec_order.len(), 4, "all tasks ran once");
    assert!(results.iter().all(|r| r.is_some()), "every task produced a result");

    // (2) each task ran AFTER its deps — checked against the real parallel execution log.
    let pos: std::collections::HashMap<usize, usize> =
        exec_order.iter().enumerate().map(|(p, &t)| (t, p)).collect();
    for (i, t) in tasks.iter().enumerate() {
        for &d in &t.deps {
            assert!(pos[&d] < pos[&i], "dep {d} must complete before task {i} (order {exec_order:?})");
        }
    }

    // (3) aggregate exact regardless of scheduling.
    let total: usize = results.iter().map(|r| r.unwrap()).sum();
    assert_eq!(total, (10 + 20 + 30 + 40) * 2, "aggregate exact");

    // (4) a cycle is rejected (no deadlock).
    let cycle = vec![
        Task { deps: vec![1], value: 1 },
        Task { deps: vec![0], value: 2 },
    ];
    assert!(execute_parallel(&cycle, 2).is_err(), "cycle detected, not deadlocked");

    println!("dag_task_runner: parallel worker pool honors deps, all-once, aggregate exact — PASS");
}
