# elo rating

**Language:** C++ · **Sphere:** data-science · **Category:** Rankings & Information Retrieval

**Signature:** `(elo1: float, elo2: float) → float`

## What it does

Elo Rating System.
C++17 self-contained port with full parity to Python oracle.

## Guarantee

When it runs, elo rating guarantees abs(expected_a - expected_a_manual) < 0.001; abs(expected_a - 0.64) < 0.01; elo_a > elo_b (proven by run on the PY original).

**Checkable constraints:**

- `elo_a > elo_b`
- `abs(expected_a - expected_a_manual) < 0.001`
- `abs(expected_a - 0.64) < 0.01`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** — established on the PY original and shared by this C++ twin (twin agreement is the evidence: consensus, xlang); the original oracle was not executed against this file
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
