"""
Levenshtein Edit Distance via Dynamic Programming

Core idea: compute minimum number of single-character edits (insert, delete, replace)
to transform one string into another using DP. Backtrace the DP table to recover
the actual edit sequence.

Use when: measuring string similarity (spelling correction, fuzzy matching),
finding near-duplicate text, or aligning sequences for comparison.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

from typing import List, Tuple


class EditDistanceDP:
    """Compute Levenshtein distance and backtrace edit operations."""

    @staticmethod
    def distance(s1: str, s2: str) -> int:
        """Compute minimum edit distance."""
        m, n = len(s1), len(s2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Base cases: distance from empty string
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j

        # Fill DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(
                        dp[i - 1][j],      # delete from s1
                        dp[i][j - 1],      # insert into s1
                        dp[i - 1][j - 1]   # replace
                    )

        return dp[m][n]

    @staticmethod
    def backtrace(s1: str, s2: str) -> List[Tuple[str, str, str]]:
        """Backtrace DP table to recover edit operations.

        Returns list of tuples: (operation, char1, char2) where operation is
        one of: "match", "replace", "insert", "delete"
        """
        m, n = len(s1), len(s2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(
                        dp[i - 1][j],
                        dp[i][j - 1],
                        dp[i - 1][j - 1]
                    )

        # Backtrace
        operations = []
        i, j = m, n
        while i > 0 or j > 0:
            if i > 0 and j > 0 and s1[i - 1] == s2[j - 1]:
                operations.append(("match", s1[i - 1], s2[j - 1]))
                i -= 1
                j -= 1
            elif i > 0 and j > 0 and dp[i - 1][j - 1] + 1 == dp[i][j]:
                operations.append(("replace", s1[i - 1], s2[j - 1]))
                i -= 1
                j -= 1
            elif i > 0 and dp[i - 1][j] + 1 == dp[i][j]:
                operations.append(("delete", s1[i - 1], ""))
                i -= 1
            else:
                operations.append(("insert", "", s2[j - 1]))
                j -= 1

        return list(reversed(operations))


if __name__ == "__main__":
    import random
    random.seed(42)

    # Test 1: Classic examples
    assert EditDistanceDP.distance("kitten", "sitting") == 3, \
        "kitten->sitting should be 3"
    assert EditDistanceDP.distance("saturday", "sunday") == 3, \
        "saturday->sunday should be 3"
    assert EditDistanceDP.distance("", "abc") == 3, \
        "empty->abc should be 3"
    assert EditDistanceDP.distance("abc", "") == 3, \
        "abc->empty should be 3"
    assert EditDistanceDP.distance("abc", "abc") == 0, \
        "identical strings should be 0"

    # Test 2: Backtrace recovers a valid edit sequence
    ops = EditDistanceDP.backtrace("kitten", "sitting")
    # Count edit operations (exclude matches)
    edit_count = sum(1 for op, _, _ in ops if op != "match")
    assert edit_count == 3, f"Expected 3 edits, got {edit_count}"

    # Test 3: Backtrace produces correct final string
    s1 = "cat"
    s2 = "car"
    ops = EditDistanceDP.backtrace(s1, s2)
    # Apply operations: should transform s1 to s2
    result = []
    s1_idx = 0
    for op, c1, c2 in ops:
        if op == "match":
            result.append(c1)
            s1_idx += 1
        elif op == "replace":
            result.append(c2)
            s1_idx += 1
        elif op == "delete":
            s1_idx += 1
        elif op == "insert":
            result.append(c2)

    assert "".join(result) == s2, f"Backtrace should produce {s2}, got {''.join(result)}"

    # Test 4: Symmetric property doesn't hold, but distance is symmetric
    d1 = EditDistanceDP.distance("hello", "hallo")
    d2 = EditDistanceDP.distance("hallo", "hello")
    assert d1 == d2, f"Distance should be symmetric: {d1} vs {d2}"

    print("PASS: Edit distance computes Levenshtein correctly, backtrace recovers valid edit sequence")
