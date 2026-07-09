"""Apriori algorithm for frequent itemsets and association rules.

Core idea: iteratively find frequent itemsets by checking support thresholds,
then generate association rules with confidence and lift metrics.

When to use: when you have a transaction database and want to discover patterns
like "customers who buy X also buy Y" (market-basket analysis).
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import random
from typing import Set, FrozenSet, Dict, List, Tuple
from itertools import combinations


def apriori(
    transactions: List[Set[int]],
    min_support: float = 0.3,
) -> Dict[FrozenSet[int], float]:
    """
    Find all frequent itemsets using Apriori algorithm.
    Returns dict mapping frozenset(itemset) -> support.
    """
    # Count 1-itemsets
    item_counts: Dict[int, int] = {}
    for trans in transactions:
        for item in trans:
            item_counts[item] = item_counts.get(item, 0) + 1

    # Filter by min_support
    min_count = int(min_support * len(transactions))
    frequent_1 = {
        frozenset([item]): count / len(transactions)
        for item, count in item_counts.items()
        if count >= min_count
    }

    all_frequent = frequent_1.copy()
    current_frequent = frequent_1

    # Generate k-itemsets iteratively
    k = 2
    while current_frequent:
        # Generate candidate k-itemsets by joining
        candidates: Dict[FrozenSet[int], int] = {}
        frequent_list = list(current_frequent.keys())
        for i in range(len(frequent_list)):
            for j in range(i + 1, len(frequent_list)):
                candidate = frequent_list[i] | frequent_list[j]
                if len(candidate) == k:
                    candidates[candidate] = 0

        # Count support for candidates
        for trans in transactions:
            for candidate in candidates:
                if candidate.issubset(trans):
                    candidates[candidate] += 1

        # Filter by min_support
        next_frequent = {
            itemset: count / len(transactions)
            for itemset, count in candidates.items()
            if count >= min_count
        }

        if not next_frequent:
            break

        all_frequent.update(next_frequent)
        current_frequent = next_frequent
        k += 1

    return all_frequent


def generate_rules(
    frequent_itemsets: Dict[FrozenSet[int], float],
    min_confidence: float = 0.6,
) -> List[Tuple[FrozenSet[int], FrozenSet[int], float]]:
    """
    Generate association rules from frequent itemsets.
    Returns list of (antecedent, consequent, confidence) tuples.
    """
    rules = []
    for itemset, support in frequent_itemsets.items():
        if len(itemset) < 2:
            continue
        for antecedent_size in range(1, len(itemset)):
            for antecedent in combinations(sorted(itemset), antecedent_size):
                antecedent = frozenset(antecedent)
                consequent = itemset - antecedent
                antecedent_support = frequent_itemsets.get(antecedent, 0)
                if antecedent_support > 0:
                    confidence = support / antecedent_support
                    if confidence >= min_confidence:
                        rules.append((antecedent, consequent, confidence))
    return rules


if __name__ == "__main__":
    random.seed(42)

    # Synthetic transaction database
    # Transaction pattern: items {0,1} appear together, {2,3} appear together
    transactions = [
        {0, 1, 2},           # 0,1 planted
        {0, 1, 4},           # 0,1 planted
        {0, 1},              # 0,1 planted
        {2, 3, 5},           # 2,3 planted
        {2, 3},              # 2,3 planted
        {1, 2},
        {3, 4, 5},
        {0, 1, 3},
    ]

    # Find frequent itemsets (min support 30%)
    frequent = apriori(transactions, min_support=0.3)

    # Check that planted itemset {0, 1} is frequent
    planted_itemset = frozenset([0, 1])
    assert planted_itemset in frequent, f"Planted itemset {planted_itemset} not found"

    # Generate rules
    rules = generate_rules(frequent, min_confidence=0.5)

    # Verify at least one rule found
    assert len(rules) > 0, "No rules generated"

    # Check that a rule involving the planted itemset exists
    rule_found = any(
        planted_itemset.issubset(ante | cons)
        for ante, cons, _ in rules
    )
    assert rule_found, "No rule involving planted itemset found"

    print(f"apriori_frequent_itemsets.py: {len(frequent)} itemsets, {len(rules)} rules PASS")
