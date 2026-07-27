# ipw ate

**Language:** Python · **Sphere:** data-science · **Category:** Causal Inference II

**Signature:** `(t_vals: List[int], y_vals: List[float], propensity: List[float]) → float`

## What it does

Inverse Propensity Weighting (IPW) for the Average Treatment Effect (ATE).

Observational data X→T, X→Y (X confounds T→Y). IPW re-weights by 1/P(T|X) to simulate
randomization. Uses the STABILIZED (Hájek / self-normalized) estimator — normalizing the
weights within each arm — which is far less volatile than the raw Horvitz–Thompson sum.
Core claim: the naive group-mean comparison is biased; stabilized IPW recovers the ATE.

## Guarantee

When it runs, ipw ate guarantees abs(ipw - 2.0) < 0.6; abs(ipw - 2.0) < abs(naive - 2.0); abs(naive - 2.0) > 0.3 (proven by run).

**Checkable constraints:**

- `abs(ipw - 2.0) < 0.6`
- `abs(naive - 2.0) > 0.3`
- `abs(ipw - 2.0) < abs(naive - 2.0)`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
