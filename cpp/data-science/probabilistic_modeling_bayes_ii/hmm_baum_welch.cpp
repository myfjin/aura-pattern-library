// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/*
 * HMM Baum-Welch (EM) training: recover emission and transition probabilities.
 *
 * Claims verified:
 *   - Learned A (transition) and B (emission) recover the planted matrices.
 *   - pi, A, B are stochastic (sum to 1).
 *   - EM log-likelihood is monotone.
 */

#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstddef>
#include <iostream>
#include <random>
#include <tuple>
#include <utility>
#include <vector>

std::tuple<std::vector<std::vector<double>>, double, std::vector<double>> forward_pass(
    const std::vector<int>& obs_seq,
    const std::vector<double>& pi,
    const std::vector<std::vector<double>>& A,
    const std::vector<std::vector<double>>& B) {

    int T = static_cast<int>(obs_seq.size());
    int N = static_cast<int>(pi.size());
    std::vector<std::vector<double>> alpha(T, std::vector<double>(N));
    std::vector<double> scales;

    for (int i = 0; i < N; ++i) {
        alpha[0][i] = pi[i] * std::max(B[i][obs_seq[0]], 1e-10);
    }
    double c0 = 0.0;
    for (double a : alpha[0]) c0 += a;
    if (c0 < 1e-300) c0 = 1e-300;
    for (int i = 0; i < N; ++i) alpha[0][i] /= c0;
    scales.push_back(c0);

    for (int t = 1; t < T; ++t) {
        for (int i = 0; i < N; ++i) {
            double s = 0.0;
            for (int j = 0; j < N; ++j) s += alpha[t - 1][j] * A[j][i];
            alpha[t][i] = std::max(B[i][obs_seq[t]], 1e-10) * s;
        }
        double ct = 0.0;
        for (double a : alpha[t]) ct += a;
        if (ct < 1e-300) ct = 1e-300;
        for (int i = 0; i < N; ++i) alpha[t][i] /= ct;
        scales.push_back(ct);
    }

    double ll = 0.0;
    for (double c : scales) ll += std::log(c);
    return std::make_tuple(alpha, ll, scales);
}

std::vector<std::vector<double>> backward_pass(
    const std::vector<int>& obs_seq,
    const std::vector<std::vector<double>>& A,
    const std::vector<std::vector<double>>& B,
    const std::vector<double>& scales) {

    int T = static_cast<int>(obs_seq.size());
    int N = static_cast<int>(A.size());
    std::vector<std::vector<double>> beta(T, std::vector<double>(N));

    for (int i = 0; i < N; ++i) beta[T - 1][i] = 1.0 / scales[T - 1];

    for (int t = T - 2; t >= 0; --t) {
        for (int i = 0; i < N; ++i) {
            double s = 0.0;
            for (int j = 0; j < N; ++j) {
                s += A[i][j] * std::max(B[j][obs_seq[t + 1]], 1e-10) * beta[t + 1][j];
            }
            beta[t][i] = s / scales[t];
        }
    }

    return beta;
}

std::vector<double> perturbed_row(int size, std::mt19937& rng) {
    std::uniform_real_distribution<double> uniform(0.0, 1.0);
    std::vector<double> row;
    for (int i = 0; i < size; ++i) {
        row.push_back(1.0 / size + 0.6 * (uniform(rng) - 0.5));
    }
    double s = 0.0;
    for (double v : row) s += v;
    for (double& v : row) v = std::max(v, 1e-3) / s;
    return row;
}

std::tuple<std::vector<double>, std::vector<std::vector<double>>,
          std::vector<std::vector<double>>, std::vector<double>> baum_welch(
    const std::vector<std::vector<int>>& obs_sequences,
    int N, int M, int max_iter, int seed) {

    std::mt19937 rng(seed);
    auto pi = perturbed_row(N, rng);
    std::vector<std::vector<double>> A(N), B(N);
    for (int i = 0; i < N; ++i) A[i] = perturbed_row(N, rng);
    for (int i = 0; i < N; ++i) B[i] = perturbed_row(M, rng);

    std::vector<double> lls;

    for (int iteration = 0; iteration < max_iter; ++iteration) {
        std::vector<double> pi_num(N, 0.0);
        std::vector<std::vector<double>> A_num(N, std::vector<double>(N, 0.0));
        std::vector<std::vector<double>> B_num(N, std::vector<double>(M, 0.0));
        std::vector<double> A_denom(N, 0.0), B_denom(N, 0.0);

        double total_ll = 0.0;

        for (const auto& obs_seq : obs_sequences) {
            auto fwd_result = forward_pass(obs_seq, pi, A, B);
            const auto& alpha = std::get<0>(fwd_result);
            double ll = std::get<1>(fwd_result);
            const auto& scales = std::get<2>(fwd_result);
            auto beta = backward_pass(obs_seq, A, B, scales);
            int T = static_cast<int>(obs_seq.size());

            for (int t = 0; t < T; ++t) {
                double denom = 0.0;
                for (int i = 0; i < N; ++i) denom += alpha[t][i] * beta[t][i];
                if (denom < 1e-10) denom = 1e-10;
                for (int i = 0; i < N; ++i) {
                    double gamma_ti = (alpha[t][i] * beta[t][i]) / denom;
                    if (t == 0) pi_num[i] += gamma_ti;
                    B_num[i][obs_seq[t]] += gamma_ti;
                    B_denom[i] += gamma_ti;
                }
            }

            for (int t = 0; t < T - 1; ++t) {
                double denom = 0.0;
                for (int i = 0; i < N; ++i) {
                    for (int j = 0; j < N; ++j) {
                        denom += alpha[t][i] * A[i][j] * std::max(B[j][obs_seq[t + 1]], 1e-10) * beta[t + 1][j];
                    }
                }
                if (denom < 1e-10) denom = 1e-10;
                for (int i = 0; i < N; ++i) {
                    for (int j = 0; j < N; ++j) {
                        double xi = (alpha[t][i] * A[i][j] * std::max(B[j][obs_seq[t + 1]], 1e-10) * beta[t + 1][j]) / denom;
                        A_num[i][j] += xi;
                        A_denom[i] += xi;
                    }
                }
            }

            total_ll += ll;
        }

        double pi_sum = 0.0;
        for (double v : pi_num) pi_sum += v;
        for (int i = 0; i < N; ++i) pi[i] = pi_num[i] / std::max(pi_sum, 1e-10);

        for (int i = 0; i < N; ++i) {
            if (A_denom[i] > 0.0) {
                for (int j = 0; j < N; ++j) A[i][j] = A_num[i][j] / A_denom[i];
            }
            if (B_denom[i] > 0.0) {
                for (int m = 0; m < M; ++m) B[i][m] = B_num[i][m] / B_denom[i];
            }
        }

        lls.push_back(total_ll);
    }

    return std::make_tuple(pi, A, B, lls);
}

