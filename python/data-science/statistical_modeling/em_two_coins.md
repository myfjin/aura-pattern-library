# em two coins

**Language:** Python · **Sphere:** data-science · **Category:** Statistical Modeling

**Signature:** `(sessions: List[List[int]], p_a_init: float, p_b_init: float, n_iter: int) → Tuple[float, float]`

## What it does

Expectation-Maximization (EM) Algorithm: Two-Coin Problem.

Estimates two coin biases from mixed flip sessions without labels.
The classic EM example: data is ambiguous (which coin produced each session?).
Use when data is incomplete or missing labels for mixture components.

## Guarantee

When it runs, em two coins guarantees min_error < 0.3 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `min_error < 0.3`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `em_two_coins(sessions, p_a_init=0.6, p_b_init=0.4, n_iter=50) → (p_a, p_b)`
**Valid input:** `sessions: List[List[int]]` — each session is a list of flips (1=heads, 0=tails). `n_iter ≥ 1`.
**Core:** Classic EM for two-coin problem. E-step: compute posterior probability that each session came from coin A (using current bias estimates). M-step: update bias estimates as weighted averages of heads/tails counts. Handles label switching by checking both orderings.
**Assert:** On 100 sessions (30 flips each) from coins with p=0.8 and p=0.3, 100 EM iterations, min recovery error < 0.3 (accounting for label switching).
**✔ Retrofitted:** a defect noted in the 2026-07-20 audit was corrected by the AURA-E retrofit pass; the current signed code reflects the fix.

---
*△ AURA Pattern Library — © Reality Optimizer*
