# ngram language model

**Language:** Python · **Sphere:** data-science · **Category:** Text / NLP

## What it does

N-gram Language Model with Add-One Smoothing

Core idea: model text as a Markov chain over n-grams (sequences of n tokens).
Estimate P(token | preceding n-1 tokens) from data; use add-one smoothing
to handle unseen contexts. Measure quality via perplexity on held-out text.

Use when: generating text, evaluating text likelihood, building simple
language models without neural networks, or studying Markov assumptions in NLP.

## Guarantee

When it runs, ngram language model guarantees prob_cat > prob_unknown; '<s>' in model.vocab; 'cat' in model.vocab (proven by run).

**Checkable constraints:**

- `'<s>' in model.vocab`
- `'cat' in model.vocab`
- `'dog' in model.vocab`
- `0.99 < total_prob < 1.01`
- `prob_cat > prob_unknown`
- `perp_train < perp_random`
- `isinstance(sample, str)`
- `len(sample) > 0`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** recovery (truth-pinned)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `class NGramLanguageModel:`, `def __init__(self, n: int = 2):`, `def _tokenize(self, text: str) -> List[str]:`, `def fit(self, documents: List[str]) -> None:`, `def get_probability(self, context: Tuple[str, ...], token: str) -> float:`, `def perplexity(self, text: str) -> float:`, `def sample(self, num_tokens: int = 10, seed_context: Tuple[str, ...] = None) -> str:`
**Valid input:** `documents` is a list of strings; `n` ≥ 1; `text` is a string using the learned vocabulary.
**Core:** Count-based n-gram language model with add-one (Laplace) smoothing. Computes conditional probabilities, perplexity on held-out text, and can sample a continuation from a seed context.
**Assert:** Vocabulary includes `<s>`, `cat`, `dog`; probabilities over the vocabulary sum to ~1.0 for a given context; common tokens have higher probability than rare unknown tokens; training-text perplexity is lower than random-text perplexity; sampling returns a non-empty string.
**⚠️ Defect:** Add-one smoothing is aggressive for large vocabularies and can drastically flatten probabilities. `sample` silently falls back to the alphabetically first token if cumulative-sum rounding causes `chosen_token` to remain `None`, which biases sampling. No handling of unseen contexts outside the initial `<s>` padding.

---
*△ AURA Pattern Library — © Reality Optimizer*