static double mat_max_abs_diff(const std::vector<std::vector<double>>& X,
                               const std::vector<std::vector<double>>& Y) {
    double e = 0.0;
    for (size_t i = 0; i < X.size(); ++i) {
        for (size_t j = 0; j < X[i].size(); ++j) {
            e = std::max(e, std::abs(X[i][j] - Y[i][j]));
        }
    }
    return e;
}

static double vec_max_abs_diff(const std::vector<double>& x,
                               const std::vector<double>& y) {
    double e = 0.0;
    for (size_t i = 0; i < x.size(); ++i) e = std::max(e, std::abs(x[i] - y[i]));
    return e;
}

static bool is_stochastic(const std::vector<double>& v, double tol = 1e-6) {
    double s = 0.0;
    for (double x : v) {
        if (x < -tol) return false;
        s += x;
    }
    return std::abs(s - 1.0) < tol;
}

int main() {
    std::mt19937 rng(42);
    std::uniform_real_distribution<double> uniform01(0.0, 1.0);

    const int N = 2, M = 3;
    std::vector<double> true_pi = {0.6, 0.4};
    std::vector<std::vector<double>> true_A = {{0.85, 0.15}, {0.2, 0.8}};
    std::vector<std::vector<double>> true_B = {{0.7, 0.25, 0.05}, {0.05, 0.25, 0.7}};

    auto generate_sequence = [&](int length) {
        int state = (uniform01(rng) < true_pi[0]) ? 0 : 1;
        std::vector<int> seq;
        for (int i = 0; i < length; ++i) {
            double r = uniform01(rng);
            int obs = 0;
            double cum = 0.0;
            for (int m = 0; m < M; ++m) {
                cum += true_B[state][m];
                if (r < cum) { obs = m; break; }
            }
            seq.push_back(obs);
            state = (uniform01(rng) < true_A[state][0]) ? 0 : 1;
        }
        return seq;
    };

    std::vector<std::vector<int>> obs_sequences;
    for (int i = 0; i < 30; ++i) obs_sequences.push_back(generate_sequence(50));

    double best_ll = -1e18;
    std::vector<double> best_lls;
    std::vector<double> best_pi;
    std::vector<std::vector<double>> best_A, best_B;

    for (int s = 1; s <= 5; ++s) {
        auto cand = baum_welch(obs_sequences, N, M, 40, s);
        const auto& cand_pi = std::get<0>(cand);
        const auto& cand_A = std::get<1>(cand);
        const auto& cand_B = std::get<2>(cand);
        const auto& cand_lls = std::get<3>(cand);
        double cand_ll = cand_lls.back();
        if (cand_ll > best_ll) {
            best_ll = cand_ll;
            best_lls = cand_lls;
            best_pi = cand_pi;
            best_A = cand_A;
            best_B = cand_B;
        }
    }

    // EM monotonicity
    for (size_t i = 1; i < best_lls.size(); ++i) {
        assert(best_lls[i] >= best_lls[i - 1] - 1e-6);
    }

    // Stochasticity
    assert(is_stochastic(best_pi));
    for (const auto& row : best_A) assert(is_stochastic(row));
    for (const auto& row : best_B) assert(is_stochastic(row));

    // Matrix recovery (allow a single state swap)
    double eA = mat_max_abs_diff(best_A, true_A);
    double eB = mat_max_abs_diff(best_B, true_B);
    double epi = vec_max_abs_diff(best_pi, true_pi);

    // Try swapped-state version and keep best fit
    std::vector<std::vector<double>> swap_A(N, std::vector<double>(N));
    std::vector<std::vector<double>> swap_B(N, std::vector<double>(M));
    std::vector<double> swap_pi(N);
    for (int i = 0; i < N; ++i) {
        swap_pi[i] = true_pi[N - 1 - i];
        for (int j = 0; j < N; ++j) swap_A[i][j] = true_A[N - 1 - i][N - 1 - j];
        for (int m = 0; m < M; ++m) swap_B[i][m] = true_B[N - 1 - i][m];
    }
    eA = std::min(eA, mat_max_abs_diff(best_A, swap_A));
    eB = std::min(eB, mat_max_abs_diff(best_B, swap_B));
    epi = std::min(epi, vec_max_abs_diff(best_pi, swap_pi));

    assert(eA < 0.20);
    assert(eB < 0.15);
    assert(epi < 0.20);

    std::cout << "hmm_baum_welch.cpp PASS (eA=" << eA << ", eB=" << eB << ", epi=" << epi << ")" << std::endl;
    return 0;
}
