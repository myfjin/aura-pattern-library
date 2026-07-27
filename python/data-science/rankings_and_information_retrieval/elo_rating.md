# elo rating

**Language:** Python · **Sphere:** data-science · **Category:** Rankings & Information Retrieval

**Signature:** `(elo1: float, elo2: float) → float`

## What it does

Elo Rating System.

Maintain skill ratings via pairwise wins/losses.
Elo(new) = Elo(old) + K * (observed - expected).
Expected score = 1 / (1 + 10^((opponent_elo - my_elo)/400)).
We plant a stronger player and verify their Elo converges higher; hand-verify
the expected-score formula against observed win rate.

## Guarantee

When it runs, elo rating guarantees abs(expected_a - expected_a_manual) < 0.001; abs(expected_a - 0.64) < 0.01; elo_a > elo_b (proven by run).

**Checkable constraints:**

- `elo_a > elo_b`
- `abs(expected_a - expected_a_manual) < 0.001`
- `abs(expected_a - 0.64) < 0.01`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
