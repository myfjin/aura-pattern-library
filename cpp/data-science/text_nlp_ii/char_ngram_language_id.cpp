// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/*
 * Character N-gram Language Identification
 * 
 * Distinguish languages via bigram profiles.
 * Builds character bigram frequencies; compares via distance.
 */

#include <string>
#include <unordered_map>
#include <unordered_set>
#include <cmath>
#include <cassert>
#include <iostream>
#include <algorithm>
#include <cctype>

std::unordered_map<std::string, int> char_bigrams(const std::string& text) {
    /* Extract character bigrams (2-char sequences). */
    std::string lower_text;
    lower_text.reserve(text.size());
    for (char c : text) {
        lower_text += static_cast<char>(std::tolower(static_cast<unsigned char>(c)));
    }

    std::unordered_map<std::string, int> bigrams;
    for (size_t i = 0; i + 1 < lower_text.size(); ++i) {
        std::string bg = lower_text.substr(i, 2);
        bigrams[bg]++;
    }
    return bigrams;
}

double ngram_distance(
    const std::unordered_map<std::string, int>& bigrams1,
    const std::unordered_map<std::string, int>& bigrams2
) {
    /* L1 distance between normalized bigram profiles. */
    int total1 = 0, total2 = 0;
    for (const auto& kv : bigrams1) total1 += kv.second;
    for (const auto& kv : bigrams2) total2 += kv.second;

    if (total1 == 0 || total2 == 0) {
        return std::numeric_limits<double>::infinity();
    }

    std::unordered_set<std::string> all_bigrams;
    for (const auto& kv : bigrams1) all_bigrams.insert(kv.first);
    for (const auto& kv : bigrams2) all_bigrams.insert(kv.first);

    double dist = 0.0;
    for (const auto& bg : all_bigrams) {
        double p1 = static_cast<double>(bigrams1.count(bg) ? bigrams1.at(bg) : 0) / total1;
        double p2 = static_cast<double>(bigrams2.count(bg) ? bigrams2.at(bg) : 0) / total2;
        dist += std::abs(p1 - p2);
    }

    return dist;
}

int main() {
    // Planted: true English text and pseudo-random text.
    std::string english_text = "the quick brown fox jumps over the lazy dog";
    auto english_bigrams = char_bigrams(english_text);

    // Pseudo-language: random characters.
    std::string pseudo_text = "xqzpjkwvmnblcdfghjkl";
    auto pseudo_bigrams = char_bigrams(pseudo_text);

    // True English should be closer to english_text than pseudo is.
    std::string test_english = "the dog is nice";
    auto test_english_bigrams = char_bigrams(test_english);

    double dist_english = ngram_distance(test_english_bigrams, english_bigrams);
    double dist_pseudo = ngram_distance(test_english_bigrams, pseudo_bigrams);

    assert(dist_english < dist_pseudo);

    std::cout << "char_ngram_language_id.cpp PASS" << std::endl;
    return 0;
}
