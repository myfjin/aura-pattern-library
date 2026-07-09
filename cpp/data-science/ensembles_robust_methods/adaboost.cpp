// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/*
 * AdaBoost Classification with Decision Stumps.
 *
 * AdaBoost sequentially fits weak learners (decision stumps) by reweighting
 * training examples: samples misclassified by the current stump get higher
 * weight in the next round. The ensemble combines weak learners with weights
 * based on their accuracy.
 */

#include <iostream>
#include <vector>
#include <cmath>
#include <cassert>
#include <random>
#include <iomanip>
#include <algorithm>

using namespace std;

struct Stump {
    int feature;
    double threshold;
    int left_label;
    int right_label;
};

// Fit a decision stump with weighted samples
Stump fit_stump_binary(const vector<pair<double, double>>& X, const vector<int>& y,
                       const vector<double>& sample_weights) {
    if (X.empty()) {
        return {0, 0.0, 0, 1};
    }
    
    int best_feature = 0;
    double best_threshold = 0.0;
    double best_accuracy = -1.0;
    int best_left_label = 0;
    int best_right_label = 1;
    
    // Try each feature
    for (int feat = 0; feat < 2; feat++) {
        vector<pair<double, int>> feature_vals;
        for (size_t i = 0; i < X.size(); i++) {
            feature_vals.push_back({(feat == 0 ? X[i].first : X[i].second), (int)i});
        }
        sort(feature_vals.begin(), feature_vals.end());
        
        // Try each split
        for (size_t i = 0; i < feature_vals.size() - 1; i++) {
            double threshold = (feature_vals[i].first + feature_vals[i+1].first) / 2.0;
            
            // Count weighted accuracy for both label assignments
            for (int left_label = 0; left_label <= 1; left_label++) {
                int right_label = 1 - left_label;
                double correct_weight = 0.0;
                
                for (size_t j = 0; j < X.size(); j++) {
                    double val = (feat == 0 ? X[j].first : X[j].second);
                    int pred = (val < threshold) ? left_label : right_label;
                    if (pred == y[j]) {
                        correct_weight += sample_weights[j];
                    }
                }
                
                double total_weight = 0.0;
                for (double w : sample_weights) total_weight += w;
                double accuracy = correct_weight / total_weight;
                
                if (accuracy > best_accuracy) {
                    best_accuracy = accuracy;
                    best_feature = feat;
                    best_threshold = threshold;
                    best_left_label = left_label;
                    best_right_label = right_label;
                }
            }
        }
    }
    
    return {best_feature, best_threshold, best_left_label, best_right_label};
}

// Predict with a single stump
int predict_stump(const pair<double, double>& x, const Stump& stump) {
    double val = (stump.feature == 0 ? x.first : x.second);
    return (val < stump.threshold) ? stump.left_label : stump.right_label;
}

// Predict with AdaBoost ensemble using weighted voting
int predict_ensemble(const pair<double, double>& x, const vector<pair<Stump, double>>& ensemble) {
    double weighted_sum = 0.0;
    for (const auto& [stump, alpha] : ensemble) {
        int pred = predict_stump(x, stump);
        weighted_sum += alpha * (pred == 1 ? 1 : -1);
    }
    return (weighted_sum >= 0) ? 1 : 0;
}

// Fit AdaBoost ensemble
vector<pair<Stump, double>> adaboost(const vector<pair<double, double>>& X, 
                                      const vector<int>& y, int n_rounds = 10) {
    int n = X.size();
    vector<double> sample_weights(n, 1.0 / n);
    vector<pair<Stump, double>> ensemble;
    
    for (int round_num = 0; round_num < n_rounds; round_num++) {
        // Fit stump with current weights
        Stump stump = fit_stump_binary(X, y, sample_weights);
        
        // Compute weighted error
        double error = 0.0;
        for (size_t i = 0; i < X.size(); i++) {
            int pred = predict_stump(X[i], stump);
            if (pred != y[i]) {
                error += sample_weights[i];
            }
        }
        
        // Prevent division by zero and stop if error is too high
        error = max(1e-10, min(1.0 - 1e-10, error));
        
        // Compute weight of this stump (alpha)
        double alpha = 0.5 * log((1.0 - error) / error);
        ensemble.push_back({stump, alpha});
        
        // Reweight samples: misclassified samples get higher weight
        double total_weight = 0.0;
        for (size_t i = 0; i < X.size(); i++) {
            int pred = predict_stump(X[i], stump);
            if (pred != y[i]) {
                sample_weights[i] *= exp(alpha);
            }
            total_weight += sample_weights[i];
        }
        
        // Normalize weights
        for (double& w : sample_weights) {
            w /= total_weight;
        }
    }
    
    return ensemble;
}

int main() {
    // Seed the RNG with same seed as Python (42)
    mt19937 gen(42);
    normal_distribution<double> norm(0.0, 1.0);
    
    // Generate 2D synthetic classification data with overlap
    int n_per_class = 40;
    vector<pair<double, double>> X;
    vector<int> y;
    
    for (int i = 0; i < n_per_class; i++) {
        X.push_back({norm(gen), norm(gen)});
        y.push_back(0);
    }
    for (int i = 0; i < n_per_class; i++) {
        X.push_back({2.0 + norm(gen), 2.0 + norm(gen)});
        y.push_back(1);
    }
    
    // Single stump baseline
    vector<double> weights(X.size(), 1.0 / X.size());
    Stump stump = fit_stump_binary(X, y, weights);
    int single_stump_correct = 0;
    for (size_t i = 0; i < X.size(); i++) {
        if (predict_stump(X[i], stump) == y[i]) {
            single_stump_correct++;
        }
    }
    double single_stump_acc = (double)single_stump_correct / y.size();
    
    // AdaBoost ensemble
    auto ensemble = adaboost(X, y, 10);
    int ada_correct = 0;
    for (size_t i = 0; i < X.size(); i++) {
        if (predict_ensemble(X[i], ensemble) == y[i]) {
            ada_correct++;
        }
    }
    double ada_acc = (double)ada_correct / y.size();
    
    cout << fixed << setprecision(4);
    cout << "adaboost: single_stump_acc=" << single_stump_acc 
         << ", ensemble_acc=" << ada_acc << endl;
    
    // Verify ensemble beats single stump
    assert(ada_acc > single_stump_acc);
    
    cout << "PASS" << endl;
    
    return 0;
}
