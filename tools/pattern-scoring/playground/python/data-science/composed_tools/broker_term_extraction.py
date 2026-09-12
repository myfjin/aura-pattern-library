"""
Broker-Term Extraction — the words that stand between topics and connect them.

CROSS-CATEGORY COMPOSED PATTERN: betweenness_centrality (Clustering & Graph) x
keyword_cooccurrence_graph (Text/NLP II) — embedding bridge 0.503, found
2026-07-08. TextRank-style methods find HUB words (high within-topic degree).
This finds BROKER words: terms that sit on the shortest paths BETWEEN topic
clusters — frequent nowhere, essential everywhere two topics must talk.
A bridge-born pattern for finding bridge-words: the method describes itself.

Human logic of the name: a broker is the party both sides must go through.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import random
from collections import defaultdict, deque
from typing import Dict, List, Set


def cooccurrence_graph(sentences: List[List[str]]) -> Dict[str, Set[str]]:
    """ADJACENT-pair windowing, deliberately: all-pairs-in-sentence would give
    the bridging sentence [fin, broker, bio] a DIRECT fin-bio edge that
    bypasses the broker — the graph construction would erase the very
    brokerage being measured (the self-erasing-measurement class)."""
    g: Dict[str, Set[str]] = defaultdict(set)
    for words in sentences:
        for a, b in zip(words, words[1:]):
            if a != b:
                g[a].add(b)
                g[b].add(a)
    return g


def betweenness(g: Dict[str, Set[str]]) -> Dict[str, float]:
    """Brandes' algorithm (unweighted): fraction of shortest paths through each node."""
    bc = {v: 0.0 for v in g}
    for s in g:
        stack, preds = [], {v: [] for v in g}
        sigma = {v: 0.0 for v in g}
        sigma[s] = 1.0
        dist = {v: -1 for v in g}
        dist[s] = 0
        q = deque([s])
        while q:
            v = q.popleft()
            stack.append(v)
            for w in g[v]:
                if dist[w] < 0:
                    dist[w] = dist[v] + 1
                    q.append(w)
                if dist[w] == dist[v] + 1:
                    sigma[w] += sigma[v]
                    preds[w].append(v)
        delta = {v: 0.0 for v in g}
        while stack:
            w = stack.pop()
            for v in preds[w]:
                delta[v] += sigma[v] / sigma[w] * (1 + delta[w])
            if w != s:
                bc[w] += delta[w]
    return bc


if __name__ == "__main__":
    random.seed(42)

    # Two topics that never share vocabulary — except through the BROKER word.
    finance = "market price bond yield equity portfolio hedge margin".split()
    biology = "cell protein enzyme membrane genome neuron tissue receptor".split()
    broker = "model"          # the word both worlds actually use

    sentences: List[List[str]] = []
    for _ in range(40):       # within-topic sentences: hubs earn their frequency
        sentences.append(random.sample(finance, 4))
        sentences.append(random.sample(biology, 4))
    for _ in range(6):        # rare bridging sentences: broker + one word each side
        sentences.append([random.choice(finance), broker, random.choice(biology)])

    g = cooccurrence_graph(sentences)
    bc = betweenness(g)
    freq: Dict[str, int] = defaultdict(int)
    for s_ in sentences:
        for w in s_:
            freq[w] += 1

    by_bc = sorted(bc, key=lambda w: -bc[w])
    by_freq = sorted(freq, key=lambda w: -freq[w])
    print(f"top by BETWEENNESS: {by_bc[:3]}  (broker bc {bc[broker]:.0f})")
    print(f"top by FREQUENCY:   {by_freq[:3]}  (broker rank {by_freq.index(broker) + 1})")

    # The composed claim, both halves measured:
    assert by_bc[0] == broker, \
        f"the broker word must top betweenness: {by_bc[:3]}"
    assert by_freq.index(broker) >= 5, \
        f"the broker must NOT be findable by frequency: rank {by_freq.index(broker) + 1}"
    assert bc[broker] > 2 * bc[by_bc[1]], \
        "the broker should dominate betweenness with a clear margin"
    print("broker_term_extraction.py PASS")
