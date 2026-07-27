# word2vec skipgram

**Language:** Python · **Sphere:** data-science · **Category:** Neural Networks From Scratch

**Signature:** `(x: float) → float`

## What it does

Skip-gram word2vec with negative sampling on a tiny built-in corpus.

Core idea: For each target word, predict context words using a learnable embedding
matrix. Use negative sampling: update embeddings to score true context pairs high
and random (context, negative-word) pairs low. Related words (co-occurring in context)
converge to nearby embeddings.

When to use: Word embeddings, unsupervised semantic learning, language modeling,
representation learning fundamentals.

## Guarantee

When it runs, word2vec skipgram guarantees avg_related > avg_unrelated (weak-grade: directional, proven by run).

**Checkable constraints:**

- `avg_related > avg_unrelated`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `SkipgramNegativeSampling(vocab_size, embedding_dim=8, lr=0.1)` → `train(corpus, epochs)` → `get_embedding(word_idx) → List[float]`
**Valid input:** `corpus: List[List[int]]` — tokenized documents (word indices). `vocab_size: int` ≥ 2.
**Core:** Skip-gram with negative sampling. For each target word, predict context words within window size 2. Use 2 negative samples per positive pair. Update embeddings via SGD: score = σ(target·context), error = score - label, gradient flows to both embeddings. Related words converge to nearby embeddings.
**Assert:** On a tiny 5-document corpus (8 unique words), 200 epochs at lr=0.1, embedding_dim=8, cosine similarity between co-occurring words > similarity between non-co-occurring words.
**✔ Retrofitted:** a defect noted in the 2026-07-20 audit was corrected by the AURA-E retrofit pass; the current signed code reflects the fix.

---
*△ AURA Pattern Library — © Reality Optimizer*
