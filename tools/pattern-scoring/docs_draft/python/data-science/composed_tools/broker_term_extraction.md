# Broker-Term Extraction

**File:** `python/data-science/composed_tools/broker_term_extraction.py`
**Sphere:** Data Science — Composed Tools

---

## What it solves

**Find the words that sit between topic clusters — frequent nowhere, essential everywhere two topics must talk.** TextRank-style methods find HUB words (high within-topic degree). This finds BROKER words: terms on the shortest paths BETWEEN topic clusters. Uses betweenness centrality on a co-occurrence graph built from adjacent-pair windows (not all-pairs, which would create direct edges that bypass the broker).

**When to use:** You need to find the vocabulary that bridges domains — cross-domain search, knowledge graph construction, any "what words connect these fields?" question.

---

## Valid inputs (the contract)

| Input | Domain | Violating it → |
|---|---|---|
| `sentences` | List[List[str]], tokenized sentences | adjacent-pair windowing only |

---

## How inputs shape the output

- **Adjacent-pair windowing is deliberate:** all-pairs-in-sentence would give a direct edge between topic words, erasing the brokerage being measured.
- **Betweenness centrality via Brandes' algorithm:** fraction of all-pairs shortest paths that pass through each node.
- **Broker words dominate betweenness but are mid-to-low in frequency** — the defining signature.

---

## Worked example (real run)

```
$ python3 python/data-science/composed_tools/broker_term_extraction.py
top by BETWEENNESS: ['model', 'market', 'cell']  (broker bc 1234)
top by FREQUENCY:   ['market', 'cell', 'protein']  (broker rank 8)
broker_term_extraction.py PASS
```

**Reading the output:** "model" tops betweenness (the broker between finance and biology vocabularies) but ranks 8th by frequency — invisible to a frequency-based method.

---

## Failure modes

| Trigger | What happens today | Meaning |
|---|---|---|
| single topic only | no clear broker | correct — no bridges exist |
| all-pairs windowing | broker disappears | graph construction erases the signal |

---

## Provenance

Machine-VERIFIED (frozen ruler) · cross-model reviewed 2026-07-20