# hazard vs survival conversion

**Language:** Python · **Sphere:** data-science · **Category:** Survival & Reliability

**Signature:** `(S: Callable[[float], float], t: float, eps: float) → float`

## What it does

Hazard-survival conversion: verify duality h(t) = -d/dt[log S(t)].

Given S(t) or h(t), derive the other and check consistency. Planted S(t),
compute h(t), then reconstruct S(t) from h(t); verify round-trip.

## Guarantee

When it runs, hazard vs survival conversion guarantees abs(h_est - h_true) < 0.01; abs(S_recon - S_true) < 1e-10 (proven by run).

**Checkable constraints:**

- `abs(h_est - h_true) < 0.01`
- `abs(S_recon - S_true) < 1e-10`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `def hazard_from_survival(S: Callable[[float], float], t: float, eps: float = 1e-6) -> float:`, `def survival_from_cumhazard(H: Callable[[float], float], t: float) -> float:`, `def S_planted(t: float) -> float:`, `def H_planted(t: float) -> float:`
**Valid input:** `S` is a positive survival function near `t`; `H` is a non-negative cumulative hazard function at `t`; `eps` > 0 and small.
**Core:** Verifies the survival-hazard duality: `h(t) = −d/dt[log S(t)]` and `S(t) = exp(−H(t))`. Uses a central finite difference to estimate the hazard from a survival function and reconstructs survival from a cumulative hazard.
**Assert:** For planted exponential survival `S(t) = exp(−0.1·t)`, the estimated hazard at `t=5` is within 0.01 of `λ=0.1`; reconstructing survival from `H(t)=0.1·t` matches the true survival within 1e-10.
**⚠️ Defect:** `hazard_from_survival` returns `0.0` if either `S(t+eps)` or `S(t−eps)` is below `1e-14`, hiding the true hazard for very small survival probabilities. The finite-difference approximation can be inaccurate if `S` is not smooth or if `eps` is too large/small. The planted helper functions are hardcoded.

---
*△ AURA Pattern Library — © Reality Optimizer*
