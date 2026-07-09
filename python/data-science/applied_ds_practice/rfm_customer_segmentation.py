"""
RFM customer segmentation: Recency, Frequency, Monetary.

Segment customers based on:
  - Recency: days since last purchase
  - Frequency: number of purchases
  - Monetary: total spend
RFM scores divide each metric into quartiles, then combine into segments
(e.g., "whale" = high on all three, "churned" = low on all).

Use: customer value analysis, retention targeting, marketing segmentation.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

from collections import defaultdict


def compute_rfm_metrics(transactions: list[dict]) -> dict[int, dict]:
    """
    Compute RFM metrics from transactions.
    Transactions are dicts: {'user_id', 'purchase_date', 'amount'}.
    Returns: user_id -> {'recency': days, 'frequency': count, 'monetary': total}.
    """
    user_metrics = defaultdict(lambda: {'frequency': 0, 'monetary': 0.0})

    max_date = max(t['purchase_date'] for t in transactions)

    for trans in transactions:
        user_id = trans['user_id']
        user_metrics[user_id]['frequency'] += 1
        user_metrics[user_id]['monetary'] += trans['amount']
        user_metrics[user_id]['recency'] = max_date - trans['purchase_date']

    return dict(user_metrics)


def quartile_score(values: list[float], recency_flag: bool = False) -> dict[float, int]:
    """
    Map values to quartile scores [1, 2, 3, 4].
    If recency_flag=True, invert (low recency is better).
    """
    sorted_vals = sorted(set(values))
    n = len(sorted_vals)

    # Define quartile boundaries (approximate)
    q1_idx = max(0, n // 4 - 1)
    q2_idx = max(0, n // 2 - 1)
    q3_idx = max(0, 3 * n // 4 - 1)

    boundaries = [sorted_vals[q1_idx], sorted_vals[q2_idx], sorted_vals[q3_idx]]

    score_map = {}
    for v in values:
        if v <= boundaries[0]:
            score = 1
        elif v <= boundaries[1]:
            score = 2
        elif v <= boundaries[2]:
            score = 3
        else:
            score = 4

        # Invert for recency (lower is better)
        if recency_flag:
            score = 5 - score

        score_map[v] = score

    return score_map


def segment_from_rfm(r: int, f: int, m: int) -> str:
    """Determine segment from RFM scores."""
    if r >= 3 and f >= 3 and m >= 3:
        return "whale"
    elif r <= 2 and f <= 2 and m <= 2:
        return "churned"
    elif f >= 3 and m >= 3:
        return "frequent"
    elif r <= 2:
        return "at_risk"
    else:
        return "regular"


if __name__ == "__main__":
    import random
    random.seed(42)

    # Generate synthetic transactions with planted archetypes
    transactions = []

    # Whale customers: frequent, high spend, recent
    for u_id in range(0, 20):
        for purchase_num in range(random.randint(8, 15)):
            days_ago = random.randint(0, 30)
            amount = random.uniform(100, 500)
            transactions.append({
                'user_id': u_id,
                'purchase_date': 100 - days_ago,
                'amount': amount
            })

    # Regular customers: moderate activity
    for u_id in range(20, 60):
        for purchase_num in range(random.randint(2, 5)):
            days_ago = random.randint(0, 90)
            amount = random.uniform(20, 100)
            transactions.append({
                'user_id': u_id,
                'purchase_date': 100 - days_ago,
                'amount': amount
            })

    # Churned customers: old activity, low frequency, low spend
    for u_id in range(60, 100):
        for purchase_num in range(random.randint(1, 2)):
            days_ago = random.randint(200, 365)
            amount = random.uniform(5, 30)
            transactions.append({
                'user_id': u_id,
                'purchase_date': 100 - days_ago,
                'amount': amount
            })

    # Compute RFM metrics
    user_metrics = compute_rfm_metrics(transactions)

    # Extract values for scoring
    recencies = [m['recency'] for m in user_metrics.values()]
    frequencies = [m['frequency'] for m in user_metrics.values()]
    monetaries = [m['monetary'] for m in user_metrics.values()]

    # Score each metric
    r_score_map = quartile_score(recencies, recency_flag=True)
    f_score_map = quartile_score(frequencies, recency_flag=False)
    m_score_map = quartile_score(monetaries, recency_flag=False)

    # Segment
    segments = defaultdict(list)

    for user_id, metrics in user_metrics.items():
        r = r_score_map[metrics['recency']]
        f = f_score_map[metrics['frequency']]
        m = m_score_map[metrics['monetary']]
        segment = segment_from_rfm(r, f, m)

        segments[segment].append(user_id)

    # Display results
    print("RFM Customer Segmentation")
    print()

    for segment in ['whale', 'frequent', 'regular', 'at_risk', 'churned']:
        users = segments[segment]
        if users:
            print(f"{segment.upper():15s}: {len(users):2d} customers")
            # Show a sample user's metrics
            sample_uid = users[0]
            m = user_metrics[sample_uid]
            print(f"                Sample: R={r_score_map[m['recency']]}, "
                  f"F={f_score_map[m['frequency']]}, "
                  f"M={m_score_map[m['monetary']]}")
            print()

    # Assertions: planted archetypes should appear
    assert len(segments['whale']) > 10, \
        f"Should have ~20 whale customers, got {len(segments['whale'])}"
    assert len(segments['churned']) > 10, \
        f"Should have ~40 churned customers, got {len(segments['churned'])}"

    # Whale should have higher avg frequency/monetary
    whale_users = segments['whale']
    churned_users = segments['churned']

    whale_freq = [user_metrics[u]['frequency'] for u in whale_users]
    churned_freq = [user_metrics[u]['frequency'] for u in churned_users]

    avg_whale_freq = sum(whale_freq) / len(whale_freq)
    avg_churned_freq = sum(churned_freq) / len(churned_freq)

    assert avg_whale_freq > avg_churned_freq, \
        f"Whale freq {avg_whale_freq:.1f} should > churned {avg_churned_freq:.1f}"

    print(f"Segmentation quality check:")
    print(f"  Whale avg frequency:   {avg_whale_freq:.1f}")
    print(f"  Churned avg frequency: {avg_churned_freq:.1f}")
    print(f"  Archetype separation: ✓")

    print("\nrfm_customer_segmentation.py PASS")
