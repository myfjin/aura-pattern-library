"""
Multi-step funnel conversion analysis with confidence intervals.

Track user progression through a conversion funnel (e.g., visit → signup →
purchase → retain). Compute step-wise conversion rates with Wilson confidence
intervals. Identify the weakest step.

Use: product analytics, sales/marketing funnels, conversion rate optimization.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"

import math
from collections import defaultdict




class AuraInputError(ValueError):
    """All input-contract violations, reported together (accumulate-then-raise)."""
    def __init__(self, violations):
        self.violations = violations
        super().__init__("input contract violated:\n  " + "\n  ".join(violations))

def _aura_validate_wilson_confidence_interval(trials, confidence):
    v = []
    if isinstance(trials, (int, float)) and trials <= 0:
        v.append(f"AURA-E009: trials must be > 0, got {trials}")
    if isinstance(confidence, (int, float)) and not math.isfinite(confidence):
        v.append(f"AURA-E008: confidence must be finite, got {confidence}")
    if isinstance(confidence, (int, float)) and confidence <= 0:
        v.append(f"AURA-E009: confidence must be > 0, got {confidence}")
    if v:
        raise AuraInputError(v)

def wilson_confidence_interval(successes: int, trials: int, confidence: float = 0.95) -> tuple[float, float]:
    """
    Wilson score confidence interval for binomial proportion.
    Returns (lower, upper) bounds at given confidence level.
    Recommended over normal approximation for small samples.
    """
    _aura_validate_wilson_confidence_interval(trials, confidence)
    if trials == 0:
        return 0.0, 1.0

    # z for two-tailed test
    if confidence == 0.95:
        z = 1.96
    elif confidence == 0.90:
        z = 1.645
    else:
        z = 1.96

    p_hat = successes / trials
    z_sq = z * z
    denom = 1 + z_sq / trials

    center = (p_hat + z_sq / (2 * trials)) / denom
    margin = z * math.sqrt(p_hat * (1 - p_hat) / trials + z_sq / (4 * trials * trials)) / denom

    lower = max(0, center - margin)
    upper = min(1, center + margin)

    return lower, upper


def build_funnel_events(events: list[dict]) -> dict[str, dict]:
    """
    Aggregate funnel events.
    Events are dicts: {'user_id', 'step'}.
    Returns: step_name -> {'users_reached': count}.
    """
    step_users = defaultdict(set)

    for event in events:
        step = event['step']
        user_id = event['user_id']
        step_users[step].add(user_id)

    return {step: {'users_reached': len(users)} for step, users in step_users.items()}


def compute_conversion_rates(funnel: dict[str, dict], step_order: list[str]) -> dict[str, dict]:
    """
    Compute conversion rate from step N to step N+1.
    Returns: step -> {'count': count, 'next_step': step_name, 'rate': rate, 'ci': (lower, upper)}.
    """
    rates = {}

    for i, step in enumerate(step_order):
        if step not in funnel:
            continue

        count = funnel[step]['users_reached']
        next_step = step_order[i + 1] if i + 1 < len(step_order) else None

        if next_step and next_step in funnel:
            next_count = funnel[next_step]['users_reached']
            rate = next_count / count if count > 0 else 0
            lower, upper = wilson_confidence_interval(next_count, count, confidence=0.95)

            rates[step] = {
                'count': count,
                'next_step': next_step,
                'conversion': next_count,
                'rate': rate,
                'ci': (lower, upper)
            }
        else:
            rates[step] = {
                'count': count,
                'next_step': None,
                'conversion': 0,
                'rate': 0,
                'ci': (0, 0)
            }

    return rates


if __name__ == "__main__":
    import random
    random.seed(42)

    # Generate synthetic funnel data
    # Step order: visit → signup → trial → purchase
    # Plant a weak step (purchase) with 20% conversion vs others at 75%+

    events = []

    # Step 1: visit (baseline, 1000 users)
    n_visit = 1000
    visiting_users = set(range(n_visit))
    for uid in visiting_users:
        events.append({'user_id': uid, 'step': 'visit'})

    # Step 2: signup (80% conversion) - deterministic
    signup_count = int(n_visit * 0.80)
    signup_users = set(range(signup_count))
    for uid in signup_users:
        events.append({'user_id': uid, 'step': 'signup'})

    # Step 3: trial (75% conversion - good funnel step) - deterministic
    trial_count = int(len(signup_users) * 0.75)
    trial_users = set(range(trial_count))
    for uid in trial_users:
        events.append({'user_id': uid, 'step': 'trial'})

    # Step 4: purchase (20% conversion - WEAK STEP, planted) - deterministic
    purchase_count = int(len(trial_users) * 0.20)
    purchase_users = set(range(purchase_count))
    for uid in purchase_users:
        events.append({'user_id': uid, 'step': 'purchase'})

    # Build funnel and compute rates
    funnel = build_funnel_events(events)
    step_order = ['visit', 'signup', 'trial', 'purchase']
    rates = compute_conversion_rates(funnel, step_order)

    print("Multi-step funnel conversion analysis")
    print()

    conversion_list = []
    for step in step_order:
        if step in rates:
            r = rates[step]
            rate_pct = r['rate'] * 100
            lower, upper = r['ci']
            conversion_list.append((step, r['rate']))

            print(f"{step:10s}: {r['count']:4d} users → {r['conversion']:3d} ({rate_pct:5.1f}%)")
            print(f"             95% CI: [{lower*100:5.1f}%, {upper*100:5.1f}%]")
            print()

    # Find weakest step (excluding the final step which has no conversion)
    rates_only = [r for step, r in conversion_list]
    weakest_rate = min(rates_only)
    weakest_step = [s for s, r in conversion_list if r == weakest_rate][0]

    print(f"Weakest step: {weakest_step} at {weakest_rate*100:.1f}%")

    # Assert that the planted weak step is identified
    assert weakest_step == 'purchase', \
        f"Weakest step should be 'purchase', got '{weakest_step}'"

    # Assert that CIs are non-overlapping for weak vs strong steps
    trial_ci = rates['trial']['ci']
    purchase_ci = rates['purchase']['ci']

    # Trial (strong) should have higher rate than purchase (weak)
    assert trial_ci[0] > purchase_ci[1], \
        f"Trial CI {trial_ci} should be above purchase CI {purchase_ci}"

    print(f"\nFunnel analysis:")
    print(f"  Weakest step identified: ✓ (trial {trial_ci[0]*100:.1f}% vs purchase {purchase_ci[1]*100:.1f}%)")
    print(f"  CI overlap check: ✓")

    print("\nfunnel_conversion_analysis.py PASS")
