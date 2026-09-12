// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/*
 * Bag-of-Words Vectorizer
 * 
 * Core idea: represent each document as a sparse count vector of word frequencies.
 * Build a shared vocabulary from all documents, then encode each document as counts
 * over that vocabulary. Useful for baseline text representation before more complex methods.
 */

#include <vector>
#include <string>
#include <map>
#include <unordered_map>
#include <algorithm>
#include <cmath>
#include <cctype>
#include <regex>
#include <cassert>
#include <iostream>

class BagOfWordsVectorizer {
    /* Learns vocabulary and converts documents to count vectors. */
public:
    std::unordered_map<std::string, int> vocab;  // word -> word_id
    int vocab_size;

    BagOfWordsVectorizer() : vocab_size(0) {}

    std::vector<std::string> tokenize(const std::string& text) {
        /* Simple word tokenization: lowercase, alphanumeric words. */
        std::string lower_text = text;
        std::transform(lower_text.begin(), lower_text.end(), lower_text.begin(), ::tolower);
        
        std::vector<std::string> words;
        std::string current_word;
        for (char c : lower_text) {
            if (std::isalpha(c)) {
                current_word += c;
            } else {
                if (!current_word.empty()) {
                    words.push_back(current_word);
                    current_word.clear();
                }
            }
        }
        if (!current_word.empty()) {
            words.push_back(current_word);
        }
        return words;
    }

    void build_vocabulary(const std::vector<std::string>& documents) {
        /* Learn vocabulary from documents. */
        std::map<std::string, bool> vocab_set;  // sorted map for determinism
        for (const auto& doc : documents) {
            auto words = tokenize(doc);
            for (const auto& word : words) {
                vocab_set[word] = true;
            }
        }
        for (const auto& kv : vocab_set) {
            vocab[kv.first] = vocab_size++;
        }
    }

    std::unordered_map<int, int> vectorize(const std::string& text) {
        /* Convert document text to sparse word-count vector: {word_id -> count}. */
        std::unordered_map<int, int> vector;
        auto words = tokenize(text);
        for (const auto& word : words) {
            auto it = vocab.find(word);
            if (it != vocab.end()) {
                vector[it->second]++;
            }
        }
        return vector;
    }

    std::vector<int> get_vector_dense(const std::string& text) {
        /* Return dense vector (vocab_size,) with word counts. */
        std::vector<int> dense(vocab_size, 0);
        auto vec = vectorize(text);
        for (const auto& kv : vec) {
            dense[kv.first] = kv.second;
        }
        return dense;
    }
};

double cosine_similarity(const std::vector<int>& vec1, const std::vector<int>& vec2) {
    /* Cosine similarity between two dense count vectors. */
    double dot = 0.0;
    double norm1_sq = 0.0;
    double norm2_sq = 0.0;
    size_t n = std::min(vec1.size(), vec2.size());
    for (size_t i = 0; i < n; ++i) {
        dot += vec1[i] * vec2[i];
        norm1_sq += vec1[i] * vec1[i];
        norm2_sq += vec2[i] * vec2[i];
    }
    double norm1 = std::sqrt(norm1_sq);
    double norm2 = std::sqrt(norm2_sq);
    if (norm1 == 0.0 || norm2 == 0.0) {
        return 0.0;
    }
    return dot / (norm1 * norm2);
}

int main() {
    // Deterministic corpus
    std::vector<std::string> corpus = {
        "The cat sat on the mat",
        "The dog played in the park",
        "Cats and dogs are pets",
        "The mat was comfortable",
        "Parks are good for dogs",
    };

    // Build vectorizer
    BagOfWordsVectorizer vec;
    vec.build_vocabulary(corpus);

    // Vectorize all documents
    std::vector<std::vector<int>> vectors;
    for (const auto& doc : corpus) {
        vectors.push_back(vec.get_vector_dense(doc));
    }

    // Test 1: similar documents should have higher cosine similarity
    double sim_0_3 = cosine_similarity(vectors[0], vectors[3]);
    double sim_0_4 = cosine_similarity(vectors[0], vectors[4]);

    // Document 0 ("The cat sat on the mat") and 3 ("The mat was comfortable")
    // share "the" and "mat", so should be more similar than 0 and 4
    assert(sim_0_3 > sim_0_4);

    // Test 2: vocabulary built correctly
    assert(vec.vocab.find("cat") != vec.vocab.end());
    assert(vec.vocab.find("dog") != vec.vocab.end());
    assert(vec.vocab_size > 0);

    // Test 3: vectorize returns valid counts
    auto test_vec = vec.vectorize("cat cat dog");
    assert(test_vec[vec.vocab["cat"]] == 2);  // Cat count should be 2
    assert(test_vec[vec.vocab["dog"]] == 1);  // Dog count should be 1

    std::cout << "PASS: Bag-of-Words vectorizer learns vocabulary, encodes documents as count vectors, similar docs rank higher" << std::endl;
    return 0;
}
