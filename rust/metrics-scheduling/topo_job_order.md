# topo job order

**Language:** Rust · **Sphere:** rust · **Category:** metrics-scheduling

**Signature:** `(id: u32, deps: Vec<u32>) → ?`

## What it does

topo_job_order — Kahn topological sort of a job DAG; planted deps respected, cycles detected.

Core idea: jobs have dependencies forming a DAG. Topological sort computes an order
respecting all dependencies. THE ONE LAW: plant a DAG with known dependencies, compute
topological order via Kahn's algorithm, and assert every job is ordered after its
dependencies. A cycle or missing dependency would break the invariant.
When to use: build systems, task pipelines, constraint-based scheduling.

## Guarantee

When it runs, topo job order guarantees assert_eq!(order.len(), 4, "all jobs should be in order"); assert!(order.iter().position(|&x| x == 1).unwrap() < order.iter().position(|&x| x == 2).unwrap(), "1 should come before 2"); assert!(order.iter().position(|&x| x == 1).unwrap() < order.iter().position(|&x| x == 3).unwrap(), "1 should come before 3") (proven by rustc-run).

**Checkable constraints:**

- `assert_eq!(order, vec![1, 2, 3], "linear chain should sort in order")`
- `assert_eq!(order.len(), 4, "all jobs should be in order")`
- `assert!(order.iter().position(|&x| x == 1).unwrap() < order.iter().position(|&x| x == 2).unwrap(), "1 should come before 2")`
- `assert!(order.iter().position(|&x| x == 1).unwrap() < order.iter().position(|&x| x == 3).unwrap(), "1 should come before 3")`
- `assert!(order.iter().position(|&x| x == 2).unwrap() < order.iter().position(|&x| x == 4).unwrap(), "2 should come before 4")`
- `assert!(order.iter().position(|&x| x == 3).unwrap() < order.iter().position(|&x| x == 4).unwrap(), "3 should come before 4")`
- `assert!(result.is_err(), "cycle should be detected")`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — none yet (green-run candidate; not an axiom under the frozen ruler)
- **Peer review:** unreviewed

---
*△ AURA Pattern Library — © Reality Optimizer*
