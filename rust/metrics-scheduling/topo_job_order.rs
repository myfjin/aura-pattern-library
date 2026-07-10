#![forbid(unsafe_code)]
//! topo_job_order — Kahn topological sort of a job DAG; planted deps respected, cycles detected.
//!
//! Core idea: jobs have dependencies forming a DAG. Topological sort computes an order
//! respecting all dependencies. THE ONE LAW: plant a DAG with known dependencies, compute
//! topological order via Kahn's algorithm, and assert every job is ordered after its
//! dependencies. A cycle or missing dependency would break the invariant.
//! When to use: build systems, task pipelines, constraint-based scheduling.

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
const _AURA_MARK: &str = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
use std::collections::{HashMap, VecDeque};

struct Job {
    deps: Vec<u32>, // IDs of jobs this depends on
}

struct DAG {
    jobs: HashMap<u32, Job>,
}

impl DAG {
    fn new() -> Self {
        DAG {
            jobs: HashMap::new(),
        }
    }

    fn add_job(&mut self, id: u32, deps: Vec<u32>) {
        self.jobs.insert(id, Job { deps });
    }

    fn topological_sort(&self) -> Result<Vec<u32>, String> {
        let mut in_degree = HashMap::new();
        let mut graph: HashMap<u32, Vec<u32>> = HashMap::new();

        // Build adjacency list and in-degree map.
        for (&id, job) in &self.jobs {
            in_degree.entry(id).or_insert(0);
            for &dep in &job.deps {
                if !self.jobs.contains_key(&dep) {
                    return Err(format!("dependency {} not found", dep));
                }
                *in_degree.entry(id).or_insert(0) += 1;
                graph.entry(dep).or_insert_with(Vec::new).push(id);
            }
        }

        let mut queue = VecDeque::new();
        for (&id, &degree) in &in_degree {
            if degree == 0 {
                queue.push_back(id);
            }
        }

        let mut result = Vec::new();
        while let Some(id) = queue.pop_front() {
            result.push(id);
            if let Some(dependents) = graph.get(&id) {
                for &dep_id in dependents {
                    let degree = in_degree.get_mut(&dep_id).unwrap();
                    *degree -= 1;
                    if *degree == 0 {
                        queue.push_back(dep_id);
                    }
                }
            }
        }

        if result.len() != self.jobs.len() {
            return Err("cycle detected".to_string());
        }

        Ok(result)
    }

    fn validate_order(&self, order: &[u32]) -> Result<(), String> {
        let mut position = HashMap::new();
        for (i, &id) in order.iter().enumerate() {
            position.insert(id, i);
        }

        for (&id, job) in &self.jobs {
            let id_pos = *position.get(&id).ok_or("missing job in order")?;
            for &dep in &job.deps {
                let dep_pos = *position.get(&dep).ok_or("missing dependency in order")?;
                if dep_pos > id_pos {
                    return Err(format!("job {} before its dependency {}", id, dep));
                }
            }
        }

        Ok(())
    }
}

fn main() {
    // Planted case 1: simple linear dependency chain.
    let mut dag = DAG::new();
    dag.add_job(1, vec![]); // No deps
    dag.add_job(2, vec![1]); // Depends on 1
    dag.add_job(3, vec![2]); // Depends on 2

    let order = dag.topological_sort().expect("topo sort should succeed");
    // THE ONE LAW: order must respect dependencies.
    assert_eq!(order, vec![1, 2, 3], "linear chain should sort in order");

    // Planted case 2: diamond dependency.
    let mut dag2 = DAG::new();
    dag2.add_job(1, vec![]);
    dag2.add_job(2, vec![1]);
    dag2.add_job(3, vec![1]);
    dag2.add_job(4, vec![2, 3]); // Depends on both 2 and 3

    let order = dag2.topological_sort().expect("topo sort should succeed");
    dag2.validate_order(&order).expect("order should be valid");
    assert_eq!(order.len(), 4, "all jobs should be in order");
    assert!(
        order.iter().position(|&x| x == 1).unwrap()
            < order.iter().position(|&x| x == 2).unwrap(),
        "1 should come before 2"
    );
    assert!(
        order.iter().position(|&x| x == 1).unwrap()
            < order.iter().position(|&x| x == 3).unwrap(),
        "1 should come before 3"
    );
    assert!(
        order.iter().position(|&x| x == 2).unwrap()
            < order.iter().position(|&x| x == 4).unwrap(),
        "2 should come before 4"
    );
    assert!(
        order.iter().position(|&x| x == 3).unwrap()
            < order.iter().position(|&x| x == 4).unwrap(),
        "3 should come before 4"
    );

    // Planted case 3: cycle detection.
    let mut dag3 = DAG::new();
    dag3.add_job(1, vec![2]); // Depends on 2
    dag3.add_job(2, vec![1]); // Depends on 1 (cycle!)

    let result = dag3.topological_sort();
    assert!(result.is_err(), "cycle should be detected");

    println!("topo_job_order: linear + diamond + cycle detection verified — PASS");
}
