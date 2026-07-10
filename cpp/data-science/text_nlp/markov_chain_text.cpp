// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/*
 * Word-Level Markov Chain Text Generator.
 *
 * Oracle asserts:
 *   transitions learned
 *   sanity check passes
 *   "the" follows START
 *   counts positive
 *   generated text is string, no START, non-empty
 *   seeded generation returns strings
 */

#include <string>
#include <vector>
#include <map>
#include <set>
#include <regex>
#include <cassert>
#include <iostream>
#include <sstream>

class MarkovChainText {
public:
    explicit MarkovChainText(int order = 1) : order_(order) {}

    void fit(const std::vector<std::string>& documents) {
        for (const auto& doc : documents) {
            auto tokens = tokenize(doc);
            vocab_.insert(tokens.begin(), tokens.end());
            for (size_t i = 0; i + order_ < tokens.size(); ++i) {
                std::vector<std::string> ctx(tokens.begin() + i, tokens.begin() + i + order_);
                transitions_[ctx].push_back(tokens[i + order_]);
            }
        }
    }

    std::string generate(int max_length = 20,
                         const std::vector<std::string>& seed_context = {}) const {
        std::vector<std::string> context;
        if (seed_context.empty()) {
            context.assign(order_, "<START>");
        } else {
            context = seed_context;
        }
        std::vector<std::string> tokens;
        for (int i = 0; i < max_length; ++i) {
            auto it = transitions_.find(context);
            if (it == transitions_.end()) break;
            const auto& next_words = it->second;
            std::string next_word = next_words[0];
            tokens.push_back(next_word);
            context.erase(context.begin());
            context.push_back(next_word);
        }
        std::string result;
        for (const auto& t : tokens) {
            if (t != "<START>") {
                if (!result.empty()) result += " ";
                result += t;
            }
        }
        return result;
    }

    std::map<std::vector<std::string>, std::map<std::string, int>> get_transition_counts() const {
        std::map<std::vector<std::string>, std::map<std::string, int>> counts;
        for (const auto& kv : transitions_) {
            for (const auto& w : kv.second) counts[kv.first][w]++;
        }
        return counts;
    }

    bool sanity_check() const {
        if (transitions_.empty()) return false;
        for (const auto& kv : transitions_) {
            if (kv.first.size() != static_cast<size_t>(order_)) return false;
            if (kv.second.empty()) return false;
        }
        return true;
    }

    const std::map<std::vector<std::string>, std::vector<std::string>>& transitions() const {
        return transitions_;
    }

private:
    int order_;
    std::map<std::vector<std::string>, std::vector<std::string>> transitions_;
    std::set<std::string> vocab_;

    std::vector<std::string> tokenize(const std::string& text) const {
        std::string lower;
        for (char c : text) lower += std::tolower(static_cast<unsigned char>(c));
        std::regex re(R"(\b[a-z]+\b)");
        std::sregex_iterator begin(lower.begin(), lower.end(), re);
        std::sregex_iterator end;
        std::vector<std::string> words;
        for (auto it = begin; it != end; ++it) words.push_back(it->str());
        words.insert(words.begin(), "<START>");
        return words;
    }
};

int main() {
    std::vector<std::string> corpus = {
        "the cat sat on the mat",
        "the dog ran in the park",
        "the cat and dog played",
        "on the mat sat the cat",
        "in the park the dog ran"
    };

    MarkovChainText model(1);
    model.fit(corpus);

    assert(!model.transitions().empty());
    std::vector<std::string> start_ctx = {"<START>"};
    assert(model.transitions().count(start_ctx));

    assert(model.sanity_check());

    const auto& start_transitions = model.transitions().at(start_ctx);
    bool has_the = false;
    for (const auto& w : start_transitions) if (w == "the") has_the = true;
    assert(has_the);

    auto counts = model.get_transition_counts();
    for (const auto& kv : counts) {
        for (const auto& wc : kv.second) assert(wc.second > 0);
    }

    std::string text = model.generate(10);
    assert(!text.empty());
    assert(text.find("<START>") == std::string::npos);

    std::string t1 = model.generate(5, {"the"});
    std::string t2 = model.generate(5, {"the"});
    assert(!t1.empty() && !t2.empty());

    std::cout << "markov_chain_text.cpp PASS" << std::endl;
    return 0;
}
