"""
Black-Scholes Monte Carlo — price a European option by simulation, then check against
the closed form.

WHAT IT DOES: The Black-Scholes formula gives the closed-form price for a European
call option. Monte Carlo simulation estimates the same price by simulating thousands
of possible price paths. The MC price should fall within ~3 standard errors of the
closed-form price, proving that simulation can price options when the closed form
doesn't exist (e.g. exotic options).

WHEN TO USE: You need to price a European option and want to understand the
relationship between the closed-form solution and simulation. Or you need a Monte
Carlo baseline for pricing options where no closed form exists.

GUARANTEES: MC price within 3 standard errors of the Black-Scholes closed-form price.
Both prices are positive. As num_sim increases, the confidence interval tightens.

NOT: A production option pricer. Only handles European calls (no puts, no American
options, no dividends). Uses simple Monte Carlo with no variance reduction
(antithetic variates, control variates).
"""
# △ AURA Pattern Library — © Reality Optimizer ⟦AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO⟧
_AURA_MARK = "AE1.PMRGG3ZCHIRFEZLBNRUXI6JAJ5YHI2LNNF5GK4RCFQRG2IR2EJAUKTKBKJFTCIRMEJXCEORCGARCYITQNFSCEORCEIWCE5DNEI5CEQKVKJASAUDBOR2GK4TOEBGGSYTSMFZHSIRMEJ3CEORRPWYSJPXO"
