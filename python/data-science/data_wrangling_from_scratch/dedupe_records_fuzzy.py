"""
Fuzzy Record Deduplication.

Normalize records and link near-duplicates via edit-distance threshold.
We plant duplicates (with typos/variations) and verify they are identified.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

from typing import List, Dict, Any


def normalize(s: str) -> str:
    """Normalize string: lowercase, strip whitespace."""
    return s.lower().strip()


def edit_distance(s1: str, s2: str) -> int:
    """Levenshtein edit distance."""
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
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

    return dp[m][n]


def find_duplicates(
    records: List[Dict[str, Any]],
    match_key: str,
    threshold: int = 2,
) -> List[List[int]]:
    """
    Find near-duplicate records via edit distance on match_key.
    Returns clusters of record indices.
    """
    n = len(records)
    visited = [False] * n
    clusters = []

    for i in range(n):
        if visited[i]:
            continue

        cluster = [i]
        visited[i] = True
        s1 = normalize(records[i][match_key])

        for j in range(i + 1, n):
            if visited[j]:
                continue

            s2 = normalize(records[j][match_key])
            dist = edit_distance(s1, s2)

            if dist <= threshold:
                cluster.append(j)
                visited[j] = True

        clusters.append(cluster)

    return clusters


def dedupe(
    records: List[Dict[str, Any]],
    match_key: str,
    threshold: int = 2,
) -> List[Dict[str, Any]]:
    """Return deduplicated records (keep first of each cluster)."""
    clusters = find_duplicates(records, match_key, threshold)
    result = []

    for cluster in clusters:
        result.append(records[cluster[0]])

    return result


if __name__ == "__main__":
    # Plant records with duplicates/typos
    records = [
        {"id": 1, "name": "Alice Johnson"},
        {"id": 2, "name": "Alice Jonson"},  # Typo: missing 'h'
        {"id": 3, "name": "Bob Smith"},
        {"id": 4, "name": "Bob Smyth"},  # Typo: 'y' instead of 'i'
        {"id": 5, "name": "Charlie Brown"},  # Distinct
    ]

    # Find duplicates (threshold=2 allows ~2 character differences)
    clusters = find_duplicates(records, "name", threshold=2)

    # Verify clusters
    assert len(clusters) == 3, (
        f"Should find 3 clusters (Alice, Bob, Charlie), got {len(clusters)}"
    )

    # Verify Alice and Bob clusters
    # Note: both Alice/Jonson and Bob/Smyth have 1-char differences, so both are 2-clusters
    two_clusters = [c for c in clusters if len(c) == 2]
    assert len(two_clusters) == 2, f"Should find 2 two-record clusters, got {len(two_clusters)}"

    # Verify Alice is one of them (indices 0-1)
    assert [0, 1] in two_clusters, f"Alice cluster [0,1] should be found, got {two_clusters}"

    # Deduplicate
    deduped = dedupe(records, "name", threshold=2)
    assert len(deduped) == 3, f"Deduplicated should have 3 records, got {len(deduped)}"

    # Verify kept records
    kept_ids = [r["id"] for r in deduped]
    assert kept_ids == [1, 3, 5], f"Kept ids should be [1,3,5], got {kept_ids}"

    print(
        f"Records: {len(records)} | Clusters: {len(clusters)} | "
        f"Deduped: {len(deduped)} | Kept ids: {kept_ids} | PASS"
    )
