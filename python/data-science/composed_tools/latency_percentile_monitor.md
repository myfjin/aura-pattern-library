# latency percentile monitor

**Language:** Python · **Sphere:** data-science · **Category:** Composed Tools

**Signature:** `(base: float, tail: float) → float`

## Guarantee

When it runs, latency percentile monitor guarantees abs(snap1['p99'] - exact_p99_1) / exact_p99_1 < 0.15; abs(snap2['p99'] - exact_p99_2) / exact_p99_2 < 0.15; abs(snap2['p50'] - snap1['p50']) / snap1['p50'] < 0.25 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `abs(snap1['p99'] - exact_p99_1) / exact_p99_1 < 0.15`
- `abs(snap2['p99'] - exact_p99_2) / exact_p99_2 < 0.15`
- `abs(snap2['p50'] - snap1['p50']) / snap1['p50'] < 0.25`
- `snap2['p99'] > 2.0 * snap1['p99']`
- `len(mon2.services['api']['p99'].q) == 5`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
