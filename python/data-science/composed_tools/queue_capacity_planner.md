# queue capacity planner

**Language:** Python · **Sphere:** data-science · **Category:** Composed Tools

**Signature:** `(arrival_rate: float, service_rate: float, workers: int, n_jobs: int, seed: int) → Dict[str, float]`

## Guarantee

When it runs, queue capacity planner guarantees served == len(arrivals); rel_err < 0.05; at['mean_wait'] <= sla (weak-grade: directional, proven by run).

**Checkable constraints:**

- `served == len(arrivals)`
- `rel_err < 0.05`
- `at['mean_wait'] <= sla`
- `below['mean_wait'] > sla`
- `all((curve[a] >= curve[b] - 1e-09 for a, b in zip(ks, ks[1:])))`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
