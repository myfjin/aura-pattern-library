"""
Interleaving Significance — the duel names a winner; the bootstrap says if it's real.

FUSED-BRIDGE COMPOSED PATTERN: ab_interleaving (Rankings & IR) x
bootstrap_model_comparison (Model Diagnostics) — proposed by BOTH signals
2026-07-10: structural edge `matrix` (per-query paired credits flow into the
paired resampler) + semantic 0.391. Team-draft interleaving is more sensitive
than a split A/B test, but people report it as a bare win-count — no confidence.
The composition collects interleaving's PER-QUERY paired preference and feeds it
to the paired bootstrap: a confidence interval on the mean preference. A genuine
ranker edge gives a CI that excludes zero; two equal rankers give a CI that
straddles zero (no false positive).

Human logic of the name: winning one tournament doesn't prove you're better —
you resample the games to see whether you'd win again.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import random
from typing import List, Tuple


# ── parent 1 mechanism: team-draft interleaving ──
def interleave_team_draft(ranking_a: List[str], ranking_b: List[str],
                          rng: random.Random) -> List[Tuple[str, str]]:
    """Alternate picks (random who-goes-first), each team taking its highest
    not-yet-chosen item. Returns [(item, owner)]."""
    ia = ib = 0
    a_turn = rng.random() < 0.5
    picked, out = set(), []
    while ia < len(ranking_a) or ib < len(ranking_b):
        if a_turn:
            while ia < len(ranking_a) and ranking_a[ia] in picked:
                ia += 1
            if ia < len(ranking_a):
                out.append((ranking_a[ia], "A")); picked.add(ranking_a[ia]); ia += 1
        else:
            while ib < len(ranking_b) and ranking_b[ib] in picked:
                ib += 1
            if ib < len(ranking_b):
                out.append((ranking_b[ib], "B")); picked.add(ranking_b[ib]); ib += 1
        a_turn = not a_turn
    return out


def query_credit(a_rank: List[str], b_rank: List[str], relevance: dict,
                 rng: random.Random) -> int:
    """One query: interleave, simulate position-decaying clicks biased toward
    relevant docs, return signed credit (A clicks − B clicks)."""
    inter = interleave_team_draft(a_rank, b_rank, rng)
    ca = cb = 0
    for pos, (item, owner) in enumerate(inter[:8]):
        p_click = relevance.get(item, 0.1) * (0.9 ** pos)      # relevance × position decay
        if rng.random() < p_click:
            if owner == "A":
                ca += 1
            else:
                cb += 1
    return ca - cb


# ── parent 2 mechanism: paired bootstrap CI ──
def paired_bootstrap_ci(diffs: List[float], n_boot: int, rng: random.Random,
                        alpha: float = 0.05) -> Tuple[float, float, float]:
    """Resample the paired per-query differences; percentile CI of the mean."""
    means = []
    n = len(diffs)
    for _ in range(n_boot):
        s = sum(diffs[rng.randint(0, n - 1)] for _ in range(n)) / n
        means.append(s)
    means.sort()
    lo = means[int(alpha / 2 * n_boot)]
    hi = means[int((1 - alpha / 2) * n_boot)]
    return sum(diffs) / n, lo, hi


def run_experiment(a_better: bool, n_queries: int, rng: random.Random):
    """Each query has its own random doc pool.
      a_better: A's ranking is truthful (relevance follows A's order); B is A
                with the top two swapped, so B mis-orders the best docs.
      null:     A and B are two INDEPENDENT shuffles and relevance is flat —
                genuinely exchangeable rankers (any structural coupling, e.g. B
                = A-with-a-swap, biases team-draft's pointer-skipping and fakes
                a signal; the null must be a TRUE null)."""
    diffs = []
    for _ in range(n_queries):
        docs = [f"d{i}" for i in range(6)]
        rng.shuffle(docs)
        if a_better:
            a_rank = docs[:]
            b_rank = docs[:]
            b_rank[0], b_rank[1] = b_rank[1], b_rank[0]
            rel = {d: 0.8 - 0.12 * i for i, d in enumerate(a_rank)}
        else:
            a_rank = docs[:]; rng.shuffle(a_rank)
            b_rank = docs[:]; rng.shuffle(b_rank)
            rel = {d: 0.4 for d in docs}
        diffs.append(query_credit(a_rank, b_rank, rel, rng))
    return diffs


if __name__ == "__main__":
    random.seed(42)

    # Case 1: A genuinely better. Case 2: A and B equivalent (null).
    diffs_real = run_experiment(True, 300, random.Random(1))
    diffs_null = run_experiment(False, 300, random.Random(2))

    mean_r, lo_r, hi_r = paired_bootstrap_ci([float(d) for d in diffs_real], 2000, random.Random(3))
    mean_n, lo_n, hi_n = paired_bootstrap_ci([float(d) for d in diffs_null], 2000, random.Random(4))

    raw_wins_r = sum(1 for d in diffs_real if d > 0)
    n_q_half = len(diffs_real) // 2
    print(f"A-better: raw per-query wins {raw_wins_r}/300 · mean credit {mean_r:+.3f} "
          f"· 95% CI [{lo_r:+.3f}, {hi_r:+.3f}]  {'SIGNIFICANT' if lo_r > 0 else 'n.s.'}")
    print(f"null    : mean credit {mean_n:+.3f} · 95% CI [{lo_n:+.3f}, {hi_n:+.3f}]  "
          f"{'FALSE POSITIVE' if lo_n > 0 or hi_n < 0 else 'correctly n.s.'}")

    # The composed claim, three parts measured:
    assert lo_r > 0, \
        f"a real ranker edge must give a CI that excludes zero: [{lo_r:.3f}, {hi_r:.3f}]"
    assert lo_n < 0 < hi_n, \
        f"two equal rankers must give a CI that straddles zero (no false positive): [{lo_n:.3f}, {hi_n:.3f}]"
    # THE POINT OF THE COMPOSITION: raw per-query win-count (107/300, under half)
    # would wrongly conclude B wins — A takes fewer queries but by larger margins,
    # and only the signed-credit bootstrap CI reveals the real edge.
    assert raw_wins_r < n_q_half, \
        f"the teaching case needs raw wins under half (so counts mislead): {raw_wins_r}/300"
    print("interleaving_significance.py PASS")
