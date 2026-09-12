// N-gram language model with add-one smoothing.
// Deterministic corpus, deterministic sampling via seeded RNG.
// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
#include <cassert>
#include <cmath>
#include <cstdint>
#include <cstdio>
#include <map>
#include <set>
#include <sstream>
#include <string>
#include <vector>

static uint64_t rng_state = 42ULL;
double uniform01() {
    rng_state = rng_state * 6364136223846793005ULL + 1442695040888963407ULL;
    return ((rng_state >> 11) & 0x1FFFFFFFFFFFFFULL) / 9007199254740992.0;
}

class NGramLanguageModel {
public:
    explicit NGramLanguageModel(int n = 2) : n_(n) {}

    void fit(const std::vector<std::string>& documents) {
        for (const auto& doc : documents) {
            auto tokens = tokenize(doc);
            vocab_.insert(tokens.begin(), tokens.end());
            for (size_t i = 0; i + n_ <= tokens.size(); ++i) {
                std::vector<std::string> ngram(tokens.begin() + i,
                                                tokens.begin() + i + n_);
                std::vector<std::string> context(tokens.begin() + i,
                                                  tokens.begin() + i + n_ - 1);
                std::string token = ngram.back();
                ++context_counts_[context];
                ++transition_counts_[ngram];
            }
        }
    }

    double get_probability(const std::vector<std::string>& context,
                           const std::string& token) const {
        std::vector<std::string> ngram = context;
        ngram.push_back(token);
        int64_t num = 1;
        int64_t den = static_cast<int64_t>(vocab_.size());
        auto it_n = transition_counts_.find(ngram);
        if (it_n != transition_counts_.end()) num += it_n->second;
        auto it_c = context_counts_.find(context);
        if (it_c != context_counts_.end()) den += it_c->second;
        return static_cast<double>(num) / static_cast<double>(den);
    }

    double perplexity(const std::string& text) const {
        auto tokens = tokenize(text);
        if (tokens.size() + 1 < static_cast<size_t>(n_)) return 1.0 / 0.0;
        double sum_log = 0.0;
        size_t count = 0;
        for (size_t i = 0; i + n_ <= tokens.size(); ++i) {
            std::vector<std::string> context(tokens.begin() + i,
                                              tokens.begin() + i + n_ - 1);
            std::string token = tokens[i + n_ - 1];
            double p = get_probability(context, token);
            sum_log += std::log(p);
            ++count;
        }
        double avg = sum_log / static_cast<double>(count);
        return std::exp(-avg);
    }

    std::string sample(int num_tokens = 10,
                       const std::vector<std::string>& seed_context = {}) const {
        std::vector<std::string> context;
        if (seed_context.empty()) {
            context.assign(n_ - 1, "<s>");
        } else {
            context = seed_context;
        }
        std::vector<std::string> tokens;
        for (int step = 0; step < num_tokens; ++step) {
            std::map<std::string, int64_t> possible_next;
            int64_t total = 0;
            for (const auto& kv : transition_counts_) {
                const auto& ngram = kv.first;
                if (ngram.size() != static_cast<size_t>(n_)) continue;
                bool match = true;
                for (int i = 0; i < n_ - 1; ++i) {
                    if (ngram[i] != context[i]) { match = false; break; }
                }
                if (match) {
                    std::string nxt = ngram.back();
                    possible_next[nxt] += kv.second;
                    total += kv.second;
                }
            }
            if (possible_next.empty()) break;
            double r = uniform01() * static_cast<double>(total);
            double cum = 0.0;
            std::string chosen;
            for (const auto& kv : possible_next) {
                cum += static_cast<double>(kv.second);
                if (r <= cum) { chosen = kv.first; break; }
            }
            if (chosen.empty()) chosen = possible_next.begin()->first;
            if (chosen == "</s>") break;
            tokens.push_back(chosen);
            if (n_ > 1) {
                context.erase(context.begin());
                context.push_back(chosen);
            } else {
                context[0] = chosen;
            }
        }
        std::string out;
        for (size_t i = 0; i < tokens.size(); ++i) {
            if (i) out += ' ';
            out += tokens[i];
        }
        return out;
    }

    const std::set<std::string>& vocab() const { return vocab_; }

private:
    std::vector<std::string> tokenize(const std::string& text) const {
        std::vector<std::string> words;
        std::string cur;
        for (unsigned char ch : text) {
            char c = static_cast<char>(std::tolower(static_cast<unsigned char>(ch)));
            if (std::isalpha(static_cast<unsigned char>(c))) {
                cur.push_back(c);
            } else {
                if (!cur.empty()) { words.push_back(cur); cur.clear(); }
            }
        }
        if (!cur.empty()) words.push_back(cur);
        std::vector<std::string> tokens;
        for (int i = 0; i < n_ - 1; ++i) tokens.push_back("<s>");
        tokens.insert(tokens.end(), words.begin(), words.end());
        tokens.push_back("</s>");
        return tokens;
    }

    int n_;
    std::map<std::vector<std::string>, int64_t> context_counts_;
    std::map<std::vector<std::string>, int64_t> transition_counts_;
    std::set<std::string> vocab_;
};

int main() {
    rng_state = 42ULL;
    std::vector<std::string> corpus = {
        "the cat sat on the mat",
        "the dog ran in the park",
        "the cat and the dog played",
        "on the mat sat the cat",
        "in the park ran the dog",
    };

    NGramLanguageModel model(2);
    model.fit(corpus);

    assert(model.vocab().count("<s>") == 1);
    assert(model.vocab().count("cat") == 1);
    assert(model.vocab().count("dog") == 1);

    double total_prob = 0.0;
    for (const auto& token : model.vocab()) {
        total_prob += model.get_probability({"<s>"}, token);
    }
    assert(total_prob > 0.99 && total_prob < 1.01);

    double prob_cat = model.get_probability({"the"}, "cat");
    double prob_unknown = model.get_probability({"the"}, "zzz_rare_word_zzz");
    assert(prob_cat > prob_unknown);

    double perp_train = model.perplexity(corpus[0]);
    double perp_random = model.perplexity("zzz qqq xxx ppp rrr mmm");
    assert(perp_train < perp_random);

    std::string sample = model.sample(10);
    assert(!sample.empty());

    std::printf("ngram_language_model.cpp: PASS (train_perp=%.3f random_perp=%.3f)\n",
                perp_train, perp_random);
    return 0;
}
