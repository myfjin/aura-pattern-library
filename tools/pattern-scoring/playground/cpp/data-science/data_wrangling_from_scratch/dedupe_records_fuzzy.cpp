// Fuzzy Record Deduplication — C++17 port.
// Normalize names, cluster by Levenshtein edit-distance threshold, keep first of each cluster.

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
#include <algorithm>
#include <cassert>
#include <cctype>
#include <functional>
#include <iostream>
#include <limits>
#include <cmath>
#include <vector>
#include <string>

using namespace std;

static string normalize(const string& s) {
    string out;
    for (char c : s) out.push_back(tolower(static_cast<unsigned char>(c)));
    // trim leading/trailing whitespace
    size_t a = 0;
    while (a < out.size() && isspace(static_cast<unsigned char>(out[a]))) ++a;
    size_t b = out.size();
    while (b > a && isspace(static_cast<unsigned char>(out[b - 1]))) --b;
    return out.substr(a, b - a);
}

static int edit_distance(const string& s1, const string& s2) {
    int m = static_cast<int>(s1.size()), n = static_cast<int>(s2.size());
    vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));
    for (int i = 0; i <= m; ++i) dp[i][0] = i;
    for (int j = 0; j <= n; ++j) dp[0][j] = j;
    for (int i = 1; i <= m; ++i) {
        for (int j = 1; j <= n; ++j) {
            if (s1[i - 1] == s2[j - 1]) dp[i][j] = dp[i - 1][j - 1];
            else dp[i][j] = 1 + min({dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]});
        }
    }
    return dp[m][n];
}

struct Record {
    int id;
    string name;
};

static vector<vector<int>> find_duplicates(const vector<Record>& records,
                                                [[maybe_unused]] const string& match_key,
                                                int threshold) {
    int n = static_cast<int>(records.size());
    vector<bool> visited(n, false);
    vector<vector<int>> clusters;
    for (int i = 0; i < n; ++i) {
        if (visited[i]) continue;
        vector<int> cluster = {i};
        visited[i] = true;
        string s1 = normalize(records[i].name);
        for (int j = i + 1; j < n; ++j) {
            if (visited[j]) continue;
            string s2 = normalize(records[j].name);
            if (edit_distance(s1, s2) <= threshold) {
                cluster.push_back(j);
                visited[j] = true;
            }
        }
        clusters.push_back(cluster);
    }
    return clusters;
}

static vector<Record> dedupe(const vector<Record>& records,
                             const string& match_key, int threshold) {
    auto clusters = find_duplicates(records, match_key, threshold);
    vector<Record> result;
    for (const auto& c : clusters) result.push_back(records[c[0]]);
    return result;
}

int main() {
    vector<Record> records = {
        {1, "Alice Johnson"},
        {2, "Alice Jonson"},
        {3, "Bob Smith"},
        {4, "Bob Smyth"},
        {5, "Charlie Brown"},
    };

    auto clusters = find_duplicates(records, "name", 2);
    assert(clusters.size() == 3);

    vector<vector<int>> two_clusters;
    for (const auto& c : clusters)
        if (c.size() == 2) two_clusters.push_back(c);
    assert(two_clusters.size() == 2);
    assert(find(two_clusters.begin(), two_clusters.end(), vector<int>{0, 1}) != two_clusters.end());

    auto deduped = dedupe(records, "name", 2);
    assert(deduped.size() == 3);
    vector<int> kept_ids;
    for (const auto& r : deduped) kept_ids.push_back(r.id);
    assert((kept_ids == vector<int>{1, 3, 5}));

    cout << "Records: " << records.size() << " | Clusters: " << clusters.size()
         << " | Deduped: " << deduped.size() << " | Kept ids: ";
    for (size_t i = 0; i < kept_ids.size(); ++i)
        cout << kept_ids[i] << (i + 1 < kept_ids.size() ? "," : "");
    cout << " | PASS\n";
    return 0;
}
