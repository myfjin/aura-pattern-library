// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/*
Target (mean) encoding of categorical features with additive smoothing toward
the global prior, plus out-of-fold encoding of training rows to avoid leakage.
Use to encode high-cardinality categoricals for supervised models. Oracle:
leaky encoding (fit on train+test, no smoothing) inflates test correlation
above 0.30, while smoothed train-only plus out-of-fold encoding holds test and
train correlation below 0.15, and smoothing pulls a rare level toward the prior.
*/
#include <iostream>
#include <vector>
#include <cmath>
#include <numeric>
#include <cstdio>
#include <map>
#include <random>
#include <cassert>

std::map<std::string, double> fit_encoding(const std::vector<std::string>& cats,
                                          const std::vector<int>& targets,
                                          double alpha) {
    std::map<std::string, double> sums;
    std::map<std::string, int> counts;
    for (size_t i = 0; i < cats.size(); ++i) {
        sums[cats[i]] += targets[i];
        counts[cats[i]]++;
    }
    double prior = targets.empty() ? 0.5 : std::accumulate(targets.begin(), targets.end(), 0.0) / static_cast<double>(targets.size());
    std::map<std::string, double> enc;
    for (const auto& kv : sums) {
        enc[kv.first] = (kv.second + alpha * prior) / (counts[kv.first] + alpha);
    }
    return enc;
}

std::vector<double> apply_encoding(const std::vector<std::string>& cats,
                                  const std::map<std::string, double>& enc,
                                  double default_val) {
    std::vector<double> out;
    for (const auto& c : cats) {
        auto it = enc.find(c);
        out.push_back(it != enc.end() ? it->second : default_val);
    }
    return out;
}

std::vector<double> oof_encode_train(const std::vector<std::string>& cats,
                                     const std::vector<int>& targets,
                                     int n_folds = 5,
                                     double alpha = 5.0) {
    double prior = std::accumulate(targets.begin(), targets.end(), 0.0) / static_cast<double>(targets.size());
    std::vector<double> out(cats.size(), 0.0);
    for (int k = 0; k < n_folds; ++k) {
        std::vector<std::string> fit_c;
        std::vector<int> fit_t;
        for (size_t i = 0; i < cats.size(); ++i) {
            if (static_cast<int>(i % n_folds) != k) {
                fit_c.push_back(cats[i]);
                fit_t.push_back(targets[i]);
            }
        }
        auto enc = fit_encoding(fit_c, fit_t, alpha);
        for (size_t i = 0; i < cats.size(); ++i) {
            if (static_cast<int>(i % n_folds) == k) {
                auto it = enc.find(cats[i]);
                out[i] = (it != enc.end() ? it->second : prior);
            }
        }
    }
    return out;
}

double abs_correlation(const std::vector<double>& X, const std::vector<int>& y) {
    size_t n = X.size();
    double mx = std::accumulate(X.begin(), X.end(), 0.0) / static_cast<double>(n);
    double my = std::accumulate(y.begin(), y.end(), 0.0) / static_cast<double>(n);
    double cov = 0.0, vx = 0.0, vy = 0.0;
    for (size_t i = 0; i < n; ++i) {
        cov += (X[i] - mx) * (y[i] - my);
        vx += (X[i] - mx) * (X[i] - mx);
        vy += (y[i] - my) * (y[i] - my);
    }
    cov /= static_cast<double>(n);
    vx /= static_cast<double>(n);
    vy /= static_cast<double>(n);
    if (vx <= 1e-12 || vy <= 1e-12) return 0.0;
    return std::abs(cov / std::sqrt(vx * vy));
}

int main() {
    std::mt19937 rng(42);
    std::uniform_int_distribution<int> binary(0, 1);

    int n_cats = 80, per_cat = 5;
    std::vector<std::pair<std::string, int>> rows;
    for (int i = 0; i < n_cats * per_cat; ++i) {
        char buf[16];
        std::snprintf(buf, sizeof(buf), "cat_%02d", i % n_cats);
        rows.push_back({std::string(buf), binary(rng)});
    }

    size_t split = static_cast<size_t>(0.7 * rows.size());
    std::vector<std::string> c_tr, c_te;
    std::vector<int> y_tr, y_te;
    for (size_t i = 0; i < split; ++i) { c_tr.push_back(rows[i].first); y_tr.push_back(rows[i].second); }
    for (size_t i = split; i < rows.size(); ++i) { c_te.push_back(rows[i].first); y_te.push_back(rows[i].second); }
    double prior = std::accumulate(y_tr.begin(), y_tr.end(), 0.0) / static_cast<double>(y_tr.size());

    // Leaky encoding fit on train+test together.
    std::vector<std::string> c_all = c_tr;
    c_all.insert(c_all.end(), c_te.begin(), c_te.end());
    std::vector<int> y_all = y_tr;
    y_all.insert(y_all.end(), y_te.begin(), y_te.end());
    auto enc_leaky = fit_encoding(c_all, y_all, 0.0);
    double corr_test_leaky = abs_correlation(apply_encoding(c_te, enc_leaky, prior), y_te);

    // Proper: OOF for train rows, train-only fit (smoothed) for test rows.
    auto X_tr_oof = oof_encode_train(c_tr, y_tr, 5, 5.0);
    auto enc_train_only = fit_encoding(c_tr, y_tr, 5.0);
    double corr_test_proper = abs_correlation(apply_encoding(c_te, enc_train_only, prior), y_te);
    double corr_train_oof = abs_correlation(X_tr_oof, y_tr);

    // Smoothing check.
    std::vector<std::string> rare_c = {"rare", "rare"};
    rare_c.insert(rare_c.end(), c_tr.begin(), c_tr.end());
    std::vector<int> rare_y = {1, 1};
    rare_y.insert(rare_y.end(), y_tr.begin(), y_tr.end());
    double raw = fit_encoding(rare_c, rare_y, 0.0)["rare"];
    double smooth = fit_encoding(rare_c, rare_y, 5.0)["rare"];
    double rare_prior = std::accumulate(rare_y.begin(), rare_y.end(), 0.0) / static_cast<double>(rare_y.size());

    assert(corr_test_leaky > 0.30);
    assert(corr_test_proper < 0.15);
    assert(corr_train_oof < 0.15);
    assert(std::abs(smooth - rare_prior) < std::abs(raw - rare_prior));

    std::cout << "target_encoding_smoothing: PASS" << std::endl;
    return 0;
}
