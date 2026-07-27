# peeking alpha inflation

**Language:** C++ · **Sphere:** data-science · **Category:** Experiments II

**Signature:** `(mean_treatment: float, mean_control: float, var_t: float, var_c: float, n_t: int, n_c: int) → float`

## What it does

peeking_alpha_inflation — C++17 twin of the sealed DS oracle.

Claim (mechanism, not tolerance-tuned): continuous peeking at a fixed-n test
inflates the type-I error rate from the nominal ~5% to ~20-30%. Measured over
replications under the null hypothesis.

Oracle: ~/ai-lab/patterns_ds/harvested/peeking_alpha_inflation.py
Seal   : 3abd742ac574c7f6f272dc8d5a9f2077e229464a05c77ab16b770523f0f0e6b4
Builder seat: opus-A (4Q capped, 2026-07-12). Staging only — never self-approved.

Portability: standard C++17, STL only. RNG is std::mt19937(42) (identical stream
on every platform); gaussians come from an in-file Box-Muller, NOT
std::normal_distribution (whose sequence differs across libstdc++/libc++). The
twin therefore does NOT reproduce Python's Mersenne/gauss draw sequence — it is
faithful by construction, and the two recovery asserts are mechanism claims that
hold independent of the exact draws (see report Divergences).

## Guarantee

When it runs, peeking alpha inflation guarantees type_i_no_peek < 0.12; type_i_peek > type_i_no_peek * 2.0 (weak-grade: directional, proven by run on the PY original).

**Checkable constraints:**

- `type_i_no_peek < 0.12`
- `type_i_peek > type_i_no_peek * 2.0`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — established on the PY original and shared by this C++ twin (twin agreement is the evidence: consensus, xlang); the original oracle was not executed against this file
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
