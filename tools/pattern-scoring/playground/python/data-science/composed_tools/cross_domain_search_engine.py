"""
Cross-Domain Search Engine — a 4-pattern WORKFLOW that finds the bridges.

PIPELINE-BRIDGE COMPOSED PATTERN (four stages, each feeds the next), found by
pipeline_search over the composability graph 2026-07-10 (coherence 0.50):
  porter_stemmer_lite → broker_term_extraction → query_expansion_prf → bm25_ranking.

A plain search returns documents that share your query's WORDS — all inside your
own domain. This engine retrieves the documents that BRIDGE domains: (1) stem the
vocabulary so surface variants unify; (2) extract the corpus's broker terms (the
words on shortest paths between topic clusters); (3) expand the query with those
broker terms; (4) BM25-rank. A domain-A query then surfaces the cross-domain
bridge documents a plain BM25 search leaves buried.

Human logic of the name: ordinary search digs deeper into your own field; this
one walks to the borders and brings back what crosses them.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import math
import random
from collections import defaultdict, deque
from typing import Dict, List, Set, Tuple


# ── stage 1: porter-lite stemming ──
def stem(word: str) -> str:
    for suf in ("ing", "edly", "ed", "ly", "es", "s"):
        if len(word) > len(suf) + 2 and word.endswith(suf):
            return word[:-len(suf)]
    return word


def stem_doc(doc: List[str]) -> List[str]:
    return [stem(w) for w in doc]


# ── stage 2: broker-term extraction (co-occurrence graph + betweenness) ──
def cooccurrence_graph(docs: List[List[str]]) -> Dict[str, Set[str]]:
    g: Dict[str, Set[str]] = defaultdict(set)
    for words in docs:
        for a, b in zip(words, words[1:]):
            if a != b:
                g[a].add(b); g[b].add(a)
    return g


def betweenness(g: Dict[str, Set[str]]) -> Dict[str, float]:
    bc = {v: 0.0 for v in g}
    for s in g:
        stack, preds = [], {v: [] for v in g}
        sigma = {v: 0.0 for v in g}; sigma[s] = 1.0
        dist = {v: -1 for v in g}; dist[s] = 0
        q = deque([s])
        while q:
            v = q.popleft(); stack.append(v)
            for w in g[v]:
                if dist[w] < 0:
                    dist[w] = dist[v] + 1; q.append(w)
                if dist[w] == dist[v] + 1:
                    sigma[w] += sigma[v]; preds[w].append(v)
        delta = {v: 0.0 for v in g}
        while stack:
            w = stack.pop()
            for v in preds[w]:
                delta[v] += sigma[v] / sigma[w] * (1 + delta[w])
            if w != s:
                bc[w] += delta[w]
    return bc


def broker_terms(docs: List[List[str]], top: int = 3) -> List[str]:
    bc = betweenness(cooccurrence_graph(docs))
    return [w for w in sorted(bc, key=lambda w: -bc[w])[:top]]


# ── stage 3: query expansion with broker terms ──
def expand_query(query: List[str], brokers: List[str]) -> List[str]:
    return query + [b for b in brokers if b not in query]


# ── stage 4: BM25 ranking ──
def bm25_rank(query: List[str], docs: List[List[str]], k1: float = 1.5,
              b: float = 0.75) -> List[Tuple[int, float]]:
    n = len(docs)
    avgdl = sum(len(d) for d in docs) / n
    df: Dict[str, int] = defaultdict(int)
    for d in docs:
        for w in set(d):
            df[w] += 1
    scores = []
    for i, d in enumerate(docs):
        tf: Dict[str, int] = defaultdict(int)
        for w in d:
            tf[w] += 1
        s = 0.0
        for q in query:
            if q not in df:
                continue
            idf = math.log((n - df[q] + 0.5) / (df[q] + 0.5) + 1)
            num = tf[q] * (k1 + 1)
            den = tf[q] + k1 * (1 - b + b * len(d) / avgdl)
            s += idf * num / den
        scores.append((i, s))
    return sorted(scores, key=lambda t: -t[1])


if __name__ == "__main__":
    random.seed(42)

    fin = "market price bond yield equity hedge margin portfolio".split()
    bio = "cell protein enzyme membrane genome neuron receptor tissue".split()
    brokers_planted = ["model", "network"]

    docs: List[List[str]] = []
    kind: List[str] = []
    for _ in range(14):                                   # finance-only
        docs.append([random.choice(fin) for _ in range(8)]); kind.append("fin")
    for _ in range(14):                                   # biology-only
        docs.append([random.choice(bio) for _ in range(8)]); kind.append("bio")
    bridge_ids = []
    for _ in range(4):                                    # BRIDGE docs: brokers are
        # the ONLY adjacency between fin and bio (every fin↔bio transition passes
        # THROUGH a broker), so betweenness crowns the planted brokers cleanly —
        # letting fin and bio touch directly would erase the brokerage measured.
        d = [random.choice(fin), brokers_planted[0], random.choice(bio),
             brokers_planted[1], random.choice(fin), brokers_planted[0],
             random.choice(bio), brokers_planted[1]]
        bridge_ids.append(len(docs)); docs.append(d); kind.append("bridge")

    sdocs = [stem_doc(d) for d in docs]
    brokers = broker_terms(sdocs)
    query = [stem(w) for w in ["market", "yield", "hedge"]]     # a finance query
    k = 6

    plain = bm25_rank(query, sdocs)[:k]
    expanded = bm25_rank(expand_query(query, brokers), sdocs)[:k]
    plain_bridges = sum(1 for i, _ in plain if kind[i] == "bridge")
    exp_bridges = sum(1 for i, _ in expanded if kind[i] == "bridge")

    print(f"broker terms extracted: {brokers} (planted {brokers_planted})")
    print(f"bridge docs in top-{k} — plain BM25: {plain_bridges}/4 · "
          f"broker-expanded: {exp_bridges}/4")

    # The workflow claim, end-to-end (what plain search cannot do):
    assert set(brokers) & set(brokers_planted), \
        f"stage 2 must actually recover broker terms: {brokers}"
    assert plain_bridges <= 1, \
        f"plain BM25 should stay in-domain (miss the bridges): {plain_bridges}"
    assert exp_bridges >= 3, \
        f"the pipeline must surface the cross-domain bridges: {exp_bridges}"
    print("cross_domain_search_engine.py PASS")
