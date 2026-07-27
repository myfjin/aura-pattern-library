# peeking alpha inflation

**Language:** Python · **Sphere:** data-science · **Category:** Experiments II

**Signature:** `(mean_treatment: float, mean_control: float, var_t: float, var_c: float, n_t: int, n_c: int) → float`

## What it does

Peeking alpha inflation: continuous peeking at a fixed-n test inflates type-I error.

Run test, peek at p-value, continue collecting if not significant, re-test.
This inflates type-I from α=5% to ~20-30%. Core claim: peeking breaks type-I guarantee;
measured over replications under null hypothesis.

## Guarantee

When it runs, peeking alpha inflation guarantees type_i_no_peek < 0.12; type_i_peek > type_i_no_peek * 2.0 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `type_i_no_peek < 0.12`
- `type_i_peek > type_i_no_peek * 2.0`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
