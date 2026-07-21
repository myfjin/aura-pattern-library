// △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
// ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
static const char *_aura_mark = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO";
/*
 * Hash Join: Inner and Left Join.
 * Builds a hash index on the right table's join key, then probes it with each
 * left row: inner join emits only matches, left join also keeps unmatched left
 * rows (has_salary = false). Use to merge two tables in O(n+m) instead of the
 * O(n*m) nested loop. Oracle: the hash inner join equals the nested-loop join
 * row-for-row, and the left join preserves the one unmatched left row.
 */

#include <vector>
#include <map>
#include <string>
#include <string>
#include <algorithm>
#include <cassert>
#include <iostream>

struct Row {
    int id;
    std::string name;
    int salary;
    bool has_name;
    bool has_salary;
};

std::vector<Row> hash_join_inner(const std::vector<Row>& left_table,
                                   const std::vector<Row>& right_table,
                                   const std::string& join_key) {
    std::map<int, std::vector<Row>> right_hash;
    for (const auto& row : right_table) {
        right_hash[row.id].push_back(row);
    }

    std::vector<Row> result;
    for (const auto& left_row : left_table) {
        auto it = right_hash.find(left_row.id);
        if (it != right_hash.end()) {
            for (const auto& right_row : it->second) {
                Row merged;
                merged.id = left_row.id;
                merged.name = left_row.name;
                merged.salary = right_row.salary;
                merged.has_name = true;
                merged.has_salary = true;
                result.push_back(merged);
            }
        }
    }
    return result;
}

std::vector<Row> hash_join_left(const std::vector<Row>& left_table,
                                  const std::vector<Row>& right_table,
                                  const std::string& join_key) {
    std::map<int, std::vector<Row>> right_hash;
    for (const auto& row : right_table) {
        right_hash[row.id].push_back(row);
    }

    std::vector<Row> result;
    for (const auto& left_row : left_table) {
        auto it = right_hash.find(left_row.id);
        if (it != right_hash.end()) {
            for (const auto& right_row : it->second) {
                Row merged;
                merged.id = left_row.id;
                merged.name = left_row.name;
                merged.salary = right_row.salary;
                merged.has_name = true;
                merged.has_salary = true;
                result.push_back(merged);
            }
        } else {
            Row merged;
            merged.id = left_row.id;
            merged.name = left_row.name;
            merged.has_name = true;
            merged.has_salary = false;
            result.push_back(merged);
        }
    }
    return result;
}

std::vector<Row> nested_loop_inner_join(const std::vector<Row>& left_table,
                                           const std::vector<Row>& right_table,
                                           const std::string& join_key) {
    std::vector<Row> result;
    for (const auto& left_row : left_table) {
        for (const auto& right_row : right_table) {
            if (left_row.id == right_row.id) {
                Row merged;
                merged.id = left_row.id;
                merged.name = left_row.name;
                merged.salary = right_row.salary;
                merged.has_name = true;
                merged.has_salary = true;
                result.push_back(merged);
            }
        }
    }
    return result;
}

int main() {
    std::vector<Row> left = {
        {1, "Alice", 0, true, false},
        {2, "Bob", 0, true, false},
        {3, "Charlie", 0, true, false}
    };
    std::vector<Row> right = {
        {1, "", 100, false, true},
        {2, "", 150, false, true},
        {4, "", 200, false, true}
    };

    auto hash_inner = hash_join_inner(left, right, "id");
    auto brute_inner = nested_loop_inner_join(left, right, "id");

    auto sort_rows = [](std::vector<Row> rows) {
        std::sort(rows.begin(), rows.end(), [](const Row& a, const Row& b) { return a.id < b.id; });
        return rows;
    };

    auto hash_sorted = sort_rows(hash_inner);
    auto brute_sorted = sort_rows(brute_inner);

    assert(hash_sorted.size() == brute_sorted.size());
    for (size_t i = 0; i < hash_sorted.size(); ++i) {
        assert(hash_sorted[i].id == brute_sorted[i].id);
        assert(hash_sorted[i].name == brute_sorted[i].name);
        assert(hash_sorted[i].salary == brute_sorted[i].salary);
    }

    assert(hash_inner.size() == 2);

    auto hash_left = hash_join_left(left, right, "id");
    assert(hash_left.size() == 3);

    int id3_no_salary = 0;
    for (const auto& r : hash_left) {
        if (r.id == 3 && !r.has_salary) id3_no_salary++;
    }
    assert(id3_no_salary == 1);

    std::cout << "hash_join_merge.cpp PASS" << std::endl;
    return 0;
}
