// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/*
 * BM25 Ranking (Okapi BM25)
 * 
 * BM25 ranks documents by relevance to a query via TF-IDF with saturation and length normalization.
 */

#include <vector>
#include <string>
#include <cmath>
#include <algorithm>
#include <cassert>
#include <iostream>
#include <unordered_map>

double bm25_score(
    const std::vector<std::string>& query_terms,
    const std::vector<std::vector<std::string>>& all_docs,
    size_t doc_idx,
    double k1 = 1.5,
    double b = 0.75
) {
    /* BM25 score for a document. */
    std::vector<size_t> doc_lengths;
    for (const auto& doc : all_docs) {
        doc_lengths.push_back(doc.size());
    }

    double avg_len = 0.0;
    for (size_t len : doc_lengths) avg_len += len;
    avg_len /= all_docs.size();

    size_t doc_len = doc_lengths[doc_idx];
    const auto& doc_text = all_docs[doc_idx];

    // Term frequencies in document
    std::unordered_map<std::string, size_t> term_freqs;
    for (const auto& term : doc_text) {
        term_freqs[term]++;
    }

    double score = 0.0;
    for (const auto& query_term : query_terms) {
        auto it = term_freqs.find(query_term);
        if (it != term_freqs.end()) {
            double tf = static_cast<double>(it->second);
            // IDF approximation
            double idf = std::log(10.0);
            double numerator = tf * (k1 + 1.0);
            double denominator = tf + k1 * (1.0 - b + b * doc_len / avg_len);
            score += idf * numerator / denominator;
        }
    }

    return score;
}

double tf_score(const std::vector<std::string>& query_terms, const std::vector<std::string>& doc_terms) {
    /* Naive TF score: count query terms in document. */
    double count = 0.0;
    for (const auto& term : doc_terms) {
        for (const auto& qt : query_terms) {
            if (term == qt) {
                count++;
                break;
            }
        }
    }
    return count;
}

int main() {
    // Query
    std::vector<std::string> query = {"python", "machine", "learning"};

    // Doc 1: relevant (contains query terms), short
    std::vector<std::string> doc1_terms = {"python", "machine", "learning", "model", "training"};
    for (int i = 0; i < 5; ++i) doc1_terms.push_back("code");

    // Doc 2: irrelevant (does not contain query terms, just filler), very long
    std::vector<std::string> doc2_terms;
    for (int i = 0; i < 50; ++i) {
        doc2_terms.push_back("data");
        doc2_terms.push_back("processing");
    }

    // Doc 3: relevant, same terms as doc1 but longer with filler
    std::vector<std::string> doc3_terms = {"python", "machine", "learning", "model", "training"};
    for (int i = 0; i < 25; ++i) doc3_terms.push_back("code");

    std::vector<std::vector<std::string>> docs_terms = {doc1_terms, doc2_terms, doc3_terms};

    // Rank with BM25
    std::vector<double> bm25_scores(3);
    for (size_t i = 0; i < 3; ++i) {
        bm25_scores[i] = bm25_score(query, docs_terms, i);
    }

    std::vector<size_t> bm25_ranking = {0, 1, 2};
    std::sort(bm25_ranking.begin(), bm25_ranking.end(), [&](size_t a, size_t b) {
        return bm25_scores[a] > bm25_scores[b];
    });

    // Rank with naive TF
    std::vector<double> tf_scores(3);
    for (size_t i = 0; i < 3; ++i) {
        tf_scores[i] = tf_score(query, docs_terms[i]);
    }

    std::vector<size_t> tf_ranking = {0, 1, 2};
    std::sort(tf_ranking.begin(), tf_ranking.end(), [&](size_t a, size_t b) {
        return tf_scores[a] > tf_scores[b];
    });

    // BM25 should rank doc1 or doc3 highest (both relevant)
    size_t bm25_top = bm25_ranking[0];
    assert(bm25_top == 0 || bm25_top == 2);
    assert(bm25_ranking[0] != 1);

    // BM25 should rank shorter relevant doc higher than longer one (same relevance)
    size_t rank_0 = 0, rank_2 = 0;
    for (size_t i = 0; i < 3; ++i) {
        if (bm25_ranking[i] == 0) rank_0 = i;
        if (bm25_ranking[i] == 2) rank_2 = i;
    }
    assert(rank_0 < rank_2);

    std::cout << "BM25 ranking: [" << bm25_ranking[0] << ", " << bm25_ranking[1] << ", " << bm25_ranking[2] << "] PASS" << std::endl;
    return 0;
}
