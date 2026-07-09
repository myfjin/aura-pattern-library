"""Kelly Criterion: optimal betting fraction for long-run log-growth.

Kelly fraction f* = (p*b - q) / b where p = win prob, q = loss prob, b = odds.
Overbetting (2x Kelly) produces lower median terminal wealth: the classic warning.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import random
import math

def kelly_criterion() -> None:
    random.seed(42)

    # Simple bet: p = 0.6 win probability, b = 1 (even odds)
    p_win = 0.6
    p_lose = 0.4
    odds = 1.0  # b = 1

    # Kelly fraction
    kelly_f = (p_win * odds - p_lose) / odds  # (0.6 - 0.4) / 1 = 0.2

    def simulate_wealth(fraction: float, n_bets: int, seed_offset: int = 0) -> list[float]:
        random.seed(42 + seed_offset)
        wealth = 1.0
        wealth_trajectory = [wealth]

        for bet in range(n_bets):
            if random.random() < p_win:
                # Win: wealth multiplies by (1 + fraction * odds)
                wealth *= (1 + fraction * odds)
            else:
                # Lose: wealth multiplies by (1 - fraction)
                wealth *= (1 - fraction)

            wealth_trajectory.append(wealth)

        return wealth_trajectory

    # Simulate with Kelly, and 2x Kelly with SAME coin sequence
    # This tests that Kelly maximizes long-run growth with same luck
    n_bets = 100

    # THE GROWTH CLAIM, measured over MANY paths (one seeded trajectory is a
    # single realization — 2x Kelly can win any given run by luck). Paired
    # paths: both strategies face the SAME coin sequence per path.
    import math as _m
    n_paths = 300
    term_k, term_o, paired_wins = [], [], 0
    for path in range(n_paths):
        wk = simulate_wealth(kelly_f, n_bets, seed_offset=path)[-1]
        wo = simulate_wealth(2 * kelly_f, n_bets, seed_offset=path)[-1]
        term_k.append(wk)
        term_o.append(wo)
        paired_wins += wk > wo
    med_k = sorted(term_k)[n_paths // 2]
    med_o = sorted(term_o)[n_paths // 2]
    logg_k = sum(_m.log(w) for w in term_k) / n_paths
    logg_o = sum(_m.log(w) for w in term_o) / n_paths
    print(f"paths: {n_paths} · median terminal Kelly {med_k:.2f} vs 2x {med_o:.2f} · "
          f"mean log-growth {logg_k:.2f} vs {logg_o:.2f} · Kelly wins {paired_wins/n_paths:.0%}")
    assert med_k > med_o, "Kelly must beat 2x Kelly in MEDIAN terminal wealth"
    assert logg_k > logg_o, "Kelly must beat 2x Kelly in mean log-growth"
    assert paired_wins / n_paths > 0.6, (
        f"Kelly should win most paired paths: {paired_wins/n_paths:.0%}"
    )

    print("PASS")

if __name__ == "__main__":
    kelly_criterion()
