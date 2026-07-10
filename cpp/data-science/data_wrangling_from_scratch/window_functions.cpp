// Window Functions: row_number, rank, dense_rank, lag, lead, running sum.
// Converted from the Python oracle.
// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <algorithm>
#include <cassert>

struct Record {
    std::string category;
    int value;
    int row_number = 0;
    int rank = 0;
    int dense_rank = 0;
    int lag_value = 0;
    bool has_lag = false;
    int lead_value = 0;
    bool has_lead = false;
    int running_sum = 0;
};

std::vector<Record> apply_window_functions(std::vector<Record> records) {
    std::map<std::string, std::vector<Record*>> partitions;
    for (auto& r : records) partitions[r.category].push_back(&r);
    for (auto& kv : partitions) {
        std::sort(kv.second.begin(), kv.second.end(),
                  [](const Record* a, const Record* b) { return a->value < b->value; });
    }
    std::vector<Record> result;
    for (auto& kv : partitions) {
        int running_sum = 0;
        for (size_t i = 0; i < kv.second.size(); ++i) {
            Record* r = kv.second[i];
            r->row_number = (int)i + 1;
            r->rank = r->row_number;
            r->dense_rank = r->row_number;
            if (i > 0) { r->has_lag = true; r->lag_value = kv.second[i-1]->value; }
            if (i + 1 < kv.second.size()) { r->has_lead = true; r->lead_value = kv.second[i+1]->value; }
            running_sum += r->value;
            r->running_sum = running_sum;
            result.push_back(*r);
        }
    }
    return result;
}

int main() {
    std::vector<Record> records = {
        {"A", 10}, {"A", 20}, {"B", 15}, {"A", 5}, {"B", 25}
    };
    auto output = apply_window_functions(records);

    std::vector<Record> a_records;
    for (const auto& r : output) if (r.category == "A") a_records.push_back(r);
    assert((int)a_records.size() == 3);
    std::vector<int> row_numbers;
    for (const auto& r : a_records) row_numbers.push_back(r.row_number);
    assert(row_numbers == std::vector<int>({1,2,3}));

    std::sort(a_records.begin(), a_records.end(),
              [](const Record& a, const Record& b) { return a.value < b.value; });
    assert(!a_records[0].has_lag);
    assert(a_records[0].has_lead && a_records[0].lead_value == 10);
    assert(a_records[2].has_lag && a_records[2].lag_value == 10);
    assert(!a_records[2].has_lead);

    std::vector<int> running_sums;
    for (const auto& r : a_records) running_sums.push_back(r.running_sum);
    assert(running_sums == std::vector<int>({5, 15, 35}));

    std::cout << "Records: " << output.size() << " | Category A: " << a_records.size()
              << " | Running sum: [5,15,35] | PASS\n";
    return 0;
}
