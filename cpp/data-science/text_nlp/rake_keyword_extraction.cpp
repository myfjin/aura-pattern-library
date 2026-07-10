// rake_keyword_extraction.cpp — RAKE-style keyword extraction.

// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
#include <algorithm>
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <set>
#include <sstream>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>

struct RAKEExtractor {
    std::unordered_set<std::string> stopwords;

    RAKEExtractor() {
        const char* sw[] = {
            "the", "a", "an", "and", "or", "but", "is", "are", "was", "were",
            "be", "been", "being", "have", "has", "had", "do", "does", "did",
            "will", "would", "should", "could", "may", "might", "can", "must",
            "in", "on", "at", "by", "for", "with", "to", "of", "from", "up",
            "as", "if", "about", "into", "through", "during", "this", "that",
            "these", "those", "i", "you", "he", "she", "it", "we", "they",
            nullptr
        };
        for (int i = 0; sw[i]; ++i) stopwords.insert(sw[i]);
    }

    std::vector<std::string> tokenize(const std::string& text) const {
        std::vector<std::string> words;
        std::string cur;
        for (char ch : text) {
            if (std::isalpha(static_cast<unsigned char>(ch))) {
                cur.push_back(static_cast<char>(std::tolower(static_cast<unsigned char>(ch))));
            } else {
                if (!cur.empty()) {
                    words.push_back(cur);
                    cur.clear();
                }
            }
        }
        if (!cur.empty()) words.push_back(cur);
        return words;
    }

    std::vector<std::vector<std::string>> extract_phrases(const std::string& text) const {
        std::vector<std::string> words = tokenize(text);
        std::vector<std::vector<std::string>> phrases;
        std::vector<std::string> current;
        for (const auto& w : words) {
            if (stopwords.count(w)) {
                if (!current.empty()) {
                    phrases.push_back(current);
                    current.clear();
                }
            } else {
                current.push_back(w);
            }
        }
        if (!current.empty()) phrases.push_back(current);
        return phrases;
    }

    std::unordered_map<std::string, double> compute_word_scores(
            const std::vector<std::vector<std::string>>& phrases) const {
        std::unordered_map<std::string, std::set<std::string>> co_occurrence;
        std::unordered_map<std::string, int> frequency;

        for (const auto& phrase : phrases) {
            for (const auto& word : phrase) {
                ++frequency[word];
                for (const auto& other : phrase) {
                    if (other != word) co_occurrence[word].insert(other);
                }
            }
        }

        std::unordered_map<std::string, double> word_scores;
        for (const auto& kv : frequency) {
            int degree = static_cast<int>(co_occurrence[kv.first].size());
            word_scores[kv.first] = static_cast<double>(degree + 1) / (kv.second + 1);
        }
        return word_scores;
    }

    std::vector<std::pair<std::string, double>> score_phrases(
            const std::vector<std::vector<std::string>>& phrases,
            const std::unordered_map<std::string, double>& word_scores) const {
        std::vector<std::pair<std::string, double>> phrase_scores;
        for (const auto& phrase : phrases) {
            std::string text;
            double score = 0.0;
            for (std::size_t i = 0; i < phrase.size(); ++i) {
                if (i) text.push_back(' ');
                text += phrase[i];
                auto it = word_scores.find(phrase[i]);
                if (it != word_scores.end()) score += it->second;
            }
            phrase_scores.emplace_back(text, score);
        }
        return phrase_scores;
    }

    std::vector<std::pair<std::string, double>> extract_keywords(
            const std::string& text, int top_k = 5) const {
        auto phrases = extract_phrases(text);
        auto word_scores = compute_word_scores(phrases);
        auto phrase_scores = score_phrases(phrases, word_scores);
        std::sort(phrase_scores.begin(), phrase_scores.end(),
                  [](const auto& a, const auto& b) { return a.second > b.second; });
        if (static_cast<int>(phrase_scores.size()) > top_k)
            phrase_scores.resize(top_k);
        return phrase_scores;
    }
};

int main() {
    const char* text =
        "Machine learning is a subset of artificial intelligence that focuses on "
        "learning from data. Deep learning uses neural networks with multiple layers. "
        "Natural language processing is used for text analysis. Machine learning models "
        "are trained on large datasets. Deep learning is powerful for image recognition "
        "and language understanding.";

    RAKEExtractor extractor;

    auto phrases = extractor.extract_phrases(text);
    assert(!phrases.empty());
    for (const auto& p : phrases) {
        assert(!p.empty());
        for (const auto& w : p) {
            assert(!extractor.stopwords.count(w));
            assert(!w.empty());
        }
    }

    auto word_scores = extractor.compute_word_scores(phrases);
    assert(!word_scores.empty());
    for (const auto& kv : word_scores) assert(kv.second >= 0.0);

    auto keywords = extractor.extract_keywords(text, 5);
    assert(keywords.size() <= 5);
    for (const auto& kv : keywords) {
        assert(!kv.first.empty());
        assert(!std::isnan(kv.second));
    }

    // descending by score
    for (std::size_t i = 1; i < keywords.size(); ++i)
        assert(keywords[i - 1].second >= keywords[i].second - 1e-12);

    bool has_learning = false;
    for (const auto& kv : keywords)
        if (kv.first.find("learning") != std::string::npos) has_learning = true;
    assert(has_learning);

    auto empty = extractor.extract_keywords("", 5);
    assert(empty.empty());

    std::printf("PASS: RAKE extracts phrases, scores by degree/frequency, ranks technical terms higher\n");
    return 0;
}
