// Dirichlet-multinomial posterior and log-likelihood — C++17 port.
// Includes Stirling log-gamma approximation matching the Python oracle.

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
#include <cassert>
#include <cmath>
#include <iostream>
#include <random>
#include <vector>

using namespace std;

static const double PI = acos(-1.0);

static double log_gamma(double x) {
    if (x < 1.0) {
        // Python oracle path: this branch is unused for integer/float values >= 1 in tests,
        // but we keep the same structure for compatibility.
        return log(1.0 / (x * (1.0 - x) * PI / sin(PI * x)));
    }
    return 0.5 * log(2.0 * PI) + (x - 0.5) * log(x) - x;
}

static vector<double> dirichlet_multinomial_posterior(const vector<int>& counts,
                                                         const vector<double>& alpha_prior) {
    size_t K = alpha_prior.size();
    vector<double> map_probs;
    for (size_t i = 0; i < K; ++i) {
        double num = alpha_prior[i] + counts[i] - 1.0;
        if (num < 0.0) num = 0.0;
        map_probs.push_back(num);
    }
    double norm = 0.0;
    for (double p : map_probs) norm += p;
    if (norm <= 0.0) {
        return vector<double>(K, 1.0 / K);
    }
    for (double& p : map_probs) p /= norm;
    return map_probs;
}

static double dirichlet_multinomial_ll(const vector<int>& counts,
                                       const vector<double>& alpha_prior) {
    size_t K = alpha_prior.size();
    int total_counts = 0;
    for (int c : counts) total_counts += c;
    double total_alpha = 0.0;
    for (double a : alpha_prior) total_alpha += a;
    double ll = 0.0;
    for (size_t i = 0; i < K; ++i)
        ll += log_gamma(counts[i] + alpha_prior[i]) - log_gamma(alpha_prior[i]);
    ll += log_gamma(total_alpha) - log_gamma(total_alpha + total_counts);
    return ll;
}

int main() {
    mt19937 rng(42);
    vector<double> true_probs = {0.5, 0.3, 0.2};
    const size_t K = 3;

    // discrete_distribution directly matches the given probabilities.
    discrete_distribution<int> dist(true_probs.begin(), true_probs.end());
    vector<int> counts(K, 0);
    for (int i = 0; i < 100; ++i)
        counts[dist(rng)]++;

    vector<double> weak_prior = {1.0, 1.0, 1.0};
    auto weak_post = dirichlet_multinomial_posterior(counts, weak_prior);

    vector<double> strong_prior = {20.0, 5.0, 1.0};
    auto strong_post = dirichlet_multinomial_posterior(counts, strong_prior);

    double sum_weak = 0.0, sum_strong = 0.0;
    for (double p : weak_post) sum_weak += p;
    for (double p : strong_post) sum_strong += p;
    assert(fabs(sum_weak - 1.0) < 0.01);
    assert(fabs(sum_strong - 1.0) < 0.01);

    int total = 0;
    for (int c : counts) total += c;
    vector<double> empirical_freqs;
    for (int c : counts) empirical_freqs.push_back(static_cast<double>(c) / total);
    for (size_t i = 0; i < K; ++i)
        assert(fabs(weak_post[i] - empirical_freqs[i]) < 0.15);

    assert(strong_post[0] > weak_post[0] - 0.05);

    auto weak_post2 = dirichlet_multinomial_posterior(counts, weak_prior);
    assert(weak_post == weak_post2);

    double ll = dirichlet_multinomial_ll(counts, weak_prior);
    assert(!isnan(ll) && !isinf(ll));

    vector<double> informed_prior;
    for (int c : counts) informed_prior.push_back(c + 1.0);
    double ll_informed = dirichlet_multinomial_ll(counts, informed_prior);
    assert(!isnan(ll_informed));

    cout << "PASS\n";
    return 0;
}
