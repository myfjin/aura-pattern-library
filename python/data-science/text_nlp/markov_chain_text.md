# markov chain text

**Language:** Python · **Sphere:** data-science · **Category:** Text / NLP

## What it does

Word-Level Markov Chain Text Generator

Core idea: build a transition matrix of word frequencies (conditional on previous word).
Generate text by sampling from this distribution at each step, deterministic given seed.
Useful for understanding Markov assumptions, text generation baselines, and data exploration.

Use when: generating synthetic text, understanding term co-occurrence, building simple
language models, or studying order-n dependencies in text.

## Guarantee

When it runs, markov chain text guarantees ('<START>',) in model.transitions; 'the' in start_transitions; count > 0 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `len(model.transitions) > 0`
- `('<START>',) in model.transitions`
- `valid`
- `'the' in start_transitions`
- `count > 0`
- `isinstance(text, str)`
- `'<START>' not in text`
- `len(text) > 0`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `class MarkovChainText:`, `def __init__(self, order: int = 1):`, `def _tokenize(self, text: str) -> List[str]:`, `def fit(self, documents: List[str]) -> None:`, `def generate(self, max_length: int = 20, seed_context: Tuple[str, ...] = None) -> str:`, `def get_transition_counts(self) -> Dict[Tuple[str, ...], Dict[str, int]]:`, `def sanity_check(self) -> Tuple[bool, str]:`
**Valid input:** `documents` is a list of strings; `order` is a positive integer; `seed_context` is a tuple of length `order`.
**Core:** Word-level Markov chain: learns conditional transition counts for n-grams of the requested order and generates text by sampling from observed next-word lists.
**Assert:** After fitting a small corpus, transitions are non-empty, sanity check passes, START transitions exist, every transition count is positive, and generated text is a non-empty string without the internal `<START>` marker.
**⚠️ Defect:** Generation uses `random.choice` on the observed next-word list, which samples with replacement relative to raw occurrence counts but is not the same as normalized probability sampling with smoothing. Unseen contexts cause generation to stop early. `sanity_check` only validates structure, not that probabilities sum to one.

---
*△ AURA Pattern Library — © Reality Optimizer*
