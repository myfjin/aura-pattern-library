# kelly criterion

**Language:** Python · **Sphere:** data-science · **Category:** Simulation & Decision Science

**Signature:** `() → None`

## What it does

Kelly Criterion: optimal betting fraction for long-run log-growth.

Kelly fraction f* = (p*b - q) / b where p = win prob, q = loss prob, b = odds.
Overbetting (2x Kelly) produces lower median terminal wealth: the classic warning.

## Guarantee

When it runs, kelly criterion guarantees med_k > med_o; logg_k > logg_o; paired_wins / n_paths > 0.6 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `med_k > med_o`
- `logg_k > logg_o`
- `paired_wins / n_paths > 0.6`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `def kelly_criterion() -> None:`, `def simulate_wealth(fraction: float, n_bets: int, seed_offset: int = 0) -> list[float]:`
**Valid input:** `fraction` ∈ [0, 1]; `n_bets` > 0; `seed_offset` any integer.
**Core:** Kelly criterion: optimal bet fraction `f* = (p·b − q) / b`. Demonstrates that full Kelly maximizes median terminal wealth and mean log-growth compared to overbetting (2× Kelly) across 300 paired seeded paths.
**Assert:** With `p_win = 0.6`, `odds = 1.0`, Kelly fraction is `0.2`; Kelly's median terminal wealth and mean log-growth exceed 2× Kelly's, and Kelly wins more than 60% of paired paths.
**⚠️ Defect:** `simulate_wealth` reseeds with `42 + seed_offset`, so different fractions on the same path are correlated by the same base seed, but the same `seed_offset` always produces the same sequence — the randomness is fully deterministic per path. The win/loss probability is hardcoded inside `kelly_criterion`; `simulate_wealth` cannot be used for arbitrary bet probabilities.

---
*△ AURA Pattern Library — © Reality Optimizer*
