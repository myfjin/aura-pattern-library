# position bias click model

**Language:** Python · **Sphere:** data-science · **Category:** Rankings & Information Retrieval

**Signature:** `(ranking: List[str], true_relevances: Dict[str, float], position_bias: float) → Dict[str, int]`

## What it does

Position Bias in Click Models and Inverse Propensity Weighting.

Users click documents based on both relevance and position (position bias).
Naive click-count ranking is confounded by position.
Inverse propensity weighting (IPW) corrects for position bias; we verify
that IPW recovers the true relevance order while naive click-count does not.

## Guarantee

When it runs, position bias click model guarantees naive_ranking[0] != 'A'; ipw_ranking[0] == 'A'; ipw_top == 'A' (weak-grade: directional, proven by run).

**Checkable constraints:**

- `naive_ranking[0] != 'A'`
- `ipw_ranking[0] == 'A'`
- `ipw_top == 'A'`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
