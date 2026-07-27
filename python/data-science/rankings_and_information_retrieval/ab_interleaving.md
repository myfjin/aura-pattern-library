# ab interleaving

**Language:** Python · **Sphere:** data-science · **Category:** Rankings & Information Retrieval

**Signature:** `(ranking_a: List[str], ranking_b: List[str]) → List[tuple]`

## What it does

Team-Draft Interleaving for A/B Testing Rankers.

Compare two rankers (A and B) by interleaving their results in a single ranking.
Users click on interleaved results. The ranker whose document the user clicked on wins
that "team". We count wins and determine which ranker is better.
We plant a stronger ranker and verify it wins the interleaving.

## Guarantee

When it runs, ab interleaving guarantees total_wins['A'] > total_wins['B']; a_win_ratio > 0.5 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `total_wins['A'] > total_wins['B']`
- `a_win_ratio > 0.5`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
