# garch lite volatility clustering

**Language:** Python · **Sphere:** data-science · **Category:** Econometrics & Finance

**Signature:** `(returns: List[float], max_pass: int) → Tuple[float, float, float]`

## What it does

GARCH(1,1): volatility clustering via autoregressive conditional heteroskedasticity.

σ²_t = ω + α·ε²_{t-1} + β·σ²_{t-1}. The ARCH coefficient α measures how strongly a
large shock today raises tomorrow's variance — the signature of volatility clustering.
Core claim: fitting GARCH to clustered returns recovers a POSITIVE α (clustering
present); fitting to iid returns drives α→0 (no clustering). All three params (ω, α, β)
are estimated by coordinate ascent on the Gaussian log-likelihood.

## Guarantee

When it runs, garch lite volatility clustering guarantees alpha_cluster > alpha_iid; alpha_cluster > 0.02; alpha_iid >= 0 and beta_iid >= 0 and (alpha_iid + beta_iid < 1.0) (weak-grade: directional, proven by run).

**Checkable constraints:**

- `alpha_cluster > alpha_iid`
- `alpha_cluster > 0.02`
- `alpha_iid >= 0 and beta_iid >= 0 and (alpha_iid + beta_iid < 1.0)`
- `alpha_cluster >= 0 and beta_cluster >= 0 and (alpha_cluster + beta_cluster < 1.0)`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
