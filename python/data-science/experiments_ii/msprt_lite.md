# msprt lite

**Language:** Python · **Sphere:** data-science · **Category:** Experiments II

**Signature:** `(diff_gen: Callable[[], float], alpha: float, tau2: float, v: float, max_n: int) → bool`

## What it does

mSPRT (mixture Sequential Probability Ratio Test): an always-valid test.

Under continuous peeking a fixed-α test inflates type-I badly. The mixture SPRT (Robbins)
mixes the likelihood ratio over a normal prior on the effect, giving a statistic whose
type-I error is controlled UNIFORMLY over all sample sizes (Ville's inequality): you may
peek after every observation and reject the first time Λ_n ≥ 1/α.
Core claim: naive peeking inflates type-I; mSPRT holds type-I under peeking, with power.

## Guarantee

When it runs, msprt lite guarantees msprt_typeI <= 0.06; naive_typeI > 0.2; msprt_power > 0.5 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `msprt_typeI <= 0.06`
- `naive_typeI > 0.2`
- `msprt_power > 0.5`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
