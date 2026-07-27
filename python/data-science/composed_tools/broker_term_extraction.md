# broker term extraction

**Language:** Python · **Sphere:** data-science · **Category:** Composed Tools

**Signature:** `(sentences: List[List[str]]) → Dict[str, Set[str]]`

## What it does

Broker-Term Extraction — the words that stand between topics and connect them.

CROSS-CATEGORY COMPOSED PATTERN: betweenness_centrality (Clustering & Graph) x
keyword_cooccurrence_graph (Text/NLP II) — embedding bridge 0.503, found
2026-07-08. TextRank-style methods find HUB words (high within-topic degree).
This finds BROKER words: terms that sit on the shortest paths BETWEEN topic
clusters — frequent nowhere, essential everywhere two topics must talk.
A bridge-born pattern for finding bridge-words: the method describes itself.

Human logic of the name: a broker is the party both sides must go through.

## Guarantee

When it runs, broker term extraction guarantees by_bc[0] == broker; by_freq.index(broker) >= 5; bc[broker] > 2 * bc[by_bc[1]] (weak-grade: directional, proven by run).

**Checkable constraints:**

- `by_bc[0] == broker`
- `by_freq.index(broker) >= 5`
- `bc[broker] > 2 * bc[by_bc[1]]`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

---
*△ AURA Pattern Library — © Reality Optimizer*
