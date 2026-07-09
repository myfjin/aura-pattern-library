"""
Viterbi Decoding for Hidden Markov Models

Core idea: find the most-likely sequence of hidden states given observations using
dynamic programming. Compare Viterbi result against brute-force enumeration to
verify correctness.

Use when: POS tagging, named entity recognition, sequence labeling problems, or
understanding the Viterbi algorithm on toy examples.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

from typing import List, Tuple, Dict
import math


class SimpleHMM:
    """Toy HMM for POS tagging: states=(NOUN, VERB), observations=(word)."""

    def __init__(self):
        # Hand-specified probabilities for toy example
        # States: NOUN, VERB
        # Observations: dog, cat, runs, sleeps

        # Initial state probabilities
        self.start_probs = {
            "NOUN": 0.6,
            "VERB": 0.4,
        }

        # Transition probabilities: P(next_state | current_state)
        self.trans_probs = {
            "NOUN": {"NOUN": 0.3, "VERB": 0.7},
            "VERB": {"NOUN": 0.8, "VERB": 0.2},
        }

        # Emission probabilities: P(observation | state)
        self.emit_probs = {
            "NOUN": {"dog": 0.4, "cat": 0.4, "runs": 0.1, "sleeps": 0.1},
            "VERB": {"dog": 0.1, "cat": 0.1, "runs": 0.4, "sleeps": 0.4},
        }

        self.states = list(self.start_probs.keys())

    def viterbi(self, observations: List[str]) -> Tuple[float, List[str]]:
        """Find most-likely state sequence using Viterbi.

        Returns (log_probability, state_sequence).
        """
        n = len(observations)
        # viterbi[t][state] = (log_prob, previous_state)
        viterbi = [{} for _ in range(n)]

        # Initialize first timestep
        for state in self.states:
            emit_prob = self.emit_probs[state].get(observations[0], 1e-10)
            start_prob = self.start_probs[state]
            viterbi[0][state] = (math.log(start_prob) + math.log(emit_prob), None)

        # Forward pass
        for t in range(1, n):
            for curr_state in self.states:
                emit_prob = self.emit_probs[curr_state].get(observations[t], 1e-10)

                best_log_prob = -math.inf
                best_prev_state = None

                for prev_state in self.states:
                    trans_prob = self.trans_probs[prev_state][curr_state]
                    prev_log_prob, _ = viterbi[t - 1][prev_state]
                    log_prob = prev_log_prob + math.log(trans_prob) + math.log(emit_prob)

                    if log_prob > best_log_prob:
                        best_log_prob = log_prob
                        best_prev_state = prev_state

                viterbi[t][curr_state] = (best_log_prob, best_prev_state)

        # Backtrack to recover path
        path = []
        curr_state = max(viterbi[n - 1].keys(), key=lambda s: viterbi[n - 1][s][0])
        final_log_prob = viterbi[n - 1][curr_state][0]

        for t in range(n - 1, -1, -1):
            path.append(curr_state)
            if viterbi[t][curr_state][1] is not None:
                curr_state = viterbi[t][curr_state][1]

        path.reverse()
        return final_log_prob, path

    def brute_force_best_path(self, observations: List[str]) -> Tuple[float, List[str]]:
        """Enumerate all possible state sequences and return the best.

        For verification only; exponentially slow.
        """

        def enumerate_paths(obs_idx: int, current_seq: List[str], current_log_prob: float):
            """Recursively enumerate all paths."""
            if obs_idx == len(observations):
                return [(current_log_prob, current_seq)]

            results = []
            for state in self.states:
                emit_prob = self.emit_probs[state].get(observations[obs_idx], 1e-10)

                if obs_idx == 0:
                    new_log_prob = math.log(self.start_probs[state]) + math.log(emit_prob)
                else:
                    trans_prob = self.trans_probs[current_seq[-1]][state]
                    new_log_prob = current_log_prob + math.log(trans_prob) + math.log(emit_prob)

                results.extend(enumerate_paths(obs_idx + 1, current_seq + [state], new_log_prob))

            return results

        all_paths = enumerate_paths(0, [], 0.0)
        best_log_prob, best_path = max(all_paths, key=lambda x: x[0])
        return best_log_prob, best_path


if __name__ == "__main__":
    import random
    random.seed(42)

    hmm = SimpleHMM()

    # Test sequences
    test_cases = [
        ["dog", "runs"],
        ["cat", "sleeps"],
        ["dog", "cat", "runs"],
        ["runs", "sleeps", "dog"],
    ]

    for obs in test_cases:
        vit_log_prob, vit_path = hmm.viterbi(obs)
        bf_log_prob, bf_path = hmm.brute_force_best_path(obs)

        # Test 1: Viterbi should find the same best path as brute force
        assert abs(vit_log_prob - bf_log_prob) < 1e-6, \
            f"Log probs differ for {obs}: Viterbi={vit_log_prob}, BF={bf_log_prob}"
        assert vit_path == bf_path, \
            f"Paths differ for {obs}: Viterbi={vit_path}, BF={bf_path}"

    # Test 2: Path length should match observation length
    vit_log_prob, vit_path = hmm.viterbi(["dog", "runs", "cat"])
    assert len(vit_path) == 3, f"Path length {len(vit_path)} should be 3"

    # Test 3: Each state in path should be valid
    for state in vit_path:
        assert state in hmm.states, f"Invalid state {state} in path"

    # Test 4: Single observation
    vit_log_prob, vit_path = hmm.viterbi(["dog"])
    bf_log_prob, bf_path = hmm.brute_force_best_path(["dog"])
    assert vit_log_prob == bf_log_prob, "Single obs should match"
    assert vit_path == bf_path, "Single obs path should match"

    print("PASS: Viterbi decoding finds optimal state sequence, matches brute-force enumeration")
