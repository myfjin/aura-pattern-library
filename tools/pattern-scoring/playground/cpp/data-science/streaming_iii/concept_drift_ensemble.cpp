// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/*
 * Concept Drift Ensemble
 * 
 * On a stream whose concept flips, a drift-aware ensemble that spawns a fresh
 * learner per window and weights learners by their RECENT accuracy adapts to the new
 * concept, while a single learner frozen on pre-drift data keeps predicting the old one.
 */

#include <vector>
#include <random>
#include <cassert>
#include <iostream>
#include <unordered_map>
#include <algorithm>

int majority(const std::vector<int>& labels) {
    if (labels.empty()) return 0;
    std::unordered_map<int, int> counts;
    for (int l : labels) counts[l]++;
    int best = labels[0], best_count = 0;
    for (const auto& kv : counts) {
        if (kv.second > best_count) {
            best_count = kv.second;
            best = kv.first;
        }
    }
    return best;
}

std::pair<double, double> concept_drift_ensemble(const std::vector<int>& y, int window = 50) {
    /* Run a drift-aware windowed ensemble AND a frozen single learner. */
    int n = static_cast<int>(y.size());
    int drift = n / 2;

    // Frozen single learner: majority of the FIRST window, never updated.
    std::vector<int> first_window(y.begin(), y.begin() + window);
    int single = majority(first_window);

    // Drift-aware ensemble: one learner per completed window
    std::vector<int> learners;
    int ens_correct = 0, single_correct = 0, post = 0;

    for (int i = 0; i < n; ++i) {
        if (i % window == 0 && i >= window) {
            std::vector<int> prev_window(y.begin() + i - window, y.begin() + i);
            learners.push_back(majority(prev_window));
        }

        if (i >= drift) {
            post++;
            std::vector<int> recent(y.begin() + std::max(0, i - window), y.begin() + i);

            int pred = single;
            if (!learners.empty() && !recent.empty()) {
                int best = learners[0];
                double best_w = -1.0;
                for (int lp : learners) {
                    int correct = 0;
                    for (int t : recent) {
                        if (t == lp) correct++;
                    }
                    double w = static_cast<double>(correct) / recent.size();
                    if (w > best_w) {
                        best_w = w;
                        best = lp;
                    }
                }
                pred = best;
            }

            if (pred == y[i]) ens_correct++;
            if (single == y[i]) single_correct++;
        }
    }

    return {static_cast<double>(ens_correct) / post, static_cast<double>(single_correct) / post};
}

int main() {
    std::mt19937 rng(42);
    std::uniform_real_distribution<double> uniform(0.0, 1.0);

    // Prior-shift drift: concept A = P(y=1)=0.15, concept B = P(y=1)=0.85 after flip.
    const int n = 4000;
    std::vector<int> y;
    y.reserve(n);

    for (int i = 0; i < n / 2; ++i) {
        y.push_back((uniform(rng) < 0.15) ? 1 : 0);
    }
    for (int i = 0; i < n / 2; ++i) {
        y.push_back((uniform(rng) < 0.85) ? 1 : 0);
    }

    auto [ens_acc, single_acc] = concept_drift_ensemble(y, 50);

    // RECOVERY ASSERT: the adaptive ensemble recovers to the new concept (~0.85) while
    // the frozen learner, stuck on the old majority (0), collapses (~0.15).
    assert(ens_acc > 0.75);
    assert(single_acc < 0.30);
    assert(ens_acc - single_acc > 0.40);

    std::cout << "Concept-drift ensemble PASS" << std::endl;
    return 0;
}
