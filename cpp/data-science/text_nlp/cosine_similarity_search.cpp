// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/*
 * Cosine Similarity Search: TF-IDF Search Engine
 * 
 * Convert documents and query to TF-IDF vectors, rank documents by cosine similarity.
 */

#include <vector>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <cmath>
#include <algorithm>
#include <cassert>
#include <iostream>
#include <sstream>
#include <cctype>
#include <map>

class SimpleSearchEngine {
    std::vector<std::string> documents;
    std::unordered_map<std::string, int> vocab;
    std::unordered_map<std::string, int> doc_freq;
    std::unordered_map<std::string, double> idf;

    std::vector<std::string> tokenize(const std::string& text) {
        std::vector<std::string> tokens;
        std::string lower_text, word;
        for (char c : text) {
            lower_text += static_cast<char>(std::tolower(static_cast<unsigned char>(c)));
        }
        for (char c : lower_text) {
            if (std::isalpha(c)) {
                word += c;
            } else if (!word.empty()) {
                tokens.push_back(word);
                word.clear();
            }
        }
        if (!word.empty()) tokens.push_back(word);
        return tokens;
    }

public:
    void index(const std::vector<std::string>& docs) {
        documents = docs;
        std::unordered_set<std::string> vocab_set;

        for (const auto& doc : documents) {
            auto words = tokenize(doc);
            std::unordered_set<std::string> unique_words(words.begin(), words.end());
            vocab_set.insert(unique_words.begin(), unique_words.end());
            for (const auto& w : unique_words) {
                doc_freq[w]++;
            }
        }

        for (const auto& word : vocab_set) {
            vocab[word] = static_cast<int>(vocab.size());
        }

        int n_docs = static_cast<int>(documents.size());
        for (const auto& kv : doc_freq) {
            idf[kv.first] = std::log((n_docs + 1.0) / (kv.second + 1.0)) + 1.0;
        }
    }

    std::unordered_map<int, double> get_tfidf_vector(const std::string& text) {
        auto words = tokenize(text);
        std::unordered_map<std::string, int> tf;
        for (const auto& word : words) {
            tf[word]++;
        }

        std::unordered_map<int, double> vector;
        for (const auto& kv : tf) {
            auto it = vocab.find(kv.first);
            if (it != vocab.end()) {
                double idf_val = idf.count(kv.first) ? idf.at(kv.first) : 0.0;
                vector[it->second] = kv.second * idf_val;
            }
        }
        return vector;
    }

    double cosine_similarity(const std::unordered_map<int, double>& vec1,
                            const std::unordered_map<int, double>& vec2) {
        double dot = 0.0, norm1 = 0.0, norm2 = 0.0;
        std::unordered_set<int> all_keys;
        for (const auto& kv : vec1) all_keys.insert(kv.first);
        for (const auto& kv : vec2) all_keys.insert(kv.first);

        for (int wid : all_keys) {
            double v1 = vec1.count(wid) ? vec1.at(wid) : 0.0;
            double v2 = vec2.count(wid) ? vec2.at(wid) : 0.0;
            dot += v1 * v2;
            norm1 += v1 * v1;
            norm2 += v2 * v2;
        }
        if (norm1 == 0.0 || norm2 == 0.0) return 0.0;
        return dot / (std::sqrt(norm1) * std::sqrt(norm2));
    }

    std::vector<std::pair<std::string, double>> search(const std::string& query, int top_k = 5) {
        auto query_vec = get_tfidf_vector(query);
        std::vector<std::pair<std::string, double>> scores;

        for (const auto& doc : documents) {
            auto doc_vec = get_tfidf_vector(doc);
            double score = cosine_similarity(query_vec, doc_vec);
            scores.push_back({doc, score});
        }

        std::sort(scores.begin(), scores.end(),
            [](const auto& a, const auto& b) { return a.second > b.second; });

        if (static_cast<int>(scores.size()) > top_k) {
            scores.resize(top_k);
        }
        return scores;
    }
};

int main() {
    std::vector<std::string> docs = {
        "machine learning algorithms",
        "deep learning neural networks",
        "python programming language",
        "web development html css",
        "machine learning classification tasks",
        "java programming for beginners",
    };

    SimpleSearchEngine engine;
    engine.index(docs);

    // Test 1: Query "machine learning" should rank docs 0 and 4 highest
    auto results = engine.search("machine learning", 3);
    std::vector<std::string> top_docs;
    for (const auto& r : results) top_docs.push_back(r.first);
    bool has_0 = false, has_4 = false;
    for (const auto& d : top_docs) {
        if (d == docs[0]) has_0 = true;
        if (d == docs[4]) has_4 = true;
    }
    assert(has_0 && has_4);

    // Test 2: Query "python" should rank doc 2 highest
    auto results2 = engine.search("python", 1);
    assert(results2[0].first == docs[2]);

    // Test 3: Query and exact doc match should have high similarity
    auto results3 = engine.search(docs[0], 1);
    assert(results3[0].first == docs[0]);
    assert(results3[0].second > 0.9);

    // Test 4: Unrelated query should have lower scores overall
    auto results_ml = engine.search("machine learning", 6);
    auto results_web = engine.search("web development", 1);
    std::vector<double> scores_ml, scores_web;
    for (const auto& r : results_ml) scores_ml.push_back(r.second);
    for (const auto& r : results_web) scores_web.push_back(r.second);

    // Web query should be less similar to ML docs than ML query
    assert(*std::max_element(scores_web.begin(), scores_web.end()) <=
           *std::max_element(scores_ml.begin(), scores_ml.end()));

    std::cout << "Cosine similarity search PASS" << std::endl;
    return 0;
}
