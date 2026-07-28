# simpsons paradox demo

**Language:** C++ · **Sphere:** data-science · **Category:** Applied DS Practice

**Signature:** `(numerator: int, denominator: int) → float`

## What it does

Simpson's Paradox: aggregate trend reverses within strata.
C++17 self-contained implementation.

## Guarantee

When it runs, simpsons paradox demo guarantees not b_wins_aggregate (weak-grade: directional, proven by run on the PY original).

**Checkable constraints:**

- `b_wins_s1`
- `b_wins_s2`
- `not b_wins_aggregate`
- `paradox_detected`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** — established on the PY original and shared by this C++ twin (twin agreement is the evidence: consensus, xlang); the original oracle was not executed against this file
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `def compute_rate(numerator: int, denominator: int) -> float:`
**Valid input:** `denominator > 0`; `0 <= numerator <= denominator`.
**Core:** Demonstrates Simpson's paradox: treatment B can beat treatment A within every stratum yet lose in the aggregate because the strata have different base rates and unequal treatment allocation.
**Assert:** On the planted two-strata example, B wins stratum 1 (90% vs 80%), B wins stratum 2 (12% vs 10%), but A wins aggregate (73% vs 19%). The paradox is detected and asserted.
**⚠ Retrofit NOT in this twin:** a defect noted in the 2026-07-20 audit was corrected by the AURA-E input-contract retrofit on the PY original (7497d40, 2026-07-21). That pass deliberately excluded the compiled lanes, so this C++ twin does NOT carry the contract its source now enforces. Declared in MANIFEST.json `twin_contract_divergence`; unblocking it needs the cpp attack lane. Corrected 2026-07-28 — the card previously claimed the fix was in this file.

---
*△ AURA Pattern Library — © Reality Optimizer*
