// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/*
 * Walk-forward early stopping for a gradient-boosted stump forecaster.
 * Boosts stumps on lagged (autoregressive) features while tracking out-of-sample
 * MAE on a held-out forward window each round; stops after `patience` rounds with
 * no forward improvement. Use to pick boosting rounds without overfitting a time
 * series. Oracle: training MAE keeps falling below the best forward MAE, the
 * final-round forward error is >5% worse than the best, and the stop fires at
 * best_round + patience, strictly before max_rounds.
 */
#include <algorithm>
#include <cassert>
#include <cmath>
#include <iostream>
#include <numeric>
#include <random>
#include <set>
#include <vector>

using namespace std;

using Stump = tuple<int, double, double, double>;

Stump fit_stump_to_residuals(const vector<vector<double>>& X, const vector<double>& r) {
    Stump best = {0, 0.0, 0.0, 0.0};
    double best_sse = 1e300;
    int nf = X[0].size();
    for (int f = 0; f < nf; ++f) {
        set<double> s;
        for (const auto& x : X) s.insert(x[f]);
        vector<double> vals(s.begin(), s.end());
        for (size_t k = 1; k < vals.size(); ++k) {
            double thr = (vals[k-1] + vals[k]) / 2.0;
            vector<double> left, right;
            for (size_t i = 0; i < X.size(); ++i) {
                if (X[i][f] <= thr) left.push_back(r[i]); else right.push_back(r[i]);
            }
            double lm = left.empty() ? 0.0 : accumulate(left.begin(), left.end(), 0.0) / left.size();
            double rm = right.empty() ? 0.0 : accumulate(right.begin(), right.end(), 0.0) / right.size();
            double sse = 0.0;
            for (double v : left) sse += (v - lm) * (v - lm);
            for (double v : right) sse += (v - rm) * (v - rm);
            if (sse < best_sse) { best_sse = sse; best = {f, thr, lm, rm}; }
        }
    }
    return best;
}

double predict_stump(const vector<double>& x, const Stump& s) {
    int f; double thr, lm, rm;
    tie(f, thr, lm, rm) = s;
    return x[f] <= thr ? lm : rm;
}

double predict_ensemble(const vector<double>& x, const vector<Stump>& stumps, double lr) {
    double p = 0.0;
    for (const auto& s : stumps) p += lr * predict_stump(x, s);
    return p;
}

double mae(const vector<double>& y_true, const vector<double>& y_pred) {
    double s = 0.0;
    for (size_t i = 0; i < y_true.size(); ++i) s += abs(y_true[i] - y_pred[i]);
    return s / y_true.size();
}

int main() {
    mt19937 rng(42);
    normal_distribution<double> noise(0.0, 0.8);
    int n = 110;
    vector<double> y;
    for (int t = 0; t < n; ++t) {
        y.push_back(0.03 * t + 2.0 * sin(2.0 * M_PI * t / 25.0) + noise(rng));
    }
    vector<pair<vector<double>, double>> rows;
    for (int t = 3; t < n; ++t) rows.push_back({{y[t-1], y[t-2], y[t-3]}, y[t]});

    int split = 80;
    vector<vector<double>> X_tr, X_fw;
    vector<double> y_tr, y_fw;
    for (int i = 0; i < split; ++i) { X_tr.push_back(rows[i].first); y_tr.push_back(rows[i].second); }
    for (int i = split; i < (int)rows.size(); ++i) { X_fw.push_back(rows[i].first); y_fw.push_back(rows[i].second); }

    double lr = 0.4;
    int max_rounds = 120, patience = 15;
    vector<Stump> stumps;
    vector<double> fit_tr(X_tr.size(), 0.0);
    vector<double> forward_curve;
    double best_fw = 1e300;
    int best_round = 0, since_best = 0, stopped_at = max_rounds;

    for (int rnd = 1; rnd <= max_rounds; ++rnd) {
        vector<double> residuals(X_tr.size());
        for (size_t i = 0; i < X_tr.size(); ++i) residuals[i] = y_tr[i] - fit_tr[i];
        Stump s = fit_stump_to_residuals(X_tr, residuals);
        stumps.push_back(s);
        for (size_t i = 0; i < X_tr.size(); ++i) fit_tr[i] += lr * predict_stump(X_tr[i], s);
        vector<double> preds;
        for (const auto& x : X_fw) preds.push_back(predict_ensemble(x, stumps, lr));
        double fw_err = mae(y_fw, preds);
        forward_curve.push_back(fw_err);
        if (fw_err < best_fw - 1e-9) {
            best_fw = fw_err; best_round = rnd; since_best = 0;
        } else {
            ++since_best;
            if (since_best >= patience && stopped_at == max_rounds) stopped_at = rnd;
        }
    }

    double final_fw = forward_curve.back();
    double train_final = mae(y_tr, fit_tr);
    cout << "train MAE at round " << max_rounds << ": " << train_final << "\n";
    cout << "forward MAE: best " << best_fw << " @ round " << best_round << " · final " << final_fw << " @ round " << max_rounds << " · early-stopped @ " << stopped_at << "\n";

    assert(train_final < best_fw);
    assert(final_fw > best_fw * 1.05);
    assert(stopped_at < max_rounds);
    assert(stopped_at - best_round == patience);
    cout << "walk_forward_early_stopping.py PASS\n";
    return 0;
}
