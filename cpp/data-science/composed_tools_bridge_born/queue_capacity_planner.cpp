// queue_capacity_planner.cpp — Discrete-event queue simulation + capacity planning.
// Matches the Python oracle: Poisson arrivals, exponential service, FIFO workers.

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
#include <algorithm>
#include <cassert>
#include <cstddef>
#include <cmath>
#include <cstdio>
#include <functional>
#include <queue>
#include <random>
#include <vector>

struct WaitStats {
    double mean_wait = 0.0;
    double p90_wait = 0.0;
};

static double exponential_variate(std::mt19937& rng, double rate) {
    std::uniform_real_distribution<double> u(0.0, 1.0);
    // avoid log(0)
    double x = u(rng);
    while (x == 0.0) x = u(rng);
    return -std::log(x) / rate;
}

static WaitStats simulate_queue(double arrival_rate, double service_rate,
                                int workers, int n_jobs, unsigned seed) {
    std::mt19937 rng(seed);

    std::vector<double> arrivals;
    arrivals.reserve(n_jobs);
    double t = 0.0;
    for (int i = 0; i < n_jobs; ++i) {
        t += exponential_variate(rng, arrival_rate);
        arrivals.push_back(t);
    }

    std::priority_queue<double, std::vector<double>, std::greater<double>> free_at;
    for (int w = 0; w < workers; ++w) free_at.push(0.0);

    std::vector<double> waits;
    waits.reserve(n_jobs);
    int served = 0;
    for (double at : arrivals) {
        double worker_free = free_at.top();
        free_at.pop();
        double start = std::max(at, worker_free);
        waits.push_back(start - at);
        free_at.push(start + exponential_variate(rng, service_rate));
        ++served;
    }

    assert(served == static_cast<int>(arrivals.size()));

    std::sort(waits.begin(), waits.end());
    WaitStats stats;
    stats.mean_wait = std::accumulate(waits.begin(), waits.end(), 0.0) / waits.size();
    stats.p90_wait = waits[static_cast<std::size_t>(0.9 * waits.size())];
    return stats;
}

static std::pair<int, std::vector<std::pair<int, double>>> plan_capacity(
        double arrival_rate, double service_rate, double sla_mean_wait,
        int n_jobs = 30000) {
    std::vector<std::pair<int, double>> curve;
    int k = std::max(1, static_cast<int>(arrival_rate / service_rate) + 1);
    while (k < 50) {
        double mw = simulate_queue(arrival_rate, service_rate, k, n_jobs, k).mean_wait;
        curve.emplace_back(k, mw);
        if (mw <= sla_mean_wait) return {k, curve};
        ++k;
    }
    std::fprintf(stderr, "no worker count met the SLA\n");
    std::exit(1);
}

int main() {
    // M/M/1 validation
    double lam = 6.0, mu = 10.0;
    double rho = lam / mu;
    double wq_theory = rho / (mu - lam);
    auto sim = simulate_queue(lam, mu, 1, 200000, 1);
    double rel_err = std::abs(sim.mean_wait - wq_theory) / wq_theory;
    std::printf("M/M/1 validation: simulated Wq %.4f vs theory %.4f (rel err %.1f%%)\n",
                sim.mean_wait, wq_theory, 100.0 * rel_err);
    assert(rel_err < 0.05);

    // Production capacity plan
    double lam_prod = 40.0, mu_prod = 9.0, sla = 0.010;
    auto [k_star, curve] = plan_capacity(lam_prod, mu_prod, sla);
    std::printf("capacity plan: %d workers (wait curve: ", k_star);
    for (std::size_t i = 0; i < curve.size(); ++i) {
        if (i) std::printf(", ");
        std::printf("%d->%.0fms", curve[i].first, curve[i].second * 1000.0);
    }
    std::printf(")\n");

    auto below = simulate_queue(lam_prod, mu_prod, k_star - 1, 30000, k_star - 1);
    auto at = simulate_queue(lam_prod, mu_prod, k_star, 30000, k_star);
    std::printf("check: %d workers -> %.1fms (violates) · %d workers -> %.1fms (meets)\n",
                k_star - 1, below.mean_wait * 1000.0, k_star, at.mean_wait * 1000.0);
    assert(at.mean_wait <= sla);
    assert(below.mean_wait > sla);

    // Curve non-increasing
    for (std::size_t i = 1; i < curve.size(); ++i) {
        assert(curve[i - 1].second >= curve[i].second - 1e-9);
    }

    std::printf("queue_capacity_planner.cpp PASS\n");
    return 0;
}
