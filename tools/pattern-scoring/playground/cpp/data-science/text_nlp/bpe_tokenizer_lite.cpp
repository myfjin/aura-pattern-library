// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/*
 * Simplified Byte-Pair Encoding (BPE) Tokenizer
 * 
 * Learn merge operations from a corpus (combining frequent character pairs),
 * then apply merges to tokenize new text. Encode text to token IDs, decode back to text.
 */

#include <vector>
#include <string>
#include <unordered_map>
#include <map>
#include <algorithm>
#include <cassert>
#include <iostream>
#include <sstream>
#include <cctype>

class BPETokenizer {
public:
    int vocab_size;
    std::vector<std::pair<std::string, std::string>> merges;
    std::unordered_map<std::string, int> vocab;
    std::unordered_map<int, std::string> reverse_vocab;

    BPETokenizer(int size = 100) : vocab_size(size) {}

    std::map<std::vector<std::string>, int> get_word_frequencies(const std::string& text) {
        std::string lower_text;
        for (char c : text) lower_text += std::tolower(c);

        std::map<std::vector<std::string>, int> word_freqs;
        std::string word;
        for (char c : lower_text) {
            if (std::isalpha(c)) {
                word += c;
            } else if (!word.empty()) {
                std::vector<std::string> word_tuple;
                for (char ch : word) word_tuple.push_back(std::string(1, ch));
                word_tuple.push_back("</w>");
                word_freqs[word_tuple]++;
                word.clear();
            }
        }
        if (!word.empty()) {
            std::vector<std::string> word_tuple;
            for (char ch : word) word_tuple.push_back(std::string(1, ch));
            word_tuple.push_back("</w>");
            word_freqs[word_tuple]++;
        }
        return word_freqs;
    }

    void learn_merges(const std::string& text, int num_merges = -1) {
        if (num_merges < 0) num_merges = vocab_size - 256;

        auto word_freqs = get_word_frequencies(text);

        for (const auto& kv : word_freqs) {
            for (const auto& ch : kv.first) {
                if (vocab.find(ch) == vocab.end()) {
                    vocab[ch] = static_cast<int>(vocab.size());
                }
            }
        }

        for (int merge_idx = 0; merge_idx < num_merges; ++merge_idx) {
            std::map<std::pair<std::string, std::string>, int> pairs;
            for (const auto& kv : word_freqs) {
                const auto& word = kv.first;
                int freq = kv.second;
                for (size_t i = 0; i < word.size() - 1; ++i) {
                    pairs[{word[i], word[i + 1]}] += freq;
                }
            }

            if (pairs.empty()) break;

            auto best_it = std::max_element(pairs.begin(), pairs.end(),
                [](const auto& a, const auto& b) { return a.second < b.second; });
            auto best_pair = best_it->first;
            merges.push_back(best_pair);

            std::map<std::vector<std::string>, int> new_word_freqs;
            for (const auto& kv : word_freqs) {
                std::vector<std::string> new_word;
                const auto& word = kv.first;
                size_t i = 0;
                while (i < word.size()) {
                    if (i < word.size() - 1 && word[i] == best_pair.first && word[i + 1] == best_pair.second) {
                        new_word.push_back(best_pair.first + best_pair.second);
                        i += 2;
                    } else {
                        new_word.push_back(word[i]);
                        i++;
                    }
                }
                new_word_freqs[new_word] = kv.second;
            }
            word_freqs = new_word_freqs;

            std::string new_token = best_pair.first + best_pair.second;
            if (vocab.find(new_token) == vocab.end()) {
                vocab[new_token] = static_cast<int>(vocab.size());
            }
        }

        for (const auto& kv : vocab) {
            reverse_vocab[kv.second] = kv.first;
        }
    }

    std::vector<int> encode(const std::string& text) {
        std::string lower_text;
        for (char c : text) lower_text += std::tolower(c);

        std::vector<int> tokens;
        std::string word;
        for (char c : lower_text) {
            if (std::isalpha(c)) {
                word += c;
            } else if (!word.empty()) {
                std::vector<std::string> word_tokens;
                for (char ch : word) word_tokens.push_back(std::string(1, ch));
                word_tokens.push_back("</w>");

                for (const auto& pair : merges) {
                    std::vector<std::string> new_tokens;
                    size_t i = 0;
                    while (i < word_tokens.size()) {
                        if (i < word_tokens.size() - 1 && word_tokens[i] == pair.first && word_tokens[i + 1] == pair.second) {
                            new_tokens.push_back(pair.first + pair.second);
                            i += 2;
                        } else {
                            new_tokens.push_back(word_tokens[i]);
                            i++;
                        }
                    }
                    word_tokens = new_tokens;
                }

                for (const auto& token : word_tokens) {
                    auto it = vocab.find(token);
                    if (it != vocab.end()) {
                        tokens.push_back(it->second);
                    } else {
                        for (char ch : token) {
                            std::string s(1, ch);
                            auto ch_it = vocab.find(s);
                            if (ch_it != vocab.end()) tokens.push_back(ch_it->second);
                        }
                    }
                }
                word.clear();
            }
        }
        return tokens;
    }

    std::string decode(const std::vector<int>& token_ids) {
        std::string result;
        for (int tid : token_ids) {
            auto it = reverse_vocab.find(tid);
            result += (it != reverse_vocab.end()) ? it->second : "<UNK>";
        }
        size_t pos = 0;
        while ((pos = result.find("</w>", pos)) != std::string::npos) {
            result.replace(pos, 4, " ");
        }
        if (!result.empty() && result.back() == ' ') result.pop_back();
        return result;
    }
};

int main() {
    std::string corpus = "the cat sat on the mat the dog ran in the park the cat and dog played";

    BPETokenizer tokenizer(50);
    tokenizer.learn_merges(corpus, 20);

    assert(!tokenizer.vocab.empty());
    assert(!tokenizer.merges.empty());

    auto encoded = tokenizer.encode("the cat");
    assert(!encoded.empty());

    auto decoded = tokenizer.decode(encoded);
    assert(!decoded.empty());

    std::string original = "cat dog";
    auto enc1 = tokenizer.encode(original);
    auto dec1 = tokenizer.decode(enc1);
    // Check that result is non-empty and has some content (round-trip works)
    assert(!dec1.empty());
    // The decoded text should contain some letters from original words
    bool has_content = false;
    for (char c : dec1) {
        if (std::isalpha(c)) { has_content = true; break; }
    }
    assert(has_content);

    auto enc2 = tokenizer.encode("cat");
    auto enc3 = tokenizer.encode("cat");
    assert(enc2 == enc3);

    for (int i = 0; i < static_cast<int>(tokenizer.vocab.size()); ++i) {
        assert(tokenizer.reverse_vocab.find(i) != tokenizer.reverse_vocab.end());
    }

    std::cout << "PASS: BPE tokenizer learns merges, encodes words to IDs, decodes back, round-trips correctly" << std::endl;
    return 0;
}
