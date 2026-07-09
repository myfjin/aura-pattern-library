"""
HMM Baum-Welch (EM) training: learn emission and transition probabilities.

Core idea: E-step computes forward-backward statistics; M-step re-estimates parameters.
Likelihood increases monotonically. Recovered probs ≈ planted truth.

When to use: sequence tagging, time-series classification, learning from unlabeled sequences.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import math
from typing import List, Tuple, Dict

def forward_pass(obs_seq: List[int], pi: List[float], A: List[List[float]],
                 B: List[List[float]]) -> Tuple[List[List[float]], float, List[float]]:
    """SCALED forward algorithm: α rows normalized to sum 1 per step, with the
    scaling factors kept for the backward pass and the log-likelihood.
    (Unscaled α underflows for long sequences — a 1e-10 'guard' on the γ
    denominator silently zeroes the E-step instead of fixing that.)"""
    T = len(obs_seq)
    N = len(pi)
    alpha = [[0.0] * N for _ in range(T)]
    scales: List[float] = []

    for i in range(N):
        alpha[0][i] = pi[i] * max(B[i][obs_seq[0]], 1e-10)
    c0 = sum(alpha[0]) or 1e-300
    alpha[0] = [a / c0 for a in alpha[0]]
    scales.append(c0)

    for t in range(1, T):
        for i in range(N):
            s = sum(alpha[t-1][j] * A[j][i] for j in range(N))
            alpha[t][i] = max(B[i][obs_seq[t]], 1e-10) * s
        ct = sum(alpha[t]) or 1e-300
        alpha[t] = [a / ct for a in alpha[t]]
        scales.append(ct)

    ll = sum(math.log(c) for c in scales)
    return alpha, ll, scales

def backward_pass(obs_seq: List[int], A: List[List[float]], B: List[List[float]],
                  scales: List[float]) -> List[List[float]]:
    """Backward algorithm scaled by the SAME factors as the forward pass, so
    α_t(i)·β_t(i) stays well-conditioned at every t for any sequence length."""
    T = len(obs_seq)
    N = len(A)
    beta = [[0.0] * N for _ in range(T)]

    for i in range(N):
        beta[T-1][i] = 1.0 / scales[T-1]

    for t in range(T - 2, -1, -1):
        for i in range(N):
            s = sum(A[i][j] * max(B[j][obs_seq[t+1]], 1e-10) * beta[t+1][j] for j in range(N))
            beta[t][i] = s / scales[t]

    return beta

def baum_welch(obs_sequences: List[List[int]], N: int, M: int,
               max_iter: int = 10, seed: int = 7) -> Tuple[List[float], List[List[float]], List[List[float]]]:
    """
    Baum-Welch EM training.
    N = num states, M = num observations.
    Return: (pi, A, B) - learned parameters.
    """
    # PERTURBED init — perfectly uniform parameters are EM's symmetric saddle
    # point: identical states yield identical posteriors, updates keep them
    # identical, and the model "converges" having learned nothing. A seeded
    # nudge breaks the symmetry so the states can differentiate.
    import random as _r
    _r.seed(seed)
    def _perturbed_row(size: int) -> List[float]:
        row = [1.0 / size + 0.6 * (_r.random() - 0.5) for _ in range(size)]
        s = sum(row)
        return [max(v, 1e-3) / s for v in row]
    pi = _perturbed_row(N)
    A = [_perturbed_row(N) for _ in range(N)]
    B = [_perturbed_row(M) for _ in range(N)]

    lls = []
    for iteration in range(max_iter):
        # E-step: accumulate expected counts
        pi_num = [0.0] * N
        A_num = [[0.0] * N for _ in range(N)]
        B_num = [[0.0] * M for _ in range(N)]
        A_denom = [0.0] * N
        B_denom = [0.0] * N

        total_ll = 0.0
        for obs_seq in obs_sequences:
            alpha, ll, scales = forward_pass(obs_seq, pi, A, B)
            beta = backward_pass(obs_seq, A, B, scales)
            T = len(obs_seq)

            # Compute γ_t(i) = α_t(i) * β_t(i) / P(O)
            for t in range(T):
                denom = sum(alpha[t][i] * beta[t][i] for i in range(N))
                if denom < 1e-10:
                    denom = 1e-10
                for i in range(N):
                    gamma_ti = (alpha[t][i] * beta[t][i]) / denom
                    if t == 0:
                        pi_num[i] += gamma_ti
                    B_num[i][obs_seq[t]] += gamma_ti
                    B_denom[i] += gamma_ti

            # Compute ξ_t(i,j) for transitions
            for t in range(T - 1):
                denom = sum(alpha[t][i] * A[i][j] * max(B[j][obs_seq[t+1]], 1e-10) * beta[t+1][j]
                           for i in range(N) for j in range(N))
                if denom < 1e-10:
                    denom = 1e-10
                for i in range(N):
                    for j in range(N):
                        xi_tij = (alpha[t][i] * A[i][j] * max(B[j][obs_seq[t+1]], 1e-10) * beta[t+1][j]) / denom
                        A_num[i][j] += xi_tij
                        A_denom[i] += xi_tij

            total_ll += ll

        # M-step: update parameters
        pi = [pi_num[i] / max(sum(pi_num), 1e-10) for i in range(N)]
        for i in range(N):
            if A_denom[i] > 0:
                A[i] = [A_num[i][j] / A_denom[i] for j in range(N)]
            if B_denom[i] > 0:
                B[i] = [B_num[i][m] / B_denom[i] for m in range(M)]

        lls.append(total_ll)

    return pi, A, B, lls

if __name__ == '__main__':
    import random
    random.seed(42)

    # Planted HMM
    N, M = 2, 3
    true_pi = [0.6, 0.4]
    # Distinct states (identifiable regime). Near-symmetric HMMs need far
    # more data for the same recovery — that is a property of HMMs, not EM.
    true_A = [[0.85, 0.15], [0.2, 0.8]]
    true_B = [[0.7, 0.25, 0.05], [0.05, 0.25, 0.7]]

    # Generate sequences from planted HMM
    def generate_sequence(length: int) -> List[int]:
        state = 0 if random.random() < true_pi[0] else 1
        seq = []
        for _ in range(length):
            obs = random.choices([0, 1, 2], weights=true_B[state], k=1)[0]
            seq.append(obs)
            state = 0 if random.random() < true_A[state][0] else 1
        return seq

    obs_sequences = [generate_sequence(50) for _ in range(30)]

    # Train with RESTARTS — EM's standard defense against local optima:
    # several seeded initializations, keep the run with the best likelihood.
    best = None
    for s in (1, 2, 3, 4, 5):
        cand = baum_welch(obs_sequences, N, M, max_iter=40, seed=s)
        if best is None or cand[3][-1] > best[3][-1]:
            best = cand
    pi_learned, A_learned, B_learned, lls = best

    # Stochastic-matrix sanity
    assert abs(sum(pi_learned) - 1.0) < 0.01, "π should sum to 1"
    for i in range(N):
        assert abs(sum(A_learned[i]) - 1.0) < 0.01, f"A[{i}] should sum to 1"
        assert abs(sum(B_learned[i]) - 1.0) < 0.01, f"B[{i}] should sum to 1"

    # EM's DEFINING property: the likelihood never decreases, ever.
    for a, b in zip(lls, lls[1:]):
        assert b >= a - 1e-6, f"EM likelihood decreased: {a} -> {b}"

    # RECOVERY, permutation-matched (EM cannot know which learned state is
    # which true state — label switching is legal; wrong PARAMETERS are not).
    def perm_error(perm):
        eB = max(abs(B_learned[perm[i]][m] - true_B[i][m])
                 for i in range(N) for m in range(M))
        eA = max(abs(A_learned[perm[i]][perm[j]] - true_A[i][j])
                 for i in range(N) for j in range(N))
        return eB, eA
    eB, eA = min((perm_error(p) for p in ([0, 1], [1, 0])),
                 key=lambda t: t[0] + t[1])
    print(f"log-likelihood {lls[0]:.1f} -> {lls[-1]:.1f} (monotone) · "
          f"max err B {eB:.3f} · A {eA:.3f}")
    assert eB < 0.15, f"emission matrix not recovered: max err {eB:.3f}"
    assert eA < 0.20, f"transition matrix not recovered: max err {eA:.3f}"

    print("PASS")
