"""
Cohort retention analysis from event logs.

Group users by cohort (e.g., signup month/cohort), track which cohorts
return in subsequent periods, and compute retention curves. Identifies
which cohorts have better/worse long-term engagement.

Use: subscription/SaaS analytics, user lifecycle analysis, retention funnels.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

from collections import defaultdict


def build_cohort_table(events: list[dict]) -> dict[str, dict[int, int]]:
    """
    Build cohort retention table from events.
    Events are dicts with keys: 'user_id', 'cohort', 'period'.
    Returns: cohort_name -> {period: count_of_users_active}.
    """
    cohort_data = defaultdict(lambda: defaultdict(set))

    for event in events:
        user_id = event['user_id']
        cohort = event['cohort']
        period = event['period']
        cohort_data[cohort][period].add(user_id)

    # Convert sets to counts
    cohort_table = {}
    for cohort, periods in cohort_data.items():
        cohort_table[cohort] = {p: len(users) for p, users in periods.items()}

    return cohort_table


def compute_retention_rates(cohort_table: dict[str, dict[int, int]]) -> dict[str, list[float]]:
    """
    Compute retention rates: users active in period p / users active in period 0.
    Returns: cohort -> [rate_p0, rate_p1, rate_p2, ...].
    """
    retention_rates = {}

    for cohort, periods in cohort_table.items():
        if 0 not in periods or periods[0] == 0:
            continue

        cohort_size = periods[0]
        rates = []

        for p in sorted(periods.keys()):
            active = periods[p]
            rate = active / cohort_size
            rates.append(rate)

        retention_rates[cohort] = rates

    return retention_rates


if __name__ == "__main__":
    import random
    random.seed(42)

    # Generate synthetic user event logs
    # Cohort A: better retention (planted difference)
    # Cohort B: worse retention

    events = []

    # Cohort A: 200 users, high retention
    cohort_a_users = list(range(0, 200))
    for user_id in cohort_a_users:
        # Period 0: all users active
        events.append({'user_id': user_id, 'cohort': 'A', 'period': 0})

        # Periods 1-4: 80% retention per period
        for period in range(1, 5):
            if random.random() < (0.8 ** period):  # Exponential decay
                events.append({'user_id': user_id, 'cohort': 'A', 'period': period})

    # Cohort B: 200 users, poor retention
    cohort_b_users = list(range(200, 400))
    for user_id in cohort_b_users:
        # Period 0: all users active
        events.append({'user_id': user_id, 'cohort': 'B', 'period': 0})

        # Periods 1-4: 50% retention per period (much lower)
        for period in range(1, 5):
            if random.random() < (0.5 ** period):
                events.append({'user_id': user_id, 'cohort': 'B', 'period': period})

    # Build cohort table and compute retention
    cohort_table = build_cohort_table(events)
    retention_rates = compute_retention_rates(cohort_table)

    print("Cohort retention analysis")
    print()

    for cohort in sorted(retention_rates.keys()):
        rates = retention_rates[cohort]
        print(f"Cohort {cohort}:")
        print(f"  Period 0 (cohort size): {cohort_table[cohort][0]}")

        for p, rate in enumerate(rates):
            active = cohort_table[cohort][p]
            print(f"  Period {p}: {active:3d} active ({rate:.1%} retention)")

        print()

    # Assertions: verify planted difference
    rates_a = retention_rates['A']
    rates_b = retention_rates['B']

    # Cohort A should have better (higher) retention at each period (starting p=1)
    for p in range(1, len(rates_a)):
        assert rates_a[p] > rates_b[p], \
            f"Cohort A period {p}: {rates_a[p]:.2%} should > B {rates_b[p]:.2%}"

    # Specifically, at period 4, difference should be large
    assert rates_a[-1] > rates_b[-1] * 2, \
        f"Period 4: A {rates_a[-1]:.2%} should be > 2x B {rates_b[-1]:.2%}"

    print(f"Period 4 retention: A {rates_a[-1]:.1%} vs B {rates_b[-1]:.1%}")
    print(f"Retention difference detected: ✓")

    print("\ncohort_retention_analysis.py PASS")
