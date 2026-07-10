// Three-Stage Dedup Pipeline — C++17 port of the Python oracle.
// Stages: MinHash candidate generation, edit-distance verification, LCS word diff.

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <random>
#include <sstream>
#include <string>
#include <unordered_set>
#include <utility>
#include <vector>

using namespace std;

// Deterministic 64-bit hash for strings (splitmix64 seeded per hash index).
static uint64_t splitmix64(uint64_t& state) {
    uint64_t z = (state += 0x9e3779b97f4a7c15ULL);
    z = (z ^ (z >> 30)) * 0xbf58476d1ce4e5b9ULL;
    z = (z ^ (z >> 27)) * 0x94d049bb133111ebULL;
    return z ^ (z >> 31);
}

static uint64_t hash_string(const string& s, uint64_t seed) {
    // FNV-1a variant seeded by the hash index.
    uint64_t state = seed + 0xcbf29ce484222325ULL;
    for (unsigned char c : s) {
        state ^= static_cast<uint64_t>(c);
        state *= 0x100000001b3ULL;
    }
    // mix with splitmix64 for better distribution
    return splitmix64(state);
}

static vector<string> words(const string& s) {
    vector<string> out;
    string cur;
    for (char c : s) {
        if (isspace(static_cast<unsigned char>(c))) {
            if (!cur.empty()) { out.push_back(cur); cur.clear(); }
        } else {
            cur.push_back(static_cast<char>(tolower(static_cast<unsigned char>(c))));
        }
    }
    if (!cur.empty()) out.push_back(cur);
    return out;
}

static unordered_set<string> shingles(const string& text, int k = 3) {
    auto w = words(text);
    unordered_set<string> out;
    int n = max(1, static_cast<int>(w.size()) - k + 1);
    for (int i = 0; i < n; ++i) {
        string sh;
        for (int j = 0; j < k; ++j) {
            if (j) sh.push_back(' ');
            sh += w[i + j];
        }
        out.insert(sh);
    }
    return out;
}

static vector<uint64_t> minhash_signature(const unordered_set<string>& sh, int num_hashes = 64) {
    vector<uint64_t> sig(num_hashes, 0);
    for (int seed = 0; seed < num_hashes; ++seed) {
        if (sh.empty()) {
            sig[seed] = 0;
        } else {
            uint64_t best = UINT64_MAX;
            for (const auto& s : sh) {
                best = min(best, hash_string(s, static_cast<uint64_t>(seed)));
            }
            sig[seed] = best;
        }
    }
    return sig;
}

static double estimated_jaccard(const vector<uint64_t>& a, const vector<uint64_t>& b) {
    int eq = 0;
    for (size_t i = 0; i < a.size(); ++i) eq += (a[i] == b[i]);
    return static_cast<double>(eq) / a.size();
}

static int edit_distance(const string& a, const string& b) {
    int m = static_cast<int>(a.size()), n = static_cast<int>(b.size());
    vector<int> prev(n + 1), cur(n + 1);
    for (int j = 0; j <= n; ++j) prev[j] = j;
    for (int i = 1; i <= m; ++i) {
        cur[0] = i;
        for (int j = 1; j <= n; ++j) {
            cur[j] = min({prev[j] + 1, cur[j - 1] + 1,
                          prev[j - 1] + (a[i - 1] != b[j - 1])});
        }
        swap(prev, cur);
    }
    return prev[n];
}

static vector<string> word_diff(const string& a, const string& b) {
    auto wa = words(a), wb = words(b);
    int m = static_cast<int>(wa.size()), n = static_cast<int>(wb.size());
    vector<vector<int>> L(m + 1, vector<int>(n + 1, 0));
    for (int i = m - 1; i >= 0; --i) {
        for (int j = n - 1; j >= 0; --j) {
            if (wa[i] == wb[j]) L[i][j] = L[i + 1][j + 1] + 1;
            else L[i][j] = max(L[i + 1][j], L[i][j + 1]);
        }
    }
    vector<string> out;
    int i = 0, j = 0;
    while (i < m && j < n) {
        if (wa[i] == wb[j]) { ++i; ++j; }
        else if (L[i + 1][j] >= L[i][j + 1]) {
            out.push_back("-" + wa[i++]);
        } else {
            out.push_back("+" + wb[j++]);
        }
    }
    for (; i < m; ++i) out.push_back("-" + wa[i]);
    for (; j < n; ++j) out.push_back("+" + wb[j]);
    return out;
}

