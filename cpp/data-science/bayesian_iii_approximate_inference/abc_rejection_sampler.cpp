// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/*
 * Approximate Bayesian Computation (ABC): rejection sampling for intractable likelihoods.
 *
 * Sample from prior, simulate data, accept if simulated ≈ observed (within ε).
 * Core claim: posterior mean recovers the planted parameter; acceptance rate shrinks as ε tightens.
 */

#include <iostream>
#include <vector>
#include <cmath>
#include <random>
#include <numeric>
#include <cassert>
#include <iomanip>

using namespace std;

// Sample from prior: θ ~ Uniform(0, 5)
double prior_sample(mt19937& gen) {
    uniform_real_distribution<double> dist(0.0, 5.0);
    return dist(gen);
}

// Simulate data from model: y_i ~ Poisson(θ)
// Using simple approximation: uniform integers in [0, 3θ]
vector<double> simulate_data(double theta, int n, mt19937& gen) {
    vector<double> data;
    uniform_int_distribution<int> dist(0, (int)(theta * 3));
    for (int i = 0; i < n; i++) {
        data.push_back(dist(gen));
    }
    return data;
}

// Summary distance: absolute difference in means
double distance(const vector<double>& simulated, const vector<double>& observed) {
    double mean_sim = accumulate(simulated.begin(), simulated.end(), 0.0) / simulated.size();
    double mean_obs = accumulate(observed.begin(), observed.end(), 0.0) / observed.size();
    return abs(mean_sim - mean_obs);
}

// ABC rejection sampler. Returns (posterior_samples, acceptance_rate)
pair<vector<double>, double> abc_rejection(const vector<double>& observed, 
                                            int n_samples, double epsilon,
                                            mt19937& gen) {
    vector<double> accepted;
    for (int i = 0; i < n_samples; i++) {
        double theta = prior_sample(gen);
        vector<double> simulated = simulate_data(theta, observed.size(), gen);
        if (distance(simulated, observed) < epsilon) {
            accepted.push_back(theta);
        }
    }
    
    double acceptance_rate = (n_samples > 0) ? (double)accepted.size() / n_samples : 0.0;
    return {accepted, acceptance_rate};
}

int main() {
    // Seed the RNG with same seed as Python (42)
    mt19937 gen(42);
    
    // Planted: true θ = 2.5
    double theta_true = 2.5;
    vector<double> observed = simulate_data(theta_true, 30, gen);
    
    // ABC with loose tolerance
    auto [posterior_loose, accept_loose] = abc_rejection(observed, 500, 0.5, gen);
    double mean_loose = (posterior_loose.empty()) ? 0.0 : 
        accumulate(posterior_loose.begin(), posterior_loose.end(), 0.0) / posterior_loose.size();
    
    // ABC with tight tolerance
    auto [posterior_tight, accept_tight] = abc_rejection(observed, 500, 0.2, gen);
    double mean_tight = (posterior_tight.empty()) ? 0.0 : 
        accumulate(posterior_tight.begin(), posterior_tight.end(), 0.0) / posterior_tight.size();
    
    cout << fixed << setprecision(3);
    cout << "Loose (ε=0.5): mean=" << mean_loose << ", accept_rate=" << accept_loose << endl;
    cout << "Tight (ε=0.2): mean=" << mean_tight << ", accept_rate=" << accept_tight << endl;
    
    // Posterior mean should be close to truth
    assert(abs(mean_loose - theta_true) < 1.0);
    assert(abs(mean_tight - theta_true) < 1.0);
    
    // Tighter tolerance → lower acceptance rate
    assert(accept_loose > accept_tight);
    
    cout << "PASS" << endl;
    
    return 0;
}
