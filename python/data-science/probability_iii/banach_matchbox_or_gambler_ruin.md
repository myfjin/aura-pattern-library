# banach matchbox or gambler ruin

**Language:** Python · **Sphere:** data-science · **Category:** Probability III

**Signature:** `(a: int, b: int, p: float) → float`

## What it does

Gambler's ruin: absorption probability of a bounded ±1 random walk.

A gambler starts with wealth a against an opponent with b (total N = a+b); each play
moves wealth ±1 (P(+1)=p). "Ruin" = hitting 0 before N. The classic result:
    p = q = ½:  P(ruin) = b/(a+b)          (= (N−a)/N)
    p ≠ q:      P(ruin) = (rᴺ − rᵃ)/(rᴺ − 1),  r = q/p.
Core claim: the exact ruin probability matches simulation — verified on an ASYMMETRIC
game so the answer is not the self-symmetric ½ (where ruin ≡ survival and any sign error
would hide).

## Guarantee

When it runs, banach matchbox or gambler ruin guarantees abs(exact_fair - b / (a + b)) < 1e-09; abs(exact_fair - sim_fair) < 0.03; exact_biased < 0.1 (proven by run).

**Checkable constraints:**

- `abs(exact_fair - b / (a + b)) < 1e-09`
- `abs(exact_fair - sim_fair) < 0.03`
- `exact_biased < 0.1`
- `abs(exact_biased - sim_biased) < 0.03`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
