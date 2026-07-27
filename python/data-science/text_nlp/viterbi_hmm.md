# viterbi hmm

**Language:** Python · **Sphere:** data-science · **Category:** Text / NLP

## What it does

Viterbi Decoding for Hidden Markov Models

Core idea: find the most-likely sequence of hidden states given observations using
dynamic programming. Compare Viterbi result against brute-force enumeration to
verify correctness.

Use when: POS tagging, named entity recognition, sequence labeling problems, or
understanding the Viterbi algorithm on toy examples.

## Guarantee

When it runs, viterbi hmm guarantees abs(vit_log_prob - bf_log_prob) < 1e-06; vit_path == bf_path; state in hmm.states (weak-grade: directional, proven by run).

**Checkable constraints:**

- `abs(vit_log_prob - bf_log_prob) < 1e-06`
- `vit_path == bf_path`
- `len(vit_path) == 3`
- `state in hmm.states`
- `vit_log_prob == bf_log_prob`
- `vit_path == bf_path`

## Verification evidence

- **Green-run:** ✓ passes (re-run under the extractor's gate)
- **Constraint strength:** weak (directional)
- **Independent oracle:** ✓ **consensus** — xlang (validator v1.9)
- **Peer review:** ver-corroborated

## Detail (audited)

*Audited 2026-07-20.*

**Entry fn:** `class SimpleHMM:`, `def __init__(self):`, `def viterbi(self, observations: List[str]) -> Tuple[float, List[str]]:`, `def brute_force_best_path(self, observations: List[str]) -> Tuple[float, List[str]]:`, `def enumerate_paths(obs_idx: int, current_seq: List[str], current_log_prob: float):`
**Valid input:** `observations` is a list of observation strings that are keys in the toy emission table.
**Core:** Viterbi decoding for a toy two-state HMM (NOUN/VERB) with hand-specified start, transition, and emission probabilities. Returns the log probability of the most likely state sequence and the sequence itself. Includes a brute-force enumerator for verification on short sequences.
**Assert:** Viterbi log probability and path match brute-force enumeration for all planted test cases; path length equals observation length; every state in the path is valid; single-observation inputs match brute force.
**⚠️ Defect:** The model probabilities and observation vocabulary are hardcoded in `__init__`, so the class cannot be reused for other HMMs. `enumerate_paths` is a nested helper that accumulates paths exponentially and is only practical for very short observation sequences. Missing observations use a tiny `1e-10` emission probability without raising.

---

## Category: text_nlp_ii

---
*△ AURA Pattern Library — © Reality Optimizer*
