// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
#include <algorithm>
#include <cassert>
#include <cmath>
#include <iostream>
#include <random>
#include <vector>

using namespace std;

using Point = pair<double, double>;

struct Classifier {
    virtual ~Classifier() = default;
    virtual int predict(const Point& x) const = 0;
};

double threshold_classifier_x(const vector<Point>& X, const vector<int>& y, int split_dim) {
    vector<double> values;
    for (const auto& p : X) values.push_back(split_dim == 0 ? p.first : p.second);
    sort(values.begin(), values.end());
    double threshold = values[values.size() / 2];
    double best_err = 1e300;
    double best_thr = threshold;
    int step = max(1, static_cast<int>(values.size()) / 5);
    for (size_t i = 0; i < values.size(); i += step) {
        double t = values[i];
        int err = 0;
        for (size_t j = 0; j < X.size(); ++j) {
            double v = split_dim == 0 ? X[j].first : X[j].second;
            int pred = v > t ? 1 : 0;
            if (pred != y[j]) ++err;
        }
        if (err < best_err) { best_err = err; best_thr = t; }
    }
    return best_thr;
}

int predict_classifier_x(const Point& x, double threshold, int split_dim) {
    double v = split_dim == 0 ? x.first : x.second;
    return v > threshold ? 1 : 0;
}

struct WeakClassifier1 : Classifier {
    double threshold;
    WeakClassifier1(const vector<Point>& X, const vector<int>& y) {
        threshold = threshold_classifier_x(X, y, 0);
    }
    int predict(const Point& x) const override { return predict_classifier_x(x, threshold, 0); }
};

struct WeakClassifier2 : Classifier {
    double threshold;
    WeakClassifier2(const vector<Point>& X, const vector<int>& y) {
        threshold = threshold_classifier_x(X, y, 1);
    }
    int predict(const Point& x) const override { return predict_classifier_x(x, threshold, 1); }
};

struct WeakClassifier3 : Classifier {
    double threshold;
    WeakClassifier3(const vector<Point>& X, const vector<int>& y) {
        vector<double> diffs;
        for (const auto& p : X) diffs.push_back(p.first - p.second);
        sort(diffs.begin(), diffs.end());
        threshold = diffs[diffs.size() / 2];
        double best_err = 1e300;
        int step = max(1, static_cast<int>(diffs.size()) / 5);
        for (size_t i = 0; i < diffs.size(); i += step) {
            double t = diffs[i];
            int err = 0;
            for (size_t j = 0; j < X.size(); ++j) {
                int pred = (X[j].first - X[j].second) > t ? 1 : 0;
                if (pred != y[j]) ++err;
            }
            if (err < best_err) { best_err = err; threshold = t; }
        }
    }
    int predict(const Point& x) const override { return (x.first - x.second) > threshold ? 1 : 0; }
};

vector<int> hard_voting(const vector<Point>& X, const vector<Classifier*>& clfs) {
    vector<int> preds;
    for (const auto& x : X) {
        int s = 0;
        for (const auto* clf : clfs) s += clf->predict(x);
        double avg = static_cast<double>(s) / clfs.size();
        preds.push_back(avg >= 0.5 ? 1 : 0);
    }
    return preds;
}

int main() {
    mt19937 rng(42);
    normal_distribution<double> d0(2.0, 1.5), d1(8.0, 1.5);
    vector<Point> X;
    vector<int> y;
    for (int i = 0; i < 40; ++i) { X.push_back({d0(rng), d0(rng)}); y.push_back(0); }
    for (int i = 0; i < 40; ++i) { X.push_back({d1(rng), d1(rng)}); y.push_back(1); }

    WeakClassifier1 clf1(X, y);
    WeakClassifier2 clf2(X, y);
    WeakClassifier3 clf3(X, y);
    vector<Classifier*> clfs = {&clf1, &clf2, &clf3};

    auto acc = [&](const Classifier* c) {
        int s = 0;
        for (size_t i = 0; i < X.size(); ++i) if (c->predict(X[i]) == y[i]) ++s;
        return static_cast<double>(s) / X.size();
    };
    double a1 = acc(&clf1), a2 = acc(&clf2), a3 = acc(&clf3);
    double avg_ind = (a1 + a2 + a3) / 3.0;

    auto voting_preds = hard_voting(X, clfs);
    int s = 0;
    for (size_t i = 0; i < X.size(); ++i) if (voting_preds[i] == y[i]) ++s;
    double voting_acc = static_cast<double>(s) / X.size();

    assert(voting_acc > avg_ind);
    cout << "voting_classifier: avg_individual=" << avg_ind << ", ensemble=" << voting_acc << " PASS\n";
    return 0;
}
