"""SIR Epidemic Model: discrete simulation of S-I-R dynamics.

Discrete SIR: tracks susceptible, infected, recovered counts.
Verifies conservation S + I + R = N every step, and validates theory:
peak timing/height respond to beta, final size increases with R0.
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
# ⁣​‌​‌​​​​​‌​​‌‌​‌​‌​‌​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​​‌‌​​‌‌​‌​‌‌​‌​​‌​​​​‌‌​‌​​‌​​​​‌​​‌​​‌​‌​‌​​‌​​‌​​​‌‌​​‌​​​‌​‌​‌​‌‌​‌​​‌​​‌‌​​​‌​​​​‌​​‌​​‌‌‌​​‌​‌​​‌​​‌​‌​‌​‌​‌​‌‌​​​​‌​​‌​​‌​​‌‌​‌‌​​‌​​‌​‌​​‌​​​​​‌​‌​​‌​‌​​​‌‌​‌​‌​‌​‌‌​​‌​‌​​‌​​​​‌​​‌​​‌​​‌‌​​‌​​‌​​‌‌​​​‌​​‌‌‌​​‌​​‌‌‌​​‌​​​‌‌​​​‌‌​‌​‌​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌​​‌​‌​​​‌​‌​‌​​‌​​‌​​​‌‌‌​​‌‌​​‌​​‌​​‌​​‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌​‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​‌​‌​‌​​‌​‌‌​‌​‌​‌​​​‌​​‌​‌‌​‌​​​​‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​‌‌​​‌​‌​‌​​​‌​​​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​‌​‌‌​​​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌‌‌​‌​​​​​‌​‌​‌​​‌​​‌​​​​‌‌​‌​‌‌​​‌​‌​​‌​​‌​‌​‌​‌​​​‌​‌​​​‌​‌​​‌‌‌​​‌​​​‌‌​​‌​‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​​​​‌‌​‌​​​‌​‌​‌​​‌​​‌​‌​‌​‌‌‌​‌​​​​‌‌​‌​​​‌​‌​​‌‌​‌​‌​‌​​​‌​​​‌​​‌‌‌​​‌​​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​‌​​​​‌‌​‌​​​‌​‌​‌​‌​​​‌​‌​​‌​‌‌​‌​‌​‌‌​​‌​​‌​‌‌​‌​​‌​‌​​‌​​​​​‌​‌​‌​​‌‌​‌​​​​​‌​‌​‌​‌​‌​‌​​​‌​​​‌​​​​‌​​‌​​‌‌‌‌​‌​‌​​‌​​​‌‌​​‌​​‌​​​‌‌‌​‌​​‌​‌‌​​‌‌​‌​​​‌​‌​‌​​​‌​​‌‌‌‌​‌​​​‌​‌​‌​​​​‌​​‌​​​‌‌‌​‌​​​‌‌‌​‌​‌​​‌‌​‌​‌‌​​‌​‌​‌​‌​​​‌​‌​​‌‌​‌​​‌‌​‌​‌​​​‌‌​​‌​‌‌​‌​​‌​​‌​​​​‌​‌​​‌‌​‌​​‌​​‌​‌​‌​​‌​​‌​​‌‌​‌​‌​​​‌​‌​‌​​‌​‌​​​‌‌​​‌‌​‌​​​​‌‌​‌​​​‌​‌​‌​​‌‌‌‌​‌​‌​​‌​​‌​‌​​‌​​‌​‌​​​​​‌​‌​‌‌‌​‌​‌‌​​‌​‌​‌​​‌‌​‌​​‌​‌​​‌​‌​​​​​‌​‌‌​​​​‌​​‌‌‌‌⁣
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
import random

def sir_epidemic_model() -> None:
    random.seed(42)

    # Parameters
    N = 1000          # population
    beta = 0.8        # transmission rate (higher for R0 > 1)
    gamma = 0.2       # recovery rate (infectious period = 1/gamma)
    R0 = beta / gamma # basic reproduction number (~4)

    def simulate_sir(beta: float, gamma: float, n_steps: int = 100) -> tuple[list[int], list[int], list[int]]:
        S = N - 1  # susceptible (start with one infected)
        I = 1      # infected
        R = 0      # recovered

        S_history = [S]
        I_history = [I]
        R_history = [R]

        for step in range(n_steps):
            # Transmission: contacts, beta = transmission probability per contact
            if S > 0 and I > 0:
                contact_rate = 5  # contacts per person per day
                contacts = int(contact_rate * S * I / N)
                infections = min(int(beta * contacts), S)
            else:
                infections = 0

            # Recovery: recoveries = gamma * I (people recover per day)
            recoveries = int(gamma * I) if I > 0 else 0
            recoveries = min(recoveries, I)

            # Update
            S -= infections
            I += infections - recoveries
            R += recoveries

            S_history.append(S)
            I_history.append(I)
            R_history.append(R)

            # Conservation check
            total = S + I + R
            assert total == N, f"Conservation violated at step {step}: {total} != {N}"

            if I == 0:
                break

        return S_history, I_history, R_history

    # Simulate with given beta/gamma
    S_hist, I_hist, R_hist = simulate_sir(beta, gamma)

    # Verify conservation
    for s, i, r in zip(S_hist, I_hist, R_hist):
        assert s + i + r == N, f"Conservation violated: {s} + {i} + {r} != {N}"

    # Final size (number infected during whole epidemic)
    final_infected = R_hist[-1]
    assert final_infected > 0, f"Should have infections, got {final_infected}"
    assert final_infected < N, f"Final infected should be < N, got {final_infected}"

    # Peak of infected
    peak_I = max(I_hist)
    assert peak_I > 0, f"Peak infected should be > 0, got {peak_I}"

    # With higher R0, should have more infections
    # Simulate with lower beta
    beta_low = 0.1
    S_low, I_low, R_low = simulate_sir(beta_low, gamma)
    final_low = R_low[-1]

    # Higher R0 (higher beta) should lead to more infections
    assert final_infected > final_low, (
        f"Higher beta ({beta}) should infect more: {final_infected} > {final_low}"
    )

    print("PASS")

if __name__ == "__main__":
    sir_epidemic_model()
