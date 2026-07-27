# bpe tokenizer lite

**Language:** Python · **Sphere:** data-science · **Category:** Text / NLP

## What it does

Simplified Byte-Pair Encoding (BPE) Tokenizer

Core idea: learn merge operations from a corpus (combining frequent character pairs),
then apply merges to tokenize new text. Encode text to token IDs, decode back to text.

Use when: understanding subword tokenization, building custom tokenizers for small
models, or studying how BPE reduces vocabulary size.

## Guarantee

When it runs, bpe tokenizer lite guarantees 'cat' in decoded or 'c' in decoded; 'dog' in decoded or 'd' in decoded; enc1 == enc2 (weak-grade: directional, proven by run).

**Checkable constraints:**

- `len(tokenizer.vocab) > 0`
- `len(tokenizer.merges) > 0`
- `isinstance(encoded, list)`
- `all((isinstance(t, int) for t in encoded))`
- `len(encoded) > 0`
- `isinstance(decoded, str)`
- `len(decoded) > 0`
- `'cat' in decoded or 'c' in decoded`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **hard** — positive, roundtrip, xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `class BPETokenizer:`, `def __init__(self, vocab_size: int = 100):`, `def _get_word_frequencies(self, text: str) -> Dict[Tuple[str, ...], int]:`, `def learn_merges(self, text: str, num_merges: int = None) -> None:`, `def encode(self, text: str) -> List[int]:`, `def decode(self, token_ids: List[int]) -> str:`
**Valid input:** `text` is a lowercase-able ASCII string containing words matching `\b[a-z]+\b`; `vocab_size` is a positive integer; `num_merges` defaults to `vocab_size - 256`.
**Core:** Simplified byte-pair encoding: learns the most frequent character/bigram merges from a corpus, builds a vocabulary, encodes new text to token IDs, and decodes IDs back to a space-separated approximation of the original.
**Assert:** `learn_merges` produces a non-empty vocab and merge list; `encode` returns a list of ints; `decode` returns a non-empty string; the same word encodes identically across two calls.
**⚠️ Defect:** Tokenization drops all non-alphabetic tokens, numbers, punctuation, and mixed-case words. If `num_merges` exceeds available pairs the loop simply breaks, but the default formula `vocab_size - 256` can be negative for small `vocab_size`. Decode strips `</w>` into spaces, which can mis-recover word order and spacing.

---
*△ AURA Pattern Library — © Reality Optimizer*