struct Result {
    vector<pair<int,int>> candidates;
    vector<pair<int,int>> verified;
    vector<vector<string>> explanations; // aligned with verified
};

static Result dedup_pipeline(const vector<string>& docs, double cand_thresh = 0.5,
                            double verify_ratio = 0.25) {
    vector<vector<uint64_t>> sigs;
    for (const auto& d : docs) sigs.push_back(minhash_signature(shingles(d)));
    int n = static_cast<int>(docs.size());
    Result r;
    for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j < n; ++j) {
            if (estimated_jaccard(sigs[i], sigs[j]) >= cand_thresh)
                r.candidates.emplace_back(i, j);
        }
    }
    for (auto [i, j] : r.candidates) {
        int dist = edit_distance(docs[i], docs[j]);
        int denom = max(static_cast<int>(docs[i].size()), static_cast<int>(docs[j].size()));
        if (dist / static_cast<double>(denom) <= verify_ratio) {
            r.verified.emplace_back(i, j);
            r.explanations.push_back(word_diff(docs[i], docs[j]));
        }
    }
    return r;
}

int main() {
    mt19937 rng(42);

    vector<string> base = {
        "the quick brown fox jumps over the lazy dog near the river bank",
        "machine learning models require careful validation on held out data",
        "the gateway daemon restarts automatically after every clean shutdown",
        "seasonal patterns in retail sales peak sharply before winter holidays"
    };
    vector<string> docs;
    vector<pair<int,int>> planted;
    for (const auto& b : base) {
        docs.push_back(b);
        // small honest edit: replace first "the " with "a " and append " today"
        string near = b;
        size_t pos = near.find("the ");
        if (pos != string::npos) near.replace(pos, 4, "a ");
        near += " today";
        planted.emplace_back(static_cast<int>(docs.size()) - 1, static_cast<int>(docs.size()));
        docs.push_back(near);
    }
    vector<string> vocab = {
        "alpha", "beta", "gamma", "delta", "metrics", "kernel", "tensor",
        "stream", "buffer", "socket", "ledger", "raft", "quorum", "shard",
        "vector", "matrix", "entropy", "gradient"
    };
    uniform_int_distribution<int> vocab_dist(0, static_cast<int>(vocab.size()) - 1);
    for (int k = 0; k < 22; ++k) {
        string doc;
        for (int w = 0; w < 12; ++w) {
            if (w) doc.push_back(' ');
            doc += vocab[vocab_dist(rng)];
        }
        docs.push_back(doc);
    }

    auto r = dedup_pipeline(docs);
    int total_pairs = static_cast<int>(docs.size()) * (static_cast<int>(docs.size()) - 1) / 2;

    cout << "docs: " << docs.size() << " all-pairs " << total_pairs
         << " MinHash candidates " << r.candidates.size()
         << " verified near-dups " << r.verified.size() << "\n";
    cout << "explanation for pair (" << r.verified[0].first << ","
         << r.verified[0].second << "): ";
    for (size_t i = 0; i < min<size_t>(6, r.explanations[0].size()); ++i)
        cout << r.explanations[0][i] << (i + 1 < min<size_t>(6, r.explanations[0].size()) ? " " : "\n");

    // All planted pairs must be verified.
    for (const auto& p : planted)
        assert(find(r.verified.begin(), r.verified.end(), p) != r.verified.end());
    // No false pairs may pass exact verification.
    for (const auto& p : r.verified)
        assert(find(planted.begin(), planted.end(), p) != planted.end());
    // Candidate stage must prune >80% of all-pairs comparisons.
    assert(r.candidates.size() < 0.2 * total_pairs);
    // Diff must actually explain the difference.
    bool has_diff = false;
    for (const auto& tok : r.explanations[0])
        if (!tok.empty() && (tok[0] == '-' || tok[0] == '+')) has_diff = true;
    assert(has_diff);

    cout << "dedup_pipeline.cpp PASS\n";
    return 0;
}
