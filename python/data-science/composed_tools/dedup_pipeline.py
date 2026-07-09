"""
Three-Stage Dedup Pipeline — find fast, verify exactly, explain honestly.

CROSS-SPHERE COMPOSED PATTERN (three parents): minhash_dedup (DS) generates
candidate pairs cheaply, edit_distance (DS/Text) VERIFIES them exactly, and
diff_engine (programming sphere, awesome-python-patterns) EXPLAINS what
actually differs — embedding bridges 0.545/0.530/0.486, found 2026-07-06.
Each stage covers the previous one's weakness: MinHash is fast but
approximate, edit distance is exact but O(n*m) per pair, a diff is readable
but only worth computing for confirmed near-duplicates.

Use when: deduplicating document collections where all-pairs exact comparison
is too expensive and silent deletion is unacceptable (the diff is the audit).
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import hashlib
import random
from typing import Dict, List, Set, Tuple


def shingles(text: str, k: int = 3) -> Set[str]:
    words = text.lower().split()
    return {" ".join(words[i:i + k]) for i in range(max(1, len(words) - k + 1))}


def minhash_signature(sh: Set[str], num_hashes: int = 64) -> Tuple[int, ...]:
    sig = []
    for seed in range(num_hashes):
        sig.append(min(int(hashlib.md5(f"{seed}:{s}".encode()).hexdigest()[:12], 16)
                       for s in sh) if sh else 0)
    return tuple(sig)


def estimated_jaccard(a: Tuple[int, ...], b: Tuple[int, ...]) -> float:
    return sum(1 for x, y in zip(a, b) if x == y) / len(a)


def edit_distance(a: str, b: str) -> int:
    m, n = len(a), len(b)
    prev = list(range(n + 1))
    for i in range(1, m + 1):
        cur = [i] + [0] * n
        for j in range(1, n + 1):
            cur[j] = min(prev[j] + 1, cur[j - 1] + 1,
                         prev[j - 1] + (a[i - 1] != b[j - 1]))
        prev = cur
    return prev[n]


def word_diff(a: str, b: str) -> List[str]:
    """LCS-based word diff: the explanation stage. '-' removed, '+' added."""
    wa, wb = a.split(), b.split()
    m, n = len(wa), len(wb)
    L = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            L[i][j] = L[i + 1][j + 1] + 1 if wa[i] == wb[j] else max(L[i + 1][j], L[i][j + 1])
    out, i, j = [], 0, 0
    while i < m and j < n:
        if wa[i] == wb[j]:
            i += 1; j += 1
        elif L[i + 1][j] >= L[i][j + 1]:
            out.append(f"-{wa[i]}"); i += 1
        else:
            out.append(f"+{wb[j]}"); j += 1
    out += [f"-{w}" for w in wa[i:]] + [f"+{w}" for w in wb[j:]]
    return out


def dedup_pipeline(docs: List[str], cand_thresh: float = 0.5,
                   verify_ratio: float = 0.25):
    sigs = [minhash_signature(shingles(d)) for d in docs]
    n = len(docs)
    candidates = [(i, j) for i in range(n) for j in range(i + 1, n)
                  if estimated_jaccard(sigs[i], sigs[j]) >= cand_thresh]
    verified, explanations = [], {}
    for i, j in candidates:
        dist = edit_distance(docs[i], docs[j])
        if dist / max(len(docs[i]), len(docs[j])) <= verify_ratio:
            verified.append((i, j))
            explanations[(i, j)] = word_diff(docs[i], docs[j])
    return candidates, verified, explanations


if __name__ == "__main__":
    random.seed(42)

    base = ["the quick brown fox jumps over the lazy dog near the river bank",
            "machine learning models require careful validation on held out data",
            "the gateway daemon restarts automatically after every clean shutdown",
            "seasonal patterns in retail sales peak sharply before winter holidays"]
    docs = []
    planted: List[Tuple[int, int]] = []
    for b in base:
        docs.append(b)
        near = b.replace("the ", "a ", 1) + " today"     # small honest edit
        planted.append((len(docs) - 1, len(docs)))
        docs.append(near)
    vocab = ("alpha beta gamma delta metrics kernel tensor stream buffer socket "
             "ledger raft quorum shard vector matrix entropy gradient").split()
    for _ in range(22):                                   # unrelated filler docs
        docs.append(" ".join(random.choice(vocab) for _ in range(12)))

    candidates, verified, expl = dedup_pipeline(docs)
    total_pairs = len(docs) * (len(docs) - 1) // 2

    print(f"docs: {len(docs)} · all-pairs {total_pairs} · MinHash candidates "
          f"{len(candidates)} · verified near-dups {len(verified)}")
    sample = expl[verified[0]]
    print(f"explanation for pair {verified[0]}: {' '.join(sample[:6])}")

    # The composed claims, all three stages measured:
    assert set(planted) <= set(verified), \
        f"all planted near-dup pairs must survive verification: {verified}"
    assert all(p in planted for p in verified), \
        f"no false pairs may pass exact verification: {verified}"
    assert len(candidates) < 0.2 * total_pairs, \
        "candidate stage must prune >80% of all-pairs comparisons"
    assert any(tok.startswith(("-", "+")) for tok in sample), \
        "the diff must actually explain the difference"
    print("dedup_pipeline.py PASS")
