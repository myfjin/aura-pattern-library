// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/*
Viterbi decoding for a small hidden Markov model: finds the maximum-probability
hidden state sequence for an observation sequence via log-space dynamic
programming with backpointers, then reconstructs the path by backtracking.
Use for POS-tagging-style most-likely-path decoding over discrete states and
emissions. Oracle: on every test observation the Viterbi path and its
log-probability exactly match brute-force enumeration of all state sequences,
so the DP recurrence and backtracking are proven correct, not merely plausible.
*/
#include <algorithm>
#include <cassert>
#include <cmath>
#include <iostream>
#include <limits>
#include <map>
#include <string>
#include <vector>

using namespace std;

class SimpleHMM {
public:
    map<string, double> start_probs = {{"NOUN", 0.6}, {"VERB", 0.4}};
    map<string, map<string, double>> trans_probs = {
        {"NOUN", {{"NOUN", 0.3}, {"VERB", 0.7}}},
        {"VERB", {{"NOUN", 0.8}, {"VERB", 0.2}}}
    };
    map<string, map<string, double>> emit_probs = {
        {"NOUN", {{"dog", 0.4}, {"cat", 0.4}, {"runs", 0.1}, {"sleeps", 0.1}}},
        {"VERB", {{"dog", 0.1}, {"cat", 0.1}, {"runs", 0.4}, {"sleeps", 0.4}}}
    };
    vector<string> states = {"NOUN", "VERB"};

    pair<double, vector<string>> viterbi(const vector<string>& observations) {
        size_t n = observations.size();
        vector<map<string, pair<double, string>>> vit(n);
        for (const string& s : states) {
            double emit = getEmit(s, observations[0]);
            vit[0][s] = {log(start_probs[s]) + log(emit), ""};
        }
        for (size_t t = 1; t < n; ++t) {
            for (const string& cur : states) {
                double emit = getEmit(cur, observations[t]);
                double best = -numeric_limits<double>::infinity();
                string best_prev;
                for (const string& prev : states) {
                    double lp = vit[t-1][prev].first + log(trans_probs[prev][cur]) + log(emit);
                    if (lp > best) { best = lp; best_prev = prev; }
                }
                vit[t][cur] = {best, best_prev};
            }
        }
        string curr = states[0];
        double final_lp = vit[n-1][curr].first;
        for (const string& s : states) {
            if (vit[n-1][s].first > final_lp) { final_lp = vit[n-1][s].first; curr = s; }
        }
        vector<string> path;
        for (int t = static_cast<int>(n) - 1; t >= 0; --t) {
            path.push_back(curr);
            if (t > 0) curr = vit[t][curr].second;
        }
        reverse(path.begin(), path.end());
        return {final_lp, path};
    }

    pair<double, vector<string>> brute_force_best_path(const vector<string>& observations) {
        vector<pair<double, vector<string>>> all;
        enumerate_paths(observations, 0, {}, 0.0, all);
        double best = -numeric_limits<double>::infinity();
        vector<string> best_path;
        for (auto& p : all) {
            if (p.first > best) { best = p.first; best_path = p.second; }
        }
        return {best, best_path};
    }

private:
    double getEmit(const string& s, const string& o) {
        auto it = emit_probs[s].find(o);
        return (it == emit_probs[s].end()) ? 1e-10 : it->second;
    }

    void enumerate_paths(const vector<string>& observations, size_t idx,
                         const vector<string>& current_seq, double current_log_prob,
                         vector<pair<double, vector<string>>>& out) {
        if (idx == observations.size()) {
            out.push_back({current_log_prob, current_seq});
            return;
        }
        for (const string& s : states) {
            double emit = getEmit(s, observations[idx]);
            double new_lp;
            if (idx == 0) new_lp = log(start_probs[s]) + log(emit);
            else new_lp = current_log_prob + log(trans_probs[current_seq.back()][s]) + log(emit);
            vector<string> next = current_seq;
            next.push_back(s);
            enumerate_paths(observations, idx + 1, next, new_lp, out);
        }
    }
};

int main() {
    SimpleHMM hmm;
    vector<vector<string>> test_cases = {
        {"dog", "runs"},
        {"cat", "sleeps"},
        {"dog", "cat", "runs"},
        {"runs", "sleeps", "dog"}
    };

    for (auto& obs : test_cases) {
        auto [vlp, vpath] = hmm.viterbi(obs);
        auto [blp, bpath] = hmm.brute_force_best_path(obs);
        assert(abs(vlp - blp) < 1e-6);
        assert(vpath == bpath);
    }

    auto [vlp, vpath] = hmm.viterbi({"dog", "runs", "cat"});
    assert(vpath.size() == 3);
    for (const string& s : vpath) assert(s == "NOUN" || s == "VERB");

    auto [slp, spath] = hmm.viterbi({"dog"});
    auto [sblp, sbpath] = hmm.brute_force_best_path({"dog"});
    assert(slp == sblp);
    assert(spath == sbpath);

    cout << "PASS: Viterbi decoding finds optimal state sequence, matches brute-force enumeration\n";
    return 0;
}
